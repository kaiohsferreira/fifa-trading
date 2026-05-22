#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.platypus.flowables import PageBreak
from reportlab.lib.colors import HexColor
import os

# ─── Palette ─────────────────────────────────────────────────────────────────
VERDE       = HexColor("#00C853")
VERDE_DARK  = HexColor("#007E33")
VERDE_LIGHT = HexColor("#E8F5E9")
AMARELO     = HexColor("#FFD600")
LARANJA     = HexColor("#FF6D00")
AZUL_DARK   = HexColor("#0D1B2A")
CINZA_MED   = HexColor("#37474F")
CINZA_LIGHT = HexColor("#ECEFF1")
BRANCO      = colors.white
PRETO       = colors.black
VERMELHO    = HexColor("#D50000")

OUTPUT_FILE = "relatorio-trading-2026-05-22-14h.pdf"

def build_styles():
    base = getSampleStyleSheet()
    styles = {}

    styles["titulo_principal"] = ParagraphStyle(
        "titulo_principal",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=BRANCO,
        alignment=TA_CENTER,
        leading=28,
        spaceAfter=4,
    )
    styles["subtitulo"] = ParagraphStyle(
        "subtitulo",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=AMARELO,
        alignment=TA_CENTER,
        leading=18,
        spaceAfter=2,
    )
    styles["data_hora"] = ParagraphStyle(
        "data_hora",
        fontName="Helvetica",
        fontSize=10,
        textColor=CINZA_LIGHT,
        alignment=TA_CENTER,
        spaceAfter=0,
    )
    styles["section_title"] = ParagraphStyle(
        "section_title",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=BRANCO,
        spaceBefore=14,
        spaceAfter=6,
        leading=18,
    )
    styles["body"] = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=AZUL_DARK,
        leading=14,
        spaceAfter=4,
    )
    styles["body_bold"] = ParagraphStyle(
        "body_bold",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=AZUL_DARK,
        leading=14,
        spaceAfter=4,
    )
    styles["bullet"] = ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=AZUL_DARK,
        leading=14,
        leftIndent=14,
        spaceAfter=3,
        bulletIndent=4,
    )
    styles["disclaimer"] = ParagraphStyle(
        "disclaimer",
        fontName="Helvetica-Oblique",
        fontSize=8,
        textColor=CINZA_MED,
        leading=12,
        alignment=TA_JUSTIFY,
    )
    styles["rule_num"] = ParagraphStyle(
        "rule_num",
        fontName="Helvetica-Bold",
        fontSize=10,
        textColor=VERDE_DARK,
        leading=14,
        spaceAfter=2,
    )
    styles["tag"] = ParagraphStyle(
        "tag",
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=BRANCO,
        alignment=TA_CENTER,
        leading=10,
    )
    return styles


def header_block(styles):
    """Dark green header banner."""
    header_data = [
        [Paragraph("EA FC 26 · RELATÓRIO DE TRADING", styles["titulo_principal"])],
        [Paragraph("Ultimate Team Market Intelligence", styles["subtitulo"])],
        [Paragraph("22/05/2026  14:06 UTC", styles["data_hora"])],
    ]
    tbl = Table(header_data, colWidths=[17 * cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), AZUL_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
        ("ROUNDEDCORNERS", [8]),
    ]))
    return tbl


