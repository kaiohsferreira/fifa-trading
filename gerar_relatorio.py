#!/usr/bin/env python3
"""Gerador de relatório diário de trading EA FC 26."""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak

# ── Cores tema EA FC ──────────────────────────────────────────────────────────
EA_GREEN   = colors.HexColor("#00C853")
EA_DARK    = colors.HexColor("#0D1117")
EA_GOLD    = colors.HexColor("#FFD700")
EA_BLUE    = colors.HexColor("#1565C0")
EA_RED     = colors.HexColor("#C62828")
EA_GRAY    = colors.HexColor("#37474F")
EA_LIGHT   = colors.HexColor("#ECEFF1")
EA_ORANGE  = colors.HexColor("#FF6F00")
WHITE      = colors.white

REPORT_DATE   = "22/05/2026 20:10"
REPORT_HOUR   = "20h"
FILENAME      = "relatorio-trading-2026-05-22-20h.pdf"

# ── Estilos ───────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def style(name, **kw):
    s = styles[name].clone(name + str(id(kw)))
    for k, v in kw.items():
        setattr(s, k, v)
    return s

H1 = style("Heading1", fontSize=22, textColor=WHITE,         alignment=TA_CENTER, spaceAfter=4, fontName="Helvetica-Bold")
H2 = style("Heading2", fontSize=13, textColor=EA_GOLD,       alignment=TA_LEFT,   spaceAfter=4, fontName="Helvetica-Bold")
H3 = style("Heading3", fontSize=11, textColor=EA_GREEN,      alignment=TA_LEFT,   spaceAfter=2, fontName="Helvetica-Bold")
BODY   = style("Normal",  fontSize=9,  textColor=EA_DARK,    alignment=TA_JUSTIFY, leading=14, spaceAfter=4)
SMALL  = style("Normal",  fontSize=8,  textColor=EA_GRAY,    alignment=TA_JUSTIFY, leading=12, spaceAfter=3)
CENTER = style("Normal",  fontSize=9,  textColor=EA_DARK,    alignment=TA_CENTER)
DISC_S = style("Normal",  fontSize=7,  textColor=EA_GRAY,    alignment=TA_JUSTIFY, leading=11, spaceAfter=2)
GOLD_C = style("Normal",  fontSize=10, textColor=EA_GOLD,    alignment=TA_CENTER, fontName="Helvetica-Bold")
WHITE_C= style("Normal",  fontSize=9,  textColor=WHITE,      alignment=TA_CENTER, fontName="Helvetica-Bold")
GREEN_C= style("Normal",  fontSize=9,  textColor=EA_GREEN,   alignment=TA_CENTER, fontName="Helvetica-Bold")
RED_C  = style("Normal",  fontSize=9,  textColor=EA_RED,     alignment=TA_CENTER, fontName="Helvetica-Bold")
BODY_B = style("Normal",  fontSize=9,  textColor=EA_DARK,    alignment=TA_LEFT,   fontName="Helvetica-Bold")
SECTION_TITLE = style("Normal", fontSize=15, textColor=WHITE, alignment=TA_CENTER,
                       fontName="Helvetica-Bold", spaceAfter=6)

# ── Helpers ───────────────────────────────────────────────────────────────────
def section_header(title):
    """Retorna bloco de cabeçalho de seção com fundo escuro."""
    data = [[Paragraph(title, SECTION_TITLE)]]
    tbl  = Table(data, colWidths=[17*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), EA_DARK),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("RIGHTPADDING",  (0,0), (-1,-1), 6),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return tbl

def hr(color=EA_GREEN, width=1.5):
    return HRFlowable(width="100%", thickness=width, color=color, spaceAfter=6, spaceBefore=2)

def bullet(text):
    return Paragraph(f"<b>•</b>  {text}", BODY)

def sp(h=6):
    return Spacer(1, h)

# ── Documento ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    FILENAME, pagesize=A4,
    rightMargin=1.8*cm, leftMargin=1.8*cm,
    topMargin=1.5*cm, bottomMargin=1.5*cm
)

story = []

# ── CAPA / HEADER ─────────────────────────────────────────────────────────────
header_data = [[Paragraph("⚽  EA FC 26 — RELATÓRIO DE TRADING", H1)]]
header_tbl  = Table(header_data, colWidths=[17*cm])
header_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), EA_DARK),
    ("TOPPADDING",    (0,0), (-1,-1), 14),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ("LEFTPADDING",   (0,0), (-1,-1), 8),
]))
story.append(header_tbl)

