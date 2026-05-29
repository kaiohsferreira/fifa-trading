#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime

# ── Config ──────────────────────────────────────────────────────────────────
REPORT_DATE = "29/05/2026 08:06"
OUTPUT_FILE = "relatorio-trading-2026-05-29-08h.pdf"

# ── Color palette ────────────────────────────────────────────────────────────
DARK_BG    = colors.HexColor("#0D1117")
CARD_BG    = colors.HexColor("#161B22")
ACCENT     = colors.HexColor("#00D4AA")
ACCENT2    = colors.HexColor("#FFD700")
TEXT_WHITE = colors.HexColor("#E6EDF3")
TEXT_GRAY  = colors.HexColor("#8B949E")
GREEN_POS  = colors.HexColor("#3FB950")
RED_NEG    = colors.HexColor("#F85149")
HEADER_BG  = colors.HexColor("#1F2937")
ROW_ALT    = colors.HexColor("#1A2233")
ROW_MAIN   = colors.HexColor("#111827")

# ── Document ──────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=A4,
    rightMargin=1.5*cm,
    leftMargin=1.5*cm,
    topMargin=1.5*cm,
    bottomMargin=1.5*cm,
)

# ── Styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def style(name, parent="Normal", **kw):
    s = ParagraphStyle(name, parent=styles[parent], **kw)
    return s

S = {
    "title": style("title", fontSize=22, textColor=ACCENT, alignment=TA_CENTER,
                   spaceAfter=4, fontName="Helvetica-Bold"),
    "subtitle": style("subtitle", fontSize=13, textColor=ACCENT2,
                      alignment=TA_CENTER, spaceAfter=2, fontName="Helvetica-Bold"),
    "date": style("date", fontSize=10, textColor=TEXT_GRAY, alignment=TA_CENTER,
                  spaceAfter=8),
    "section": style("section", fontSize=13, textColor=ACCENT,
                     fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=4),
    "body": style("body", fontSize=9, textColor=TEXT_WHITE, leading=14,
                  alignment=TA_JUSTIFY, spaceAfter=4),
    "bullet": style("bullet", fontSize=9, textColor=TEXT_WHITE, leading=13,
                    leftIndent=14, spaceAfter=2),
    "small": style("small", fontSize=8, textColor=TEXT_GRAY, leading=11,
                   alignment=TA_JUSTIFY),
    "highlight": style("highlight", fontSize=9, textColor=ACCENT2,
                       fontName="Helvetica-Bold", leading=13, leftIndent=14,
                       spaceAfter=2),
    "rule_title": style("rule_title", fontSize=10, textColor=ACCENT2,
                        fontName="Helvetica-Bold", spaceAfter=2),
    "rule_body": style("rule_body", fontSize=9, textColor=TEXT_WHITE,
                       leading=13, leftIndent=12, spaceAfter=6),
    "warning": style("warning", fontSize=8, textColor=colors.HexColor("#FFA657"),
                     leading=11, alignment=TA_JUSTIFY),
}

def HR():
    return HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=6, spaceBefore=6)

def SP(h=6):
    return Spacer(1, h)

# ── Build content ──────────────────────────────────────────────────────────────
story = []

# ─── HEADER BANNER ───────────────────────────────────────────────────────────
banner_data = [[
    Paragraph("⚽ EA FC 26 ULTIMATE TEAM", S["title"]),
]]
banner = Table(banner_data, colWidths=[17.5*cm])
banner.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), DARK_BG),
    ("TOPPADDING",    (0, 0), (-1, -1), 14),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING",   (0, 0), (-1, -1), 10),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
    ("ROUNDEDCORNERS", [6]),
]))
story.append(banner)
story.append(SP(4))

story.append(Paragraph("RELATÓRIO DIÁRIO DE TRADING", S["subtitle"]))
story.append(Paragraph(f"Data/Hora: {REPORT_DATE} UTC", S["date"]))
story.append(Paragraph("Budget: 40.000 coins  |  Estratégia: SBC Fodder + Thursday Flip + Evolution Invest", S["date"]))
story.append(HR())

# ─── 1. CONTEXTO DO MERCADO ───────────────────────────────────────────────────
story.append(Paragraph("1. CONTEXTO DO MERCADO — 29/05/2026", S["section"]))

