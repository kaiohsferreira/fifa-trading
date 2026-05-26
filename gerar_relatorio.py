#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Relatório de Trading - EA FC 26 Ultimate Team
Data: 2026-05-26 20:07 UTC
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer,
    HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak

# ──────────────────────────────────────────────────────────────
# CONFIGURAÇÕES GERAIS
# ──────────────────────────────────────────────────────────────
REPORT_DATE_DISPLAY = "26/05/2026 20:07"
REPORT_DATE_FILE    = "2026-05-26-20h"
PDF_FILENAME        = f"relatorio-trading-{REPORT_DATE_FILE}.pdf"

# Cores do tema EA FC 26
VERDE_EA    = colors.HexColor("#00B140")
VERDE_ESCURO = colors.HexColor("#006B28")
AMARELO_EA  = colors.HexColor("#F5A623")
CINZA_ESCURO = colors.HexColor("#1A1A2E")
CINZA_MEDIO = colors.HexColor("#2D2D4E")
CINZA_CLARO = colors.HexColor("#F0F0F0")
BRANCO      = colors.white
VERMELHO    = colors.HexColor("#D0021B")
AZUL_INFO   = colors.HexColor("#0066CC")
LARANJA     = colors.HexColor("#FF6B00")

# ──────────────────────────────────────────────────────────────
# ESTILOS
# ──────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

style_titulo = ParagraphStyle(
    "Titulo",
    parent=styles["Heading1"],
    fontSize=22,
    textColor=BRANCO,
    alignment=TA_CENTER,
    spaceAfter=4,
    fontName="Helvetica-Bold",
    leading=26,
)
style_subtitulo = ParagraphStyle(
    "Subtitulo",
    parent=styles["Heading2"],
    fontSize=13,
    textColor=AMARELO_EA,
    alignment=TA_CENTER,
    spaceAfter=2,
    fontName="Helvetica-Bold",
    leading=16,
)
style_data = ParagraphStyle(
    "DataHora",
    fontSize=10,
    textColor=CINZA_CLARO,
    alignment=TA_CENTER,
    spaceAfter=0,
    fontName="Helvetica",
)
style_section = ParagraphStyle(
    "Section",
    fontSize=13,
    textColor=CINZA_ESCURO,
    fontName="Helvetica-Bold",
    spaceBefore=14,
    spaceAfter=6,
    borderPad=4,
)
style_body = ParagraphStyle(
    "Body",
    fontSize=9.5,
    textColor=colors.HexColor("#222222"),
    fontName="Helvetica",
    spaceBefore=3,
    spaceAfter=3,
    alignment=TA_JUSTIFY,
    leading=14,
)
style_bullet = ParagraphStyle(
    "Bullet",
    fontSize=9.5,
    textColor=colors.HexColor("#222222"),
    fontName="Helvetica",
    spaceBefore=2,
    spaceAfter=2,
    leftIndent=14,
    leading=14,
)
style_highlight = ParagraphStyle(
    "Highlight",
    fontSize=9.5,
    textColor=VERDE_ESCURO,
    fontName="Helvetica-Bold",
    spaceBefore=2,
    spaceAfter=2,
    leading=14,
)
style_disclaimer = ParagraphStyle(
    "Disclaimer",
    fontSize=8,
    textColor=colors.HexColor("#555555"),
    fontName="Helvetica-Oblique",
    spaceBefore=4,
    spaceAfter=4,
    alignment=TA_JUSTIFY,
    leading=11,
)
style_footer_text = ParagraphStyle(
    "FooterText",
    fontSize=8,
    textColor=colors.HexColor("#888888"),
    fontName="Helvetica",
    alignment=TA_CENTER,
)
style_rule = ParagraphStyle(
    "Rule",
    fontSize=9.5,
    textColor=CINZA_ESCURO,
    fontName="Helvetica",
    spaceBefore=3,
    spaceAfter=3,
    leftIndent=18,
    leading=14,
)
style_rule_title = ParagraphStyle(
    "RuleTitle",
    fontSize=10,
    textColor=VERDE_ESCURO,
    fontName="Helvetica-Bold",
    spaceBefore=3,
    spaceAfter=1,
    leftIndent=18,
    leading=14,
)