def section_header(text, styles):
    row = [[Paragraph(f"  {text}", styles["section_title"])]]
    tbl = Table(row, colWidths=[17 * cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), VERDE_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return tbl


def badge(text, cor, styles):
    row = [[Paragraph(text, styles["tag"])]]
    tbl = Table(row, colWidths=[2.2 * cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), cor),
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return tbl


def players_table(styles):
    """Main recommendations table."""

    col_headers = [
        Paragraph("<b>Jogador</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
            fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>OVR</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
            fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Clube / Liga</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
            fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Posição</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
            fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Compra\n(coins)</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
            fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Venda\n(coins)</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
            fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Margem\n(–5% EA)</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
            fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Estratégia</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
            fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
    ]

    # (Jogador, OVR, Clube/Liga, Posição, Compra, Venda, Margem líquida, Estratégia)
    # Margem = Venda × 0.95 – Compra
    cards = [
        ("Sadio Mané",        "83", "Al-Nassr\n(Saudi Pro Lg)", "LW",  800,  2_000,  1_100, "SBC Fodder"),
        ("Luka Modrić",       "83", "Al-Qadsiah\n(Saudi Pro Lg)","CM", 850,  2_200,  1_240, "SBC Fodder"),
        ("Micky van de Ven",  "83", "Tottenham\n(Premier Lg)",   "CB",  800,  1_900,  1_005, "SBC Fodder"),
        ("Mikel Merino",      "83", "Arsenal\n(Premier Lg)",     "CM",  800,  2_100,  1_195, "SBC Fodder"),
        ("Moise Kean",        "83", "Fiorentina\n(Serie A)",     "ST",  750,  1_850,    957, "SBC Fodder"),
        ("Alessandro Acerbi", "84", "Inter Milan\n(Serie A)",    "CB",  950,  2_600,  1_520, "SBC Fodder"),
        ("Bernardo Silva",    "84", "Manchester City\n(Premier Lg)","CM",1_100,2_800, 1_560, "SBC Fodder"),
        ("Alejandro Grimaldo","84", "Bayer Leverkusen\n(Bundesliga)","LB",1_050,2_700,1_515,"SBC Fodder"),
        ("Valverde",          "85", "Real Madrid\n(La Liga)",    "CM",  2_200, 5_200, 2_740, "La Liga SBC"),
        ("Pedri",             "86", "Barcelona\n(La Liga)",      "CM",  2_500, 5_800, 3_010, "La Liga SBC"),
    ]

    def fmt(n):
        return f"{n:,}".replace(",", ".")

    cell_style = ParagraphStyle("cell", fontName="Helvetica", fontSize=8.5,
                                 textColor=AZUL_DARK, alignment=TA_CENTER, leading=12)
    cell_bold  = ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=8.5,
                                 textColor=AZUL_DARK, alignment=TA_CENTER, leading=12)

    data = [col_headers]
    for i, (nome, ovr, clube, pos, compra, venda, margem, estrategia) in enumerate(cards):
        row_bg = CINZA_LIGHT if i % 2 == 0 else BRANCO
        data.append([
            Paragraph(nome, cell_bold),
            Paragraph(ovr, cell_bold),
            Paragraph(clube, cell_style),
            Paragraph(pos, cell_style),
            Paragraph(fmt(compra), cell_style),
            Paragraph(fmt(venda), cell_style),
            Paragraph(f"<b>{fmt(margem)}</b>", ParagraphStyle("mg", fontName="Helvetica-Bold",
                fontSize=8.5, textColor=VERDE_DARK, alignment=TA_CENTER, leading=12)),
            Paragraph(estrategia, cell_style),
        ])

    col_widths = [3.3*cm, 1.2*cm, 3.2*cm, 1.5*cm, 1.7*cm, 1.7*cm, 2.0*cm, 2.4*cm]

    tbl = Table(data, colWidths=col_widths, repeatRows=1)
    tbl.setStyle(TableStyle([
        # Header
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_DARK),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("TOPPADDING",    (0, 0), (-1, 0), 7),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
        # Data rows alternating
        *[("BACKGROUND", (0, i+1), (-1, i+1),
           CINZA_LIGHT if i % 2 == 0 else BRANCO) for i in range(len(cards))],
        # All cells
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING",    (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("GRID",          (0, 0), (-1, -1), 0.5, HexColor("#B0BEC5")),
        ("BOX",           (0, 0), (-1, -1), 1,   VERDE_DARK),
        # Highlight margin column
        ("BACKGROUND",    (6, 1), (6, -1), VERDE_LIGHT),
    ]))
    return tbl