context_items = [
    ("<b>TOTS ENCERRADO:</b> O Team of the Season terminou hoje (29/05) e as cartas TOTS "
     "saíram dos packs normais. Isso gera dois efeitos: (a) preços de fodder atingem o "
     "piso sazonal enquanto o mercado ainda digere o excesso de supply; (b) nos próximos "
     "2–3 dias a demanda por SBC fodder vai subir com os novos SBCs do Prime Heroes."),

    ("<b>PRIME HEROES LIVE HOJE:</b> O novo promo Prime Heroes foi ao ar nesta sexta-feira "
     "(29/05) às 18h BST / 14h BRT. A promo traz cartas Heroes com 99 em um atributo fixo "
     "(ex.: Eden Hazard 99 Dribbling, Yaya Touré 99 Passing, Jaap Stam 99 Defending). "
     "Duração: 1 semana (até 05/06). SBCs e Objetivos serão liberados ao longo da semana "
     "gerando picos de demanda por fodder 85–88."),

    ("<b>FESTIVAL OF FOOTBALL se aproxima:</b> A partir de 05/06 começa o Festival of "
     "Football com Path to Glory (live cards ligados ao Mundial). Isso aumenta o apetite "
     "geral por cartas de qualidade e pode elevar preços de TOTS e Heroes até lá."),

    ("<b>MERCADO EM BAIXA TÉCNICA:</b> A release das cartas RTTF das vencedoras da Women's "
     "Champions League causou pânico e venda massiva. O mercado está em queda livre no "
     "topo (cartas 94+), mas o fodder de médio rating (83–88) está próximo de mínimas "
     "históricas — janela ideal de compra."),

    ("<b>QUINTA-FEIRA FLIP WINDOW:</b> Rewards do Division Rivals foram distribuídos "
     "ontem (28/05). A onda de supply extra ainda está no mercado hoje cedo, criando "
     "oportunidade de compra antes da abertura de packs do Prime Heroes esta tarde."),
]
for item in context_items:
    story.append(Paragraph(f"• {item}", S["bullet"]))
    story.append(SP(3))

story.append(HR())

# ─── 2. TABELA DE OPORTUNIDADES ───────────────────────────────────────────────
story.append(Paragraph("2. TABELA DE CARTAS RECOMENDADAS", S["section"]))
story.append(Paragraph(
    "Preços baseados em FUTBIN/FUT.GG (29/05/2026 manhã). Margem líquida = "
    "(Venda × 0,95) − Compra. Verificar preços em tempo real antes de executar.",
    S["small"]
))
story.append(SP(6))

# Table header
col_headers = [
    "Jogador", "OVR", "Clube", "Compra\n(coins)", "Venda\n(coins)",
    "Margem\nLíquida", "% Lucro", "Estratégia"
]

# Data rows: [name, ovr, club, buy, sell, net, pct, strategy]
def net(buy, sell):
    return int(sell * 0.95) - buy

def pct(buy, sell):
    n = net(buy, sell)
    return f"+{int(n/buy*100)}%"

cards = [
    ("Unai Simón",      85, "Athletic Club",    800,  1_300, net(800, 1_300),  pct(800, 1_300),  "SBC Fodder"),
    ("V. Miedema",      85, "Arsenal WSL",      850,  1_350, net(850, 1_350),  pct(850, 1_350),  "SBC Fodder"),
    ("Ibou Konaté",     86, "Liverpool",        750,  1_200, net(750, 1_200),  pct(750, 1_200),  "SBC Fodder"),
    ("Sandro Tonali",   86, "Newcastle Utd",  1_000,  1_800, net(1000,1_800),  pct(1000,1_800),  "Flip + SBC"),
    ("Jonathan Tah",    87, "Bayern Munich",  1_500,  2_600, net(1500,2_600),  pct(1500,2_600),  "SBC Fodder"),
    ("Sam Kerr",        87, "Chelsea",        1_400,  2_400, net(1400,2_400),  pct(1400,2_400),  "SBC Fodder"),
    ("Alexia Putellas", 88, "FC Barcelona",   2_500,  4_200, net(2500,4_200),  pct(2500,4_200),  "Flip Premium"),
    ("Rúben Dias",      88, "Man. City",      2_800,  4_800, net(2800,4_800),  pct(2800,4_800),  "Flip Premium"),
]

def fmt(n):
    return f"{n:,}".replace(",", ".")

table_data = [col_headers]
for name, ovr, club, buy, sell, margin, p, strat in cards:
    table_data.append([
        name, str(ovr), club, fmt(buy), fmt(sell), fmt(margin), p, strat
    ])

col_w = [3.4*cm, 1.1*cm, 3.0*cm, 1.8*cm, 1.8*cm, 1.9*cm, 1.5*cm, 2.5*cm]

