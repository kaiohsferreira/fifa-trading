#!/usr/bin/env python3
"""Gera relatório de trading EA FC 26 Ultimate Team em PDF."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak
import os

REPORT_DATE = "06/06/2026"
REPORT_TIME = "14:04"
FILENAME = "relatorio-trading-2026-06-06-14h.pdf"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), FILENAME)

# ─── Cores ────────────────────────────────────────────────────────────────────
VERDE_EA    = colors.HexColor("#00B140")
VERDE_ESCURO= colors.HexColor("#007A2E")
AMARELO_EA  = colors.HexColor("#FFD700")
AZUL_ESCURO = colors.HexColor("#0D1B2A")
CINZA_CLARO = colors.HexColor("#F5F5F5")
CINZA_MEDIO = colors.HexColor("#CCCCCC")
BRANCO      = colors.white
PRETO       = colors.black
VERMELHO    = colors.HexColor("#C0392B")
LARANJA     = colors.HexColor("#E67E22")

def build_styles():
    base = getSampleStyleSheet()
    styles = {}

    styles["title"] = ParagraphStyle(
        "title", parent=base["Title"],
        fontSize=22, textColor=BRANCO, alignment=TA_CENTER,
        spaceAfter=4, fontName="Helvetica-Bold"
    )
    styles["subtitle"] = ParagraphStyle(
        "subtitle", parent=base["Normal"],
        fontSize=13, textColor=AMARELO_EA, alignment=TA_CENTER,
        spaceAfter=2, fontName="Helvetica-Bold"
    )
    styles["datetime"] = ParagraphStyle(
        "datetime", parent=base["Normal"],
        fontSize=10, textColor=CINZA_CLARO, alignment=TA_CENTER,
        spaceAfter=0, fontName="Helvetica"
    )
    styles["section"] = ParagraphStyle(
        "section", parent=base["Normal"],
        fontSize=13, textColor=BRANCO, alignment=TA_LEFT,
        spaceBefore=14, spaceAfter=6, fontName="Helvetica-Bold",
        backColor=VERDE_ESCURO, leftIndent=-10, rightIndent=-10,
        borderPadding=(4, 8, 4, 8)
    )
    styles["body"] = ParagraphStyle(
        "body", parent=base["Normal"],
        fontSize=9.5, textColor=PRETO, alignment=TA_JUSTIFY,
        spaceAfter=5, fontName="Helvetica", leading=14
    )
    styles["bullet"] = ParagraphStyle(
        "bullet", parent=base["Normal"],
        fontSize=9.5, textColor=PRETO, alignment=TA_LEFT,
        spaceAfter=3, leftIndent=14, fontName="Helvetica", leading=13
    )
    styles["highlight"] = ParagraphStyle(
        "highlight", parent=base["Normal"],
        fontSize=9.5, textColor=AZUL_ESCURO, alignment=TA_LEFT,
        spaceAfter=3, fontName="Helvetica-Bold", leading=13
    )
    styles["regra_num"] = ParagraphStyle(
        "regra_num", parent=base["Normal"],
        fontSize=12, textColor=VERDE_EA, alignment=TA_CENTER,
        fontName="Helvetica-Bold"
    )
    styles["regra_txt"] = ParagraphStyle(
        "regra_txt", parent=base["Normal"],
        fontSize=9.5, textColor=PRETO, alignment=TA_LEFT,
        fontName="Helvetica", leading=13
    )
    styles["disclaimer"] = ParagraphStyle(
        "disclaimer", parent=base["Normal"],
        fontSize=7.5, textColor=colors.HexColor("#666666"),
        alignment=TA_JUSTIFY, fontName="Helvetica-Oblique", leading=11
    )
    styles["small_bold"] = ParagraphStyle(
        "small_bold", parent=base["Normal"],
        fontSize=9, textColor=AZUL_ESCURO, alignment=TA_CENTER,
        fontName="Helvetica-Bold"
    )
    return styles


def header_block(styles):
    """Bloco de cabeçalho com fundo escuro."""
    header_data = [[
        Paragraph("⚽  EA FC 26 ULTIMATE TEAM", styles["title"]),
    ], [
        Paragraph("RELATÓRIO DIÁRIO DE TRADING", styles["subtitle"]),
    ], [
        Paragraph(
            f"Data: {REPORT_DATE}  |  Hora: {REPORT_TIME} UTC  |  Budget: 40.000 coins",
            styles["datetime"]
        ),
    ]]
    tbl = Table(header_data, colWidths=[17.5 * cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return tbl


def section_header(text, styles):
    bg_data = [[Paragraph(f"  {text}", styles["section"])]]
    tbl = Table(bg_data, colWidths=[17.5 * cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), VERDE_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ]))
    return tbl


def cards_table(styles):
    """Tabela principal de cartas recomendadas."""
    headers = [
        Paragraph("<b>Jogador</b>", styles["small_bold"]),
        Paragraph("<b>OVR</b>", styles["small_bold"]),
        Paragraph("<b>Clube</b>", styles["small_bold"]),
        Paragraph("<b>Compra\n(coins)</b>", styles["small_bold"]),
        Paragraph("<b>Venda\n(coins)</b>", styles["small_bold"]),
        Paragraph("<b>Margem\nLíq. -5%</b>", styles["small_bold"]),
        Paragraph("<b>Estratégia</b>", styles["small_bold"]),
    ]

    def p(txt, bold=False, color=PRETO):
        s = ParagraphStyle("td", fontName="Helvetica-Bold" if bold else "Helvetica",
                           fontSize=8.5, textColor=color, leading=12, alignment=TA_CENTER)
        return Paragraph(txt, s)

    def pl(txt):
        s = ParagraphStyle("tdl", fontName="Helvetica", fontSize=8, textColor=PRETO,
                           leading=11, alignment=TA_LEFT)
        return Paragraph(txt, s)

    rows = [
        # ── SBC Fodder 83-84 ──────────────────────────────────────────────────
        [
            p("Giovanni Di Lorenzo", bold=True),
            p("83"),
            p("Napoli"),
            p("800"),
            p("1.500"),
            p("+615", bold=True, color=VERDE_ESCURO),
            pl("Fodder SBC 83+\nThursday Flip"),
        ],
        [
            p("Nathan Aké", bold=True),
            p("83"),
            p("Man. City"),
            p("800"),
            p("1.500"),
            p("+615", bold=True, color=VERDE_ESCURO),
            pl("Fodder SBC 83+\nDemanda Freq."),
        ],
        [
            p("Mateo Kovačić", bold=True),
            p("83"),
            p("Man. City"),
            p("850"),
            p("1.600"),
            p("+670", bold=True, color=VERDE_ESCURO),
            pl("Fodder SBC 83+\nLink Premier"),
        ],
        [
            p("Iago Aspas", bold=True),
            p("83"),
            p("Celta Vigo"),
            p("750"),
            p("1.400"),
            p("+580", bold=True, color=VERDE_ESCURO),
            pl("Fodder SBC 83+\nSnipe Price Floor"),
        ],
        # ── SBC Fodder 84-85 ──────────────────────────────────────────────────
        [
            p("Diogo Costa", bold=True),
            p("84"),
            p("FC Porto"),
            p("900"),
            p("1.800"),
            p("+810", bold=True, color=VERDE_ESCURO),
            pl("Fodder SBC 84+\nToken Swap Demand"),
        ],
        [
            p("Rúben Neves", bold=True),
            p("84"),
            p("Al-Hilal"),
            p("950"),
            p("1.900"),
            p("+855", bold=True, color=VERDE_ESCURO),
            pl("Fodder SBC 84+\nThursday Flip"),
        ],
        [
            p("Granit Xhaka", bold=True),
            p("85"),
            p("B. Leverkusen"),
            p("1.100"),
            p("2.200"),
            p("+990", bold=True, color=VERDE_ESCURO),
            pl("Token Swap 85 OVR\nAlta liquidez"),
        ],
        [
            p("Joao Felix", bold=True),
            p("85"),
            p("Chelsea"),
            p("1.200"),
            p("2.400"),
            p("+1.080", bold=True, color=VERDE_ESCURO),
            pl("Token Swap 85 OVR\nLink PL/LaLiga"),
        ],
        # ── Path to Glory Invest. ──────────────────────────────────────────────
        [
            p("Frenkie de Jong", bold=True),
            p("92"),
            p("FC Barcelona"),
            p("30.000"),
            p("55.000"),
            p("+22.250", bold=True, color=AMARELO_EA),
            pl("PtG: Holanda avança\nComprar em 48h"),
        ],
        [
            p("Ronald Araújo", bold=True),
            p("91"),
            p("FC Barcelona"),
            p("18.000"),
            p("35.000"),
            p("+15.250", bold=True, color=AMARELO_EA),
            pl("PtG: Uruguai avança\nRisco médio"),
        ],
        # ── RTTF Oportunidade ─────────────────────────────────────────────────
        [
            p("Bukayo Saka", bold=True),
            p("93"),
            p("Arsenal"),
            p("38.000"),
            p("68.000"),
            p("+26.600", bold=True, color=LARANJA),
            pl("PtG+RTTF: Inglaterra\nHold p/ QF/SF"),
        ],
    ]

    col_w = [3.5*cm, 1.2*cm, 2.6*cm, 2.0*cm, 2.0*cm, 2.2*cm, 4.0*cm]
    data = [headers] + rows
    tbl = Table(data, colWidths=col_w, repeatRows=1)

    style = TableStyle([
        # Cabeçalho
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 9),
        ("ALIGN",         (0, 0), (-1, 0), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        # Zebra
        *[("BACKGROUND", (0, i), (-1, i), CINZA_CLARO) for i in range(2, len(data), 2)],
        # Bordas
        ("GRID",     (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, VERDE_EA),
        # Separadores de grupo
        ("LINEABOVE", (0, 5), (-1, 5), 1, VERDE_EA),
        ("LINEABOVE", (0, 7), (-1, 7), 1, VERDE_EA),
        ("LINEABOVE", (0, 9), (-1, 9), 1, AMARELO_EA),
        ("LINEABOVE", (0, 11), (-1, 11), 1, LARANJA),
        # Arredondamento de OVR
        ("FONTNAME",  (1, 1), (1, -1), "Helvetica-Bold"),
        ("TEXTCOLOR", (1, 1), (1, -1), AZUL_ESCURO),
    ])
    tbl.setStyle(style)
    return tbl


def retorno_table(styles):
    """Tabela de estimativa de retorno em 48h."""
    def p(t, bold=False, c=PRETO):
        s = ParagraphStyle("r", fontName="Helvetica-Bold" if bold else "Helvetica",
                           fontSize=9, textColor=c, leading=12, alignment=TA_CENTER)
        return Paragraph(t, s)

    headers = [p("Estratégia", bold=True), p("Capital\nInvestido", bold=True),
               p("Retorno\nConservador", bold=True), p("Retorno\nOtimista", bold=True),
               p("ROI\nConservador", bold=True), p("ROI\nOtimista", bold=True)]

    rows = [
        [p("Fodder Flip 83-84"), p("12.000"), p("16.800"), p("21.600"),
         p("+40%", c=VERDE_ESCURO), p("+80%", c=VERDE_EA)],
        [p("Fodder Flip 85"), p("10.000"), p("14.500"), p("20.000"),
         p("+45%", c=VERDE_ESCURO), p("+100%", c=VERDE_EA)],
        [p("Path to Glory"), p("18.000"), p("23.000"), p("38.000"),
         p("+28%", c=VERDE_ESCURO), p("+111%", c=AMARELO_EA)],
        [p("TOTAL", bold=True), p("40.000", bold=True),
         p("54.300", bold=True, c=VERDE_ESCURO), p("79.600", bold=True, c=VERDE_EA),
         p("+36%", bold=True, c=VERDE_ESCURO), p("+99%", bold=True, c=VERDE_EA)],
    ]

    col_w = [4.2*cm, 2.8*cm, 3.2*cm, 3.2*cm, 2.2*cm, 2.2*cm]
    data = [headers] + rows
    tbl = Table(data, colWidths=col_w)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("BACKGROUND",    (0, 4), (-1, 4), colors.HexColor("#E8F5E9")),
        ("FONTNAME",      (0, 4), (-1, 4), "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
        ("LINEBELOW",     (0, 0), (-1, 0), 1.5, VERDE_EA),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        *[("BACKGROUND", (0, i), (-1, i), CINZA_CLARO) for i in range(2, 4, 2)],
    ]))
    return tbl


def regras_table(styles):
    """Tabela das 8 regras de ouro."""
    regras = [
        ("1", "NUNCA compre no pico de hype.",
         "Aguarde 24-48h após lançamento de promo para o mercado estabilizar."),
        ("2", "Respeite a taxa de 5% da EA.",
         "Calcule sempre: Preço de Venda × 0,95 = Receita real. Margem mínima: 15%."),
        ("3", "Quinta-feira é dia de compra.",
         "Recompensas de Rivals inundam o mercado → preços caem → oportunidade de snipe."),
        ("4", "Diversifique o portfólio.",
         "Não coloque mais de 40% do budget em uma única carta ou estratégia."),
        ("5", "Fodder 83-85 é dinheiro seguro.",
         "SBCs são sempre ativos. Compre quando o mercado está saturado, venda antes do fim."),
        ("6", "Path to Glory: siga os resultados.",
         "Compre jogadores de seleções que estão vencendo, venda antes das quartas de final."),
        ("7", "Monitore o mercado em horários de pico.",
         "18h–22h (horário de Brasília) = mais vendedores e compradores → mais lucro."),
        ("8", "Tenha disciplina de saída.",
         "Defina preço-alvo ANTES de comprar. Venda no alvo, não seja ganancioso."),
    ]

    def pn(t):
        return Paragraph(t, ParagraphStyle("rn", fontName="Helvetica-Bold", fontSize=14,
                                            textColor=VERDE_EA, alignment=TA_CENTER))
    def pt(t):
        return Paragraph(f"<b>{t}</b>", ParagraphStyle("rt", fontName="Helvetica-Bold",
                                                         fontSize=9.5, textColor=AZUL_ESCURO))
    def pd(t):
        return Paragraph(t, ParagraphStyle("rd", fontName="Helvetica", fontSize=8.5,
                                           textColor=PRETO, leading=12))

    data = [[pn(r[0]), pt(r[1]), pd(r[2])] for r in regras]
    col_w = [1.2*cm, 5.5*cm, 10.8*cm]
    tbl = Table(data, colWidths=col_w)
    tbl.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("LINEBELOW",     (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
        *[("BACKGROUND", (0, i), (-1, i), CINZA_CLARO) for i in range(1, 8, 2)],
    ]))
    return tbl


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=1.5*cm, rightMargin=1.5*cm,
        topMargin=1.5*cm, bottomMargin=1.5*cm,
        title="Relatório Trading EA FC 26",
        author="EA FC 26 Trading Agent",
    )

    styles = build_styles()
    story = []

    # ── Cabeçalho ────────────────────────────────────────────────────────────
    story.append(header_block(styles))
    story.append(Spacer(1, 0.4*cm))

    # ── 1. Contexto de Mercado ────────────────────────────────────────────────
    story.append(section_header("1. CONTEXTO DO MERCADO — 06/06/2026", styles))
    story.append(Spacer(1, 0.2*cm))

    contexto_data = [
        [
            Paragraph("<b>🏆 Evento Ativo</b>", ParagraphStyle("ch", fontName="Helvetica-Bold",
                       fontSize=10, textColor=AZUL_ESCURO)),
            Paragraph("<b>📈 Tendência Geral</b>", ParagraphStyle("ch", fontName="Helvetica-Bold",
                       fontSize=10, textColor=AZUL_ESCURO)),
        ],
        [
            Paragraph(
                "<b>Festival of Football — Copa do Mundo 2026</b><br/>"
                "5 Jun – 24 Jul 2026<br/><br/>"
                "• <b>Path to Glory</b> (5–19 Jun): Cartas live que sobem de OVR "
                "conforme a seleção avança na Copa do Mundo. Lançado ontem — mercado "
                "ainda volátil.<br/>"
                "• <b>Greats of the Game</b> (19–26 Jun): Novos ICONs — Mario Kempes "
                "e Rivellino debutam no game.<br/>"
                "• <b>Glory Hunters</b> (26 Jun – 10 Jul): PlayStyle Promo.<br/>"
                "• <b>Pelé 93 OVR</b>: Grátis (untradeable) para quem logar até 24 Jul.",
                styles["body"]
            ),
            Paragraph(
                "• Mercado em <b>queda moderada</b>: packs do festival aumentaram "
                "oferta de jogadores 83-88 OVR.<br/><br/>"
                "• <b>Hoje é sábado</b>: demanda de Weekend League alta — bom momento "
                "para VENDER fodder acumulado.<br/><br/>"
                "• <b>SBC 83+ Summer Tournament</b> ativo até 12 Jun (ilimitado): "
                "gera demanda constante por cartas 83+.<br/><br/>"
                "• <b>Token Swap 85 OVR</b>: exige 8 jogadores 85-rated — forte "
                "pressão de demanda nessa faixa.",
                styles["body"]
            ),
        ]
    ]
    tbl_ctx = Table(contexto_data, colWidths=[8.5*cm, 9.0*cm])
    tbl_ctx.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), colors.HexColor("#E8F5E9")),
        ("BACKGROUND",    (0, 1), (0, 1), CINZA_CLARO),
        ("BACKGROUND",    (1, 1), (1, 1), BRANCO),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("BOX",           (0, 0), (-1, -1), 1, VERDE_EA),
        ("INNERGRID",     (0, 0), (-1, -1), 0.5, CINZA_MEDIO),
    ]))
    story.append(tbl_ctx)
    story.append(Spacer(1, 0.3*cm))

    # ── 2. Cartas Recomendadas ────────────────────────────────────────────────
    story.append(section_header("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA", styles))
    story.append(Spacer(1, 0.15*cm))

    legend_data = [[
        Paragraph("🟢 Fodder 83-84", ParagraphStyle("lg", fontName="Helvetica-Bold",
                   fontSize=8, textColor=VERDE_ESCURO, alignment=TA_CENTER)),
        Paragraph("🟢 Fodder 85", ParagraphStyle("lg", fontName="Helvetica-Bold",
                   fontSize=8, textColor=VERDE_ESCURO, alignment=TA_CENTER)),
        Paragraph("🟡 Path to Glory", ParagraphStyle("lg", fontName="Helvetica-Bold",
                   fontSize=8, textColor=colors.HexColor("#B8860B"), alignment=TA_CENTER)),
        Paragraph("🟠 PtG + Alto Risco", ParagraphStyle("lg", fontName="Helvetica-Bold",
                   fontSize=8, textColor=LARANJA, alignment=TA_CENTER)),
    ]]
    tbl_leg = Table(legend_data, colWidths=[4.375*cm]*4)
    tbl_leg.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, CINZA_MEDIO),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, CINZA_MEDIO),
        ("BACKGROUND", (0, 0), (1, 0), colors.HexColor("#E8F5E9")),
        ("BACKGROUND", (2, 0), (2, 0), colors.HexColor("#FFFDE7")),
        ("BACKGROUND", (3, 0), (3, 0), colors.HexColor("#FFF3E0")),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(tbl_leg)
    story.append(Spacer(1, 0.15*cm))
    story.append(cards_table(styles))
    story.append(Spacer(1, 0.2*cm))

    nota = Paragraph(
        "<b>Nota:</b> Margem Líq. = (Preço Venda × 0,95) − Preço Compra. "
        "Preços são estimativas baseadas em dados de mercado de 06/06/2026. "
        "Path to Glory: comprar APENAS se a seleção do jogador vencer Grupos.",
        styles["disclaimer"]
    )
    story.append(nota)
    story.append(Spacer(1, 0.3*cm))

    # ── 3. Estratégia de Timing ───────────────────────────────────────────────
    story.append(section_header("3. ESTRATÉGIA DE TIMING", styles))
    story.append(Spacer(1, 0.2*cm))

    timing_data = [
        [
            Paragraph("<b>HOJE — Sáb 06/06 (Agora)</b>",
                      ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9.5,
                                     textColor=BRANCO, alignment=TA_CENTER)),
            Paragraph("<b>Dom–Ter 07–09/06</b>",
                      ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9.5,
                                     textColor=BRANCO, alignment=TA_CENTER)),
            Paragraph("<b>Qui 11/06 (Rivals Day)</b>",
                      ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9.5,
                                     textColor=BRANCO, alignment=TA_CENTER)),
            Paragraph("<b>Sex-Dom 12–14/06</b>",
                      ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9.5,
                                     textColor=BRANCO, alignment=TA_CENTER)),
        ],
        [
            Paragraph(
                "• <b>VENDER</b> fodder acumulado\n"
                "• <b>SEGURAR</b> coins para comprar\n"
                "• Monitorar resultados Copa\n"
                "• SBC 83+ ainda ativo → demanda",
                styles["body"]
            ),
            Paragraph(
                "• <b>COMPRAR</b> fodder 83-84\n"
                "  se preço cair abaixo de 900\n"
                "• Avaliar PtG por resultados\n"
                "• SBC 83+ expira dia 12 →\n"
                "  demanda pode aumentar",
                styles["body"]
            ),
            Paragraph(
                "• <b>COMPRAR AGRESSIVO</b>\n"
                "  fodder 83-85 (queda típica)\n"
                "• Pico de oferta do dia\n"
                "• Monitorar 18h–22h BRT\n"
                "• Snipe abaixo do price floor",
                styles["body"]
            ),
            Paragraph(
                "• <b>VENDER</b> todo o fodder\n"
                "• WL final → alta demanda\n"
                "• Novos SBCs podem surgir\n"
                "• Realizar lucros antes\n"
                "  do próximo reset",
                styles["body"]
            ),
        ]
    ]
    tbl_timing = Table(timing_data, colWidths=[4.375*cm]*4)
    tbl_timing.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_ESCURO),
        ("BACKGROUND",    (0, 1), (0, 1), colors.HexColor("#E8F5E9")),
        ("BACKGROUND",    (1, 1), (1, 1), CINZA_CLARO),
        ("BACKGROUND",    (2, 1), (2, 1), colors.HexColor("#E3F2FD")),
        ("BACKGROUND",    (3, 1), (3, 1), colors.HexColor("#E8F5E9")),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("BOX",           (0, 0), (-1, -1), 1, VERDE_EA),
        ("INNERGRID",     (0, 0), (-1, -1), 0.5, CINZA_MEDIO),
        ("LINEBELOW",     (0, 0), (-1, 0), 1.5, VERDE_EA),
    ]))
    story.append(tbl_timing)
    story.append(Spacer(1, 0.3*cm))

    # ── 4. Estimativa de Retorno 48h ──────────────────────────────────────────
    story.append(section_header("4. ESTIMATIVA DE RETORNO EM 48H", styles))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Distribuição sugerida do budget de <b>40.000 coins</b>:",
        styles["body"]
    ))
    story.append(Paragraph(
        "• <b>12.000 coins</b> → Fodder SBC 83-84 (≈ 14 cartas × 850 coins médio)",
        styles["bullet"]
    ))
    story.append(Paragraph(
        "• <b>10.000 coins</b> → Fodder SBC 85 (≈ 9 cartas × 1.100 coins médio)",
        styles["bullet"]
    ))
    story.append(Paragraph(
        "• <b>18.000 coins</b> → Path to Glory (1-2 cartas de seleções favoritas)",
        styles["bullet"]
    ))
    story.append(Spacer(1, 0.2*cm))
    story.append(retorno_table(styles))
    story.append(Spacer(1, 0.15*cm))
    story.append(Paragraph(
        "<b>⚠️ Cenário Conservador:</b> Venda moderada, sem valorização Path to Glory, "
        "mercado estável. <b>Cenário Otimista:</b> SBCs ativos + seleções PtG avançam "
        "na Copa + Weekend League aumenta demanda.",
        styles["body"]
    ))
    story.append(Spacer(1, 0.3*cm))

    # ── 5. Regras de Ouro ─────────────────────────────────────────────────────
    story.append(section_header("5. 8 REGRAS DE OURO DO TRADE", styles))
    story.append(Spacer(1, 0.2*cm))
    story.append(regras_table(styles))
    story.append(Spacer(1, 0.35*cm))

    # ── 6. Disclaimer ─────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1, color=CINZA_MEDIO))
    story.append(Spacer(1, 0.15*cm))
    story.append(Paragraph(
        "<b>DISCLAIMER:</b> Este relatório é gerado por um agente de análise automatizado "
        "com base em dados públicos de mercado (FUTBIN, FUT.GG, Sportskeeda, Dexerto, "
        "Team Gullit, Reddit) coletados em 06/06/2026 às 14:04 UTC. "
        "Os preços são estimativas e podem variar significativamente. "
        "Trading em EA FC 26 Ultimate Team envolve risco de perda de coins. "
        "Nenhuma estratégia garante lucro. Use as informações como referência e sempre "
        "verifique os preços em tempo real no mercado de transferências antes de comprar. "
        "Este documento não possui afiliação com a Electronic Arts Inc.",
        styles["disclaimer"]
    ))

    doc.build(story)
    print(f"PDF gerado: {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    build_pdf()