def portfolio_table(styles):
    """Budget allocation table."""
    cell_c = ParagraphStyle("cc", fontName="Helvetica", fontSize=9,
                             textColor=AZUL_DARK, alignment=TA_CENTER)
    cell_b = ParagraphStyle("cb", fontName="Helvetica-Bold", fontSize=9,
                             textColor=AZUL_DARK, alignment=TA_CENTER)

    header = [
        Paragraph("<b>Faixa de OVR</b>",   ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Qtd de Cartas</b>",   ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Preço Médio Compra</b>",ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Capital Alocado</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>% do Budget</b>",     ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
    ]
    rows = [
        ("83 rated (fodder bulk)",  "20", "850",   "17.000",  "42,5%"),
        ("84 rated (fodder mid)",   "10", "1.050",  "10.500",  "26,3%"),
        ("85–86 rated (La Liga)",    "4", "2.500",  "10.000",  "25,0%"),
        ("Reserva (liquidez)",       "—",    "—",    "2.500",   "6,2%"),
    ]
    data = [header]
    for i, r in enumerate(rows):
        data.append([Paragraph(x, cell_b if i == 3 else cell_c) for x in r])
    # Total row
    data.append([
        Paragraph("<b>TOTAL</b>",      cell_b),
        Paragraph("<b>34</b>",         cell_b),
        Paragraph("—",                 cell_c),
        Paragraph("<b>40.000</b>",     cell_b),
        Paragraph("<b>100%</b>",       cell_b),
    ])

    col_widths = [5.0*cm, 2.8*cm, 3.5*cm, 3.2*cm, 2.5*cm]
    tbl = Table(data, colWidths=col_widths)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  AZUL_DARK),
        *[("BACKGROUND",  (0, i+1), (-1, i+1),
           CINZA_LIGHT if i % 2 == 0 else BRANCO) for i in range(len(rows))],
        ("BACKGROUND",    (0, -1), (-1, -1), VERDE_DARK),
        ("TEXTCOLOR",     (0, -1), (-1, -1), BRANCO),
        ("VALIGN",        (0, 0),  (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0),  (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0),  (-1, -1), 6),
        ("GRID",          (0, 0),  (-1, -1), 0.5, HexColor("#B0BEC5")),
        ("BOX",           (0, 0),  (-1, -1), 1,   VERDE_DARK),
    ]))
    return tbl


def return_table(styles):
    """48h return estimate table."""
    cell_c = ParagraphStyle("cc", fontName="Helvetica", fontSize=9,
                             textColor=AZUL_DARK, alignment=TA_CENTER)
    cell_b = ParagraphStyle("cb", fontName="Helvetica-Bold", fontSize=9,
                             textColor=AZUL_DARK, alignment=TA_CENTER)

    header = [
        Paragraph("<b>Cenário</b>",          ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Capital Inicial</b>",  ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Capital Final</b>",    ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Lucro Estimado</b>",   ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Retorno (%)</b>",      ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Premissa</b>",         ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
    ]
    rows = [
        ("🔵 Conservador", "40.000", "54.000 – 58.000", "+14.000 – 18.000", "35% – 45%",
         "SBCs moderados, venda\ncautela, 1–2 ciclos"),
        ("🟢 Otimista",    "40.000", "68.000 – 80.000", "+28.000 – 40.000", "70% – 100%",
         "SBCs grandes (EoA),\n2–3 ciclos, timing preciso"),
    ]
    data = [header]
    for i, r in enumerate(rows):
        cor = CINZA_LIGHT if i == 0 else VERDE_LIGHT
        data.append([Paragraph(x, cell_c) for x in r])

    col_widths = [2.8*cm, 2.5*cm, 3.5*cm, 3.5*cm, 2.2*cm, 2.5*cm]
    tbl = Table(data, colWidths=col_widths)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  AZUL_DARK),
        ("BACKGROUND",    (0, 1), (-1, 1),  CINZA_LIGHT),
        ("BACKGROUND",    (0, 2), (-1, 2),  VERDE_LIGHT),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("GRID",          (0, 0), (-1, -1), 0.5, HexColor("#B0BEC5")),
        ("BOX",           (0, 0), (-1, -1), 1,   VERDE_DARK),
    ]))
    return tbl