tbl = Table(table_data, colWidths=col_w, repeatRows=1)
tbl.setStyle(TableStyle([
    # Header
    ("BACKGROUND",   (0, 0), (-1, 0), HEADER_BG),
    ("TEXTCOLOR",    (0, 0), (-1, 0), ACCENT),
    ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE",     (0, 0), (-1, 0), 8),
    ("ALIGN",        (0, 0), (-1, 0), "CENTER"),
    ("VALIGN",       (0, 0), (-1, 0), "MIDDLE"),
    ("TOPPADDING",   (0, 0), (-1, 0), 6),
    ("BOTTOMPADDING",(0, 0), (-1, 0), 6),
    # Rows
    ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE",     (0, 1), (-1, -1), 8),
    ("TEXTCOLOR",    (0, 1), (-1, -1), TEXT_WHITE),
    ("ALIGN",        (1, 1), (-1, -1), "CENTER"),
    ("ALIGN",        (0, 1), (0, -1), "LEFT"),
    ("ALIGN",        (2, 1), (2, -1), "LEFT"),
    ("VALIGN",       (0, 1), (-1, -1), "MIDDLE"),
    ("TOPPADDING",   (0, 1), (-1, -1), 5),
    ("BOTTOMPADDING",(0, 1), (-1, -1), 5),
    ("LEFTPADDING",  (0, 0), (-1, -1), 5),
    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    # Alternating rows
    ("BACKGROUND", (0, 1), (-1, 1), ROW_MAIN),
    ("BACKGROUND", (0, 2), (-1, 2), ROW_ALT),
    ("BACKGROUND", (0, 3), (-1, 3), ROW_MAIN),
    ("BACKGROUND", (0, 4), (-1, 4), ROW_ALT),
    ("BACKGROUND", (0, 5), (-1, 5), ROW_MAIN),
    ("BACKGROUND", (0, 6), (-1, 6), ROW_ALT),
    ("BACKGROUND", (0, 7), (-1, 7), ROW_MAIN),
    ("BACKGROUND", (0, 8), (-1, 8), ROW_ALT),
    # Margin column green
    ("TEXTCOLOR",  (5, 1), (5, -1), GREEN_POS),
    ("FONTNAME",   (5, 1), (5, -1), "Helvetica-Bold"),
    ("TEXTCOLOR",  (6, 1), (6, -1), GREEN_POS),
    ("FONTNAME",   (6, 1), (6, -1), "Helvetica-Bold"),
    # Border
    ("LINEBELOW",  (0, 0), (-1, 0), 1.5, ACCENT),
    ("LINEBELOW",  (0, -1), (-1, -1), 0.5, TEXT_GRAY),
    ("LINEBEFORE", (0, 0), (0, -1), 2, ACCENT),
    ("LINEAFTER",  (-1, 0), (-1, -1), 0.5, TEXT_GRAY),
    ("ROWBACKGROUNDS", (0, 0), (-1, -1), [None]),
    ("BOX",        (0, 0), (-1, -1), 1, colors.HexColor("#30363D")),
    ("INNERGRID",  (0, 0), (-1, -1), 0.3, colors.HexColor("#21262D")),
]))
story.append(tbl)
story.append(SP(4))

# Budget allocation mini-table
story.append(Paragraph("Alocação do Budget (40.000 coins):", S["highlight"]))

budget_data = [
    ["Segmento", "Cartas", "Qtd", "Investimento"],
    ["85-rated SBC Fodder", "Simón / Miedema",        "20x", "16.500c"],
    ["86-rated SBC Fodder", "Konaté / Tonali",         "10x",  "8.750c"],
    ["87-rated Fodder",     "Tah / Kerr",               "6x",  "8.700c"],
    ["88-rated Premium",    "Putellas / Dias",          "2x",  "5.300c"],
    ["Reserva de emergência", "—",                      "—",   "0.750c"],
    ["TOTAL",               "",                         "",  "40.000c"],
]

