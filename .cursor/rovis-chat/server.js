import express from "express";
import cors from "cors";
import multer from "multer";
import dotenv from "dotenv";
import { spawn, spawnSync } from "node:child_process";
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { randomUUID } from "node:crypto";
import readline from "node:readline";
import { fileURLToPath } from "node:url";

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const upload = multer({ limits: { fileSize: 8 * 1024 * 1024, files: 4 } });

app.use(cors());
app.use(express.json({ limit: "2mb" }));
app.use(express.static("public"));

const isWindows = process.platform === "win32";
const codexCmd = "codex";
const spawnOpts = isWindows ? { shell: true } : {};

const port = Number(process.env.PORT || 3000);
const model = process.env.CODEX_MODEL || "gpt-5";
const codexTimeoutMs = Number(process.env.CODEX_TIMEOUT_MS || 0);
const workspaceRoot = String(process.env.WORKSPACE_ROOT || path.resolve(__dirname, "..", "..")).trim();
const frontendProjectPath = String(process.env.FRONTEND_PROJECT_PATH || "").trim();
const backendProjectPath = String(process.env.BACKEND_PROJECT_PATH || "").trim();

const systemPrompt = [
  "Voce e o ROVIS, um assistente extremamente forte, direto e tecnico quando necessario.",
  "Seu objetivo: resolver de verdade, com clareza, estrategia e execucao.",
  "Regras:",
  "1) Responda em portugues do Brasil.",
  "2) Seja objetivo e pratico, sem enrolacao.",
  "3) Se receber imagem, analise com detalhes uteis para acao.",
  "4) Quando faltar contexto, pergunte apenas o minimo necessario.",
  "5) Sempre priorize resultado real para o usuario.",
  "6) Considere .cursor apenas como camada de memoria, contratos, QA e orquestracao.",
  "7) Quando houver implementacao real, trabalhe nos projetos de front/back fora da .cursor.",
].join("\n");

function buildProjectScopeInstructions() {
  const lines = [
    "[REGRAS_DE_WORKSPACE]",
    `Workspace raiz real: ${workspaceRoot}`,
    ".cursor e camada de orquestracao, memoria, contratos, QA e suporte.",
    "Nao trate .cursor como app principal de front/back, exceto quando a tarefa for explicitamente sobre ferramentas internas da .cursor.",
  ];

  if (frontendProjectPath) {
    lines.push(`Projeto frontend real: ${frontendProjectPath}`);
  } else {
    lines.push("Projeto frontend real: NAO CONFIGURADO");
  }

  if (backendProjectPath) {
    lines.push(`Projeto backend real: ${backendProjectPath}`);
  } else {
    lines.push("Projeto backend real: NAO CONFIGURADO");
  }

  lines.push(
    "Para perguntas de leitura, diagnostico, listagem, identificacao de tecnologia, estrutura de pastas e inspecao de arquivos: executar imediatamente e devolver o resultado final.",
    "Nao responder apenas com intencao do tipo 'vou verificar', 'vou localizar' ou 'vou inspecionar'. Primeiro execute a leitura e depois responda com o achado.",
    "So pedir aprovacao explicita antes de alteracoes que escrevem, instalam, apagam, movem arquivos ou executam mudancas irreversiveis.",
    "Se o usuario pedir para entrar em uma pasta e dizer a tecnologia, localizar a pasta, ler arquivos como package.json, tsconfig, vite.config, next.config, dockerfile ou equivalentes e responder objetivamente com a stack encontrada.",
    "Quando a tarefa envolver frontend, entrar/escrever no projeto frontend real fora da .cursor.",
    "Quando a tarefa envolver backend, entrar/escrever no projeto backend real fora da .cursor.",
    "Se o usuario pedir implementacao de produto e algum caminho real nao estiver configurado, informar isso objetivamente antes de executar a implementacao."
  );

  return lines.join("\n");
}

const codexCheck = spawnSync(codexCmd, ["--version"], {
  encoding: "utf8",
  windowsHide: true,
  ...spawnOpts,
});
const codexCliAvailable = codexCheck.status === 0;

