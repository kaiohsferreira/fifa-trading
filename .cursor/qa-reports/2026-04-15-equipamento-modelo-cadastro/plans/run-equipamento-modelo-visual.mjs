import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(
  path.resolve(".cursor/testing-module/ai-engine/package.json"),
);
const { chromium } = require("playwright");

const scope = "2026-04-15-equipamento-modelo-cadastro";
const scopeRoot = path.resolve(`.cursor/qa-reports/${scope}`);
const screenshotsDir = path.join(scopeRoot, "screenshots");
const jsonDir = path.join(scopeRoot, "json");
const htmlDir = path.join(scopeRoot, "html");
const videoDir = path.join(screenshotsDir, "videos");

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
        return [
          line.slice(0, index).trim(),
          line
            .slice(index + 1)
            .trim()
            .replace(/^["']|["']$/g, ""),
        ];
      }),
  );
}

function sanitizeText(value) {
  return String(value || "").replace(/\s+/g, " ").trim().slice(0, 600);
}

function ensureDirs() {
  [scopeRoot, screenshotsDir, jsonDir, htmlDir, videoDir].forEach((dir) =>
    fs.mkdirSync(dir, { recursive: true }),
  );
}

function status(condition) {
  return condition ? "pass" : "fail";
}

async function capture(page, fileName, label, report) {
  const filePath = path.join(screenshotsDir, fileName);
  await page.screenshot({ path: filePath, fullPage: true });
  const relPath = path.relative(scopeRoot, filePath).replaceAll("\\", "/");
  report.evidences.push({ type: "screenshot", label, path: relPath });
  return relPath;
}

async function inspectModelField(page) {
  const data = await page.evaluate(async () => {
    const normalize = (text) =>
      String(text || "")
        .replace("*", "")
        .replace(/\s+/g, " ")
        .trim()
        .toLowerCase();

    const modelLabel = Array.from(document.querySelectorAll("span")).find(
      (item) => normalize(item.textContent) === "modelo de equipamento",
    );
    if (!modelLabel) {
      return { found: false };
    }

    let container = modelLabel.closest("div");
    while (container && !container.querySelector("button")) {
      container = container.parentElement;
    }
    if (!container) {
      return { found: false };
    }

    const button = container.querySelector("button");
    if (!button) {
      return { found: false };
    }

    const selectedNode = button.querySelector("span");
    const textBefore = (
      selectedNode?.textContent ||
      button.textContent ||
      ""
    ).trim();
    const beforeOpenInputs = document.querySelectorAll(
      'input[placeholder="Pesquisar..."], input[placeholder="Toque em uma opção abaixo"]',
    ).length;

    button.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    await new Promise((resolve) => setTimeout(resolve, 250));

    const afterOpenInputs = document.querySelectorAll(
      'input[placeholder="Pesquisar..."], input[placeholder="Toque em uma opção abaixo"]',
    ).length;
    const dropdownOpened = afterOpenInputs > beforeOpenInputs;

    if (dropdownOpened) {
      button.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await new Promise((resolve) => setTimeout(resolve, 150));
    } else {
      document.body.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await new Promise((resolve) => setTimeout(resolve, 100));
    }

    const buttonBg = window.getComputedStyle(button).backgroundColor;

    return {
      found: true,
      text: textBefore,
      dropdownOpened,
      buttonBg,
    };
  });

  return data;
}

