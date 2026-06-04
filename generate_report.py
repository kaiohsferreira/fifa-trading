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
import os

REPORT_DATE = "04/06/2026 14:07"
FILENAME = "relatorio-trading-2026-06-04-14h.pdf"
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAME)

DARK_BG   = colors.HexColor("#0D1117")
ACCENT    = colors.HexColor("#00D4AA")
ACCENT2   = colors.HexColor("#FF6B35")
GOLD      = colors.HexColor("#FFD700")
LIGHT_TXT = colors.HexColor("#E6EDF3")
MID_TXT   = colors.HexColor("#8B949E")
TABLE_HDR = colors.HexColor("#161B22")
TABLE_ROW = colors.HexColor("#0D1117")
TABLE_ALT = colors.HexColor("#13202E")
BORDER    = colors.HexColor("#30363D")

# shared cell paragraph styles (module level so helpers can use them)
_CELL_BODY = None
_CELL_HDR  = None
_CELL_GOLD = None


def make_styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle("RTitle",
        fontName="Helvetica-Bold", fontSize=22, textColor=ACCENT,
        alignment=TA_CENTER, spaceAfter=4, leading=28))
    s.add(ParagraphStyle("RSub",
        fontName="Helvetica", fontSize=11, textColor=MID_TXT,
        alignment=TA_CENTER, spaceAfter=2))
    s.add(ParagraphStyle("RDate",
        fontName="Helvetica-Bold", fontSize=13, textColor=GOLD,
        alignment=TA_CENTER, spaceAfter=8))
    s.add(ParagraphStyle("RSection",
        fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT,
        spaceBefore=14, spaceAfter=6, leading=18))
    s.add(ParagraphStyle("RSubSec",
        fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT2,
        spaceBefore=8, spaceAfter=4, leading=14))
    s.add(ParagraphStyle("RBody",
        fontName="Helvetica", fontSize=9, textColor=LIGHT_TXT,
        leading=14, spaceAfter=4, alignment=TA_JUSTIFY))
    s.add(ParagraphStyle("RBullet",
        fontName="Helvetica", fontSize=9, textColor=LIGHT_TXT,
        leading=13, spaceAfter=2, leftIndent=12))
    s.add(ParagraphStyle("RGold",
        fontName="Helvetica-Bold", fontSize=9, textColor=GOLD,
        leading=13, spaceAfter=2, leftIndent=12))
    s.add(ParagraphStyle("RDisclaim",
        fontName="Helvetica-Oblique", fontSize=7.5, textColor=MID_TXT,
        leading=11, spaceAfter=2, alignment=TA_JUSTIFY))
    s.add(ParagraphStyle("RHighlight",
        fontName="Helvetica-Bold", fontSize=10, textColor=GOLD,
        alignment=TA_CENTER, spaceAfter=4))
    s.add(ParagraphStyle("CellHdr",
        fontName="Helvetica-Bold", fontSize=8, textColor=ACCENT,
        alignment=TA_CENTER, leading=10))
    s.add(ParagraphStyle("CellBody",
        fontName="Helvetica", fontSize=8, textColor=LIGHT_TXT,
        leading=10, alignment=TA_LEFT))
    s.add(ParagraphStyle("CellCenter",
        fontName="Helvetica", fontSize=8, textColor=LIGHT_TXT,
        leading=10, alignment=TA_CENTER))
    s.add(ParagraphStyle("CellGold",
        fontName="Helvetica-Bold", fontSize=8, textColor=GOLD,
        leading=10, alignment=TA_CENTER))
    s.add(ParagraphStyle("CellAccent",
        fontName="Helvetica-Bold", fontSize=8, textColor=ACCENT,
        leading=10, alignment=TA_LEFT))
    return s


def hr(color=BORDER, thickness=0.5):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceAfter=6, spaceBefore=6)


def p_cell(text, style, bold=False):
    """Wrap text in a Paragraph for table cells."""
    if bold:
        text = f"<b>{text}</b>"
    return Paragraph(text, style)