# Sub-header band
sub_data = [[
    Paragraph(f"Data: {REPORT_DATE} UTC", GOLD_C),
    Paragraph("Budget: 40.000 coins", GOLD_C),
    Paragraph("Evento: Ultimate TOTS 🔥", GOLD_C),
]]
sub_tbl = Table(sub_data, colWidths=[5.66*cm, 5.66*cm, 5.68*cm])
sub_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), EA_GRAY),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
]))
story.append(sub_tbl)
story.append(sp(10))

# ── 1. CONTEXTO DO MERCADO ────────────────────────────────────────────────────
story.append(section_header("1. CONTEXTO DO MERCADO — 22/05/2026"))
story.append(sp(6))

story.append(Paragraph("🔥 Ultimate TOTS — Lançado HOJE (22/05/2026 às 18h BST)", H2))
story.append(hr())
story.append(Paragraph(
    "O <b>Ultimate Team of the Season (TOTS)</b> foi lançado hoje com mais de 60 cartas TOTS disponíveis "
    "em packs, incluindo astros como <b>Messi, Cristiano Ronaldo, Mbappé e Lamine Yamal</b>. "
    "Este é o evento mais importante do ciclo TOTS e termina em <b>29/05/2026</b>. "
    "A demanda por SBC fodder está no pico — cada nova SBC de 'End of an Era' "
    "consome centenas de milhares de cartas 84–88 rated.", BODY))
story.append(sp(4))

ctx_data = [
    ["Evento", "Status", "Término"],
    ["Ultimate TOTS", "🟢 ATIVO (lançado hoje)", "29/05/2026"],
    ["End of an Era — Salah (95 OVR)", "🟢 ATIVO", "29/05/2026"],
    ["End of an Era — Robertson, Griezmann, B. Silva, Goretzka", "🟢 ATIVO", "29/05/2026"],
    ["RTTF (Road to the Final)", "🟢 ATIVO", "30/05/2026"],
    ["Fantasy FC / Path to Glory", "🟢 ATIVO", "29/05/2026"],
    ["TOTS (ciclo completo)", "🟢 ATIVO", "29/05/2026"],
]
ctx_tbl = Table(ctx_data, colWidths=[6*cm, 6.5*cm, 4.5*cm])
ctx_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), EA_DARK),
    ("TEXTCOLOR",  (0,0), (-1,0), WHITE),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("ALIGN",      (0,0), (-1,-1), "CENTER"),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [EA_LIGHT, WHITE]),
    ("GRID",       (0,0), (-1,-1), 0.5, EA_GRAY),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(ctx_tbl)
story.append(sp(8))

story.append(Paragraph("Tendência Geral do Mercado", H3))
story.append(bullet("Preços de fodder 84–86 estão <b>subindo</b> com o lançamento do Ultimate TOTS — momento ideal para venda."))
story.append(bullet("SBCs 'End of an Era' (Salah requer ~36 squads e ~1,2M coins) drenam massivamente o mercado de fodder."))
story.append(bullet("Sexta-feira 20h UTC: mercado aquecido pré-Weekend League — boa janela de venda."))
story.append(bullet("TOTS encerra em 29/05 (7 dias) — após isso, espera-se queda acentuada nos preços de fodder."))
story.append(bullet("Mercado de 86-rated está anômalo: mais barato que 85-rated em alguns casos — oportunidade de arbitragem."))
story.append(sp(10))

# ── 2. TABELA DE CARTAS RECOMENDADAS ─────────────────────────────────────────
story.append(section_header("2. CARTAS RECOMENDADAS — COMPRA & VENDA"))
story.append(sp(6))
story.append(Paragraph(
    "Margem líquida calculada após taxa de 5% da EA no momento da venda. "
    "Todos os preços em coins. Dados baseados em FUTBIN/FUT.GG em 22/05/2026.", SMALL))
story.append(sp(6))

hdr = ["Jogador", "Rat.", "Clube / Liga", "Compra\n(máx.)", "Venda\n(alvo)", "Margem\nLíq.", "Risco"]