async function tryLogin(page, frontendUrl, username, password, report) {
  await page.goto(frontendUrl, { waitUntil: "networkidle", timeout: 45000 });
  await page.waitForLoadState("domcontentloaded");

  const emailInput = page.locator('input[name="email"], input[type="email"]').first();
  const passwordInput = page
    .locator('input[name="password"], input[type="password"]')
    .first();
  const loginButton = page.getByRole("button", { name: /entrar/i }).first();

  const loginFormVisible =
    (await emailInput.isVisible().catch(() => false)) &&
    (await passwordInput.isVisible().catch(() => false)) &&
    (await loginButton.isVisible().catch(() => false));

  await capture(page, "00-login-view.png", "Tela inicial de login", report);

  if (!loginFormVisible || !username || !password) {
    return {
      authenticated: false,
      reason: !loginFormVisible
        ? "formulario de login nao detectado"
        : "credenciais de teste nao configuradas",
    };
  }

  await emailInput.fill(username);
  await passwordInput.fill(password);
  await capture(
    page,
    "01-login-filled.png",
    "Login preenchido (senha omitida)",
    report,
  );

  await Promise.allSettled([
    page.waitForResponse(
      (response) => /\/Account\/Login/i.test(response.url()),
      { timeout: 25000 },
    ),
    loginButton.click(),
  ]);

  await page.waitForTimeout(4000);
  await capture(page, "02-post-login.png", "Resultado apos tentativa de login", report);

  const currentUrl = page.url();
  const hasLoginElements =
    (await emailInput.isVisible().catch(() => false)) ||
    (await passwordInput.isVisible().catch(() => false));

  const authenticated =
    !hasLoginElements && /\/adm\/|\/crm\/|\/financeiro\//i.test(currentUrl);

  return {
    authenticated,
    reason: authenticated ? "ok" : `nao autenticou; url final: ${currentUrl}`,
  };
}

function addScenario(report, scenario) {
  report.scenarios.push(scenario);
}

async function runScenario(page, report, scenarioId, title, routeState, expected) {
  const targetPath = "/adm/equipamentos/adicionar";
  const baseUrl = report.metadata.frontendUrl;
  await page.goto(new URL(targetPath, baseUrl).toString(), {
    waitUntil: "networkidle",
    timeout: 45000,
  });

  if (routeState) {
    await page.evaluate((state) => {
      const current = window.history.state || {};
      window.history.replaceState(
        {
          ...current,
          usr: state,
          key: current.key || `qa-${Date.now()}`,
        },
        "",
        window.location.href,
      );
    }, routeState);
    await page.reload({ waitUntil: "networkidle", timeout: 45000 });
  }

  await page.waitForTimeout(1200);
  const fieldData = await inspectModelField(page);
  const evidencePath = await capture(
    page,
    `${scenarioId}.png`,
    `${title} - tela`,
    report,
  );

  const found = Boolean(fieldData.found);
  const selectedText = sanitizeText(fieldData.text);
  const isEnabled = Boolean(fieldData.dropdownOpened);
  const expectedLabel = expected.defaultLabel || "";
  const labelMatch =
    !expectedLabel ||
    selectedText.toLowerCase().includes(expectedLabel.toLowerCase());
  const enabledMatch = isEnabled === expected.enabled;

  addScenario(report, {
    id: scenarioId,
    title,
    route: targetPath,
    expected,
    obtained: {
      found,
      selectedText,
      enabled: isEnabled,
      buttonBg: fieldData.buttonBg || "",
    },
    evidence: evidencePath,
    status: status(found && labelMatch && enabledMatch),
  });
}