def make_table(header_row, data_rows, col_widths_cm):
    """Build a styled Table with Paragraph cells."""
    S = _S
    col_w = [w * cm for w in col_widths_cm]

    # Convert header
    hdr = [p_cell(h, S["CellHdr"]) for h in header_row]
    # Convert data rows
    rows = []
    for row in data_rows:
        p_row = []
        for i, cell in enumerate(row):
            # first column left-aligned
            style = S["CellBody"] if i == 0 else S["CellCenter"]
            p_row.append(p_cell(str(cell), style))
        rows.append(p_row)

    data = [hdr] + rows

    t = Table(data, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  TABLE_HDR),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [TABLE_ROW, TABLE_ALT]),
        ("GRID",          (0, 0), (-1, -1), 0.3, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    return t


_S = None  # module-level style registry


def main():
    global _S
    _S = make_styles()
    S = _S

    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=1.8*cm, rightMargin=1.8*cm,
        topMargin=2*cm,    bottomMargin=2*cm,
        title="Relatório de Trading EA FC 26",
        author="Agente de Mercado FUT",
    )

    story = []

    # ── CABEÇALHO ────────────────────────────────────────────────────────────
    story.append(Paragraph("EA FC 26 ULTIMATE TEAM", S["RTitle"]))
    story.append(Paragraph("RELATÓRIO DE ANÁLISE DE MERCADO", S["RSub"]))
    story.append(hr(ACCENT, 1.5))
    story.append(Paragraph(f"Data e Hora do Relatório: {REPORT_DATE} UTC", S["RDate"]))
    story.append(hr(BORDER))
    story.append(Spacer(1, 0.3*cm))

    # ── 1. CONTEXTO DO MERCADO ───────────────────────────────────────────────
    story.append(Paragraph("1. CONTEXTO DO MERCADO ATUAL", S["RSection"]))
    story.append(Paragraph(
        "<b>Evento Ativo Principal:</b> Festival of Football — Season 8 "
        "(lançamento AMANHÃ, 05/06/2026 às 18h BST)",
        S["RBody"]))
    story.append(Spacer(1, 0.2*cm))

    ctx_hdr  = ["INDICADOR", "STATUS", "IMPACTO NO MERCADO"]
    ctx_rows = [
        ["Rivals Rewards (Thursday)", "ATIVO AGORA", "Preços no MÍNIMO semanal — momento de COMPRAR"],
        ["Festival of Football",      "Inicia 05/06 18h BST", "Demanda por fodder vai DISPARAR"],
        ["Path to Glory Promo",       "Inicia 05/06 (c/ FoF)", "SBCs 84+ ativos => fodder sobe"],
        ["EVO Undo Feature",          "LIVE HOJE 04/06", "Cartas evoluídas voltam ao mercado"],
        ["10x 84+ Upgrade SBC",       "Ativo até 12/06", "Custo ~15.750c / valor ~22.625c"],
        ["Shapeshifters",             "12/06 – 10/07", "Nova onda de SBCs em ~8 dias"],
        ["Greats of the Game",        "19/06 – 26/06", "Novas ICONs: Kempes e Rivelino"],
    ]

    # Custom widths for context table
    ctx_col = [4.8, 3.8, 7.7]
    ctx_data = [[p_cell(h, S["CellHdr"]) for h in ctx_hdr]]
    for row in ctx_rows:
        ctx_data.append([
            p_cell(row[0], S["CellBody"]),
            p_cell(row[1], S["CellCenter"]),
            p_cell(row[2], S["CellBody"]),
        ])
    ctx_t = Table(ctx_data, colWidths=[w*cm for w in ctx_col], repeatRows=1)
    ctx_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  TABLE_HDR),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [TABLE_ROW, TABLE_ALT]),
        ("GRID",          (0, 0), (-1, -1), 0.3, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    story.append(ctx_t)

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<b>Análise:</b> Hoje é QUINTA-FEIRA — o melhor momento semanal para COMPRAR. "
        "Os rewards de Division Rivals inundam o mercado às quintas, derrubando preços. "
        "Amanhã (5/jun) começa o Festival of Football: 6 semanas de promos, 100+ cartas de "
        "seleções nacionais em packs e SBCs de 84+ ativos. Comprar fodder agora e vender "
        "sexta-sábado quando a demanda explodir é a estratégia ideal.",
        S["RBody"]))

    story.append(Paragraph(
        "<b>Path to Glory Team 1 — Vazamentos confirmados:</b> Vinicius Jr. (Brasil), "
        "Kevin De Bruyne (Bélgica), Bukayo Saka (Inglaterra), Jamal Musiala (Alemanha), "
        "Christian Pulisic (EUA), Frenkie De Jong (Holanda). "
        "Upgrades automáticos conforme as seleções avançam na Copa do Mundo 2026.",
        S["RBody"]))

    story.append(Spacer(1, 0.3*cm))

    # ── 2. TABELA DE CARTAS RECOMENDADAS ────────────────────────────────────
    story.append(Paragraph("2. CARTAS RECOMENDADAS — BUDGET 40.000 COINS", S["RSection"]))
    story.append(Paragraph(
        "Preços de quinta-feira (piso semanal). "
        "Margem líquida já com 5% de taxa EA descontada na venda.",
        S["RBody"]))
    story.append(Spacer(1, 0.2*cm))

    cards_hdr = ["JOGADOR", "RTG", "CLUBE / LIGA", "COMPRA", "VENDA", "REC. LÍQ.", "MARGEM"]
    cards_rows = [
        ["Amir Rrahmani",       "83", "Napoli / Serie A",       "750c",   "1.100c", "1.045c", "+295c (+39%)"],
        ["Mateo Kovacic",       "83", "Chelsea / PL",           "750c",   "1.000c", "950c",   "+200c (+27%)"],
        ["Thomas Partey",       "83", "Arsenal / PL",           "750c",   "1.050c", "998c",   "+248c (+33%)"],
        ["Jarrod Bowen",        "83", "West Ham / PL",          "750c",   "1.000c", "950c",   "+200c (+27%)"],
        ["Alejandro Grimaldo",  "84", "B.Leverkusen / BL",      "800c",   "1.300c", "1.235c", "+435c (+54%)"],
        ["Bernardo Silva",      "84", "Man City / PL",          "800c",   "1.200c", "1.140c", "+340c (+43%)"],
        ["James Maddison",      "84", "Spurs / PL",             "850c",   "1.350c", "1.283c", "+433c (+51%)"],
        ["Manuel Locatelli",    "84", "Juventus / Serie A",     "850c",   "1.300c", "1.235c", "+385c (+45%)"],
        ["Francesco Acerbi",    "84", "Inter / Serie A",        "850c",   "1.250c", "1.188c", "+338c (+40%)"],
        ["Alex Baena",          "84", "Villarreal / LaLiga",    "800c",   "1.200c", "1.140c", "+340c (+43%)"],
        ["Patrik Schick",       "85", "B.Leverkusen / BL",      "1.300c", "1.900c", "1.805c", "+505c (+39%)"],
        ["Keira Walsh",         "85", "FC Barcelona / WPL",     "1.100c", "1.700c", "1.615c", "+515c (+47%)"],
        ["Manuela Giugliano",   "85", "Roma / Wom. Italy",      "1.100c", "1.650c", "1.568c", "+468c (+43%)"],
        ["88-rated (genérico)", "88", "Vários",                 "6.500c", "8.000c", "7.600c", "+1.100c (+17%)"],
    ]

    c_col = [3.5, 0.9, 3.4, 1.7, 1.7, 1.9, 2.5]
    c_data = [[p_cell(h, S["CellHdr"]) for h in cards_hdr]]
    for i, row in enumerate(cards_rows):
        # margem in gold for positive values
        margin_style = S["CellGold"] if "+" in row[6] else S["CellCenter"]
        c_data.append([
            p_cell(row[0], S["CellBody"]),
            p_cell(row[1], S["CellCenter"]),
            p_cell(row[2], S["CellBody"]),
            p_cell(row[3], S["CellCenter"]),
            p_cell(row[4], S["CellCenter"]),
            p_cell(row[5], S["CellCenter"]),
            p_cell(row[6], margin_style),
        ])
    c_t = Table(c_data, colWidths=[w*cm for w in c_col], repeatRows=1)
    c_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  TABLE_HDR),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [TABLE_ROW, TABLE_ALT]),
        ("GRID",          (0, 0), (-1, -1), 0.3, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    story.append(c_t)

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>Destaques:</b> Alejandro Grimaldo (84, Leverkusen) lidera com +54% de margem — "
        "LM/LB premium com altíssima demanda em SBCs de lado esquerdo. "
        "James Maddison (84, Spurs) oferece +51% e liquidez máxima na Premier League.",
        S["RBody"]))

    story.append(Spacer(1, 0.3*cm))

    # ── 3. ALOCAÇÃO DO BUDGET ───────────────────────────────────────────────
    story.append(Paragraph("3. ALOCAÇÃO SUGERIDA DO BUDGET (40.000 coins)", S["RSection"]))

    alloc_hdr = ["ESTRATÉGIA", "INVESTIMENTO", "QTDE", "RETORNO LÍQ. ESTIMADO", "TIMING"]
    alloc_rows = [
        ["Fodder 83-rated (mix)", "15.000c", "~20 cartas", "+3.050c cons. / +7.800c otim.", "Vender sex-sáb"],
        ["Fodder 84-rated (mix)", "8.500c",  "~10 cartas", "+3.500c cons. / +5.400c otim.", "Vender sex-sáb"],
        ["Fodder 85-rated (mix)", "6.500c",  "~5 cartas",  "+2.100c cons. / +3.800c otim.", "Vender sáb-dom"],
        ["88-rated Thursday flip","10.000c", "~1-2 cartas","+1.500c cons. / +3.150c otim.", "Vender sex-sáb"],
        ["RESERVA estratégica",   "5.000c",  "—",          "Oportunidades surgidas",        "Flexível"],
        ["TOTAL",                 "45.000c*","—",           "+10.150c cons. / +20.150c otim.","48h"],
    ]

    a_col = [4.0, 2.5, 1.8, 4.5, 2.5]
    a_data = [[p_cell(h, S["CellHdr"]) for h in alloc_hdr]]
    for row in alloc_rows:
        is_total = row[0] == "TOTAL"
        st_name  = S["CellAccent"] if is_total else S["CellBody"]
        st_val   = S["CellGold"]   if is_total else S["CellCenter"]
        a_data.append([
            p_cell(row[0], st_name),
            p_cell(row[1], st_val),
            p_cell(row[2], S["CellCenter"]),
            p_cell(row[3], S["CellCenter"]),
            p_cell(row[4], S["CellCenter"]),
        ])
    a_t = Table(a_data, colWidths=[w*cm for w in a_col], repeatRows=1)
    a_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  TABLE_HDR),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [TABLE_ROW, TABLE_ALT]),
        ("GRID",          (0, 0), (-1, -1), 0.3, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    story.append(a_t)
    story.append(Paragraph(
        "* Recomendado usar até 40.000c de investimento ativo + 5.000c de reserva estratégica.",
        S["RDisclaim"]))

    story.append(Spacer(1, 0.3*cm))

    # ── 4. ESTRATÉGIA DE TIMING ──────────────────────────────────────────────
    story.append(Paragraph("4. ESTRATÉGIA DE TIMING", S["RSection"]))

    timing_hdr = ["HORÁRIO (UTC)", "AÇÃO", "JUSTIFICATIVA"]
    timing_rows = [
        ["04/06 — 14h–20h",     "COMPRAR fodder 83-88",    "Thursday Rivals Rewards — piso de preço semanal"],
        ["04/06 — 20h–23h",     "COMPRAR 88-rated (1-2x)", "Preços baixos antes da antecipação do Festival"],
        ["05/06 — 16h–18h BST", "AGUARDAR / NÃO VENDER",  "Última hora antes do Festival — preços ainda baixos"],
        ["05/06 — 18h–20h BST", "MONITORAR (Festival live)","Abertura de packs => preços caem brevemente"],
        ["05/06 — 20h–23h BST", "VENDER fodder 83-85",     "SBCs ativos => demanda sobe rapidamente"],
        ["06/06 — Manhã UTC",   "VENDER 88-rated",         "Preços altos do fim de semana pós-evento"],
        ["06/06 – 07/06",       "VENDER restante do fodder","Weekend League => alta demanda por SBCs"],
        ["Quinta 11/06",        "Repetir ciclo Thursday",  "Novo ciclo de Rivals Rewards"],
    ]

    ti_col = [4.0, 4.5, 7.8]
    ti_data = [[p_cell(h, S["CellHdr"]) for h in timing_hdr]]
    for row in timing_rows:
        ti_data.append([
            p_cell(row[0], S["CellCenter"]),
            p_cell(row[1], S["CellBody"]),
            p_cell(row[2], S["CellBody"]),
        ])
    ti_t = Table(ti_data, colWidths=[w*cm for w in ti_col], repeatRows=1)
    ti_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  TABLE_HDR),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [TABLE_ROW, TABLE_ALT]),
        ("GRID",          (0, 0), (-1, -1), 0.3, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    story.append(ti_t)

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>Regra de timing:</b> Nunca venda fodder entre 15h–18h BST na sexta-feira "
        "(abertura de packs do Festival inunda o mercado). Espere os SBCs serem ativados "
        "entre 20h–23h BST para vender com margem máxima.",
        S["RBody"]))

    story.append(Spacer(1, 0.3*cm))

    # ── 5. ESTIMATIVA DE RETORNO 48H ────────────────────────────────────────
    story.append(Paragraph("5. ESTIMATIVA DE RETORNO EM 48H", S["RSection"]))

    ret_hdr = ["CENÁRIO", "INVEST. ATIVO", "RETORNO BRUTO", "TAXA EA (5%)", "LUCRO LÍQUIDO", "ROI"]
    ret_rows = [
        ["Conservador", "35.000c", "46.450c", "-2.323c", "+9.127c",  "+26%"],
        ["Realista",    "35.000c", "50.100c", "-2.505c", "+12.595c", "+36%"],
        ["Otimista",    "35.000c", "57.190c", "-2.860c", "+19.330c", "+55%"],
    ]

    r_col = [2.8, 2.8, 2.8, 2.5, 3.2, 2.0]
    r_data = [[p_cell(h, S["CellHdr"]) for h in ret_hdr]]
    for row in ret_rows:
        r_data.append([
            p_cell(row[0], S["CellBody"]),
            p_cell(row[1], S["CellCenter"]),
            p_cell(row[2], S["CellCenter"]),
            p_cell(row[3], S["CellCenter"]),
            p_cell(row[4], S["CellGold"]),
            p_cell(row[5], S["CellGold"]),
        ])
    r_t = Table(r_data, colWidths=[w*cm for w in r_col], repeatRows=1)
    r_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  TABLE_HDR),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [TABLE_ROW, TABLE_ALT]),
        ("GRID",          (0, 0), (-1, -1), 0.3, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    story.append(r_t)

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>Nota:</b> Conservador = 60% das cartas vendidas no pico; Realista = 80%; "
        "Otimista = 95%+ com Festival em plena atividade. Risco principal: preços não "
        "subirem o suficiente se houver excesso de supply de packs gratuitos.",
        S["RBody"]))

    story.append(Spacer(1, 0.3*cm))

    # ── 6. OPORTUNIDADE EXTRA — SBC ARBITRAGE ───────────────────────────────
    story.append(Paragraph("6. OPORTUNIDADE EXTRA: SBC ARBITRAGE", S["RSection"]))
    story.append(Paragraph(
        "O <b>10x 84+ Upgrade SBC</b> (ativo até 12/06/2026) apresenta valor positivo claro: "
        "custo de montagem ~15.750c, valor esperado dos packs ~22.625c. "
        "Com 5% de taxa EA ao vender as cartas: receita ~21.494c. "
        "<b>Lucro líquido por submissão: ~5.744c (+36%).</b>",
        S["RBody"]))
    story.append(Paragraph(
        "Estratégia: monte o squad com 83-84 rated baratos (tabela acima), complete o SBC, "
        "venda as cartas do pack. Repetível até 3x. "
        "Máximo com 40.000c: <b>2 submissões = lucro estimado ~11.500c.</b>",
        S["RBody"]))

    story.append(Spacer(1, 0.3*cm))

    # ── 7. OITO REGRAS DE OURO ───────────────────────────────────────────────
    story.append(Paragraph("7. AS 8 REGRAS DE OURO DO TRADE", S["RSection"]))

    rules = [
        ("#1 — Compre na quinta, venda no fim de semana.",
         "Rivals Rewards derrubam preços toda quinta. Weekend League sobe a demanda sábado-domingo."),
        ("#2 — Nunca segure fodder por mais de 48-72h.",
         "O mercado de fodder é volátil. Se o preço atingir a meta, venda imediatamente."),
        ("#3 — Respeite a taxa de 5% sempre nos cálculos.",
         "Esquecer a taxa EA transforma lucros em prejuízo. Sempre: preco_venda x 0,95."),
        ("#4 — Diversifique entre ratings e ligas.",
         "Não concentre tudo em um tipo de carta. Distribua para reduzir risco de supply shock."),
        ("#5 — Monitore SBCs novos em tempo real.",
         "Um novo SBC pode disparar a demanda por um tipo específico de fodder em minutos."),
        ("#6 — Evite comprar 15-30 min após um drop de promo.",
         "Na abertura de packs, preços caem temporariamente. Espere estabilizar antes de comprar."),
        ("#7 — Nunca invista 100% do capital em uma única carta.",
         "Máximo de 30% do budget em uma posição. Mantenha liquidez para oportunidades surgidas."),
        ("#8 — Lucro realizado é intocável — reinvista apenas o lucro.",
         "Separe o capital base do lucro. Reinvista o lucro para crescer de forma sustentável."),
    ]
    for titulo, desc in rules:
        story.append(Paragraph(titulo, S["RGold"]))
        story.append(Paragraph(f"   {desc}", S["RBullet"]))

    story.append(Spacer(1, 0.3*cm))

    # ── 8. RESUMO EXECUTIVO ──────────────────────────────────────────────────
    story.append(hr(ACCENT, 1))
    story.append(Paragraph("RESUMO EXECUTIVO", S["RHighlight"]))

    resumo_rows = [
        ["Hoje (04/06)", "COMPRAR. Quinta-feira = piso semanal. Festival of Football amanhã."],
        ["Janela ideal", "14h-21h UTC hoje para compras. Vender 05/06 após 20h BST."],
        ["Melhor trade", "Grimaldo 84 (Leverkusen): +54% margem. Maddison 84: +51%."],
        ["SBC Extra",    "10x 84+ Upgrade: +36% por submissão (máx 3x, limite 12/06)."],
        ["Retorno 48h",  "Conservador: +9.127c  |  Realista: +12.595c  |  Otimista: +19.330c"],
        ["Budget final", "Budget: 40.000c  =>  Meta 48h: 49.000c - 59.000c"],
    ]
    res_data = []
    for label, value in resumo_rows:
        res_data.append([
            p_cell(label, S["CellAccent"]),
            p_cell(value, S["CellBody"]),
        ])
    res_t = Table(res_data, colWidths=[3.8*cm, 12.5*cm])
    res_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, -1), TABLE_HDR),
        ("BACKGROUND",    (1, 0), (1, -1), TABLE_ALT),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",          (0, 0), (-1, -1), 0.3, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ]))
    story.append(res_t)

    story.append(Spacer(1, 0.4*cm))
    story.append(hr(BORDER))

    # ── DISCLAIMER ────────────────────────────────────────────────────────────
    story.append(Paragraph("AVISO LEGAL / DISCLAIMER", S["RSubSec"]))
    story.append(Paragraph(
        "Este relatório é gerado automaticamente por um agente de análise de mercado para fins "
        "educacionais e de entretenimento. As previsões de preço e estimativas de lucro são "
        "baseadas em tendências históricas, dados públicos e análise de eventos do EA FC 26. "
        "O mercado do Ultimate Team é altamente volátil e os resultados reais podem diferir "
        "significativamente das projeções apresentadas. Não garantimos lucro. "
        "Invista apenas o que está disposto a perder. EA Sports pode alterar as mecânicas do jogo, "
        "introduzir novos packs ou modificar eventos sem aviso prévio. "
        "Este documento não é aconselhamento financeiro. "
        "Fontes: FUTBIN, FUT.GG, Team Gullit, EA Sports Official, Sportskeeda, "
        "RealSport101, FifaUTeam, ItemD2R.",
        S["RDisclaim"]))

    story.append(Spacer(1, 0.15*cm))
    story.append(Paragraph(
        "© 2026 Agente de Análise de Mercado FUT  |  EA FC 26 Ultimate Team Trading Report",
        S["RDisclaim"]))

    doc.build(story)
    print(f"PDF gerado com sucesso: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