def timing_table(styles):
    cell_c = ParagraphStyle("cc", fontName="Helvetica", fontSize=9,
                             textColor=AZUL_DARK, alignment=TA_LEFT)
    cell_b = ParagraphStyle("cb", fontName="Helvetica-Bold", fontSize=9,
                             textColor=AZUL_DARK, alignment=TA_CENTER)
    header = [
        Paragraph("<b>Horário (UTC)</b>",  ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Ação</b>",           ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Justificativa</b>",  ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Prioridade</b>",     ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
    ]
    timing_rows = [
        ("14:00–17:00\n(AGORA)",
         "COMPRAR 83–84 rated\nbulk + 85–86 La Liga",
         "Preços no piso antes do drop.\nÚltima janela de compra barata.",
         "🔴 URGENTE"),
        ("17:00–17:30",
         "AGUARDAR drop e\nlistar SBCs disponíveis",
         "Ultimate TOTS cai às 18h BST\n(17h UTC). Analisar SBCs novos.",
         "⚡ CRÍTICO"),
        ("17:30–20:00",
         "VENDER fodder 83–84\nprimeira onda",
         "Demanda explode nos\nprimeiros SBCs do TOTS.",
         "🟢 EXECUTAR"),
        ("20:00–23:00",
         "RECOMPRAR 83–84\nse preços caírem",
         "Após primeira onda de SBCs,\npreços podem baixar levemente.",
         "🔵 OPORTUNIDADE"),
        ("23/05 · 09:00–12:00",
         "VENDER 85–86 rated\n(La Liga focus)",
         "SBCs de End of an Era tendem\na puxar La Liga 85–86.",
         "🟢 EXECUTAR"),
        ("23/05 · 13:00–17:00",
         "VENDER restante\ne fechar posições",
         "Antes de novas cartas fifth-day.\nRealizar lucro antes de Weekend.",
         "🔵 FINALIZAR"),
    ]
    data = [header]
    for i, r in enumerate(timing_rows):
        data.append([Paragraph(x, cell_b if j == 0 or j == 3 else cell_c)
                     for j, x in enumerate(r)])
    col_widths = [2.9*cm, 4.0*cm, 6.3*cm, 3.8*cm]
    tbl = Table(data, colWidths=col_widths)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0),  (-1, 0),  AZUL_DARK),
        *[("BACKGROUND",  (0, i+1), (-1, i+1),
           CINZA_LIGHT if i % 2 == 0 else BRANCO) for i in range(len(timing_rows))],
        ("VALIGN",        (0, 0),  (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0),  (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0),  (-1, -1), 5),
        ("LEFTPADDING",   (0, 0),  (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0),  (-1, -1), 5),
        ("GRID",          (0, 0),  (-1, -1), 0.5, HexColor("#B0BEC5")),
        ("BOX",           (0, 0),  (-1, -1), 1,   VERDE_DARK),
    ]))
    return tbl