async function main() {
  ensureDirs();

  const envConfig = JSON.parse(fs.readFileSync(envConfigPath, "utf8"));
  const active = envConfig.environments[envConfig.activeEnvironment];
  const engineEnv = readDotEnv(engineEnvPath);

  const frontendUrl = process.env.FRONTEND_URL || active.frontendUrl;
  const backendUrl = process.env.BACKEND_URL || active.backendUrl;
  const username =
    process.env.TEST_USERNAME || process.env.TEST_EMAIL || engineEnv.TEST_USERNAME || "";
  const password = process.env.TEST_PASSWORD || engineEnv.TEST_PASSWORD || "";

  const report = {
    metadata: {
      scope,
      startedAt: new Date().toISOString(),
      frontendUrl,
      backendUrl,
      browser: "chromium",
      viewport: "1440x900",
      usernameMask: username ? `${username.slice(0, 3)}***` : "nao configurado",
      command: "node .cursor/qa-reports/.../run-equipamento-modelo-visual.mjs",
    },
    evidences: [],
    consoleErrors: [],
    failedRequests: [],
    scenarios: [],
    summary: {},
  };

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    ignoreHTTPSErrors: true,
    recordVideo: { dir: videoDir, size: { width: 1440, height: 900 } },
  });
  const page = await context.newPage();

  page.on("console", (msg) => {
    if (msg.type() === "error") {
      report.consoleErrors.push({
        type: msg.type(),
        text: sanitizeText(msg.text()),
      });
    }
  });
  page.on("requestfailed", (request) => {
    report.failedRequests.push({
      method: request.method(),
      url: request.url(),
      failure: sanitizeText(request.failure()?.errorText || "unknown"),
    });
  });

  const auth = await tryLogin(page, frontendUrl, username, password, report);
  report.metadata.authenticated = auth.authenticated;
  report.metadata.authReason = auth.reason;

  if (!auth.authenticated) {
    report.summary = {
      totalScenarios: 3,
      executed: 0,
      pass: 0,
      fail: 0,
      skip: 3,
      qualityScore: 0,
      band: "Critical",
      note: "Nao foi possivel autenticar para acessar rota privada.",
    };
  } else {
    await runScenario(page, report, "cenario-01-direto", "Acesso direto", null, {
      enabled: true,
      defaultLabel: "",
      expectedVisual: "Campo visivel com placeholder para selecao manual.",
    });

    await runScenario(
      page,
      report,
      "cenario-02-comum",
      "Acesso com origem estoque comum",
      {
        returnPath: "/adm/equipamentos-comuns/lista?tab=buscar-estoque",
        equipmentOrigin: "stock-common",
      },
      {
        enabled: false,
        defaultLabel: "Comum",
        expectedVisual: "Campo visivel, pre-selecionado em Comum e bloqueado.",
      },
    );

    await runScenario(
      page,
      report,
      "cenario-03-seguranca",
      "Acesso com origem estoque seguranca",
      {
        returnPath: "/adm/estoque/lista?tab=buscar-estoque",
        equipmentOrigin: "stock-security",
      },
      {
        enabled: false,
        defaultLabel: "Segurança",
        expectedVisual:
          "Campo visivel, pre-selecionado em Seguranca e bloqueado.",
      },
    );

    const pass = report.scenarios.filter((item) => item.status === "pass").length;
    const fail = report.scenarios.filter((item) => item.status === "fail").length;
    const total = report.scenarios.length;
    const baseScore = total ? Math.round((pass / total) * 100) : 0;
    const qualityScore = Math.max(0, baseScore - Math.min(fail * 8, 24));
    report.summary = {
      totalScenarios: total,
      executed: total,
      pass,
      fail,
      skip: 0,
      qualityScore,
      band:
        qualityScore >= 85
          ? "Excellent"
          : qualityScore >= 70
            ? "Acceptable"
            : qualityScore >= 50
              ? "Warning"
              : "Critical",
    };
  }

  await context.close();
  await browser.close();

  const videos = fs
    .readdirSync(videoDir, { withFileTypes: true })
    .filter((entry) => entry.isFile())
    .map((entry) => entry.name);
  videos.forEach((videoName) => {
    report.evidences.push({
      type: "video",
      label: "Gravacao completa da execucao",
      path: path
        .relative(scopeRoot, path.join(videoDir, videoName))
        .replaceAll("\\", "/"),
    });
  });

  report.metadata.finishedAt = new Date().toISOString();
  fs.writeFileSync(
    path.join(jsonDir, "equipamento-modelo-visual-report.json"),
    JSON.stringify(report, null, 2),
    "utf8",
  );
  console.log(JSON.stringify(report.summary, null, 2));
}

main().catch((error) => {
  const fallback = {
    fatal: true,
    message: sanitizeText(error.message),
    stack: sanitizeText(error.stack),
    finishedAt: new Date().toISOString(),
  };
  ensureDirs();
  fs.writeFileSync(
    path.join(jsonDir, "equipamento-modelo-visual-report.json"),
    JSON.stringify(fallback, null, 2),
    "utf8",
  );
  console.error(error);
  process.exitCode = 1;
});
