const STORAGE_KEY = "rovis_chat_sessions_v1";

const chatEl = document.getElementById("chat");
const composer = document.getElementById("composer");
const messageEl = document.getElementById("message");
const imagesEl = document.getElementById("images");
const previewEl = document.getElementById("preview");
const statusEl = document.getElementById("status");
const sendBtn = document.getElementById("sendBtn");
const tpl = document.getElementById("messageTpl");
const modeGateEl = document.getElementById("modeGate");
const modeOptionsEl = document.getElementById("modeOptions");
const activeModeEl = document.getElementById("activeMode");
const changeModeBtn = document.getElementById("changeModeBtn");
const heroKickerEl = document.getElementById("heroKicker");
const heroTitleEl = document.getElementById("heroTitle");
const heroTextEl = document.getElementById("heroText");
const sessionsListEl = document.getElementById("sessionsList");
const newSessionBtn = document.getElementById("newSessionBtn");

let sessionId = crypto.randomUUID();
let currentMode = "";
let availableModes = [];
let streamRunning = false;
let selectedFiles = [];
let sessions = loadSessions();
let livePanelNode = null;
let liveFeedNode = null;
let liveStateNode = null;
let progressPulseTimer = null;

const progressPulseMessages = [
  "Lendo o contexto atual.",
  "Refinando a proxima etapa.",
  "Conectando o pedido com o modo ativo.",
  "Organizando a execucao antes de responder.",
  "Consolidando o proximo passo para voce.",
];

const modeThemes = {
  DEFAULT: {
    bodyMode: "default",
    heroKicker: "Modo ROVIS",
    heroTitle: "Conversa simples, direta e com comportamento guiado por modo.",
    heroText: "O Codex CLI roda por tras dos panos. A interface fica focada em modo, chat, imagem e historico.",
  },
  ROVIS: {
    bodyMode: "rovis",
    heroKicker: "Modo central",
    heroTitle: "Planejamento, aprovacao, execucao e QA em um fluxo unico.",
    heroText: "Use este modo quando quiser o comportamento mais completo do ROVIS.",
  },
  ROVIS_FE: {
    bodyMode: "rovis-fe",
    heroKicker: "Modo frontend",
    heroTitle: "Foco em interface, comportamento visual e consumo de contrato.",
    heroText: "Use este modo para telas, interacoes, estados e acabamento de UI.",
  },
  ROVIS_BE: {
    bodyMode: "rovis-be",
    heroKicker: "Modo backend",
    heroTitle: "Foco em contrato, arquitetura, implementacao e handoff.",
    heroText: "Use este modo para fluxo PM, ARCH, BACK e validacao com mais rigidez.",
  },
  QA: {
    bodyMode: "qa",
    heroKicker: "Modo QA",
    heroTitle: "Foco em testes, qualidade, evidencias e relatorio.",
    heroText: "Use este modo para validar sistema, explorar falhas e medir qualidade.",
  },
};

function loadSessions() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveSessions() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(sessions));
}

function getActiveSession() {
  return sessions.find((item) => item.id === sessionId) || null;
}