# ──────────────────────────────────────────────────────────────
# FUNÇÕES AUXILIARES
# ──────────────────────────────────────────────────────────────
def header_block():
    """Bloco de cabeçalho com fundo escuro."""
    header_data = [
        [Paragraph("⚽  EA FC 26 ULTIMATE TEAM", style_titulo)],
        [Paragraph("Relatório Diário de Trading", style_subtitulo)],
        [Paragraph(f"📅  {REPORT_DATE_DISPLAY}  UTC", style_data)],
    ]
    t = Table(header_data, colWidths=[17 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CINZA_ESCURO),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [CINZA_ESCURO]),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return t


def section_header(text, icon="▶"):
    items = []
    items.append(HRFlowable(width="100%", thickness=2, color=VERDE_EA, spaceAfter=4))
    items.append(Paragraph(f"{icon}  {text}", style_section))
    return items


def badge(text, bg=VERDE_EA, fg=BRANCO, fontsize=9):
    badge_data = [[Paragraph(
        f'<font name="Helvetica-Bold" size="{fontsize}" color="white">{text}</font>',
        ParagraphStyle("b", alignment=TA_CENTER, leading=fontsize + 4)
    )]]
    t = Table(badge_data, colWidths=[3.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return t


# ──────────────────────────────────────────────────────────────
# DADOS DAS CARTAS RECOMENDADAS
# ──────────────────────────────────────────────────────────────
# Colunas: Jogador | OVR | Clube | Pos | Compra | Venda | Margem | Estratégia
recomendacoes = [
    # 85-rated SBC fodder (cheap rare golds)
    {
        "jogador": "Scott McTominay",
        "ovr": 85,
        "clube": "SSC Napoli",
        "pos": "CM",
        "compra": 2100,
        "venda": 3900,
        "estrategia": "SBC Fodder Flip",
        "prazo": "24h",
    },
    {
        "jogador": "Ryan Gravenberch",
        "ovr": 85,
        "clube": "Liverpool",
        "pos": "CDM",
        "compra": 2300,
        "venda": 4100,
        "estrategia": "SBC Fodder Flip",
        "prazo": "24h",
    },
    {
        "jogador": "Youri Tielemans",
        "ovr": 85,
        "clube": "Aston Villa",
        "pos": "CM",
        "compra": 1900,
        "venda": 3600,
        "estrategia": "SBC Fodder Flip",
        "prazo": "24h",
    },
    {
        "jogador": "Yann Sommer",
        "ovr": 85,
        "clube": "Inter Milan",
        "pos": "GK",
        "compra": 1800,
        "venda": 3400,
        "estrategia": "SBC Fodder Flip",
        "prazo": "24h",
    },
    # 86-rated SBC fodder
    {
        "jogador": "Bruno Guimarães",
        "ovr": 86,
        "clube": "Newcastle Utd",
        "pos": "CM",
        "compra": 3200,
        "venda": 5800,
        "estrategia": "SBC Fodder Flip",
        "prazo": "36h",
    },
    {
        "jogador": "Marc-André ter Stegen",
        "ovr": 86,
        "clube": "Barcelona",
        "pos": "GK",
        "compra": 2800,
        "venda": 5200,
        "estrategia": "SBC Fodder Flip",
        "prazo": "36h",
    },
    # 87-rated higher margin
    {
        "jogador": "Teun Koopmeiners",
        "ovr": 87,
        "clube": "Juventus",
        "pos": "CM",
        "compra": 6000,
        "venda": 10500,
        "estrategia": "SBC High Tier Flip",
        "prazo": "48h",
    },
    {
        "jogador": "Leroy Sané",
        "ovr": 87,
        "clube": "Bayern Munich",
        "pos": "LW",
        "compra": 5500,
        "venda": 9500,
        "estrategia": "SBC High Tier Flip",
        "prazo": "48h",
    },
    # Thursday flip (TOTS cheap)
    {
        "jogador": "Orkun Kökçü",
        "ovr": 85,
        "clube": "Benfica",
        "pos": "CM",
        "compra": 2000,
        "venda": 3800,
        "estrategia": "Thursday Flip",
        "prazo": "48h",
    },
    {
        "jogador": "Sandro Tonali",
        "ovr": 86,
        "clube": "Newcastle Utd",
        "pos": "CM",
        "compra": 3800,
        "venda": 7000,
        "estrategia": "Thursday Flip",
        "prazo": "48h",
    },
]

def calc_margem(compra, venda):
    """Margem líquida após taxa EA de 5%."""
    return int(venda * 0.95) - compra


def format_coins(v):
    if v >= 1000:
        return f"{v:,.0f}c".replace(",", ".")
    return f"{v}c"


# ──────────────────────────────────────────────────────────────
# CONSTRUÇÃO DO DOCUMENTO
# ──────────────────────────────────────────────────────────────
def build_pdf():
    doc = SimpleDocTemplate(
        PDF_FILENAME,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=1.8 * cm,
        bottomMargin=2 * cm,
        title="Relatório Trading EA FC 26",
        author="EA FC 26 Trading Agent",
    )

    story = []

    # ── CABEÇALHO ──────────────────────────────────────────────
    story.append(header_block())
    story.append(Spacer(1, 0.4 * cm))

    # Banner de alertas ativos
    alert_data = [[
        Paragraph(
            '<font name="Helvetica-Bold" size="9" color="white">'
            '🔥 SEMANA ULTIMATE TOTS ATIVA  |  📅 Encerra: 29/05/2026  |  💰 Budget: 40.000 coins'
            '</font>',
            ParagraphStyle("alert", alignment=TA_CENTER, leading=14)
        )
    ]]
    alert_t = Table(alert_data, colWidths=[17 * cm])
    alert_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), VERDE_EA),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("ROUNDEDCORNERS", [4]),
    ]))
    story.append(alert_t)
    story.append(Spacer(1, 0.5 * cm))

    # ── 1. CONTEXTO DE MERCADO ──────────────────────────────────
    story += section_header("CONTEXTO DO MERCADO — 26/05/2026", "📊")

    story.append(Paragraph(
        "O mercado do EA FC 26 Ultimate Team encontra-se na fase mais crítica do ano: a <b>Semana "
        "Ultimate TOTS (Team of the Season)</b>, ativa de 22 a 29 de maio de 2026. Todos os "
        "melhores jogadores de cada liga das semanas anteriores foram reunidos em packs simultâneos, "
        "gerando grande oferta de cartas especiais e alta demanda por fodder de alto rating para "
        "os SBCs da temporada.",
        style_body
    ))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("<b>EVENTOS ATIVOS:</b>", style_highlight))

    eventos = [
        ("🏆", "Ultimate TOTS", "22/05 – 29/05/2026",
         "60 TOTS players em packs. SBCs End of an Era ativos (Salah 96 OVR, Griezmann 94 OVR, "
         "Bernardo Silva 93 OVR, Robertson, Goretzka, Stones). Alta demanda por fodder 85-88 rated."),
        ("🔮", "Fantasy FC", "20/02 – 29/05/2026",
         "Cartas live com upgrades vinculados a desempenhos em ligas domésticas e copas. "
         "Últimos upgrades desta semana — última chance de vender no pico."),
        ("🛣️", "UEFA RTTF", "13/02 – 30/05/2026",
         "Road to the Finals: cartas live ligadas às campanhas das equipes na UEFA. "
         "Atenção para a Final da Champions League — cartas dos finalistas podem disparar."),
        ("⬆️", "Week 5 TOTS Upgrade SBC", "Ativo agora",
         "Custo ~27.450 coins (2 squads: 85+ com TOTW/TOTS + squad 86+). "
         "Recompensa: TOTS da LaLiga, Liga F ou Liga Portugal. Repetível 3x."),
        ("🇩🇪", "Bundesliga TOTS Upgrade SBC", "Ativo agora",
         "Upgrade SBC focado em jogadores do Bundesliga TOTS. Alta procura por fodder alemão."),
    ]

    evento_rows = []
    for icon, nome, periodo, desc in eventos:
        evento_rows.append([
            Paragraph(f"<b>{icon} {nome}</b>", ParagraphStyle(
                "en", fontSize=9, fontName="Helvetica-Bold",
                textColor=CINZA_ESCURO, leading=13)),
            Paragraph(periodo, ParagraphStyle(
                "ep", fontSize=8.5, fontName="Helvetica",
                textColor=AZUL_INFO, alignment=TA_CENTER, leading=13)),
            Paragraph(desc, ParagraphStyle(
                "ed", fontSize=8.5, fontName="Helvetica",
                textColor=colors.HexColor("#333333"), leading=13)),
        ])

    evento_t = Table(
        evento_rows,
        colWidths=[4.2 * cm, 2.8 * cm, 10 * cm],
        rowHeights=None,
    )
    evento_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CINZA_CLARO),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#CCCCCC")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#DDDDDD")),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(evento_t)
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph(
        "<b>Tendência geral:</b> Mercado em alta volatilidade. Preços de fodder 85-88 rated "
        "pressionados para cima pela demanda dos SBCs End of an Era (Salah exige ~1,2M em fodder). "
        "Meta players comuns sofreram crash de -30% a -50% no início do TOTS. "
        "Janela de compra favorável para recuperação de preços após o término do evento (29/05).",
        style_body
    ))
    story.append(Spacer(1, 0.3 * cm))

    # ── 2. TABELA DE CARTAS RECOMENDADAS ──────────────────────
    story += section_header("CARTAS RECOMENDADAS — COMPRA E VENDA", "💳")

    story.append(Paragraph(
        "Tabela com jogadores específicos selecionados com base na demanda atual de SBCs, "
        "volume de transações e histórico de preços. Margens calculadas <b>após taxa de 5% da EA</b>.",
        style_body
    ))
    story.append(Spacer(1, 0.3 * cm))

    # Cabeçalho da tabela
    header_row = [
        Paragraph("<b>Jogador</b>", ParagraphStyle("th", fontSize=9, fontName="Helvetica-Bold",
                                                    textColor=BRANCO, alignment=TA_CENTER, leading=12)),
        Paragraph("<b>OVR</b>", ParagraphStyle("th2", fontSize=9, fontName="Helvetica-Bold",
                                               textColor=BRANCO, alignment=TA_CENTER, leading=12)),
        Paragraph("<b>Clube</b>", ParagraphStyle("th3", fontSize=9, fontName="Helvetica-Bold",
                                                 textColor=BRANCO, alignment=TA_CENTER, leading=12)),
        Paragraph("<b>Pos</b>", ParagraphStyle("th4", fontSize=9, fontName="Helvetica-Bold",
                                               textColor=BRANCO, alignment=TA_CENTER, leading=12)),
        Paragraph("<b>Compra (c)</b>", ParagraphStyle("th5", fontSize=9, fontName="Helvetica-Bold",
                                                       textColor=BRANCO, alignment=TA_CENTER, leading=12)),
        Paragraph("<b>Venda (c)</b>", ParagraphStyle("th6", fontSize=9, fontName="Helvetica-Bold",
                                                      textColor=BRANCO, alignment=TA_CENTER, leading=12)),
        Paragraph("<b>Margem Líq.*</b>", ParagraphStyle("th7", fontSize=9, fontName="Helvetica-Bold",
                                                         textColor=BRANCO, alignment=TA_CENTER, leading=12)),
        Paragraph("<b>Estratégia</b>", ParagraphStyle("th8", fontSize=9, fontName="Helvetica-Bold",
                                                       textColor=BRANCO, alignment=TA_CENTER, leading=12)),
    ]

    card_rows = [header_row]

    strategy_colors = {
        "SBC Fodder Flip":    colors.HexColor("#E8F5E9"),
        "SBC High Tier Flip": colors.HexColor("#FFF8E1"),
        "Thursday Flip":      colors.HexColor("#E3F2FD"),
    }

    row_bgs = []
    for rec in recomendacoes:
        margem = calc_margem(rec["compra"], rec["venda"])
        pct_ret = (margem / rec["compra"]) * 100

        st_body_cell = ParagraphStyle(
            "tc", fontSize=8.5, fontName="Helvetica",
            alignment=TA_CENTER, leading=12,
            textColor=colors.HexColor("#222222")
        )
        st_jogador = ParagraphStyle(
            "tj", fontSize=8.5, fontName="Helvetica-Bold",
            alignment=TA_LEFT, leading=12,
            textColor=CINZA_ESCURO
        )
        st_margem = ParagraphStyle(
            "tm", fontSize=8.5, fontName="Helvetica-Bold",
            alignment=TA_CENTER, leading=12,
            textColor=VERDE_ESCURO
        )
        st_ovr = ParagraphStyle(
            "to", fontSize=9, fontName="Helvetica-Bold",
            alignment=TA_CENTER, leading=12,
            textColor=CINZA_ESCURO
        )

        if rec["ovr"] >= 87:
            ovr_color_str = "#00B140"
        elif rec["ovr"] == 86:
            ovr_color_str = "#F5A623"
        else:
            ovr_color_str = "#0066CC"

        row = [
            Paragraph(rec["jogador"], st_jogador),
            Paragraph(f'<font color="{ovr_color_str}" name="Helvetica-Bold">{rec["ovr"]}</font>', st_ovr),
            Paragraph(rec["clube"], st_body_cell),
            Paragraph(rec["pos"], st_body_cell),
            Paragraph(format_coins(rec["compra"]), st_body_cell),
            Paragraph(format_coins(rec["venda"]), st_body_cell),
            Paragraph(f'+{format_coins(margem)}\n({pct_ret:.0f}%)', st_margem),
            Paragraph(rec["estrategia"], ParagraphStyle(
                "ts", fontSize=8, fontName="Helvetica-Bold",
                alignment=TA_CENTER, leading=12,
                textColor=AZUL_INFO if "Thursday" in rec["estrategia"] else VERDE_ESCURO
            )),
        ]
        card_rows.append(row)
        row_bgs.append(strategy_colors.get(rec["estrategia"], BRANCO))

    col_widths = [3.8*cm, 1.0*cm, 2.8*cm, 0.8*cm, 1.9*cm, 1.9*cm, 2.1*cm, 2.7*cm]

    card_t = Table(card_rows, colWidths=col_widths, repeatRows=1)

    ts_commands = [
        ("BACKGROUND", (0, 0), (-1, 0), CINZA_ESCURO),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#AAAAAA")),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ]

    for i, bg in enumerate(row_bgs, start=1):
        ts_commands.append(("BACKGROUND", (0, i), (-1, i), bg))

    card_t.setStyle(TableStyle(ts_commands))
    story.append(card_t)

    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "* Margem líquida = (preço de venda × 0,95) – preço de compra, por unidade. "
        "Preços estimados com base em dados de mercado de 26/05/2026.",
        style_disclaimer
    ))

    # Legenda
    legenda_data = [[
        Paragraph("🟢 SBC Fodder Flip: Compra agora (Ter/Qua) → Vende Qui/Sex",
                  ParagraphStyle("lg", fontSize=8.5, fontName="Helvetica", leading=12)),
        Paragraph("🟡 SBC High Tier Flip: Margem maior, menor volume",
                  ParagraphStyle("lg2", fontSize=8.5, fontName="Helvetica", leading=12)),
        Paragraph("🔵 Thursday Flip: Compra após rewards Qui → Vende Sex",
                  ParagraphStyle("lg3", fontSize=8.5, fontName="Helvetica", leading=12)),
    ]]
    legenda_t = Table(legenda_data, colWidths=[5.7*cm, 5.5*cm, 5.8*cm])
    legenda_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CINZA_CLARO),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(legenda_t)
    story.append(Spacer(1, 0.4 * cm))

    # ── 3. ESTRATÉGIA DE TIMING ─────────────────────────────────
    story += section_header("ESTRATÉGIA DE TIMING", "⏰")

    timing_rows = [
        [
            Paragraph("<b>Quando / Horário UTC</b>", ParagraphStyle(
                "tt1", fontSize=9, fontName="Helvetica-Bold",
                textColor=BRANCO, alignment=TA_CENTER, leading=12)),
            Paragraph("<b>Ação</b>", ParagraphStyle(
                "tt2", fontSize=9, fontName="Helvetica-Bold",
                textColor=BRANCO, alignment=TA_CENTER, leading=12)),
            Paragraph("<b>Justificativa</b>", ParagraphStyle(
                "tt3", fontSize=9, fontName="Helvetica-Bold",
                textColor=BRANCO, alignment=TA_CENTER, leading=12)),
        ],
        [
            Paragraph("Ter 26/05 — 20:00-23:59 UTC\n<b>(AGORA)</b>", ParagraphStyle(
                "ta", fontSize=8.5, fontName="Helvetica", alignment=TA_CENTER, leading=13,
                textColor=VERMELHO)),
            Paragraph("🛒 <b>COMPRAR</b> fodder 85-86 rated\n(McTominay, Gravenberch, Sommer, Bruno G.)",
                      ParagraphStyle("tb", fontSize=8.5, fontName="Helvetica-Bold", leading=13,
                                     textColor=VERDE_ESCURO)),
            Paragraph("Mercado mais vazio à noite. Menos competição. Preços próximos ao mínimo diário.",
                      ParagraphStyle("tc_", fontSize=8.5, fontName="Helvetica", leading=13)),
        ],
        [
            Paragraph("Qua 27/05 — 06:00-12:00 UTC", ParagraphStyle(
                "ta2", fontSize=8.5, fontName="Helvetica", alignment=TA_CENTER, leading=13)),
            Paragraph("🛒 Complementar posição em 87 rated\n(Koopmeiners, Sané)",
                      ParagraphStyle("tb2", fontSize=8.5, fontName="Helvetica-Bold", leading=13,
                                     textColor=VERDE_ESCURO)),
            Paragraph("Jogadores europeus acordando, mercado ainda calmo antes do pico tarde.",
                      ParagraphStyle("tc2", fontSize=8.5, fontName="Helvetica", leading=13)),
        ],
        [
            Paragraph("Qui 28/05 — 09:00-12:00 UTC\n(Rewards Division Rivals)", ParagraphStyle(
                "ta3", fontSize=8.5, fontName="Helvetica", alignment=TA_CENTER, leading=13)),
            Paragraph("🛒 Comprar TOTS baratos após flood de packs\n(Thursday Flip)",
                      ParagraphStyle("tb3", fontSize=8.5, fontName="Helvetica-Bold", leading=13,
                                     textColor=AZUL_INFO)),
            Paragraph("Rivals rewards geram enxurrada de packs → mercado floodado → preços caem temporariamente.",
                      ParagraphStyle("tc3", fontSize=8.5, fontName="Helvetica", leading=13)),
        ],
        [
            Paragraph("Qui 28/05 — 18:00-22:00 UTC\n(Pré-FUT Champs)", ParagraphStyle(
                "ta4", fontSize=8.5, fontName="Helvetica", alignment=TA_CENTER, leading=13)),
            Paragraph("💰 <b>VENDER</b> todo o fodder 85-86\nVender Thursday Flip",
                      ParagraphStyle("tb4", fontSize=8.5, fontName="Helvetica-Bold", leading=13,
                                     textColor=VERMELHO)),
            Paragraph("Jogadores comprando cartas para FUT Champs (Sex-Dom) → pico de demanda. Melhor janela de venda.",
                      ParagraphStyle("tc4", fontSize=8.5, fontName="Helvetica", leading=13)),
        ],
        [
            Paragraph("Sex 29/05 — 06:00-14:00 UTC\n(Ultimate TOTS encerra)", ParagraphStyle(
                "ta5", fontSize=8.5, fontName="Helvetica", alignment=TA_CENTER, leading=13)),
            Paragraph("💰 Vender 87 rated e posições remanescentes\n+ Observar pós-TOTS recovery",
                      ParagraphStyle("tb5", fontSize=8.5, fontName="Helvetica-Bold", leading=13,
                                     textColor=LARANJA)),
            Paragraph("Fim do TOTS reduz oferta de packs. Cartas de ouro raras tendem a recuperar valor.",
                      ParagraphStyle("tc5", fontSize=8.5, fontName="Helvetica", leading=13)),
        ],
    ]

    timing_t = Table(timing_rows, colWidths=[3.8*cm, 5.5*cm, 7.7*cm], repeatRows=1)
    timing_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CINZA_MEDIO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#AAAAAA")),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#FFF3CD")),  # quinta compra = destaque
        ("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#D4EDDA")),  # quinta venda = destaque
    ]))
    story.append(timing_t)
    story.append(Spacer(1, 0.4 * cm))

    # ── 4. ESTIMATIVA DE RETORNO ────────────────────────────────
    story += section_header("ESTIMATIVA DE RETORNO EM 48H", "📈")

    story.append(Paragraph(
        "Simulação com investimento total de <b>40.000 coins</b>, dividido entre as estratégias "
        "identificadas. Retornos calculados após taxa de 5% da EA em todas as vendas.",
        style_body
    ))
    story.append(Spacer(1, 0.2 * cm))

    ret_rows = [
        [
            Paragraph("<b>Estratégia</b>", ParagraphStyle("rh1", fontSize=9, fontName="Helvetica-Bold",
                                                           textColor=BRANCO, alignment=TA_CENTER, leading=12)),
            Paragraph("<b>Investimento</b>", ParagraphStyle("rh2", fontSize=9, fontName="Helvetica-Bold",
                                                             textColor=BRANCO, alignment=TA_CENTER, leading=12)),
            Paragraph("<b>Cenário Conservador</b>", ParagraphStyle("rh3", fontSize=9, fontName="Helvetica-Bold",
                                                                    textColor=BRANCO, alignment=TA_CENTER, leading=12)),
            Paragraph("<b>Cenário Otimista</b>", ParagraphStyle("rh4", fontSize=9, fontName="Helvetica-Bold",
                                                                 textColor=BRANCO, alignment=TA_CENTER, leading=12)),
        ],
        [
            Paragraph("SBC Fodder Flip\n(85-86 rated — 12 unidades)", ParagraphStyle(
                "rs1", fontSize=8.5, fontName="Helvetica", alignment=TA_CENTER, leading=13)),
            Paragraph("20.000c", ParagraphStyle(
                "rs2", fontSize=8.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13)),
            Paragraph("+4.800c\n(+24%)", ParagraphStyle(
                "rs3", fontSize=8.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13,
                textColor=VERDE_EA)),
            Paragraph("+8.200c\n(+41%)", ParagraphStyle(
                "rs4", fontSize=8.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13,
                textColor=VERDE_ESCURO)),
        ],
        [
            Paragraph("SBC High Tier Flip\n(87 rated — 3 unidades)", ParagraphStyle(
                "rs5", fontSize=8.5, fontName="Helvetica", alignment=TA_CENTER, leading=13)),
            Paragraph("17.000c", ParagraphStyle(
                "rs6", fontSize=8.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13)),
            Paragraph("+4.100c\n(+24%)", ParagraphStyle(
                "rs7", fontSize=8.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13,
                textColor=AMARELO_EA)),
            Paragraph("+7.500c\n(+44%)", ParagraphStyle(
                "rs8", fontSize=8.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13,
                textColor=VERDE_ESCURO)),
        ],
        [
            Paragraph("Thursday Flip\n(TOTS cheap + 86 rated)", ParagraphStyle(
                "rs9", fontSize=8.5, fontName="Helvetica", alignment=TA_CENTER, leading=13)),
            Paragraph("3.000c\n(reserva)", ParagraphStyle(
                "rs10", fontSize=8.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13)),
            Paragraph("+900c\n(+30%)", ParagraphStyle(
                "rs11", fontSize=8.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13,
                textColor=AZUL_INFO)),
            Paragraph("+2.100c\n(+70%)", ParagraphStyle(
                "rs12", fontSize=8.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13,
                textColor=VERDE_ESCURO)),
        ],
        [
            Paragraph("<b>TOTAL ESTIMADO</b>", ParagraphStyle(
                "rt1", fontSize=9.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13,
                textColor=CINZA_ESCURO)),
            Paragraph("<b>40.000c</b>", ParagraphStyle(
                "rt2", fontSize=9.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13)),
            Paragraph("<b>+9.800c\n(Capital: ~49.800c)</b>", ParagraphStyle(
                "rt3", fontSize=9.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13,
                textColor=VERDE_EA)),
            Paragraph("<b>+17.800c\n(Capital: ~57.800c)</b>", ParagraphStyle(
                "rt4", fontSize=9.5, fontName="Helvetica-Bold", alignment=TA_CENTER, leading=13,
                textColor=VERDE_ESCURO)),
        ],
    ]

    ret_t = Table(ret_rows, colWidths=[5.0*cm, 3.2*cm, 4.4*cm, 4.4*cm], repeatRows=1)
    ret_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CINZA_ESCURO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [BRANCO, CINZA_CLARO]),
        ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#C8E6C9")),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#AAAAAA")),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEBELOW", (0, -2), (-1, -2), 1.5, VERDE_ESCURO),
    ]))
    story.append(ret_t)
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph(
        "⚠️ <b>Risco:</b> Preços podem variar significativamente se a EA lançar SBCs inesperados, "
        "drops de jogadores famosos em packs, ou mudanças de preço-range. Diversifique o portfolio "
        "e não concentre todo o capital em um único jogador.",
        style_body
    ))
    story.append(Spacer(1, 0.4 * cm))

    # ── 5. 8 REGRAS DE OURO ─────────────────────────────────────
    story += section_header("8 REGRAS DE OURO DO TRADE", "🏅")

    regras = [
        ("1", "Nunca invista mais de 30% do budget em um único jogador",
         "Concentração de risco pode levar à perda total do capital investido naquele ativo."),
        ("2", "Compre na baixa, venda no pico — nunca ao contrário",
         "FOMO (Fear Of Missing Out) é o maior inimigo do trader. Não compre quando todo mundo já está vendendo."),
        ("3", "Respeite a taxa de 5% da EA em todos os cálculos",
         "Toda venda tem 5% retido. Margem real = (preço de venda × 0,95) – preço de compra."),
        ("4", "O horário importa tanto quanto o preço",
         "Terça à noite e quinta de manhã são janelas de compra. Quinta à tarde e sexta são janelas de venda."),
        ("5", "SBCs novos = oportunidade, não ameaça",
         "Cada novo SBC gera demanda por fodder específico. Quem comprou antes lucra; quem compra depois perde."),
        ("6", "Diversifique entre ligas e nações",
         "Players de ligas menos populares (Série A, Bundesliga, Liga Portugal) frequentemente têm "
         "melhor relação custo/benefício como fodder."),
        ("7", "Defina preço-alvo antes de comprar — e respeite-o",
         "Coloque a ordem de venda assim que comprar. Sem alvo definido, você segura demais ou vende cedo demais."),
        ("8", "Nunca persiga uma perda dobrando a posição",
         "Se um investimento caiu, avalie o contexto. Dobrar em ativos em queda é a forma mais rápida de quebrar o budget."),
    ]

    rules_rows = []
    for num, titulo, desc in regras:
        rules_rows.append([
            Paragraph(f"<b>#{num}</b>", ParagraphStyle(
                "rn", fontSize=14, fontName="Helvetica-Bold",
                alignment=TA_CENTER, textColor=VERDE_EA, leading=20)),
            [
                Paragraph(f"<b>{titulo}</b>", ParagraphStyle(
                    "rt_", fontSize=9.5, fontName="Helvetica-Bold",
                    textColor=CINZA_ESCURO, leading=13)),
                Paragraph(desc, ParagraphStyle(
                    "rd", fontSize=8.5, fontName="Helvetica",
                    textColor=colors.HexColor("#555555"), leading=12)),
            ],
        ])

    rules_t = Table(rules_rows, colWidths=[1.3*cm, 15.7*cm])
    rules_ts = [
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#EEEEEE")),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEAFTER", (0, 0), (0, -1), 2, VERDE_EA),
    ]
    rules_t.setStyle(TableStyle(rules_ts))
    story.append(rules_t)
    story.append(Spacer(1, 0.5 * cm))

    # ── DISCLAIMER ───────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#AAAAAA")))
    story.append(Spacer(1, 0.2 * cm))

    disclaimer_box = [[
        Paragraph(
            "⚠️  <b>DISCLAIMER</b>  —  Este relatório é produzido exclusivamente para fins "
            "informativos e educacionais sobre estratégias de trading no EA FC 26 Ultimate Team. "
            "As análises, preços e recomendações são estimativas baseadas em dados de mercado "
            "publicamente disponíveis em sites como FUTBIN, FUT.GG e FutWiz e podem não refletir "
            "os valores exatos do mercado no momento da leitura. O mercado do FUT é altamente "
            "volátil e sujeito a mudanças abruptas causadas por novos SBCs, promos ou decisões "
            "da EA. Nenhuma operação de trading é garantida. O autor não se responsabiliza por "
            "perdas de coins decorrentes do uso deste material. Comprar ou vender coins via "
            "terceiros viola os Termos de Serviço da EA e pode resultar em ban permanente da conta.",
            style_disclaimer
        )
    ]]
    disc_t = Table(disclaimer_box, colWidths=[17*cm])
    disc_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFF9C4")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#F0C000")),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
    ]))
    story.append(disc_t)
    story.append(Spacer(1, 0.3 * cm))

    # Footer
    story.append(Paragraph(
        f"Relatório gerado em {REPORT_DATE_DISPLAY} UTC  •  EA FC 26 Ultimate Team Trading Report  •  "
        "Repositório: github.com/kaiohsferreira/fifa-trading",
        style_footer_text
    ))

    # ── BUILD ────────────────────────────────────────────────────
    doc.build(story)
    print(f"✅ PDF gerado: {PDF_FILENAME}")


if __name__ == "__main__":
    build_pdf()
