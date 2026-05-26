#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import KeepTogether
import os

# ── Configurações ──────────────────────────────────────────────────────────────
DATA_HORA   = "26/05/2026 14:07"
NOME_ARQUIVO = "relatorio-trading-2026-05-26-14h.pdf"
CAMINHO_PDF  = os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)

# ── Cores ──────────────────────────────────────────────────────────────────────
VERDE_ESCURO  = colors.HexColor("#1B5E20")
VERDE_MEDIO   = colors.HexColor("#2E7D32")
VERDE_CLARO   = colors.HexColor("#43A047")
VERDE_FUNDO   = colors.HexColor("#E8F5E9")
VERDE_HEADER  = colors.HexColor("#A5D6A7")
AMARELO       = colors.HexColor("#F9A825")
AMARELO_CLARO = colors.HexColor("#FFF9C4")
VERMELHO      = colors.HexColor("#C62828")
CINZA_ESCURO  = colors.HexColor("#212121")
CINZA_CLARO   = colors.HexColor("#F5F5F5")
BRANCO        = colors.white

# ── Documento ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    CAMINHO_PDF,
    pagesize=A4,
    leftMargin=1.8*cm,
    rightMargin=1.8*cm,
    topMargin=2*cm,
    bottomMargin=2*cm,
    title="Relatório Trading EA FC 26 – 26/05/2026",
    author="Trading Bot EA FC 26"
)

# ── Estilos ───────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def estilo(nome, **kw):
    return ParagraphStyle(nome, **kw)

s_titulo = estilo("titulo",
    fontSize=22, fontName="Helvetica-Bold",
    textColor=BRANCO, alignment=TA_CENTER, spaceAfter=4)

s_subtitulo = estilo("subtitulo",
    fontSize=12, fontName="Helvetica",
    textColor=VERDE_CLARO, alignment=TA_CENTER, spaceAfter=2)

s_data = estilo("data",
    fontSize=11, fontName="Helvetica",
    textColor=AMARELO, alignment=TA_CENTER, spaceAfter=0)

s_section = estilo("section",
    fontSize=13, fontName="Helvetica-Bold",
    textColor=BRANCO, spaceBefore=12, spaceAfter=6,
    backColor=VERDE_MEDIO, leftIndent=-6, rightIndent=-6,
    borderPad=5)

s_body = estilo("body",
    fontSize=9.5, fontName="Helvetica",
    textColor=CINZA_ESCURO, spaceAfter=4,
    leading=14, alignment=TA_JUSTIFY)

s_bullet = estilo("bullet",
    fontSize=9.5, fontName="Helvetica",
    textColor=CINZA_ESCURO, spaceAfter=3,
    leading=14, leftIndent=14, bulletIndent=4)

s_bold = estilo("bold",
    fontSize=9.5, fontName="Helvetica-Bold",
    textColor=CINZA_ESCURO, spaceAfter=3, leading=14)

s_aviso = estilo("aviso",
    fontSize=8.5, fontName="Helvetica-Oblique",
    textColor=colors.HexColor("#555555"), alignment=TA_JUSTIFY,
    leading=12, spaceAfter=4)

s_regra_num = estilo("regra_num",
    fontSize=10, fontName="Helvetica-Bold",
    textColor=VERDE_MEDIO, spaceAfter=2)

s_regra = estilo("regra",
    fontSize=9.2, fontName="Helvetica",
    textColor=CINZA_ESCURO, spaceAfter=5, leading=13,
    alignment=TA_JUSTIFY, leftIndent=12)

# ── Header Banner ─────────────────────────────────────────────────────────────
def header_banner():
    data = [
        [Paragraph("⚽ EA FC 26 — RELATÓRIO DE TRADING", s_titulo)],
        [Paragraph("Ultimate Team Market Intelligence", s_subtitulo)],
        [Paragraph(f"📅  {DATA_HORA}  UTC", s_data)],
    ]
    t = Table(data, colWidths=[17.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), VERDE_ESCURO),
        ("TOPPADDING",  (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,-1),(-1,-1), 10),
        ("ROUNDEDCORNERS", [8]),
    ]))
    return t