const modeDefinitions = {
  ROVIS: {
    label: "ROVIS",
    description: "Orquestrador geral com PM, aprovacao, contracts e QA.",
    prompt: [
      "Ative o modo ROVIS.",
      "Use os arquivos da pasta .cursor como fonte de verdade.",
      "Sempre opere como orquestrador do sistema.",
      "Sempre comece no papel de PM quando receber um pedido novo.",
      "Antes de qualquer implementacao: resumir, classificar, estimar impacto, propor plano, riscos e pedir aprovacao explicita.",
      "So avance para arquitetura/execucao quando o usuario aprovar.",
      "Excecao: se a solicitacao for somente leitura, diagnostico, analise, listagem de pastas, leitura de arquivos ou identificacao de stack, execute imediatamente sem pedir aprovacao.",
      "Sempre seja transparente com dashboard ROVIS contendo estado, agente ativo, tarefa, etapa, progresso, arquivos em foco, proxima acao e fonte de verdade.",
      "Ative AI-TESTING quando o usuario pedir testes ou quando uma implementacao terminar.",
      "Sempre registrar planejamento e historico na memoria quando o contexto pedir execucao real no workspace.",
      "Toda implementacao de produto deve acontecer preferencialmente nos projetos reais de front/back fora da .cursor.",
    ].join("\n"),
  },
  ROVIS_FE: {
    label: "ROVIS-FE",
    description: "Modo frontend: UI, UX, estado e consumo de contrato.",
    prompt: [
      "Ative o modo ROVIS-FE.",
      "Voce e o orquestrador dedicado do Front-end.",
      "Atue somente em tarefas de front-end. Nao implemente backend. Nao altere contratos.",
      "Entre e escreva no projeto frontend real fora da .cursor quando houver implementacao de tela, logica ou consumo.",
      "Para leitura de stack, estrutura e diagnostico do frontend, execute imediatamente e responda com o resultado final.",
      "Classifique a tarefa como VISUAL_ONLY, FRONT_LOGIC ou CONTRACT_CONSUMPTION.",
      "Se for CONTRACT_CONSUMPTION, exija contrato em .cursor/contracts e siga exatamente o contrato.",
      "Sempre responda com dashboard ROVIS_FE contendo estado, subagente ativo, tarefa, etapa, progresso, contratos em foco, arquivos em foco e proxima acao.",
      "Quando houver UI, validacao visual, formulario ou navegacao, acione AI-TESTING com foco em browser.",
    ].join("\n"),
  },
  ROVIS_BE: {
    label: "ROVIS-BE",
    description: "Modo backend: PM, ARCH, contrato e implementacao backend.",
    prompt: [
      "Ative o modo ROVIS-BE.",
      "Voce e o orquestrador dedicado do Backend.",
      "Entre e escreva no projeto backend real fora da .cursor quando houver implementacao de backend.",
      "Sempre siga o fluxo PM -> aprovacao explicita -> ARCH -> contrato -> BACK -> validacao -> handoff.",
      "Para leitura de stack, estrutura e diagnostico do backend, execute imediatamente e responda com o resultado final.",
      "Nao inicie front-end. Nao implemente sem contrato. Se houver divergencia, pare e solicite ajuste do ARCH.",
      "Sempre responda com dashboard ROVIS_BE contendo estado, agente ativo, tarefa, etapa, progresso, contratos em foco, arquivos em foco e proxima acao.",
      "Ao finalizar backend, entregue handoff claro para o front com os contratos prontos.",
    ].join("\n"),
  },
  QA: {
    label: "QA",
    description: "Modo QA e AI-TESTING com foco em validacao e relatorios.",
    prompt: [
      "Ative somente o modo QA.",
      "Use o agente AI-TESTING como principal.",
      "Nao execute implementacoes de produto/codigo, exceto automacao de teste, relatorios, planejamento e configuracao de QA.",
      "Quando houver intencao de teste, estruture a resposta como dashboard AI_TESTING com estado, fase ativa, casos, quality score e proxima acao.",
      "Leia e respeite .cursor/qa-reports, .cursor/testing-module e .cursor/qa-reports/config/environment.json quando a tarefa envolver execucao real.",
      "Priorize geracao de cenarios, execucao, analise de falhas e relatorio objetivo.",
    ].join("\n"),
  },
};

const sessions = new Map();

function sendStreamEvent(res, payload) {
  res.write(`${JSON.stringify(payload)}\n`);
}