players = [
    # [Nome, Rating, Clube/Liga, Compra, Venda, Margem Calculada, Risco]
    # Margem = Venda * 0.95 - Compra
    ("Patrik Schick",       "85", "Bayer Leverkusen",   "1.600",  "2.300",  "+585",  "🟡 Médio"),
    ("Scott McTominay",     "85", "Napoli / Serie A",   "1.600",  "2.200",  "+490",  "🟢 Baixo"),
    ("Federico Dimarco",    "85", "Inter de Milão",     "1.650",  "2.300",  "+535",  "🟡 Médio"),
    ("Yusuf Chawinga",      "85", "Wolfsburg / Bund.",  "1.600",  "2.100",  "+395",  "🟢 Baixo"),
    ("Michael Olise",       "86", "Bayern Munique",     "1.450",  "2.100",  "+545",  "🟢 Baixo"),
    ("Hakan Çalhanoğlu",    "86", "Inter de Milão",     "1.500",  "2.200",  "+590",  "🟢 Baixo"),
    ("Paulo Dybala",        "86", "Roma / Serie A",     "1.500",  "2.200",  "+590",  "🟢 Baixo"),
    ("Rúben Dias",          "86", "Man. City / PL",     "1.500",  "2.200",  "+590",  "🟢 Baixo"),
    ("Bruno Guimarães",     "86", "Newcastle / PL",     "1.500",  "2.200",  "+590",  "🟢 Baixo"),
    ("Romelu Lukaku",       "84", "Roma / Serie A",     "850",    "1.300",  "+385",  "🟢 Baixo"),
    ("Alejandro Grimaldo",  "84", "Bayer Leverkusen",   "800",    "1.250",  "+388",  "🟢 Baixo"),
    ("Rodrigo de Paul",     "84", "Atlético Madrid",    "800",    "1.200",  "+340",  "🟢 Baixo"),
]

table_header = [
    Paragraph(c, WHITE_C) for c in ["Jogador", "Rat.", "Clube / Liga", "Compra\n(máx.)", "Venda\n(alvo)", "Margem\nLíq.", "Risco"]
]
table_rows = [table_header]
for (nome, rat, clube, buy, sell, margin, risk) in players:
    row = [
        Paragraph(nome, BODY),
        Paragraph(rat, CENTER),
        Paragraph(clube, SMALL),
        Paragraph(buy, CENTER),
        Paragraph(sell, CENTER),
        Paragraph(margin, GREEN_C),
        Paragraph(risk, CENTER),
    ]
    table_rows.append(row)

col_w = [4.5*cm, 1.3*cm, 3.7*cm, 1.8*cm, 1.8*cm, 1.8*cm, 2.1*cm]
cards_tbl = Table(table_rows, colWidths=col_w, repeatRows=1)
cards_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), EA_DARK),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("ALIGN",      (0,0), (-1,-1), "CENTER"),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [EA_LIGHT, WHITE]),
    ("GRID",       (0,0), (-1,-1), 0.4, EA_GRAY),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 4),
]))
story.append(cards_tbl)
story.append(sp(6))

# Legenda
story.append(Paragraph(
    "⚠️  <b>Margem líquida</b> = Preço de venda × 0,95 – Preço de compra. "
    "Valores estimados com base em tendência de mercado TOTS ativo. "
    "Verifique sempre em FUTBIN ou FUT.GG antes de comprar.", DISC_S))
story.append(sp(10))

# ── 3. ESTRATÉGIA DE ALOCAÇÃO ─────────────────────────────────────────────────
story.append(section_header("3. ESTRATÉGIA DE ALOCAÇÃO DO BUDGET (40.000 coins)"))
story.append(sp(6))

alloc_data = [
    ["Estratégia", "Budget", "Qtd. Cartas", "Alvo", "Retorno Estimado"],
    ["86-rated Fodder\n(Olise, Çalhanoğlu, Dybala, R.Dias, B.Guimarães)",
     "20.000", "13 cartas\n(~1.500 cada)", "Vender em 24h\n durante SBC rush", "+7.700 líq."],
    ["85-rated Fodder\n(Schick, McTominay, Dimarco, Chawinga)",
     "13.000", "8 cartas\n(~1.600 cada)", "Vender em 12–24h", "+4.300 líq."],
    ["84-rated Massa\n(Lukaku, Grimaldo, De Paul)",
     "5.000", "6 cartas\n(~830 cada)", "Vender em 6–12h", "+2.200 líq."],
    ["Reserva de Liquidez\n(não investir)", "2.000", "—", "Cobrir gaps / oport.", "—"],
]
alloc_tbl = Table(alloc_data, colWidths=[5*cm, 2.5*cm, 3.2*cm, 3.3*cm, 3*cm])
alloc_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), EA_BLUE),
    ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 8),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [EA_LIGHT, WHITE]),
    ("GRID",          (0,0), (-1,-1), 0.4, EA_GRAY),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("FONTNAME",      (0,4), (-1,-1), "Helvetica-Bold"),
    ("TEXTCOLOR",     (0,4), (0,-1), EA_DARK),
    ("TEXTCOLOR",     (4,1), (4,-1), EA_GREEN),
]))
story.append(alloc_tbl)
story.append(sp(10))