# ── Seção ──────────────────────────────────────────────────────────────────────
def secao(texto):
    data = [[Paragraph(f"  {texto}", s_section)]]
    t = Table(data, colWidths=[17.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), VERDE_MEDIO),
        ("TOPPADDING",  (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return t

# ── Separador ──────────────────────────────────────────────────────────────────
def sep():
    return HRFlowable(width="100%", thickness=0.5, color=VERDE_CLARO, spaceAfter=6)

# ── Conteúdo ──────────────────────────────────────────────────────────────────
story = []

# HEADER
story.append(header_banner())
story.append(Spacer(1, 10))

# ─── 1. CONTEXTO DO MERCADO ────────────────────────────────────────────────────
story.append(secao("1 │ CONTEXTO DO MERCADO — 26/05/2026"))
story.append(Spacer(1, 6))

contexto_items = [
    ("🔥 Evento Ativo Principal", "Ultimate TOTS (Team of the Season) — lançado em 22/05/2026, ativo até 29/05/2026. "
     "Os 60 melhores cards TOTS da temporada estão em packs simultaneamente (92–97 OVR). "
     "Inclui Harry Kane 97, Lamine Yamal 97, Luka Modrić 97, Bruno Fernandes 97 e Vitinha 97."),
    ("📜 SBCs End of an Era", "Série especial de SBCs liberados ao longo desta semana final de TOTS: "
     "Mohamed Salah 95 (Liverpool), Andrew Robertson 93 (Liverpool), Antoine Griezmann 93 (Atlético de Madrid), "
     "Bernardo Silva 93 (Man. City), Leon Goretzka e John Stones 91. "
     "Cada SBC exige squads de alto rating — aumentando a demanda por fodder 83–88."),
    ("📉 Tendência de Mercado", "CRASH de preços em andamento desde 22/05. Pack openings massivos derrubaram "
     "preços de jogadores META em 30–60%. É o momento ideal para comprar fodder barato e revendê-lo "
     "quando novos SBCs surgirem (geralmente quarta e quinta-feira)."),
    ("📆 Próximos Eventos (janela 48h)", "Novos SBCs de upgrade e desafios diários são esperados na "
     "quarta-feira 27/05 (17h BST) e quinta-feira 28/05. Div Rivals rewards abrem quinta de manhã, "
     "inundando o mercado de packs — preços caem pela manhã e sobem à noite."),
    ("🎮 Evolução de Cartas", "Evolution Max-90 OVR ativa, permitindo boostar cards 85–87 para até 90 OVR. "
     "Cartas de fullback (RB/LB) e volantes com potencial evolutivo estão subvalorizadas agora."),
]

for titulo_item, desc in contexto_items:
    row_data = [[
        Paragraph(f"<b>{titulo_item}</b>", s_bold),
        Paragraph(desc, s_body)
    ]]
    t = Table(row_data, colWidths=[4.2*cm, 13.2*cm])
    t.setStyle(TableStyle([
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("BACKGROUND",   (0,0), (-1,-1), VERDE_FUNDO),
        ("ROUNDEDCORNERS", [4]),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [VERDE_FUNDO, CINZA_CLARO]),
    ]))
    story.append(t)
    story.append(Spacer(1, 3))

story.append(Spacer(1, 8))

# ─── 2. TABELA DE OPORTUNIDADES ────────────────────────────────────────────────
story.append(secao("2 │ CARTAS RECOMENDADAS (Budget: 40.000 coins)"))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Margem líquida calculada após a taxa de 5% da EA sobre o preço de venda. "
    "<b>Preços baseados em médias de mercado coletadas em 26/05/2026 às 14h07 UTC.</b>",
    s_body))
story.append(Spacer(1, 6))

# Cabeçalho da tabela
cabecalho = [
    Paragraph("<b>Jogador</b>", estilo("th", fontSize=8.5, fontName="Helvetica-Bold",
              textColor=BRANCO, alignment=TA_CENTER)),
    Paragraph("<b>OVR</b>", estilo("th2", fontSize=8.5, fontName="Helvetica-Bold",
              textColor=BRANCO, alignment=TA_CENTER)),
    Paragraph("<b>Clube / Liga</b>", estilo("th3", fontSize=8.5, fontName="Helvetica-Bold",
              textColor=BRANCO, alignment=TA_CENTER)),
    Paragraph("<b>Compra\n(coins)</b>", estilo("th4", fontSize=8.5, fontName="Helvetica-Bold",
              textColor=BRANCO, alignment=TA_CENTER)),
    Paragraph("<b>Venda\n(coins)</b>", estilo("th5", fontSize=8.5, fontName="Helvetica-Bold",
              textColor=BRANCO, alignment=TA_CENTER)),
    Paragraph("<b>Margem\nLíquida</b>", estilo("th6", fontSize=8.5, fontName="Helvetica-Bold",
              textColor=BRANCO, alignment=TA_CENTER)),
    Paragraph("<b>Estratégia</b>", estilo("th7", fontSize=8.5, fontName="Helvetica-Bold",
              textColor=BRANCO, alignment=TA_CENTER)),
]