function buildPrompt(sessionId, modeKey, userMessage, initMode = false) {
  const session = sessions.get(sessionId) || { history: [] };
  const history = session.history.slice(-20);
  const mode = modeDefinitions[modeKey] || modeDefinitions.ROVIS;

  const conversation = history
    .map((item, index) => `${index + 1}. ${item.role.toUpperCase()}: ${item.text}`)
    .join("\n");

  return [
    "[SISTEMA]",
    systemPrompt,
    "",
    buildProjectScopeInstructions(),
    "",
    "[MODO_ROVIS_ATIVO]",
    `${mode.label}: ${mode.description}`,
    mode.prompt,
    "",
    "[CONTEXTO]",
    "Conversa anterior resumida em turnos:",
    conversation || "(sem historico)",
    "",
    "[ENTRADA_ATUAL_USUARIO]",
    initMode
      ? "O usuario acabou de entrar no chat deste modo. Apresente o modo ativo, como voce vai operar e qual e o primeiro passo esperado."
      : userMessage || "(somente imagem enviada)",
    "",
    initMode
      ? "Responda como mensagem inicial do chat, curta e util, sem metadados."
      : "Responda apenas com a mensagem final para o usuario, sem metadados.",
  ].join("\n");
}

function normalizeCodexErrorMessage(error) {
  const rawMessage = String(error?.message || "").trim();

  if (!rawMessage) {
    return "Falha ao processar a solicitacao no ROVIS.";
  }

  if (rawMessage === "__CODEX_TIMEOUT__" || /tempo limite|timeout/i.test(rawMessage)) {
    return "A resposta demorou mais que o esperado. Tente dividir a solicitacao em partes menores.";
  }

  if (
    rawMessage === "__CODEX_PROCESS_ERROR__" ||
    /finalizou com codigo/i.test(rawMessage) ||
    /process exited/i.test(rawMessage)
  ) {
    return "O Codex CLI nao conseguiu concluir essa execucao. Tente reformular a solicitacao.";
  }

  return rawMessage;
}

function runCodexExec(prompt, imagePaths) {
  return new Promise(async (resolve, reject) => {
    const outputFile = path.join(tmpdir(), `rovis-answer-${randomUUID()}.txt`);

    const args = [
      "exec",
      "--skip-git-repo-check",
      "--sandbox",
      "danger-full-access",
      "--model",
      model,
      "--output-last-message",
      outputFile,
      prompt,
    ];

    for (const imagePath of imagePaths) {
      args.push("--image", imagePath);
    }

    const child = spawn(codexCmd, args, {
      cwd: workspaceRoot,
      windowsHide: true,
      stdio: ["ignore", "pipe", "pipe"],
      ...spawnOpts,
    });

    let stderr = "";
    child.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
    });

    const timeout =
      codexTimeoutMs > 0
        ? setTimeout(() => {
            child.kill("SIGKILL");
            reject(new Error("__CODEX_TIMEOUT__"));
          }, codexTimeoutMs)
        : null;

    child.on("error", (err) => {
      if (timeout) {
        clearTimeout(timeout);
      }
      reject(err);
    });

    child.on("close", async (code) => {
      if (timeout) {
        clearTimeout(timeout);
      }

      try {
        if (code !== 0) {
          reject(new Error(stderr.trim() || "__CODEX_PROCESS_ERROR__"));
          return;
        }

        const answer = await readFile(outputFile, "utf8");
        resolve(answer.trim() || "Nao consegui gerar resposta agora.");
      } catch (error) {
        reject(error);
      } finally {
        await rm(outputFile, { force: true }).catch(() => undefined);
      }
    });
  });
}