def golden_rules_block(styles):
    rules = [
        ("01", "Nunca compre acima do preço de compra recomendado.",
               "Sua margem é definida na compra, não na venda."),
        ("02", "Use buy orders, não compre pelo preço de venda imediato.",
               "Economize 10–20% usando ordens de compra pacientes."),
        ("03", "Liste sempre pelo tempo máximo (1h no pico, 3–6h fora do pico).",
               "Listagens curtas se acumulam em taxas invisíveis."),
        ("04", "Nunca liste mais de 10 cópias do mesmo card simultaneamente.",
               "Excesso de oferta colapsa o preço durante o processo de venda."),
        ("05", "Venda ANTES do grande drop de conteúdo, compre DEPOIS.",
               "O mercado sobre na antecipação e cai na realização."),
        ("06", "Monitore o reddit (r/EAFC) e Twitter para leaks 30–60min antes.",
               "Leaks confirmados são oportunidades de arbitragem de tempo."),
        ("07", "Reserve sempre ≥5% do capital como liquidez de emergência.",
               "Permite aproveitar picos inesperados sem desmontar posições."),
        ("08", "Registre cada trade: card, preço de compra, venda e lucro líquido.",
               "Sem dados históricos, você repete os mesmos erros."),
    ]
    body_style = ParagraphStyle("br", fontName="Helvetica", fontSize=9,
                                 textColor=AZUL_DARK, leading=13)
    bold_style = ParagraphStyle("bb", fontName="Helvetica-Bold", fontSize=9,
                                 textColor=AZUL_DARK, leading=13)
    num_style  = ParagraphStyle("bn", fontName="Helvetica-Bold", fontSize=11,
                                 textColor=VERDE_DARK, alignment=TA_CENTER)

    rows = []
    for num, regra, motivo in rules:
        row = [
            Paragraph(num, num_style),
            [Paragraph(regra, bold_style), Paragraph(motivo, body_style)],
        ]
        rows.append(row)

    tbl = Table(rows, colWidths=[1.2*cm, 15.8*cm])
    style_cmds = [
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#B0BEC5")),
        ("BOX",           (0, 0), (-1, -1), 1,   VERDE_DARK),
    ]
    for i in range(len(rules)):
        bg = VERDE_LIGHT if i % 2 == 0 else BRANCO
        style_cmds.append(("BACKGROUND", (0, i), (-1, i), bg))
    tbl.setStyle(TableStyle(style_cmds))
    return tbl


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        leftMargin=2*cm,
        rightMargin=2*cm,
        topMargin=1.8*cm,
        bottomMargin=1.8*cm,
        title="Relatório de Trading EA FC 26",
        author="EA FC 26 Market Intelligence",
    )

    styles = build_styles()
    story  = []

    # ── CABEÇALHO ─────────────────────────────────────────────────────────────
    story.append(header_block(styles))
    story.append(Spacer(1, 0.5*cm))

    # ── 1. CONTEXTO DE MERCADO ────────────────────────────────────────────────
    story.append(section_header("1. CONTEXTO DE MERCADO — 22/05/2026", styles))
    story.append(Spacer(1, 0.25*cm))

    ctx_items = [
        ("<b>🏆 Ultimate TOTS</b> — A maior promo do ano chega HOJE (22/05) às <b>18h BST / 17h UTC</b>. "
         "É o squad final da temporada com os melhores OVRs de todos os TOTS anteriores. Esperados: "
         "Mbappe (97+), Messi, Ronaldo, Lamine Yamal, Rice, Gabriel e dezenas de cartas 92–96 OVR."),
        ("<b>📋 End of an Era SBCs</b> — EA costuma lançar 4–8 SBCs de EoA junto ao Ultimate TOTS. "
         "Leaks apontam Bernardo Silva, Salah, Griezmann e Stones. Cada SBC consome dezenas de cartas "
         "83–86 rated, criando <b>picos de demanda de fodder nas próximas 48h</b>."),
        ("<b>📈 Ratings Reload (ativo até 12/06)</b> — Cartas de upgrade ainda ativas. Jogadores "
         "da Saudi Pro League e ligas menores lideram os upgrades, mantendo demanda por cartas 83–84."),
        ("<b>⚽ UEFA Knockout Stage (até 30/05)</b> — Live cards ainda ativos. Jogadores de equipes "
         "que avançaram nas copas europeias têm cartas em valorização contínua."),
        ("<b>📉 Fodder no piso</b> — Com o Ultimate TOTS prestes a chegar, o mercado está temporariamente "
         "saturado de cartas antigas. Cartas 83–84 estão perto do preço mínimo histórico — "
         "<b>janela de compra ideal nas próximas 2–3 horas</b>."),
    ]
    for item in ctx_items:
        story.append(Paragraph(f"• {item}", styles["bullet"]))
        story.append(Spacer(1, 0.1*cm))

    story.append(Spacer(1, 0.3*cm))

    # ── 2. TABELA DE RECOMENDAÇÕES ────────────────────────────────────────────
    story.append(section_header("2. CARTAS RECOMENDADAS PARA COMPRA", styles))
    story.append(Spacer(1, 0.25*cm))
    story.append(Paragraph(
        "Margem líquida = (Preço de Venda × 0,95) – Preço de Compra. "
        "Preços estimados com base em padrões históricos de TOTS e comportamento de mercado em 22/05/2026.",
        styles["body"]
    ))
    story.append(Spacer(1, 0.2*cm))
    story.append(players_table(styles))
    story.append(Spacer(1, 0.3*cm))

    # ── 3. ALOCAÇÃO DO BUDGET ─────────────────────────────────────────────────
    story.append(section_header("3. ALOCAÇÃO DO BUDGET (40.000 coins)", styles))
    story.append(Spacer(1, 0.25*cm))
    story.append(portfolio_table(styles))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Nota: A reserva de 2.500 coins permite reagir a oportunidades intraday sem desmontar posições abertas. "
        "Priorize buy orders para reduzir custo médio em até 15%.",
        styles["body"]
    ))
    story.append(Spacer(1, 0.3*cm))

    # ── 4. TIMING ────────────────────────────────────────────────────────────
    story.append(section_header("4. ESTRATÉGIA DE TIMING — 22 E 23/05/2026", styles))
    story.append(Spacer(1, 0.25*cm))
    story.append(timing_table(styles))
    story.append(Spacer(1, 0.25*cm))
    story.append(Paragraph(
        "<b>⚠️ Atenção ao ciclo de SBCs:</b> Cada novo SBC lançado gera uma onda de demanda de 30–90 minutos. "
        "Se múltiplos SBCs forem lançados ao mesmo tempo (prática comum no dia de TOTS), o pico de preço do "
        "fodder pode durar 2–4 horas. Liste suas cartas no início de cada onda para maximizar o retorno.",
        styles["body"]
    ))
    story.append(Spacer(1, 0.3*cm))

    # ── 5. ESTIMATIVA DE RETORNO ──────────────────────────────────────────────
    story.append(section_header("5. ESTIMATIVA DE RETORNO EM 48H", styles))
    story.append(Spacer(1, 0.25*cm))
    story.append(return_table(styles))
    story.append(Spacer(1, 0.2*cm))

    notes = [
        "Os cenários assumem <b>2–3 ciclos de compra-e-venda</b> no período de 48h, aproveitando múltiplos "
        "drops de SBC durante a semana de Ultimate TOTS.",
        "O cenário conservador considera apenas 1 ciclo completo com venda abaixo do pico máximo.",
        "O cenário otimista assume timing preciso, SBCs de End of an Era com alto consumo de fodder e "
        "pelo menos 2 ciclos completos.",
        "Estes valores <b>não garantem lucro</b> — o mercado pode se comportar diferente se EA alterar o "
        "calendário de conteúdo ou se houver problemas de servidor.",
    ]
    for n in notes:
        story.append(Paragraph(f"• {n}", styles["bullet"]))

    story.append(Spacer(1, 0.3*cm))

    # ── 6. 8 REGRAS DE OURO ───────────────────────────────────────────────────
    story.append(section_header("6. AS 8 REGRAS DE OURO DO TRADE", styles))
    story.append(Spacer(1, 0.25*cm))
    story.append(golden_rules_block(styles))
    story.append(Spacer(1, 0.3*cm))

    # ── 7. DISCLAIMER ─────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor("#B0BEC5"),
                             spaceAfter=8))
    story.append(Paragraph("DISCLAIMER", ParagraphStyle(
        "disc_title", fontName="Helvetica-Bold", fontSize=9,
        textColor=CINZA_MED, spaceAfter=4)))
    story.append(Paragraph(
        "Este relatório é produzido exclusivamente para fins informativos e educacionais sobre o "
        "mercado de Ultimate Team do EA FC 26. As análises, preços e recomendações aqui contidas "
        "são estimativas baseadas em dados históricos de comportamento de mercado e padrões "
        "observados em eventos similares anteriores — não constituem garantia de lucro. "
        "O mercado de FUT é volátil e sujeito a alterações a qualquer momento por decisão da EA Sports "
        "(mudanças de conteúdo, servidor fora do ar, alterações de price range, etc.). "
        "O autor não se responsabiliza por perdas decorrentes de decisões de trading baseadas neste documento. "
        "Nunca invista mais do que está disposto a perder. Relatório gerado em 22/05/2026 às 14:06 UTC.",
        styles["disclaimer"]
    ))

    doc.build(story)
    print(f"PDF gerado: {OUTPUT_FILE}")


if __name__ == "__main__":
    build_pdf()