def cel(txt, bold=False, align=TA_CENTER, size=8.5):
    fn = "Helvetica-Bold" if bold else "Helvetica"
    return Paragraph(txt, estilo("c", fontSize=size, fontName=fn,
                                  textColor=CINZA_ESCURO, alignment=align, leading=11))

# Dados dos jogadores
# Cálculo da margem: margem = venda * 0.95 - compra
jogadores = [
    # (Nome, OVR, Clube/Liga, Compra, Venda, Estratégia)
    ("Jonathan Tah",        "87", "B. Leverkusen\nBundesliga",  3_200,  4_800, "Fodder SBC — comprar Ter/Qua, vender quando SBC drop"),
    ("Klara Bühl",          "85", "Bayern de Munich\nBundesliga", 1_800, 2_700, "Fodder 85+ SBC, alta rotatividade"),
    ("Rubén Dias",          "85", "Man. City\nPremier League",   2_000, 3_000, "Fodder premium — buscar BIN baixo"),
    ("Ada Hegerberg",       "87", "Lyon\nD1 Arkema (W)",         3_000, 4_500, "Fodder 87 — vender qdo SBC novo cair"),
    ("Ann Katrin Berger",   "87", "Chelsea W\nWSL",              2_800, 4_200, "Fodder GK 87, raro em stock"),
    ("Lucy Bronze",         "87", "Barcelona W\nLiga F (W)",     3_000, 4_400, "Fodder FB 87 — Evolution demand"),
    ("Perle Morroni",       "83", "Paris FC W\nD1 Arkema (W)",   1_200, 1_900, "Massa de fodder 83 barato — comprar 10+"),
    ("Giovanna Hoffmann",   "83", "Eintracht Frankfurt W\nBundesliga (W)", 1_100, 1_800, "Idem acima — ST barato"),
    ("Leon Goretzka",       "86", "Bayern de Munich\nBundesliga",  2_200, 3_400, "Fodder 86 + linkagem Bundesliga"),
    ("John Stones",         "86", "Man. City\nPremier League",   2_100, 3_200, "Fodder CB PL 86"),
]

def margem(compra, venda):
    liquido = round(venda * 0.95 - compra)
    pct = round((liquido / compra) * 100)
    cor = "#1B5E20" if pct >= 20 else ("#E65100" if pct < 10 else "#1565C0")
    return f'<font color="{cor}"><b>+{liquido:,}\n({pct}%)</b></font>'.replace(",", ".")

linhas = [cabecalho]
for i, (nome, ovr, clube, compra, venda, estrat) in enumerate(jogadores):
    linha = [
        cel(nome, bold=True, align=TA_LEFT),
        cel(ovr, bold=True),
        cel(clube, align=TA_LEFT, size=8),
        cel(f"{compra:,}".replace(",", "."), bold=True),
        cel(f"{venda:,}".replace(",", "."), bold=True),
        Paragraph(margem(compra, venda), estilo("mg", fontSize=8.5, fontName="Helvetica-Bold",
                                                  alignment=TA_CENTER, leading=11,
                                                  textColor=CINZA_ESCURO)),
        cel(estrat, align=TA_LEFT, size=7.8),
    ]
    linhas.append(linha)