function formatSessionTime(value) {
  return new Date(value).toLocaleString("pt-BR", {
    day: "2-digit",
    month: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function makeSessionTitle(modeKey, firstText = "") {
  const mode = availableModes.find((item) => item.key === modeKey);
  const prefix = mode ? mode.label : modeKey;
  const clean = firstText.replace(/\s+/g, " ").trim();
  return clean ? `${prefix}: ${clean.slice(0, 42)}` : `${prefix}: nova conversa`;
}

function createSession(modeKey) {
  sessionId = crypto.randomUUID();
  const now = Date.now();
  const entry = {
    id: sessionId,
    modeKey,
    title: makeSessionTitle(modeKey),
    createdAt: now,
    updatedAt: now,
    messages: [],
  };
  sessions.unshift(entry);
  saveSessions();
  renderSessions();
  return entry;
}

function upsertSessionMessage({ who, text }) {
  const session = getActiveSession();
  if (!session) return;
  session.messages.push({ who, text, createdAt: Date.now() });
  session.updatedAt = Date.now();
  if (session.messages.length === 1 || (session.messages.length === 2 && who === "ROVIS")) {
    session.title = makeSessionTitle(session.modeKey, text);
  } else if (who === "Voce" && session.messages.filter((item) => item.who === "Voce").length === 1) {
    session.title = makeSessionTitle(session.modeKey, text);
  }
  sessions.sort((a, b) => b.updatedAt - a.updatedAt);
  saveSessions();
  renderSessions();
}

function renderSessions() {
  sessionsListEl.innerHTML = "";

  if (sessions.length === 0) {
    const empty = document.createElement("div");
    empty.className = "session-empty";
    empty.textContent = "Nenhuma conversa ainda.";
    sessionsListEl.appendChild(empty);
    return;
  }

  sessions.forEach((session) => {
    const item = document.createElement("button");
    item.type = "button";
    item.className = `session-item${session.id === sessionId ? " active" : ""}`;
    item.innerHTML = [
      `<strong>${session.title}</strong>`,
      `<span>${session.modeKey}</span>`,
      `<small>${formatSessionTime(session.updatedAt)}</small>`,
    ].join("");
    item.addEventListener("click", () => openSession(session.id));
    sessionsListEl.appendChild(item);
  });
}

function newSession() {
  sessionId = crypto.randomUUID();
}

function setComposerEnabled(enabled) {
  messageEl.disabled = !enabled;
  imagesEl.disabled = !enabled;
  sendBtn.disabled = !enabled || streamRunning;
}

function addMessage(who, text, persist = true) {
  const node = tpl.content.firstElementChild.cloneNode(true);
  node.classList.add(who === "Voce" ? "user" : "assistant");
  node.querySelector(".who").textContent = who;
  node.querySelector(".bubble").textContent = text;
  chatEl.appendChild(node);
  chatEl.scrollTop = chatEl.scrollHeight;
  if (persist) {
    upsertSessionMessage({ who, text });
  }
  return node;
}

function setTypingMessage(text = "Em execucao") {
  const node = addMessage("ROVIS", "", false);
  node.classList.add("loading-message");
  node.querySelector(".bubble").innerHTML = [
    '<div class="loading-inline">',
    '<span class="loading-dots" aria-hidden="true"><i></i><i></i><i></i></span>',
    `<span class="loading-label">${text}</span>`,
    "</div>",
  ].join("");
  return node;
}

function setTypingLabel(node, text) {
  const label = node?.querySelector(".loading-label");
  if (label) {
    label.textContent = text;
  }
}

function applyTheme(modeKey) {
  const theme = modeThemes[modeKey] || modeThemes.DEFAULT;
  document.body.dataset.mode = theme.bodyMode;
  heroKickerEl.textContent = theme.heroKicker;
  heroTitleEl.textContent = theme.heroTitle;
  heroTextEl.textContent = theme.heroText;
}

function addLiveEntry(text, variant = "status") {
  ensureLivePanel();
  const entry = document.createElement("div");
  entry.className = `live-entry ${variant}`;
  entry.textContent = text;
  liveFeedNode.prepend(entry);
}

function clearLiveFeed() {
  ensureLivePanel();
  liveFeedNode.innerHTML = "";
}

function setLiveState(text) {
  ensureLivePanel();
  liveStateNode.textContent = text;
}

function setBusy(busy) {
  streamRunning = busy;
  setComposerEnabled(Boolean(currentMode));
  if (!busy) {
    stopProgressPulse();
  }
  sendBtn.textContent = busy ? "Enviando..." : "Enviar";
}

function startProgressPulse() {
  stopProgressPulse();

  progressPulseTimer = window.setInterval(() => {
    if (!streamRunning) return;
    const nextMessage = progressPulseMessages[Math.floor(Math.random() * progressPulseMessages.length)];
    addLiveEntry(nextMessage, "status soft");
  }, 5000);
}

function stopProgressPulse() {
  if (!progressPulseTimer) return;
  window.clearInterval(progressPulseTimer);
  progressPulseTimer = null;
}

function getLiveStatusMeta(message) {
  const normalized = String(message || "").toLowerCase();

  if (normalized.includes("inicializando")) {
    return { state: "Inicializando", entry: "Iniciando o modo selecionado.", loading: "Inicializando modo" };
  }

  if (normalized.includes("preparando contexto")) {
    return { state: "Mapeando contexto", entry: "Mapeando contexto da conversa.", loading: "Mapeando contexto" };
  }

  if (normalized.includes("processando") && normalized.includes("imagem")) {
    return { state: "Lendo imagens", entry: message, loading: "Lendo imagens" };
  }

  if (normalized.includes("sessao iniciada")) {
    return { state: "Sessao pronta", entry: "Sessao aberta. Indo para a proxima etapa.", loading: "Sessao pronta" };
  }

  if (normalized.includes("processando sua solicitacao")) {
    return { state: "Em execucao", entry: "ROVIS passou para a etapa de execucao.", loading: "Em execucao" };
  }

  if (normalized.includes("executando")) {
    return { state: "Executando", entry: message, loading: "Executando" };
  }

  return { state: "Processando", entry: message, loading: "Processando" };
}

function syncFileInput() {
  const transfer = new DataTransfer();
  selectedFiles.forEach((file) => transfer.items.add(file));
  imagesEl.files = transfer.files;
}

function renderPreview() {
  previewEl.innerHTML = "";

  if (selectedFiles.length === 0) return;

  selectedFiles.forEach((file, index) => {
    const card = document.createElement("article");
    card.className = "preview-card";

    const image = document.createElement("img");
    image.src = URL.createObjectURL(file);
    image.alt = file.name;
    image.addEventListener("load", () => URL.revokeObjectURL(image.src), { once: true });

    const meta = document.createElement("div");
    meta.className = "preview-meta";

    const name = document.createElement("strong");
    name.textContent = file.name;

    const size = document.createElement("span");
    size.textContent = `${Math.max(1, Math.round(file.size / 1024))} KB`;

    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "preview-remove";
    remove.textContent = "Remover";
    remove.addEventListener("click", () => {
      selectedFiles.splice(index, 1);
      syncFileInput();
      renderPreview();
    });

    meta.append(name, size, remove);
    card.append(image, meta);
    previewEl.appendChild(card);
  });
}

function ensureLivePanel() {
  if (livePanelNode && liveFeedNode && liveStateNode) return;

  livePanelNode = document.createElement("section");
  livePanelNode.className = "live-panel inline-live-panel";
  livePanelNode.innerHTML = [
    '<div class="live-head">',
    "<strong>Atividade em tempo real</strong>",
    '<span class="live-state">Aguardando modo</span>',
    "</div>",
    '<div class="live-feed"></div>',
  ].join("");

  liveFeedNode = livePanelNode.querySelector(".live-feed");
  liveStateNode = livePanelNode.querySelector(".live-state");
}

function mountLivePanelInChat() {
  ensureLivePanel();

  if (livePanelNode.parentElement !== chatEl) {
    chatEl.prepend(livePanelNode);
  }
}

async function streamChat({ message = "", files = [], initMode = false }) {
  const form = new FormData();
  form.append("sessionId", sessionId);
  form.append("mode", currentMode);
  form.append("message", message);
  form.append("initMode", String(initMode));
  files.forEach((file) => form.append("images", file));

  setBusy(true);
  mountLivePanelInChat();
  setLiveState(initMode ? "Inicializando modo" : "Em execucao");
  clearLiveFeed();
  addLiveEntry(`Modo ativo: ${currentMode}`);
  startProgressPulse();

  const typingNode = setTypingMessage(initMode ? "Inicializando modo" : "Em execucao");

  try {
    const res = await fetch("/api/chat/stream", {
      method: "POST",
      body: form,
    });

    if (!res.ok || !res.body) {
      let errorText = "Falha ao iniciar stream.";
      try {
        const payload = await res.json();
        errorText = payload.error || errorText;
      } catch {
        // noop
      }
      typingNode.querySelector(".bubble").textContent = `Erro: ${errorText}`;
      addLiveEntry(errorText, "error");
      setLiveState("Erro");
      upsertSessionMessage({ who: "ROVIS", text: `Erro: ${errorText}` });
      return;
    }

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    let finalAnswer = "";

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split("\n");
      buffer = lines.pop() || "";

      for (const line of lines) {
        if (!line.trim()) continue;
        let event;
        try {
          event = JSON.parse(line);
        } catch {
          continue;
        }

        if (event.type === "status") {
          const meta = getLiveStatusMeta(event.message);
          addLiveEntry(meta.entry, "status");
          setLiveState(meta.state);
          setTypingLabel(typingNode, meta.loading);
        } else if (event.type === "answer") {
          finalAnswer = event.answer || "";
          typingNode.classList.remove("loading-message");
          typingNode.querySelector(".bubble").textContent = finalAnswer;
          addLiveEntry("Resposta recebida.", "answer");
          setLiveState("Concluido");
        } else if (event.type === "error") {
          typingNode.classList.remove("loading-message");
          typingNode.querySelector(".bubble").textContent = `Erro: ${event.error || "falha no stream"}`;
          addLiveEntry(event.error || "falha no stream", "error");
          setLiveState("Erro");
          upsertSessionMessage({ who: "ROVIS", text: `Erro: ${event.error || "falha no stream"}` });
        } else if (event.type === "done") {
          addLiveEntry("Execucao concluida.", "done");
          if (!finalAnswer) {
            setLiveState("Concluido");
          }
        }
      }
    }

    if (finalAnswer) {
      upsertSessionMessage({ who: "ROVIS", text: finalAnswer });
    }
  } catch {
    typingNode.classList.remove("loading-message");
    typingNode.querySelector(".bubble").textContent = "Falha de conexao com o servidor.";
    addLiveEntry("Falha de conexao com o servidor.", "error");
    setLiveState("Erro de conexao");
    upsertSessionMessage({ who: "ROVIS", text: "Falha de conexao com o servidor." });
  } finally {
    setBusy(false);
  }
}

async function initializeMode(modeKey) {
  currentMode = modeKey;
  const mode = availableModes.find((item) => item.key === modeKey);
  activeModeEl.textContent = mode ? `Modo ${mode.label}` : "Modo desconhecido";
  modeGateEl.hidden = true;
  setComposerEnabled(true);
  createSession(modeKey);
  chatEl.innerHTML = "";
  mountLivePanelInChat();
  await streamChat({ initMode: true });
}

function openSession(id) {
  const session = sessions.find((item) => item.id === id);
  if (!session) return;

  sessionId = session.id;
  currentMode = session.modeKey;
  applyTheme(session.modeKey);
  const mode = availableModes.find((item) => item.key === session.modeKey);
  activeModeEl.textContent = mode ? `Modo ${mode.label}` : `Modo ${session.modeKey}`;
  modeGateEl.hidden = true;
  setComposerEnabled(true);
  clearLiveFeed();
  setLiveState("Sessao carregada");
  chatEl.innerHTML = "";
  mountLivePanelInChat();
  session.messages.forEach((message) => addMessage(message.who, message.text, false));
  renderSessions();
}

function renderModeOptions() {
  modeOptionsEl.innerHTML = "";
  availableModes.forEach((mode) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "mode-option";
    button.innerHTML = `<strong>${mode.label}</strong><span>${mode.description}</span>`;
    button.addEventListener("click", async () => {
      applyTheme(mode.key);
      await initializeMode(mode.key);
    });
    modeOptionsEl.appendChild(button);
  });
}

async function checkHealth() {
  try {
    const res = await fetch("/api/health");
    const data = await res.json();
    availableModes = Array.isArray(data.availableModes) ? data.availableModes : [];
    renderModeOptions();
    renderSessions();

    if (!data.codexCliAvailable) {
      statusEl.textContent = "Codex CLI offline";
      statusEl.style.background = "#693133";
      return;
    }

    statusEl.textContent = `Online (${data.model} via Codex CLI)`;
    statusEl.style.background = "";
  } catch {
    statusEl.textContent = "Servidor offline";
    statusEl.style.background = "#693133";
  }
}

imagesEl.addEventListener("change", () => {
  selectedFiles = [...imagesEl.files];
  renderPreview();
});

newSessionBtn.addEventListener("click", () => {
  currentMode = "";
  selectedFiles = [];
  syncFileInput();
  renderPreview();
  applyTheme("DEFAULT");
  activeModeEl.textContent = "Modo nao selecionado";
  setComposerEnabled(false);
  modeGateEl.hidden = false;
  clearLiveFeed();
  setLiveState("Aguardando modo");
});

changeModeBtn.addEventListener("click", () => {
  currentMode = "";
  selectedFiles = [];
  syncFileInput();
  renderPreview();
  applyTheme("DEFAULT");
  activeModeEl.textContent = "Modo nao selecionado";
  setComposerEnabled(false);
  modeGateEl.hidden = false;
  clearLiveFeed();
  setLiveState("Aguardando modo");
  addMessage("ROVIS", "Escolha o novo modo ROVIS para continuar.", false);
});

composer.addEventListener("submit", async (event) => {
  event.preventDefault();

  if (!currentMode) {
    modeGateEl.hidden = false;
    return;
  }

  const message = messageEl.value.trim();
  const files = [...selectedFiles];

  if (!message && files.length === 0) return;

  if (message) addMessage("Voce", message);
  if (files.length > 0) addMessage("Voce", `[${files.length} imagem(ns) enviada(s)]`);

  messageEl.value = "";
  selectedFiles = [];
  syncFileInput();
  renderPreview();

  await streamChat({ message, files });
});

setComposerEnabled(false);
applyTheme("DEFAULT");
ensureLivePanel();
mountLivePanelInChat();
setLiveState("Aguardando modo");
addMessage("ROVIS", "Ao iniciar, eu sempre vou perguntar qual modo ROVIS voce quer usar.", false);
renderSessions();
checkHealth();