bw = [5.0*cm, 4.5*cm, 2.0*cm, 3.5*cm]
btbl = Table(budget_data, colWidths=bw)
btbl.setStyle(TableStyle([
    ("BACKGROUND",   (0, 0), (-1, 0), HEADER_BG),
    ("TEXTCOLOR",    (0, 0), (-1, 0), ACCENT2),
    ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE",     (0, 0), (-1, -1), 8),
    ("TEXTCOLOR",    (0, 1), (-1, -2), TEXT_WHITE),
    ("BACKGROUND",   (0, 1), (-1, -2), ROW_MAIN),
    ("BACKGROUND",   (0, -1), (-1, -1), HEADER_BG),
    ("TEXTCOLOR",    (0, -1), (-1, -1), ACCENT),
    ("FONTNAME",     (0, -1), (-1, -1), "Helvetica-Bold"),
    ("ALIGN",        (2, 0), (-1, -1), "CENTER"),
    ("ALIGN",        (3, 0), (-1, -1), "RIGHT"),
    ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING",   (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
    ("LEFTPADDING",  (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("INNERGRID",    (0, 0), (-1, -1), 0.3, colors.HexColor("#21262D")),
    ("BOX",          (0, 0), (-1, -1), 1, colors.HexColor("#30363D")),
]))
story.append(btbl)
story.append(HR())

# ─── 3. ESTRATÉGIA DE TIMING ──────────────────────────────────────────────────
story.append(Paragraph("3. ESTRATÉGIA DE TIMING", S["section"]))

timing = [
    ("AGORA (08h–13h BRT — pré-drop)", [
        "Comprar todo o fodder 85–86 enquanto o supply dos Rivals Rewards ainda está alto.",
        "O mercado ainda não reagiu ao Prime Heroes. Preços próximos do piso.",
        "Verificar FUTBIN antes de cada compra: procurar cartas abaixo da média das últimas 24h.",
        "Evitar cartas acima de 2.000c neste momento (risco de quedas com pack openings à tarde).",
    ]),
    ("14h–18h BRT — Prime Heroes LIVE", [
        "Apertura massiva de packs → supply sobe → preços caem 10–20% por ~1–2h.",
        "Janela de COMPRA para cards 87–88 que forem listados em pânico.",
        "Monitorar mercado a cada 15min durante este período.",
        "Não vender nada agora; aguardar a curva de recuperação.",
    ]),
    ("Sábado 29/05 — 18h BRT até Domingo 30/05", [
        "Mercado começa a absorver supply. Demanda por SBC fodder começa a subir.",
        "Primeiros SBCs do Prime Heroes serão confirmados → fodder 85–88 dispara.",
        "VENDER 50–60% do estoque de 85 e 86 neste pico de demanda.",
        "Manter as cartas 87–88 para a segunda onda (segunda/terça quando SBCs de 87+ aparecerem).",
    ]),
    ("Segunda 01/06 — Terça 02/06", [
        "Novos SBCs de Prime Heroes geralmente chegam segunda ou terça.",
        "Preços de 87–88 devem ter uma segunda valorização.",
        "VENDER restante do estoque. Meta: zerar posição antes de quinta-feira.",
        "Guardar coins para nova janela de compra na quinta (Rivals Rewards).",
    ]),
]

for period, tips in timing:
    story.append(Paragraph(f"◆ {period}", S["rule_title"]))
    for tip in tips:
        story.append(Paragraph(f"  → {tip}", S["bullet"]))
    story.append(SP(4))

story.append(HR())

# ─── 4. ESTIMATIVA DE RETORNO 48H ─────────────────────────────────────────────
story.append(Paragraph("4. ESTIMATIVA DE RETORNO EM 48H", S["section"]))

return_data = [
    ["Cenário", "Condições", "Receita Bruta", "Taxa EA (5%)", "Lucro Líquido", "Capital Final"],
    ["Conservador",
     "Fodder sobe 20–30%\nSBCs medianos",
     "48.000c", "−2.400c", "+5.600c", "45.600c"],
    ["Moderado",
     "Fodder sobe 40–50%\nSBCs ativos",
     "56.000c", "−2.800c", "+13.200c", "53.200c"],
    ["Otimista",
     "Fodder sobe 60–80%\nSBCs múltiplos + demanda",
     "64.000c", "−3.200c", "+20.800c", "60.800c"],
]

rw = [2.4*cm, 4.5*cm, 2.5*cm, 2.5*cm, 2.5*cm, 2.6*cm]
rtbl = Table(return_data, colWidths=rw, rowHeights=[None, 1.1*cm, 1.1*cm, 1.1*cm])
rtbl.setStyle(TableStyle([
    ("BACKGROUND",   (0, 0), (-1, 0), HEADER_BG),
    ("TEXTCOLOR",    (0, 0), (-1, 0), ACCENT),
    ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE",     (0, 0), (-1, -1), 8),
    ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
    ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ("TEXTCOLOR",    (0, 1), (0, -1), TEXT_WHITE),
    ("FONTNAME",     (0, 1), (0, -1), "Helvetica-Bold"),
    ("TEXTCOLOR",    (1, 1), (1, -1), TEXT_GRAY),
    ("TEXTCOLOR",    (2, 1), (4, -1), TEXT_WHITE),
    ("TEXTCOLOR",    (4, 1), (4, -1), GREEN_POS),
    ("FONTNAME",     (4, 1), (4, -1), "Helvetica-Bold"),
    ("TEXTCOLOR",    (5, 1), (5, -1), ACCENT2),
    ("FONTNAME",     (5, 1), (5, -1), "Helvetica-Bold"),
    ("BACKGROUND",   (0, 1), (-1, 1), ROW_MAIN),
    ("BACKGROUND",   (0, 2), (-1, 2), ROW_ALT),
    ("BACKGROUND",   (0, 3), (-1, 3), ROW_MAIN),
    ("TOPPADDING",   (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
    ("INNERGRID",    (0, 0), (-1, -1), 0.3, colors.HexColor("#21262D")),
    ("BOX",          (0, 0), (-1, -1), 1, colors.HexColor("#30363D")),
    ("LINEBELOW",    (0, 0), (-1, 0), 1.5, ACCENT),
]))
story.append(rtbl)

story.append(SP(6))
story.append(Paragraph(
    "<b>Premissa base:</b> Budget inicial de 40.000c, cartas vendidas com margem após taxa EA (5%). "
    "Cenário Conservador assume que apenas SBCs de 85 são ativados. Cenário Otimista considera "
    "SBCs encadeados (85+86+87 simultâneos) com demanda de início de semana.",
    S["small"]
))
story.append(HR())

# ─── 5. PRIME HEROES — PLAYERS DESTAQUE ───────────────────────────────────────
story.append(Paragraph("5. PRIME HEROES — CARTAS DESTAQUE DO PROMO", S["section"]))
story.append(Paragraph(
    "Cartas com SBC disponível tendem a criar demanda direta por fodder. "
    "Acompanhe os SBCs liberados para calibrar quais ratings serão mais demandados.",
    S["body"]
))
story.append(SP(4))

heroes_data = [
    ["Jogador",          "Ovr Est.", "Atrib. 99",     "Liga",          "Tipo de Carta"],
    ["Eden Hazard",      "94+",      "Dribbling",     "La Liga",       "Prime Hero Pack"],
    ["Yaya Touré",       "93+",      "Passing",       "Premier League","Prime Hero Pack"],
    ["Jaap Stam",        "93+",      "Defending",     "Premier League","Prime Hero Pack"],
    ["Daniele De Rossi", "92+",      "Physicality",   "Serie A",       "Prime Hero SBC"],
    ["Jill Scott",       "91+",      "Work Rate",     "WSL",           "Prime Hero Obj."],
    ["Micah Richards",   "91+",      "Pace",          "Premier League","Prime Hero Obj."],
]

hw = [4.0*cm, 2.0*cm, 2.5*cm, 3.5*cm, 3.5*cm]
htbl = Table(heroes_data, colWidths=hw, repeatRows=1)
htbl.setStyle(TableStyle([
    ("BACKGROUND",   (0, 0), (-1, 0), HEADER_BG),
    ("TEXTCOLOR",    (0, 0), (-1, 0), ACCENT2),
    ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE",     (0, 0), (-1, -1), 8),
    ("TEXTCOLOR",    (0, 1), (-1, -1), TEXT_WHITE),
    ("ALIGN",        (1, 0), (-1, -1), "CENTER"),
    ("ALIGN",        (0, 0), (0, -1), "LEFT"),
    ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ("BACKGROUND",   (0, 1), (-1, 1), ROW_MAIN),
    ("BACKGROUND",   (0, 2), (-1, 2), ROW_ALT),
    ("BACKGROUND",   (0, 3), (-1, 3), ROW_MAIN),
    ("BACKGROUND",   (0, 4), (-1, 4), ROW_ALT),
    ("BACKGROUND",   (0, 5), (-1, 5), ROW_MAIN),
    ("BACKGROUND",   (0, 6), (-1, 6), ROW_ALT),
    ("TOPPADDING",   (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
    ("LEFTPADDING",  (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("LINEBELOW",    (0, 0), (-1, 0), 1.5, ACCENT2),
    ("INNERGRID",    (0, 0), (-1, -1), 0.3, colors.HexColor("#21262D")),
    ("BOX",          (0, 0), (-1, -1), 1, colors.HexColor("#30363D")),
]))
story.append(htbl)

story.append(SP(6))
story.append(Paragraph(
    "<b>Impacto no mercado de fodder:</b> Daniele De Rossi e Jill Scott como SBC/Objetivo "
    "garantem demanda contínua por fodder 85–87 ao longo da semana. Eden Hazard em packs "
    "gera abertura massiva → mais supply de fodder alto rating → oportunidade de compra "
    "de cartas descartadas 87–88 nas primeiras horas do promo.",
    S["body"]
))
story.append(HR())

# ─── 6. OITO REGRAS DE OURO ───────────────────────────────────────────────────
story.append(Paragraph("6. AS 8 REGRAS DE OURO DO TRADE", S["section"]))

rules = [
    ("1. Verifique o preço ANTES de comprar",
     "Sempre consulte FUTBIN ou FUT.GG nos últimos 10 minutos. O mercado muda rapidamente "
     "e uma carta listada 200c acima da média já elimina toda a margem."),
    ("2. Nunca compre no topo",
     "Se o preço subiu mais de 20% nas últimas 2 horas, você perdeu a janela. Espere a "
     "próxima correção ou busque outro jogador equivalente."),
    ("3. Respeite o limite por carta",
     "Máximo de 10–15 unidades do mesmo jogador. Concentração excessiva aumenta o risco "
     "de depressão de preço ao vender e dificulta liquidação rápida."),
    ("4. A taxa EA de 5% é implacável",
     "Nunca calcule lucro sem descontar os 5%. Uma compra a 1.000c e venda a 1.040c é "
     "PREJUÍZO de 2%. Sua margem mínima para ser rentável é de 6% sobre o preço de compra."),
    ("5. Venda progressivamente",
     "Divida o estoque em 3 lotes: 40% no primeiro pico, 40% no segundo pico, 20% na "
     "reserva. Nunca tente vender tudo de uma vez — você suprime o próprio preço."),
    ("6. Não entre em pânico durante pack openings",
     "Quando o promo abre, preços caem 15–30% por 1–2 horas. Isso é normal e temporário. "
     "Seja comprador nesse momento, não vendedor."),
    ("7. Monitore SBCs em tempo real",
     "Ative notificações de EA e acompanhe Reddit/Discord de FC26. Um SBC novo pode "
     "quadruplicar a demanda por um rating específico em minutos."),
    ("8. Defina stop-loss e respite-o",
     "Se uma carta cair 25% abaixo do preço de compra, realize o prejuízo e libere coins "
     "para outra oportunidade. Capital parado em carta afundando é pior que pequena perda."),
]

for title, body in rules:
    story.append(Paragraph(title, S["rule_title"]))
    story.append(Paragraph(body, S["rule_body"]))

story.append(HR())

# ─── 7. DISCLAIMER ────────────────────────────────────────────────────────────
story.append(Paragraph("DISCLAIMER", S["section"]))

story.append(Paragraph(
    "Este relatório foi gerado automaticamente com base em dados públicos coletados em "
    "29/05/2026 via FUTBIN, FUT.GG e fontes de mídia especializadas em EA FC 26 Ultimate Team. "
    "Os preços indicados são estimativas baseadas em médias de mercado e podem variar "
    "significativamente em função de eventos não previstos, mudanças de preço range pela EA "
    "Sports, novos promos ou alterações de meta. Este documento NÃO constitui garantia de "
    "lucro. Trading em Ultimate Team envolve risco de perda de coins. Sempre verifique preços "
    "em tempo real antes de executar qualquer transação. O autor não se responsabiliza por "
    "perdas decorrentes do uso deste relatório.",
    S["warning"]
))

story.append(SP(10))
story.append(Paragraph(
    f"Gerado em: {REPORT_DATE} UTC  |  EA FC 26 Trading Bot  |  Budget: 40.000c",
    S["date"]
))

# ── Build PDF ──────────────────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # Footer
    canvas.setFillColor(TEXT_GRAY)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(1.5*cm, 0.8*cm, f"EA FC 26 Trading Report — {REPORT_DATE} UTC")
    canvas.drawRightString(A4[0] - 1.5*cm, 0.8*cm, f"Pág. {doc.page}")
    # Top accent bar
    canvas.setFillColor(ACCENT)
    canvas.rect(0, A4[1] - 4, A4[0], 4, fill=1, stroke=0)
    canvas.restoreState()

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF gerado: {OUTPUT_FILE}")