tabela = Table(linhas, colWidths=[3.0*cm, 1.0*cm, 2.8*cm, 1.7*cm, 1.7*cm, 2.0*cm, 5.2*cm])
tabela.setStyle(TableStyle([
    # Header
    ("BACKGROUND",    (0,0), (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("FONTSIZE",      (0,0), (-1,-1), 8.5),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [BRANCO, VERDE_FUNDO]),
    ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#BDBDBD")),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 4),
    ("RIGHTPADDING",  (0,0), (-1,-1), 4),
    # Alternar leve destaque nas colunas de preço
    ("BACKGROUND",    (3,1), (4,-1), colors.HexColor("#F1F8E9")),
]))
story.append(tabela)
story.append(Spacer(1, 6))

# Nota rodapé tabela
story.append(Paragraph(
    "⚠ Preços são estimativas baseadas em médias históricas e dados de mercado coletados. "
    "Verifique sempre em futbin.com ou fut.gg antes de comprar. Margem líquida = Venda × 0,95 − Compra.",
    s_aviso))
story.append(Spacer(1, 10))

# ─── 3. ESTRATÉGIA DE TIMING ───────────────────────────────────────────────────
story.append(secao("3 │ ESTRATÉGIA DE TIMING"))
story.append(Spacer(1, 6))

timing_data = [
    ["Quando", "O que fazer", "Por quê"],
    ["Agora\n(14h–18h UTC)", "Comprar fodder 83–87 em BIN baixo.\nAlvo: 10–20 cartas no total.",
     "TOTS crash ainda ativo. Preços no fundo."],
    ["Qua 27/05\n17h BST (16h UTC)", "Monitorar novos SBCs/upgrades.\nVender 30–60 min após lançamento.",
     "Spikes de preço no início de cada SBC."],
    ["Qui 28/05\n06h–10h UTC", "COMPRAR durante abertura de Rivals rewards.\nFodder 85–87 fica mais barato.",
     "Flood de packs = queda de preços. Melhor janela de compra semanal."],
    ["Qui 28/05\n18h–22h UTC", "VENDER fodder e cartas adquiridas mais cedo.",
     "Pico de jogadores online. Maior demanda, melhores preços."],
    ["Sex 29/05\n16h–18h UTC", "Ultimate TOTS sai de packs. Vender META cards.\nNão segurar hodl de longo prazo.",
     "Após saída de packs, preços de cartas TOTS tendem a subir lentamente."],
]

t_tim = Table(timing_data, colWidths=[3.0*cm, 7.5*cm, 6.9*cm])
t_tim.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), VERDE_MEDIO),
    ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 8.5),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [BRANCO, AMARELO_CLARO]),
    ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#BDBDBD")),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 5),
    ("ALIGN",         (0,0), (-1,-1), "LEFT"),
    ("ALIGN",         (0,0), (0,-1), "CENTER"),
]))
story.append(t_tim)
story.append(Spacer(1, 10))

# ─── 4. ESTIMATIVA DE RETORNO 48H ──────────────────────────────────────────────
story.append(secao("4 │ ESTIMATIVA DE RETORNO EM 48 HORAS"))
story.append(Spacer(1, 6))

retorno_data = [
    ["Cenário", "Estratégia", "Coins investidos", "Retorno estimado", "Lucro líquido", "ROI"],
    ["🐢 Conservador",
     "SBC Fodder Flip\n(83–85 rating)\n10 compras × ~1.500",
     "15.000",
     "~19.000",
     "~+3.200",
     "~21%"],
    ["⚖ Moderado",
     "Fodder 85–87 + Thursday flip\n15 compras × ~2.500",
     "37.500",
     "~50.000",
     "~+10.000",
     "~27%"],
    ["🚀 Otimista",
     "Mix 83–87 + Spike SBC qua/qui\n20 compras diversificadas",
     "40.000",
     "~57.000",
     "~+14.200",
     "~36%"],
]

t_ret = Table(retorno_data, colWidths=[2.5*cm, 5.0*cm, 2.8*cm, 2.8*cm, 2.8*cm, 1.5*cm])
t_ret.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 8.5),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [CINZA_CLARO, VERDE_FUNDO, AMARELO_CLARO]),
    ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#BDBDBD")),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 4),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("ALIGN",         (0,1), (1,-1), "LEFT"),
    # ROI em verde
    ("TEXTCOLOR",     (5,1), (5,-1), VERDE_ESCURO),
    ("FONTNAME",      (5,1), (5,-1), "Helvetica-Bold"),
]))
story.append(t_ret)
story.append(Spacer(1, 6))
story.append(Paragraph(
    "⚠ Estimativas baseadas em ciclos históricos de TOTS e dados atuais de mercado. "
    "O cenário otimista depende de pelo menos um SBC novo sendo lançado na quarta ou quinta-feira. "
    "Nunca invista mais do que está disposto a perder — o mercado pode surpreender.",
    s_aviso))
story.append(Spacer(1, 10))

# ─── 5. 8 REGRAS DE OURO ──────────────────────────────────────────────────────
story.append(secao("5 │ 8 REGRAS DE OURO DO TRADE"))
story.append(Spacer(1, 6))