function runCodexExecStream({ prompt, imagePaths, onEvent, onAnswer, onError }) {
  const args = [
    "exec",
    "--skip-git-repo-check",
    "--sandbox",
    "danger-full-access",
    "--model",
    model,
    "--json",
    prompt,
  ];

  for (const imagePath of imagePaths) {
    args.push("--image", imagePath);
  }

  const child = spawn(codexCmd, args, {
    cwd: workspaceRoot,
    windowsHide: true,
    stdio: ["ignore", "pipe", "pipe"],
  });

  let finalAnswer = "";
  let stderr = "";
  let completedTurn = false;
  let answerSent = false;
  let failed = false;

  const stdoutReader = readline.createInterface({ input: child.stdout });
  stdoutReader.on("line", (line) => {
    const trimmed = line.trim();
    if (!trimmed) return;

    try {
      const event = JSON.parse(trimmed);
      if (event.type === "thread.started") {
        onEvent({ type: "status", message: "Sessao iniciada no Codex CLI." });
      } else if (event.type === "turn.started") {
        onEvent({ type: "status", message: "ROVIS esta processando sua solicitacao." });
      } else if (event.type === "item.completed" && event.item?.type === "agent_message") {
        finalAnswer = event.item.text || "";
        if (!answerSent) {
          answerSent = true;
          onAnswer(finalAnswer);
        }
      } else if (event.type === "turn.completed") {
        completedTurn = true;
        onEvent({ type: "done", usage: event.usage || null });
      }
    } catch {
      onEvent({ type: "debug", message: trimmed });
    }
  });

  child.stderr.on("data", (chunk) => {
    stderr += chunk.toString();
  });

  const timeout =
    codexTimeoutMs > 0
      ? setTimeout(() => {
          failed = true;
          child.kill("SIGKILL");
          onError(new Error("__CODEX_TIMEOUT__"));
        }, codexTimeoutMs)
      : null;

  child.on("error", (error) => {
    if (timeout) {
      clearTimeout(timeout);
    }
    failed = true;
    onError(error);
  });

  child.on("close", (code) => {
    if (timeout) {
      clearTimeout(timeout);
    }
    stdoutReader.close();
    if (failed) return;
    if (code !== 0) {
      failed = true;
      onError(new Error(stderr.trim() || "__CODEX_PROCESS_ERROR__"));
      return;
    }
    if (!answerSent) {
      answerSent = true;
      onAnswer("Nao consegui gerar resposta agora.");
    }
    if (!completedTurn) {
      onEvent({ type: "done", usage: null });
    }
  });

  return child;
}

async function prepareRequestAssets(files) {
  const workDir = await mkdtemp(path.join(tmpdir(), "rovis-upload-"));
  const imagePaths = [];

  for (let i = 0; i < files.length; i += 1) {
    const file = files[i];
    if (!file.mimetype.startsWith("image/")) {
      throw new Error(`Arquivo invalido: ${file.originalname}`);
    }

    const ext = (file.originalname.split(".").pop() || "png").replace(/[^a-zA-Z0-9]/g, "");
    const filePath = path.join(workDir, `img-${i}.${ext || "png"}`);
    await writeFile(filePath, file.buffer);
    imagePaths.push(filePath);
  }

  return { workDir, imagePaths };
}

function appendSessionHistory({ sessionId, modeKey, message, filesCount, answer }) {
  const session = sessions.get(sessionId) || { history: [] };
  const nextHistory = [...session.history];

  if (message) {
    nextHistory.push({ role: "user", text: message });
  } else if (filesCount > 0) {
    nextHistory.push({ role: "user", text: `[enviou ${filesCount} imagem(ns)]` });
  } else {
    nextHistory.push({ role: "user", text: `[init automatico do modo ${modeKey}]` });
  }

  nextHistory.push({ role: "assistant", text: answer });

  sessions.set(sessionId, {
    mode: modeKey,
    history: nextHistory.slice(-30),
    updatedAt: Date.now(),
  });
}

app.get("/api/health", (_req, res) => {
  res.json({
    ok: true,
    service: "rovis-chat",
    model,
    codexCliAvailable,
    workspaceRoot,
    frontendProjectPath,
    backendProjectPath,
    availableModes: Object.entries(modeDefinitions).map(([key, value]) => ({
      key,
      label: value.label,
      description: value.description,
    })),
  });
});

