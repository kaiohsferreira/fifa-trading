import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(path.resolve(".cursor/testing-module/ai-engine/package.json"));
const { chromium } = require("playwright");

const root = path.resolve(".cursor/qa-reports/2026-04-07-frontend-smoke");
const screenshotsDir = path.join(root, "screenshots");
const jsonDir = path.join(root, "json");
const envConfigPath = path.resolve(".cursor/qa-reports/config/environment.json");
const engineEnvPath = path.resolve(".cursor/testing-module/ai-engine/.env");

function readDotEnv(filePath) {
  if (!fs.existsSync(filePath)) return {};
  return Object.fromEntries(
    fs
      .readFileSync(filePath, "utf8")
      .split(/\r?\n/)
      .map((line) => line.trim())
      .filter((line) => line && !line.startsWith("#") && line.includes("="))
      .map((line) => {
        const index = line.indexOf("=");
        return [line.slice(0, index).trim(), line.slice(index + 1).trim().replace(/^["']|["']$/g, "")];
      })
  );
}

function sanitizeText(text) {
  return String(text || "").replace(/\s+/g, " ").trim().slice(0, 500);
}

function isErrorConsole(msg) {
  return ["error", "assert"].includes(msg.type());
}

function statusOf(condition) {
  return condition ? "pass" : "fail";
}

const envConfig = JSON.parse(fs.readFileSync(envConfigPath, "utf8"));
const active = envConfig.environments[envConfig.activeEnvironment];
const engineEnv = readDotEnv(engineEnvPath);
const frontendUrl = process.env.FRONTEND_URL || active.frontendUrl;
const backendUrl = process.env.BACKEND_URL || active.backendUrl;
const username = process.env.TEST_USERNAME || process.env.TEST_EMAIL || engineEnv.TEST_USERNAME || engineEnv.TEST_EMAIL || "";
const password = process.env.TEST_PASSWORD || engineEnv.TEST_PASSWORD || "";

const results = {
  metadata: {
    scope: "frontend-smoke",
    startedAt: new Date().toISOString(),
    frontendUrl,
    backendUrl,
    browser: "chromium",
    credentialsProfile: username ? "TEST_USERNAME from QA engine .env" : "not configured",
    passwordRecorded: false,
  },
  checks: [],
  bugs: [],
  screenshots: [],
  console: [],
  failedRequests: [],
  responses: [],
};

function addCheck(id, name, status, route, expected, obtained, evidence = "") {
  results.checks.push({ id, name, status, route, expected, obtained, evidence });
}

function addBug(id, severity, area, steps, expected, obtained, evidence, impact, probableCause, recommendation) {
  results.bugs.push({
    id,
    severity,
    status: "Aberto",
    area,
    profile: username ? "usuario de teste configurado" : "sem usuario configurado",
    preconditions: "Frontend local disponivel e backend homologado confirmado.",
    testData: username ? "credencial de teste configurada; senha omitida" : "credencial de teste ausente",
    steps,
    expected,
    obtained,
    symptom: obtained,
    technicalEvidence: evidence,
    userImpact: impact,
    probableCause,
    recommendation,
    suggestedRegression: "Reexecutar smoke front-end e login apos correcao.",
  });
}

async function capture(page, fileName, label) {
  const filePath = path.join(screenshotsDir, fileName);
  await page.screenshot({ path: filePath, fullPage: true });
  const rel = path.relative(root, filePath).replace(/\\/g, "/");
  results.screenshots.push({ label, path: rel });
  return rel;
}

async function main() {
  fs.mkdirSync(screenshotsDir, { recursive: true });
  fs.mkdirSync(jsonDir, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, ignoreHTTPSErrors: true });
  const page = await context.newPage();

  page.on("console", (msg) => {
    const item = { type: msg.type(), text: sanitizeText(msg.text()), location: msg.location() };
    results.console.push(item);
  });
  page.on("requestfailed", (request) => {
    results.failedRequests.push({
      url: request.url(),
      method: request.method(),
      failure: request.failure()?.errorText || "unknown",
    });
  });
  page.on("response", (response) => {
    const url = response.url();
    if (url.startsWith(backendUrl) || /\/Account\/|\/User\/|\/Management\/|\/Occurrence|\/IncomeExpense|\/Crm|\/Budget/i.test(url)) {
      results.responses.push({ status: response.status(), url, method: response.request().method() });
    }
  });

  let loginLoaded = false;
  try {
    const response = await page.goto(frontendUrl, { waitUntil: "networkidle", timeout: 30000 });
    loginLoaded = !!response && response.status() < 500;
    await page.waitForLoadState("domcontentloaded");
    const loginEvidence = await capture(page, "01-login-desktop.png", "Login desktop");
    const emailVisible = await page.locator('input[name="email"], input[type="email"]').first().isVisible().catch(() => false);
    const passwordVisible = await page.locator('input[name="password"], input[type="password"]').first().isVisible().catch(() => false);
    const enterVisible = await page.getByRole("button", { name: /entrar/i }).first().isVisible().catch(() => false);
    const forgotVisible = await page.getByText(/esqueci minha senha/i).first().isVisible().catch(() => false);
    addCheck(
      "QA-SMOKE-001",
      "Login renderiza campos obrigatorios",
      statusOf(loginLoaded && emailVisible && passwordVisible && enterVisible && forgotVisible),
      "/",
      "Campos de e-mail/senha, botao Entrar e link de recuperacao visiveis.",
      `loaded=${loginLoaded}; email=${emailVisible}; password=${passwordVisible}; enter=${enterVisible}; forgot=${forgotVisible}`,
      loginEvidence
    );
    if (!(loginLoaded && emailVisible && passwordVisible && enterVisible && forgotVisible)) {
      addBug(
        "QA-FE-001",
        "Critica",
        "Login",
        ["Abrir o frontend confirmado em /."],
        "Tela de login completa e utilizavel.",
        "Um ou mais elementos obrigatorios nao ficaram visiveis.",
        loginEvidence,
        "A pessoa usuaria pode ficar impedida de autenticar.",
        "Falha de renderizacao, bundle incompleto ou markup de login alterado.",
        "Verificar console e componente de login antes de liberar."
      );
    }

    const fatalConsole = results.console.filter((item) => item.type === "error");
    addCheck(
      "QA-SMOKE-002",
      "Login sem erro fatal de console",
      statusOf(fatalConsole.length === 0),
      "/",
      "Nenhum erro de console na carga inicial.",
      `${fatalConsole.length} erro(s) de console.`,
      loginEvidence
    );
    if (fatalConsole.length > 0) {
      addBug(
        "QA-FE-002",
        "Alta",
        "Login",
        ["Abrir / e observar console do navegador."],
        "Carregar sem erro fatal.",
        `${fatalConsole.length} erro(s) de console detectado(s).`,
        JSON.stringify(fatalConsole.slice(0, 5)),
        "Pode haver quebra funcional ou comportamento instavel.",
        "Erro JavaScript em runtime ou dependencia de ambiente ausente.",
        "Corrigir erros de console e reexecutar smoke."
      );
    }
  } catch (error) {
    addCheck("QA-SMOKE-001", "Login renderiza campos obrigatorios", "fail", "/", "Frontend disponivel.", sanitizeText(error.message));
    addBug("QA-FE-001", "Critica", "Login", ["Abrir /."], "Frontend carregado.", sanitizeText(error.message), "Navegacao inicial", "A pessoa usuaria nao consegue acessar o sistema.", "Servidor local ou bundle indisponivel.", "Restaurar disponibilidade do frontend.");
  }

  try {
    await page.goto(new URL("/usuario/esqueceu_senha", frontendUrl).toString(), { waitUntil: "networkidle", timeout: 30000 });
    const forgotEvidence = await capture(page, "02-forgot-password.png", "Recuperacao de senha");
    const emailVisible = await page.locator('input[name="email"], input[type="email"]').first().isVisible().catch(() => false);
    const textVisible = await page.getByText(/esqueceu|senha|email/i).first().isVisible().catch(() => false);
    addCheck("QA-SMOKE-003", "Recuperacao de senha renderiza", statusOf(emailVisible && textVisible), "/usuario/esqueceu_senha", "Campo de e-mail e textos da tela visiveis.", `email=${emailVisible}; text=${textVisible}`, forgotEvidence);
  } catch (error) {
    addCheck("QA-SMOKE-003", "Recuperacao de senha renderiza", "fail", "/usuario/esqueceu_senha", "Tela abre.", sanitizeText(error.message));
  }

  try {
    await context.clearCookies();
    await page.goto(new URL("/adm/dashboard", frontendUrl).toString(), { waitUntil: "networkidle", timeout: 30000 });
    const privateEvidence = await capture(page, "03-private-dashboard-without-session.png", "Rota privada sem sessao");
    const currentUrl = page.url();
    const hasLoginField = await page.locator('input[name="email"], input[type="email"]').first().isVisible().catch(() => false);
    const bodyText = sanitizeText(await page.locator("body").innerText().catch(() => ""));
    const protectedBlocked = currentUrl === frontendUrl + "/" || currentUrl.endsWith("/") || hasLoginField || /login|e-mail|senha/i.test(bodyText);
    addCheck("QA-SMOKE-004", "Rota privada sem sessao nao expoe dashboard", statusOf(protectedBlocked), "/adm/dashboard", "Usuario sem token deve ser redirecionado/bloqueado.", `url=${currentUrl}; hasLoginField=${hasLoginField}`, privateEvidence);
    if (!protectedBlocked) {
      addBug("QA-FE-003", "Critica", "Autenticacao", ["Limpar sessao.", "Abrir /adm/dashboard diretamente."], "Dashboard bloqueado ou redirecionado para login.", "Conteudo privado potencialmente acessivel sem sessao.", privateEvidence, "Risco de acesso indevido a area administrativa.", "Rota privada sem wrapper/guard de autenticacao.", "Aplicar protecao de rota e reexecutar teste de acesso direto.");
    }
  } catch (error) {
    addCheck("QA-SMOKE-004", "Rota privada sem sessao nao expoe dashboard", "fail", "/adm/dashboard", "Rota tratada sem erro fatal.", sanitizeText(error.message));
  }

  let authenticated = false;
  if (username && password) {
    try {
      await page.goto(frontendUrl, { waitUntil: "networkidle", timeout: 30000 });
      await page.locator('input[name="email"], input[type="email"]').first().fill(username);
      await page.locator('input[name="password"], input[type="password"]').first().fill(password);
      const filledEvidence = await capture(page, "04-login-filled.png", "Login preenchido com senha omitida no relatorio");
      await Promise.allSettled([
        page.waitForResponse((response) => /\/Account\/Login/i.test(response.url()), { timeout: 20000 }),
        page.getByRole("button", { name: /entrar/i }).first().click(),
      ]);
      await page.waitForTimeout(3000);
      const postLoginEvidence = await capture(page, "05-post-login.png", "Resultado apos login");
      const loginResponses = results.responses.filter((response) => /\/Account\/Login/i.test(response.url));
      const lastLogin = loginResponses.at(-1);
      authenticated = !!lastLogin && lastLogin.status >= 200 && lastLogin.status < 300 && !page.url().endsWith("/");
      const tokenState = await page.evaluate(() => ({
        hasLocalStorageToken: Object.keys(localStorage).some((key) => /token/i.test(key)),
        cookies: document.cookie ? document.cookie.split(";").filter((entry) => /token/i.test(entry)).length : 0,
      })).catch(() => ({ hasLocalStorageToken: false, cookies: 0 }));
      addCheck("QA-SMOKE-005", "Login chama Account/Login sem erro 5xx", statusOf(!!lastLogin && lastLogin.status < 500), "/", "Chamada de login retorna abaixo de 500.", lastLogin ? `status=${lastLogin.status}` : "sem response /Account/Login", filledEvidence);
      addCheck("QA-SMOKE-006", "Login aceito cria sessao", statusOf(authenticated || tokenState.hasLocalStorageToken || tokenState.cookies > 0), "pos-login", "Autenticacao aceita e token/sessao presente.", `url=${page.url()}; token=${tokenState.hasLocalStorageToken}; cookieToken=${tokenState.cookies}`, postLoginEvidence);
      if (lastLogin && lastLogin.status >= 500) {
        addBug("QA-FE-004", "Alta", "Login/API", ["Preencher credenciais de teste.", "Clicar Entrar."], "API de login sem erro 5xx.", `Account/Login retornou ${lastLogin.status}.`, postLoginEvidence, "A pessoa usuaria nao consegue autenticar por falha de servidor.", "Instabilidade ou erro na API homologada.", "Analisar logs do endpoint /Account/Login.");
      }
    } catch (error) {
      addCheck("QA-SMOKE-005", "Login chama Account/Login sem erro 5xx", "fail", "/", "Login executavel.", sanitizeText(error.message));
      addCheck("QA-SMOKE-006", "Login aceito cria sessao", "skip", "pos-login", "Depende do login.", "Login nao concluiu.");
    }
  } else {
    addCheck("QA-SMOKE-005", "Login chama Account/Login sem erro 5xx", "skip", "/", "Credencial configurada.", "Credencial de teste ausente.");
    addCheck("QA-SMOKE-006", "Login aceito cria sessao", "skip", "pos-login", "Credencial configurada.", "Credencial de teste ausente.");
  }

  const internalRoutes = ["/adm/dashboard", "/adm/usuarios/lista", "/crm/lista", "/financeiro/rateio/lista", "/ocorrencias/lista", "/work-orders"];
  let internalPassed = 0;
  if (authenticated) {
    for (let index = 0; index < internalRoutes.length; index += 1) {
      const route = internalRoutes[index];
      try {
        await page.goto(new URL(route, frontendUrl).toString(), { waitUntil: "domcontentloaded", timeout: 30000 });
        await page.waitForTimeout(1500);
        const evidence = await capture(page, `06-internal-${index + 1}${route.replaceAll("/", "_")}.png`, `Rota interna ${route}`);
        const bodyText = sanitizeText(await page.locator("body").innerText().catch(() => ""));
        const hasVisibleContent = bodyText.length > 20;
        const noRecentFailedRequests = results.failedRequests.length === 0;
        if (hasVisibleContent && noRecentFailedRequests) internalPassed += 1;
        addCheck(`QA-SMOKE-007.${index + 1}`, `Rota interna ${route}`, statusOf(hasVisibleContent), route, "Rota autenticada renderiza conteudo.", `contentLength=${bodyText.length}; url=${page.url()}`, evidence);
      } catch (error) {
        addCheck(`QA-SMOKE-007.${index + 1}`, `Rota interna ${route}`, "fail", route, "Rota autenticada renderiza.", sanitizeText(error.message));
      }
    }
  } else {
    addCheck("QA-SMOKE-007", "Rotas internas autenticadas", "skip", "rotas internas", "Depende de login aceito.", "Login nao autenticado.");
  }

  const viewports = [
    ["desktop", 1440, 900],
    ["tablet", 768, 1024],
    ["mobile", 390, 844],
  ];
  let responsiveOk = 0;
  for (const [name, width, height] of viewports) {
    const vp = await browser.newContext({ viewport: { width, height }, ignoreHTTPSErrors: true });
    const vpPage = await vp.newPage();
    try {
      await vpPage.goto(frontendUrl, { waitUntil: "networkidle", timeout: 30000 });
      const evidence = await capture(vpPage, `responsive-${name}.png`, `Login ${name}`);
      const emailVisible = await vpPage.locator('input[name="email"], input[type="email"]').first().isVisible().catch(() => false);
      const passwordVisible = await vpPage.locator('input[name="password"], input[type="password"]').first().isVisible().catch(() => false);
      if (emailVisible && passwordVisible) responsiveOk += 1;
      addCheck(`QA-SMOKE-008.${name}`, `Responsivo login ${name}`, statusOf(emailVisible && passwordVisible), "/", "Campos principais visiveis no viewport.", `email=${emailVisible}; password=${passwordVisible}; viewport=${width}x${height}`, evidence);
    } catch (error) {
      addCheck(`QA-SMOKE-008.${name}`, `Responsivo login ${name}`, "fail", "/", "Viewport carrega.", sanitizeText(error.message));
    } finally {
      await vp.close();
    }
  }

  await browser.close();

  const pass = results.checks.filter((check) => check.status === "pass").length;
  const fail = results.checks.filter((check) => check.status === "fail").length;
  const skip = results.checks.filter((check) => check.status === "skip").length;
  const warnings = results.console.filter((item) => item.type === "warning").length + results.failedRequests.length;
  const denominator = Math.max(pass + fail, 1);
  const qualityScore = Math.max(0, Math.min(100, Math.round((pass / denominator) * 80 + (fail === 0 ? 10 : 0) + (warnings === 0 ? 10 : 0))));
  results.summary = {
    finishedAt: new Date().toISOString(),
    totalChecks: results.checks.length,
    pass,
    fail,
    skip,
    warnings,
    qualityScore,
    band: qualityScore >= 85 ? "Excellent" : qualityScore >= 70 ? "Acceptable" : qualityScore >= 50 ? "Warning" : "Critical",
  };

  fs.writeFileSync(path.join(jsonDir, "frontend-smoke-results.json"), JSON.stringify(results, null, 2), "utf8");
  console.log(JSON.stringify(results.summary, null, 2));
}

main().catch((error) => {
  results.summary = {
    finishedAt: new Date().toISOString(),
    totalChecks: results.checks.length,
    pass: results.checks.filter((check) => check.status === "pass").length,
    fail: results.checks.filter((check) => check.status === "fail").length + 1,
    skip: results.checks.filter((check) => check.status === "skip").length,
    warnings: results.console.filter((item) => item.type === "warning").length + results.failedRequests.length,
    qualityScore: 0,
    band: "Critical",
    fatalError: sanitizeText(error.stack || error.message),
  };
  fs.mkdirSync(jsonDir, { recursive: true });
  fs.writeFileSync(path.join(jsonDir, "frontend-smoke-results.json"), JSON.stringify(results, null, 2), "utf8");
  console.error(error);
  process.exitCode = 1;
});