regras = [
    ("1", "Compre no crash, venda no spike",
     "O TOTS é o maior crash do ano. Compre fodder enquanto o mercado está saturado de packs. "
     "Venda quando um novo SBC gerar demanda — geralmente 30–60 minutos após o lançamento."),
    ("2", "Nunca pague BIN cheio",
     "Use filtros de leilão e espere por BINs abaixo da média. "
     "Defina um preço máximo de compra e não o ultrapasse por ansiedade."),
    ("3", "Diversifique as cartas",
     "Não concentre todo o budget em uma única carta. Compre de 5 a 20 unidades de cards "
     "diferentes para diluir o risco de stagnação de preço."),
    ("4", "Respeite a taxa de 5% da EA",
     "Calcule SEMPRE: Lucro = Venda × 0,95 − Compra. "
     "Uma venda de 3.000 coins gera apenas 2.850 líquidos. Errar esse cálculo "
     "transforma lucro em prejuízo."),
    ("5", "Quinta-feira é a melhor janela de compra",
     "A abertura de rewards do Division Rivals inunda o mercado de packs. "
     "Preços despencam entre 06h–10h UTC. Compre nesse horário e venda à noite (18h–22h UTC)."),
    ("6", "Monitore SBCs ativos antes de vender",
     "Sempre verifique se há um SBC ativo que demande a carta que você quer vender. "
     "Se houver, o preço pode subir ainda mais — aguarde 1–2h para maximizar o retorno."),
    ("7", "Não segure cartas por mais de 48h",
     "No fim de ciclo (maio/junho) o power creep é acelerado. "
     "Cards que valem 5.000 coins hoje podem valer 2.000 na semana que vem. "
     "Priorize flips rápidos em vez de investimentos de longo prazo."),
    ("8", "Respeite seu stop-loss",
     "Se uma carta não vendeu em 24h ao preço alvo, abaixe 10–15% e saia. "
     "Aceitar um lucro menor é melhor do que ficar preso com cartas desvalorizando."),
]

for num, titulo_r, desc_r in regras:
    row = [[
        Paragraph(f"#{num}", estilo("rn", fontSize=14, fontName="Helvetica-Bold",
                                     textColor=VERDE_MEDIO, alignment=TA_CENTER)),
        Paragraph(f"<b>{titulo_r}</b><br/>{desc_r}",
                  estilo("rd", fontSize=9, fontName="Helvetica",
                         textColor=CINZA_ESCURO, leading=13, alignment=TA_JUSTIFY))
    ]]
    bg = VERDE_FUNDO if int(num) % 2 == 0 else BRANCO
    t = Table(row, colWidths=[1.0*cm, 16.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), bg),
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",   (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0), (-1,-1), 5),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("GRID",         (0,0), (-1,-1), 0.3, colors.HexColor("#BDBDBD")),
    ]))
    story.append(t)

story.append(Spacer(1, 12))

# ─── DISCLAIMER ───────────────────────────────────────────────────────────────
story.append(sep())
disclaimer_box = [[
    Paragraph(
        "<b>⚠ DISCLAIMER</b><br/>"
        "Este relatório é gerado automaticamente com base em dados de mercado públicos e tendências "
        "históricas do EA FC 26 Ultimate Team. Os preços apresentados são estimativas e podem variar "
        "significativamente dependendo da plataforma (PlayStation/Xbox/PC), horário e eventos em andamento. "
        "Não há garantia de lucro. O trading em FUT envolve riscos e os preços podem cair após a compra. "
        "Consulte sempre futbin.com, fut.gg ou teamgullit.com para verificar preços em tempo real antes "
        "de executar qualquer operação. O autor não se responsabiliza por perdas decorrentes do uso "
        "deste relatório. EA, EA FC e Ultimate Team são marcas registradas da Electronic Arts Inc.",
        s_aviso)
]]
t_dis = Table(disclaimer_box, colWidths=[17.4*cm])
t_dis.setStyle(TableStyle([
    ("BACKGROUND",   (0,0), (-1,-1), colors.HexColor("#FFEBEE")),
    ("TOPPADDING",   (0,0), (-1,-1), 8),
    ("BOTTOMPADDING",(0,0), (-1,-1), 8),
    ("LEFTPADDING",  (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("BOX",          (0,0), (-1,-1), 1, VERMELHO),
    ("ROUNDEDCORNERS", [4]),
]))
story.append(t_dis)
story.append(Spacer(1, 6))

# Rodapé
story.append(Paragraph(
    f"Relatório gerado em {DATA_HORA} UTC  •  Repositório: github.com/kaiohsferreira/fifa-trading  •  Budget: 40.000 coins",
    estilo("footer", fontSize=7.5, fontName="Helvetica",
           textColor=colors.HexColor("#9E9E9E"), alignment=TA_CENTER)
))

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF gerado: {CAMINHO_PDF}")