# ── 4. ESTRATÉGIA DE TIMING ───────────────────────────────────────────────────
story.append(section_header("4. ESTRATÉGIA DE TIMING"))
story.append(sp(6))

timing_items = [
    ("AGORA (20h–22h UTC, Sex.)", EA_RED,
     "Comprar 86-rated e 85-rated fodder durante pico de oferta noturna (jogadores vendendo após WL). "
     "Preços ligeiramente deprimidos. Use BIN abaixo do mínimo listado."),
    ("22h–02h UTC (Madrugada)", EA_ORANGE,
     "Monitorar preços. Evitar grandes compras. SBCs de End of an Era ainda ativas — "
     "demanda sustentada. Segurar as cartas."),
    ("Sábado 08h–14h UTC", EA_GREEN,
     "VENDER 84-rated e 85-rated. Mercado aquecido pela manhã europeia + rush de SBC. "
     "Use BIN ligeiramente acima da média. Não seja guloso."),
    ("Sábado 14h–20h UTC", EA_GREEN,
     "VENDER 86-rated. Pico máximo de demanda no sábado. "
     "Jogadores completando SBCs antes do fim do weekend league. Ideal para realizar lucro."),
    ("Domingo (após WL rewards)", EA_ORANGE,
     "Cautela: mercado inundado de cartas pós-rewards. Evitar compras grandes. "
     "Avaliar novas SBCs que possam surgir segunda-feira."),
    ("Segunda-feira 18h–21h UTC", EA_BLUE,
     "Nova rodada de conteúdo da EA. Atenção para leaks de novas SBCs — "
     "pode surgir nova demanda por fodder específico."),
]

for (time_label, color, desc) in timing_items:
    label_data = [[Paragraph(time_label, WHITE_C)]]
    label_tbl  = Table(label_data, colWidths=[17*cm])
    label_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), color),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    story.append(label_tbl)
    story.append(Paragraph(desc, BODY))
    story.append(sp(4))

story.append(sp(6))

# ── 5. ESTIMATIVA DE RETORNO EM 48H ──────────────────────────────────────────
story.append(section_header("5. ESTIMATIVA DE RETORNO EM 48H"))
story.append(sp(6))

ret_data = [
    ["Cenário", "Retorno Bruto", "Taxa EA (5%)", "Lucro Líquido", "Capital Final", "ROI"],
    ["🐌 Conservador\n(venda a -15% do alvo)", "+10.500", "-2.300", "+8.200", "48.200", "+20,5%"],
    ["🎯 Base\n(venda no alvo estimado)", "+14.200", "-3.100", "+11.100", "51.100", "+27,8%"],
    ["🚀 Otimista\n(SBC nova aumenta demanda)", "+19.000", "-4.200", "+14.800", "54.800", "+37,0%"],
]
ret_tbl = Table(ret_data, colWidths=[3.5*cm, 2.8*cm, 2.5*cm, 2.8*cm, 2.8*cm, 2.6*cm])
ret_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), EA_DARK),
    ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 8.5),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [EA_LIGHT, WHITE]),
    ("GRID",          (0,0), (-1,-1), 0.4, EA_GRAY),
    ("TOPPADDING",    (0,0), (-1,-1), 7),
    ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
    ("TEXTCOLOR",     (3,1), (3,-1), EA_GREEN),
    ("TEXTCOLOR",     (5,1), (5,-1), EA_BLUE),
    ("FONTNAME",      (3,1), (5,-1), "Helvetica-Bold"),
]))
story.append(ret_tbl)
story.append(sp(6))
story.append(Paragraph(
    "⚠️ Estimativas baseadas em padrões históricos de mercado TOTS e demanda atual de SBC. "
    "O cenário conservador assume venda parcial e variação negativa de preço. "
    "O cenário otimista pressupõe nova SBC de alta demanda lançada no período.", DISC_S))
story.append(sp(10))

# ── 6. 8 REGRAS DE OURO DO TRADE ─────────────────────────────────────────────
story.append(section_header("6. AS 8 REGRAS DE OURO DO TRADE"))
story.append(sp(6))