app.post("/api/chat", upload.array("images", 4), async (req, res) => {
  let workDir = "";

  try {
    if (!codexCliAvailable) {
      return res.status(500).json({
        error: "Codex CLI nao encontrado. Instale/configure o comando 'codex'.",
      });
    }

    const sessionId = String(req.body.sessionId || "").trim();
    const message = String(req.body.message || "").trim();
    const modeKey = String(req.body.mode || "").trim().toUpperCase();

    if (!sessionId) {
      return res.status(400).json({ error: "sessionId obrigatorio." });
    }

    if (!modeDefinitions[modeKey]) {
      return res.status(400).json({ error: "Modo ROVIS invalido ou ausente." });
    }

    if (!message && (!req.files || req.files.length === 0)) {
      return res.status(400).json({ error: "Envie texto, imagem, ou ambos." });
    }

    const files = Array.isArray(req.files) ? req.files : [];
    const prepared = await prepareRequestAssets(files);
    workDir = prepared.workDir;
    const { imagePaths } = prepared;

    const prompt = buildPrompt(sessionId, modeKey, message);
    const answer = await runCodexExec(prompt, imagePaths);
    appendSessionHistory({ sessionId, modeKey, message, filesCount: files.length, answer });

    res.json({
      id: randomUUID(),
      answer,
      mode: modeDefinitions[modeKey].label,
    });
  } catch (error) {
    res.status(500).json({
      error: normalizeCodexErrorMessage(error),
    });
  } finally {
    if (workDir) {
      await rm(workDir, { recursive: true, force: true }).catch(() => undefined);
    }
  }
});

app.post("/api/chat/stream", upload.array("images", 4), async (req, res) => {
  let workDir = "";

  try {
    if (!codexCliAvailable) {
      res.status(500).end(JSON.stringify({ error: "Codex CLI nao encontrado." }));
      return;
    }

    const sessionId = String(req.body.sessionId || "").trim();
    const message = String(req.body.message || "").trim();
    const modeKey = String(req.body.mode || "").trim().toUpperCase();
    const initMode = String(req.body.initMode || "").trim() === "true";

    if (!sessionId) {
      res.status(400).end(JSON.stringify({ error: "sessionId obrigatorio." }));
      return;
    }

    if (!modeDefinitions[modeKey]) {
      res.status(400).end(JSON.stringify({ error: "Modo ROVIS invalido ou ausente." }));
      return;
    }

    if (!initMode && !message && (!req.files || req.files.length === 0)) {
      res.status(400).end(JSON.stringify({ error: "Envie texto, imagem, ou ambos." }));
      return;
    }

    const files = Array.isArray(req.files) ? req.files : [];
    const prepared = await prepareRequestAssets(files);
    workDir = prepared.workDir;
    const { imagePaths } = prepared;

    res.writeHead(200, {
      "Content-Type": "application/x-ndjson; charset=utf-8",
      "Cache-Control": "no-cache, no-transform",
      Connection: "keep-alive",
      "Transfer-Encoding": "chunked",
    });

    sendStreamEvent(res, {
      type: "status",
      message: initMode
        ? `Inicializando o modo ${modeDefinitions[modeKey].label}.`
        : `Executando ${modeDefinitions[modeKey].label} via Codex CLI.`,
    });
    sendStreamEvent(res, { type: "status", message: "Preparando contexto da sessao." });
    if (files.length > 0) {
      sendStreamEvent(res, { type: "status", message: `Processando ${files.length} imagem(ns).` });
    }

    const prompt = buildPrompt(sessionId, modeKey, message, initMode);
    let streamClosed = false;

    const finalizeStream = async () => {
      if (streamClosed) return;
      streamClosed = true;
      if (workDir) {
        await rm(workDir, { recursive: true, force: true }).catch(() => undefined);
        workDir = "";
      }
      res.end();
    };

    runCodexExecStream({
      prompt,
      imagePaths,
      onEvent(event) {
        sendStreamEvent(res, event);
        if (event.type === "done") {
          sendStreamEvent(res, { type: "end" });
          finalizeStream();
        }
      },
      onAnswer(answer) {
        appendSessionHistory({ sessionId, modeKey, message, filesCount: files.length, answer });
        sendStreamEvent(res, { type: "answer", answer });
      },
      onError(error) {
        sendStreamEvent(res, { type: "error", error: normalizeCodexErrorMessage(error) });
        sendStreamEvent(res, { type: "end" });
        finalizeStream();
      },
    });
  } catch (error) {
    if (!res.headersSent) {
      res.status(500).end(JSON.stringify({ error: normalizeCodexErrorMessage(error) }));
    } else {
      sendStreamEvent(res, { type: "error", error: normalizeCodexErrorMessage(error) });
      sendStreamEvent(res, { type: "end" });
      res.end();
    }
  }
});

app.listen(port, () => {
  console.log(`ROVIS Chat online em http://localhost:${port}`);
});