rules = [
    ("1", "Nunca invista mais de 50% do budget em uma única carta ou estratégia.",
     "Diversificação protege contra crashes súbitos de mercado."),
    ("2", "Sempre consulte FUTBIN ou FUT.GG antes de qualquer compra.",
     "Preços mudam a cada minuto — nunca trade de memória."),
    ("3", "Compre na madrugada e nos pós-rewards (quinta e domingo); venda na tarde de sexta e sábado.",
     "O volume de vendedores define o preço — aproveite os vales de oferta."),
    ("4", "Nunca complete SBCs nas primeiras 2 horas de lançamento.",
     "O rush inicial infla os preços em até 40%. Aguarde a normalização."),
    ("5", "Diversifique entre ligas e nações na mesma faixa de rating.",
     "Se uma liga sofrer crash, as outras sustentam o portfólio."),
    ("6", "Defina seu preço-alvo de saída ANTES de comprar.",
     "Ganância é o maior inimigo do trader. Tenha disciplina e execute o plano."),
    ("7", "Fique de olho em leaks de novas SBCs e promos.",
     "Antecipe a demanda: compre o fodder ANTES do anúncio oficial."),
    ("8", "Respeite o limite de 5% de taxa da EA em todos os cálculos.",
     "Venda sem lucro é prejuízo real — sempre calcule a margem líquida."),
]

for (num, rule, why) in rules:
    rule_data = [[
        Paragraph(num, GOLD_C),
        Paragraph(f"<b>{rule}</b><br/><font color='#37474F' size='8'><i>{why}</i></font>", BODY),
    ]]
    rule_tbl = Table(rule_data, colWidths=[1*cm, 16*cm])
    rule_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (0,-1), EA_DARK),
        ("BACKGROUND",    (1,0), (1,-1), EA_LIGHT if int(num) % 2 == 0 else WHITE),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("GRID",          (0,0), (-1,-1), 0.3, EA_GRAY),
    ]))
    story.append(rule_tbl)
    story.append(sp(1))

story.append(sp(10))

# ── 7. CHECKLIST RÁPIDO ───────────────────────────────────────────────────────
story.append(section_header("7. CHECKLIST DE AÇÃO — PRÓXIMAS 2 HORAS"))
story.append(sp(6))

checklist = [
    "☐  Abrir FUT.GG / FUTBIN e verificar preços atuais de 84–86 rated",
    "☐  Comprar até 13 cartas 86-rated abaixo de 1.500 coins (BIN snipe)",
    "☐  Comprar até 8 cartas 85-rated abaixo de 1.650 coins",
    "☐  Comprar até 6 cartas 84-rated abaixo de 850 coins",
    "☐  Verificar novas SBCs lançadas com o Ultimate TOTS e ajustar fodder alvo",
    "☐  Listar todas as cartas compradas para venda no sábado manhã (BIN realista)",
    "☐  Monitorar Reddit r/FIFA e Discord FUT para leaks de novas SBCs",
    "☐  Nunca vender abaixo do preço calculado de break-even (+ taxa EA)",
]
for item in checklist:
    story.append(Paragraph(item, BODY))
    story.append(sp(2))

story.append(sp(10))

# ── DISCLAIMER ────────────────────────────────────────────────────────────────
story.append(hr(EA_RED))
story.append(Paragraph("DISCLAIMER", style("Normal", fontSize=9, textColor=EA_RED,
                                            fontName="Helvetica-Bold", alignment=TA_CENTER)))
story.append(Paragraph(
    "Este relatório é gerado automaticamente com base em dados públicos de mercado (FUTBIN, FUT.GG, "
    "RealSport101, FifaUltimateTeam.it, OperationSports) e tem caráter exclusivamente informativo. "
    "Preços de mercado em EA FC 26 são altamente voláteis e podem mudar em minutos. "
    "O autor não se responsabiliza por perdas de coins decorrentes do uso deste relatório. "
    "Sempre verifique preços em tempo real antes de realizar qualquer transação. "
    "EA Sports não endossa nem está associado a este material.",
    DISC_S))

# ── Rodapé ────────────────────────────────────────────────────────────────────
story.append(sp(6))
footer_data = [[
    Paragraph("EA FC 26 Trading Report", SMALL),
    Paragraph(f"Gerado em: {REPORT_DATE} UTC", SMALL),
    Paragraph("github.com/kaiohsferreira/fifa-trading", SMALL),
]]
footer_tbl = Table(footer_data, colWidths=[5.66*cm, 5.66*cm, 5.68*cm])
footer_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), EA_LIGHT),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("GRID",          (0,0), (-1,-1), 0.3, EA_GRAY),
]))
story.append(footer_tbl)

# ── BUILD ─────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF gerado: {FILENAME}")
