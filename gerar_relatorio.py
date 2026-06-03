#!/usr/bin/env python3
"""Gerador de relatório de trading EA FC 26 Ultimate Team."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import KeepTogether
import datetime
import os

# ─── Configuração ────────────────────────────────────────────────────────────
DATA_HORA_UTC = "2026-06-03 14:07"
DATA_HORA_DISPLAY = "03/06/2026 14:07"
NOME_ARQUIVO = "relatorio-trading-2026-06-03-14h.pdf"
CAMINHO_PDF = os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)

# ─── Cores ───────────────────────────────────────────────────────────────────
VERDE_ESCURO  = colors.HexColor("#1a6b1a")
VERDE_MEDIO   = colors.HexColor("#28a745")
VERDE_CLARO   = colors.HexColor("#d4edda")
AMARELO       = colors.HexColor("#ffc107")
AMARELO_CLARO = colors.HexColor("#fff3cd")
CINZA_ESCURO  = colors.HexColor("#343a40")
CINZA_CLARO   = colors.HexColor("#f8f9fa")
CINZA_LINHA   = colors.HexColor("#dee2e6")
VERMELHO      = colors.HexColor("#dc3545")
VERMELHO_CLARO= colors.HexColor("#f8d7da")
BRANCO        = colors.white
AZUL_ESCURO   = colors.HexColor("#1a3c5e")
AZUL_CLARO    = colors.HexColor("#cfe2f3")
LARANJA       = colors.HexColor("#fd7e14")


def build_styles():
    base = getSampleStyleSheet()

    styles = {
        "title": ParagraphStyle(
            "Title",
            fontName="Helvetica-Bold",
            fontSize=22,
            textColor=BRANCO,
            alignment=TA_CENTER,
            leading=28,
            spaceBefore=6,
            spaceAfter=4,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            fontName="Helvetica",
            fontSize=12,
            textColor=BRANCO,
            alignment=TA_CENTER,
            leading=16,
        ),
        "section": ParagraphStyle(
            "Section",
            fontName="Helvetica-Bold",
            fontSize=13,
            textColor=BRANCO,
            alignment=TA_LEFT,
            leading=18,
            spaceBefore=4,
            spaceAfter=2,
            leftIndent=6,
        ),
        "body": ParagraphStyle(
            "Body",
            fontName="Helvetica",
            fontSize=10,
            textColor=CINZA_ESCURO,
            leading=15,
            spaceAfter=4,
            alignment=TA_JUSTIFY,
        ),
        "body_bold": ParagraphStyle(
            "BodyBold",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=CINZA_ESCURO,
            leading=15,
            spaceAfter=4,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            fontName="Helvetica",
            fontSize=10,
            textColor=CINZA_ESCURO,
            leading=15,
            leftIndent=14,
            spaceAfter=3,
        ),
        "highlight": ParagraphStyle(
            "Highlight",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=VERDE_ESCURO,
            leading=15,
            spaceAfter=3,
        ),
        "warning": ParagraphStyle(
            "Warning",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=VERMELHO,
            leading=13,
            spaceAfter=3,
        ),
        "disclaimer": ParagraphStyle(
            "Disclaimer",
            fontName="Helvetica-Oblique",
            fontSize=8,
            textColor=colors.HexColor("#6c757d"),
            leading=12,
            alignment=TA_JUSTIFY,
        ),
        "table_header": ParagraphStyle(
            "TableHeader",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=BRANCO,
            alignment=TA_CENTER,
            leading=12,
        ),
        "table_cell": ParagraphStyle(
            "TableCell",
            fontName="Helvetica",
            fontSize=9,
            textColor=CINZA_ESCURO,
            alignment=TA_CENTER,
            leading=12,
        ),
        "table_cell_left": ParagraphStyle(
            "TableCellLeft",
            fontName="Helvetica",
            fontSize=9,
            textColor=CINZA_ESCURO,
            alignment=TA_LEFT,
            leading=12,
        ),
        "green_cell": ParagraphStyle(
            "GreenCell",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=VERDE_ESCURO,
            alignment=TA_CENTER,
            leading=12,
        ),
    }
    return styles


def section_header(text, styles, bg_color=VERDE_ESCURO):
    """Cria um bloco de cabeçalho de seção com fundo colorido."""
    data = [[Paragraph(text, styles["section"])]]
    tbl = Table(data, colWidths=[17.5 * cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg_color),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("ROUNDEDCORNERS", [4, 4, 4, 4]),
    ]))
    return tbl


def build_pdf():
    doc = SimpleDocTemplate(
        CAMINHO_PDF,
        pagesize=A4,
        rightMargin=1.8 * cm,
        leftMargin=1.8 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
    )
    styles = build_styles()
    story = []

    # ── CABEÇALHO ────────────────────────────────────────────────────────────
    header_data = [[
        Paragraph("EA FC 26 — RELATÓRIO DE TRADING", styles["title"]),
    ], [
        Paragraph(f"Ultimate Team | Data: {DATA_HORA_DISPLAY} UTC", styles["subtitle"]),
    ], [
        Paragraph("Festival of Football · Path to Glory · Fodder Flipping", styles["subtitle"]),
    ]]
    header_tbl = Table(header_data, colWidths=[17.5 * cm])
    header_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AZUL_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, 0), 16),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 14),
        ("TOPPADDING",    (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
    ]))
    story.append(header_tbl)
    story.append(Spacer(1, 0.4 * cm))

    # ── CONTEXTO DO MERCADO ───────────────────────────────────────────────────
    story.append(section_header("1. CONTEXTO DO MERCADO (03/06/2026)", styles))
    story.append(Spacer(1, 0.2 * cm))

    context_data = [
        [
            Paragraph("<b>Evento Ativo</b>", styles["body_bold"]),
            Paragraph("<b>Status</b>", styles["body_bold"]),
            Paragraph("<b>Impacto no Mercado</b>", styles["body_bold"]),
        ],
        [
            Paragraph("Festival of Football", styles["table_cell_left"]),
            Paragraph("ATIVO (5 Jun – 24 Jul)", styles["green_cell"]),
            Paragraph("Evento guarda-chuva da Copa do Mundo 2026", styles["table_cell_left"]),
        ],
        [
            Paragraph("Path to Glory", styles["table_cell_left"]),
            Paragraph("COMEÇA EM 2 DIAS (5 Jun)", styles["warning"]),
            Paragraph("Maior promo do momento — SBCs vão estocar fodder", styles["table_cell_left"]),
        ],
        [
            Paragraph("Answer the Call", styles["table_cell_left"]),
            Paragraph("Ativo (possíveis upgrades)", styles["table_cell_left"]),
            Paragraph("Cartas com +1 OVR se nação for convocada para WC", styles["table_cell_left"]),
        ],
        [
            Paragraph("10x 84+ Upgrade SBC", styles["table_cell_left"]),
            Paragraph("Expira 12 Jun", styles["warning"]),
            Paragraph("Consome 84+ fodder — demanda alta", styles["table_cell_left"]),
        ],
        [
            Paragraph("83+ Player Pick SBC", styles["table_cell_left"]),
            Paragraph("Expira 8 Jun", styles["warning"]),
            Paragraph("Consome 83+ fodder — últimos dias", styles["table_cell_left"]),
        ],
    ]
    ctx_tbl = Table(context_data, colWidths=[4.5 * cm, 4 * cm, 9 * cm])
    ctx_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), CINZA_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("GRID",          (0, 0), (-1, -1), 0.5, CINZA_LINHA),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(ctx_tbl)
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph(
        "JANELA CRÍTICA: O Path to Glory entra em <b>5 de junho (quinta-feira, 18h BST)</b>. "
        "Estamos a <b>2 dias do lançamento</b>. Quando a promo cair, novos SBCs vão drenar "
        "o mercado de fodder 83-86 rated. AGORA é o momento ideal de acumular antes da spike.",
        styles["highlight"]
    ))
    story.append(Spacer(1, 0.3 * cm))

    # ── CARTAS RECOMENDADAS ───────────────────────────────────────────────────
    story.append(section_header("2. CARTAS RECOMENDADAS — TABELA DE OPORTUNIDADES", styles))
    story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph(
        "Margem líquida calculada após taxa de 5% da EA (multiplique preço venda × 0,95).",
        styles["body"]
    ))
    story.append(Spacer(1, 0.15 * cm))

    # Cabeçalho da tabela
    th = styles["table_header"]
    tc = styles["table_cell"]
    tl = styles["table_cell_left"]
    gc = styles["green_cell"]

    table_headers = [
        Paragraph("Jogador", th),
        Paragraph("OVR", th),
        Paragraph("Clube / Liga", th),
        Paragraph("Compra\n(coins)", th),
        Paragraph("Venda\n(coins)", th),
        Paragraph("Margem\nLíquida", th),
        Paragraph("Estratégia", th),
    ]

    # Dados de cartas — SBC Fodder (83-86)
    cards = [
        # (nome, ovr, clube/liga, compra, venda, margem_liq, estrategia)
        ("Sergej Milinković-Savić", "84", "Al Hilal / Arábia", "1.300", "1.800", "+360", "Fodder PTG SBC"),
        ("Cody Gakpo", "84", "Liverpool / PL", "1.400", "2.000", "+500", "Fodder 84+ Upgrade"),
        ("Ollie Watkins", "84", "Aston Villa / PL", "1.350", "1.900", "+455", "Fodder PTG SBC"),
        ("Jordan Pickford", "84", "Everton / PL", "1.250", "1.750", "+413", "Fodder 84+ Upgrade"),
        ("Manuel Neuer", "84", "Bayern München / BL1", "1.300", "1.850", "+458", "Fodder SBC múltiplos"),
        ("Scott McTominay", "85", "Napoli / Serie A", "1.600", "2.400", "+680", "Fodder top-tier SBC"),
        ("Dani Carvajal", "85", "Real Madrid / LaLiga", "1.700", "2.600", "+770", "Alta demanda PL/LaLiga"),
        ("Patrik Schick", "85", "Bayer Leverkusen / BL1", "1.550", "2.300", "+635", "Fodder SBC PTG"),
        ("Trent Alexander-Arnold", "86", "Real Madrid / LaLiga", "2.200", "3.500", "+1.125", "Spike pós-PTG"),
        ("Ruben Dias", "86", "Man. City / PL", "2.100", "3.300", "+1.035", "Fodder high-tier SBC"),
        # Cartas Answer the Call / Path to Glory (investimento)
        ("Bukayo Saka PTG", "91", "Arsenal / PL", "28.000", "45.000", "+14.750", "Inglaterra avança WC → spike"),
        ("Vini Jr. PTG", "93", "Real Madrid / LaLiga", "35.000", "58.000", "+20.100", "Brasil favorito → hold"),
    ]

    def margem_color(m):
        val = int(m.replace("+", "").replace(".", ""))
        if val >= 10000:
            return colors.HexColor("#155724")
        elif val >= 700:
            return VERDE_ESCURO
        else:
            return VERDE_MEDIO

    table_rows = [table_headers]
    for i, (nome, ovr, clube, compra, venda, margem, estrategia) in enumerate(cards):
        bg = BRANCO if i % 2 == 0 else CINZA_CLARO
        row = [
            Paragraph(nome, tl),
            Paragraph(ovr, tc),
            Paragraph(clube, tl),
            Paragraph(compra, tc),
            Paragraph(venda, tc),
            Paragraph(f"<b>{margem}</b>", ParagraphStyle(
                "MG", fontName="Helvetica-Bold", fontSize=9,
                textColor=margem_color(margem), alignment=TA_CENTER, leading=12
            )),
            Paragraph(estrategia, tl),
        ]
        table_rows.append(row)

    col_widths = [4.2 * cm, 1 * cm, 3.5 * cm, 1.8 * cm, 1.8 * cm, 1.8 * cm, 3.4 * cm]
    cards_tbl = Table(table_rows, colWidths=col_widths, repeatRows=1)
    cards_tbl.setStyle(TableStyle([
        # Cabeçalho
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        # Linhas alternadas
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        # Separador SBC/Investimento
        ("BACKGROUND",    (0, 11), (-1, 12), AZUL_CLARO),
        # Grade
        ("GRID",          (0, 0), (-1, -1), 0.5, CINZA_LINHA),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("FONTSIZE",      (0, 1), (-1, -1), 9),
    ]))
    story.append(cards_tbl)
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "* Linhas em azul = cartas de investimento Path to Glory / Answer the Call (hold 48h+).",
        styles["disclaimer"]
    ))
    story.append(Spacer(1, 0.35 * cm))

    # ── ALOCAÇÃO DO BUDGET ────────────────────────────────────────────────────
    story.append(section_header("3. ALOCAÇÃO DO BUDGET — 40.000 COINS", styles, bg_color=AZUL_ESCURO))
    story.append(Spacer(1, 0.2 * cm))

    budget_data = [
        [Paragraph("Estratégia", styles["table_header"]),
         Paragraph("Alocação", styles["table_header"]),
         Paragraph("Coins", styles["table_header"]),
         Paragraph("Objetivo", styles["table_header"])],
        [Paragraph("Fodder 83-85 (flip rápido)", tc),
         Paragraph("40%", tc),
         Paragraph("16.000", tc),
         Paragraph("Vender antes/depois PTG – retorno 30-50%", tl)],
        [Paragraph("Fodder 85-86 (mid-tier)", tc),
         Paragraph("25%", tc),
         Paragraph("10.000", tc),
         Paragraph("SBCs de Icon/high-tier – retorno 40-60%", tl)],
        [Paragraph("PTG / Answer the Call invest.", tc),
         Paragraph("25%", tc),
         Paragraph("10.000", tc),
         Paragraph("Saka ou Milinkovic PTG se preço baixar", tl)],
        [Paragraph("Reserva líquida (snipe)", tc),
         Paragraph("10%", tc),
         Paragraph("4.000", tc),
         Paragraph("Oportunidades de snipe no transfer market", tl)],
    ]
    budget_tbl = Table(budget_data, colWidths=[4.5 * cm, 2.5 * cm, 2.5 * cm, 8 * cm])
    budget_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("GRID",          (0, 0), (-1, -1), 0.5, CINZA_LINHA),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(budget_tbl)
    story.append(Spacer(1, 0.35 * cm))

    # ── TIMING ────────────────────────────────────────────────────────────────
    story.append(section_header("4. ESTRATÉGIA DE TIMING", styles, bg_color=LARANJA))
    story.append(Spacer(1, 0.2 * cm))

    timing_data = [
        [Paragraph("Momento", styles["table_header"]),
         Paragraph("Horário (UTC)", styles["table_header"]),
         Paragraph("Ação Recomendada", styles["table_header"]),
         Paragraph("Motivo", styles["table_header"])],
        [Paragraph("AGORA — Qua 03/06", tc),
         Paragraph("14h–22h UTC", tc),
         Paragraph("COMPRAR fodder 83-85", ParagraphStyle("CG", fontName="Helvetica-Bold", fontSize=9,
                   textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=12)),
         Paragraph("Pré-PTG: preços ainda baixos, SBCs ainda não criaram demanda", tl)],
        [Paragraph("Qui 04/06 (amanhã)", tc),
         Paragraph("14h–18h UTC", tc),
         Paragraph("Acumular mais fodder + posição em PTG invest.", tc),
         Paragraph("Últimas horas antes do lançamento do Path to Glory", tl)],
        [Paragraph("Qui 05/06 — PTG DROP", tc),
         Paragraph("18h BST (17h UTC)", tc),
         Paragraph("VENDER 50% do estoque de fodder", ParagraphStyle("WN", fontName="Helvetica-Bold", fontSize=9,
                   textColor=AMARELO, alignment=TA_CENTER, leading=12)),
         Paragraph("Spike máximo 2-4h após lançamento. Realizar lucro parcial", tl)],
        [Paragraph("Sex 06/06–Dom 07/06", tc),
         Paragraph("Fim de semana", tc),
         Paragraph("Segurar cartas PTG de nações fortes", tc),
         Paragraph("Brasil, Alemanha, Inglaterra — jogos de abertura da Copa", tl)],
        [Paragraph("Seg 08/06", tc),
         Paragraph("Após 17h UTC", tc),
         Paragraph("VENDER restante do estoque", ParagraphStyle("WN", fontName="Helvetica-Bold", fontSize=9,
                   textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=12)),
         Paragraph("83+ Player Pick SBC expira — última chance de lucro alto", tl)],
        [Paragraph("Qui 11/06 — Copa Começa", tc),
         Paragraph("12h UTC", tc),
         Paragraph("Decidir hold/sell nas cartas PTG", tc),
         Paragraph("Cartas de nações que avançarem vão valorizar com upgrades", tl)],
    ]
    timing_tbl = Table(timing_data, colWidths=[3.5 * cm, 2.8 * cm, 4.8 * cm, 6.4 * cm])
    timing_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), CINZA_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("BACKGROUND",    (0, 3), (-1, 3), AMARELO_CLARO),  # PTG DROP destaque
        ("GRID",          (0, 0), (-1, -1), 0.5, CINZA_LINHA),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(timing_tbl)
    story.append(Spacer(1, 0.35 * cm))

    # ── ESTIMATIVA DE RETORNO ─────────────────────────────────────────────────
    story.append(section_header("5. ESTIMATIVA DE RETORNO EM 48H", styles, bg_color=VERDE_ESCURO))
    story.append(Spacer(1, 0.2 * cm))

    ret_data = [
        [Paragraph("Estratégia", styles["table_header"]),
         Paragraph("Capital Investido", styles["table_header"]),
         Paragraph("Cenário Conservador", styles["table_header"]),
         Paragraph("Cenário Otimista", styles["table_header"]),
         Paragraph("Lucro Estimado (opt.)", styles["table_header"])],
        [Paragraph("Fodder 83-85 (flip)", tc),
         Paragraph("16.000", tc),
         Paragraph("+20%  →  19.200", ParagraphStyle("SC", fontName="Helvetica", fontSize=9,
                   textColor=VERDE_MEDIO, alignment=TA_CENTER, leading=12)),
         Paragraph("+45%  →  23.200", ParagraphStyle("OC", fontName="Helvetica-Bold", fontSize=9,
                   textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=12)),
         Paragraph("+7.200 coins", gc)],
        [Paragraph("Fodder 85-86 (mid)", tc),
         Paragraph("10.000", tc),
         Paragraph("+25%  →  12.500", ParagraphStyle("SC", fontName="Helvetica", fontSize=9,
                   textColor=VERDE_MEDIO, alignment=TA_CENTER, leading=12)),
         Paragraph("+55%  →  15.500", ParagraphStyle("OC", fontName="Helvetica-Bold", fontSize=9,
                   textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=12)),
         Paragraph("+5.500 coins", gc)],
        [Paragraph("PTG / AtC Invest.", tc),
         Paragraph("10.000", tc),
         Paragraph("+15%  →  11.500", ParagraphStyle("SC", fontName="Helvetica", fontSize=9,
                   textColor=VERDE_MEDIO, alignment=TA_CENTER, leading=12)),
         Paragraph("+60%  →  16.000", ParagraphStyle("OC", fontName="Helvetica-Bold", fontSize=9,
                   textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=12)),
         Paragraph("+6.000 coins", gc)],
        [Paragraph("Reserva — snipe oport.", tc),
         Paragraph("4.000", tc),
         Paragraph("+10%  →  4.400", ParagraphStyle("SC", fontName="Helvetica", fontSize=9,
                   textColor=VERDE_MEDIO, alignment=TA_CENTER, leading=12)),
         Paragraph("+30%  →  5.200", ParagraphStyle("OC", fontName="Helvetica-Bold", fontSize=9,
                   textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=12)),
         Paragraph("+1.200 coins", gc)],
        [Paragraph("TOTAL", ParagraphStyle("TH", fontName="Helvetica-Bold", fontSize=10,
                   textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=12)),
         Paragraph("40.000", ParagraphStyle("TH", fontName="Helvetica-Bold", fontSize=10,
                   textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=12)),
         Paragraph("~47.600 coins", ParagraphStyle("TH", fontName="Helvetica-Bold", fontSize=10,
                   textColor=VERDE_MEDIO, alignment=TA_CENTER, leading=12)),
         Paragraph("~59.900 coins", ParagraphStyle("TH", fontName="Helvetica-Bold", fontSize=10,
                   textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=12)),
         Paragraph("+19.900 coins", ParagraphStyle("TH", fontName="Helvetica-Bold", fontSize=10,
                   textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=12))],
    ]
    ret_tbl = Table(ret_data, colWidths=[3.8 * cm, 3 * cm, 3.5 * cm, 3.5 * cm, 3.7 * cm])
    ret_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("ROWBACKGROUNDS",(0, 1), (-1, -2), [BRANCO, CINZA_CLARO]),
        ("BACKGROUND",    (0, -1), (-1, -1), VERDE_CLARO),
        ("FONTNAME",      (0, -1), (-1, -1), "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.5, CINZA_LINHA),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(ret_tbl)
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "Cenário conservador: spike moderado de fodder pós-PTG. | "
        "Cenário otimista: PTG gera SBCs caros que drenam mercado de fodder + "
        "nações fortes avançam na Copa, valorizando cartas de investimento.",
        styles["disclaimer"]
    ))
    story.append(Spacer(1, 0.35 * cm))

    # ── 8 REGRAS DE OURO ─────────────────────────────────────────────────────
    story.append(section_header("6. AS 8 REGRAS DE OURO DO TRADE", styles, bg_color=CINZA_ESCURO))
    story.append(Spacer(1, 0.2 * cm))

    regras = [
        ("1", "NUNCA compre no pico.", "Espere a spike passar antes de entrar. Compre na queda, venda na subida."),
        ("2", "Mantenha sempre 10-20% líquido.", "Oportunidades de snipe aparecem a qualquer hora. Liquidez é poder."),
        ("3", "Não segure por mais de 72h sem motivo.", "Mercado muda rápido. Se o plano mudou, saia e preserve o capital."),
        ("4", "Conheça o ciclo semanal.", "Quarta = preços baixos (venda de squads). Quinta = preços altos (rewards DivRivals)."),
        ("5", "SBCs são seus melhores amigos.", "Toda SBC grande cria demanda de fodder. Antecipe, compre antes, venda durante."),
        ("6", "Diversifique entre estratégias.", "Nunca coloque >50% em uma única aposta. Balance fodder + investimento + snipe."),
        ("7", "Calcule sempre a taxa de 5%.", "Preço de venda × 0,95 = o que você recebe. Margem real importa mais que bruta."),
        ("8", "Eventos ao vivo = volatilidade.", "Copa do Mundo, jogos decisivos, resultados surpresa movem o mercado em minutos."),
    ]

    regras_data = [
        [Paragraph("#", styles["table_header"]),
         Paragraph("Regra", styles["table_header"]),
         Paragraph("Explicação", styles["table_header"])],
    ]
    for num, titulo, explicacao in regras:
        regras_data.append([
            Paragraph(num, ParagraphStyle("RN", fontName="Helvetica-Bold", fontSize=12,
                      textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=16)),
            Paragraph(titulo, ParagraphStyle("RT", fontName="Helvetica-Bold", fontSize=9,
                      textColor=CINZA_ESCURO, alignment=TA_LEFT, leading=13)),
            Paragraph(explicacao, styles["table_cell_left"]),
        ])

    regras_tbl = Table(regras_data, colWidths=[1 * cm, 4.5 * cm, 12 * cm])
    regras_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), CINZA_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("GRID",          (0, 0), (-1, -1), 0.5, CINZA_LINHA),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",         (0, 0), (0, -1), "CENTER"),
    ]))
    story.append(regras_tbl)
    story.append(Spacer(1, 0.35 * cm))

    # ── RESUMO EXECUTIVO ──────────────────────────────────────────────────────
    story.append(section_header("7. RESUMO EXECUTIVO — PRÓXIMAS AÇÕES", styles, bg_color=VERDE_MEDIO))
    story.append(Spacer(1, 0.2 * cm))

    acoes = [
        "HOJE (14h-22h UTC): Comprar 10-12 cartas 84-rated (Gakpo, Milinkovic, Watkins, Neuer) "
        "entre 1.300-1.500 coins cada. Custo total: ~16.000 coins.",
        "HOJE: Comprar 4-5 cartas 85-86 rated (McTominay, Carvajal, TAA) entre 1.700-2.200 coins. "
        "Custo: ~10.000 coins.",
        "QUINTA 05/06 (antes das 17h UTC): Listar 50% do estoque de fodder 84 a 1.900-2.200 coins. "
        "Aproveitar spike do lançamento do Path to Glory.",
        "QUINTA 05/06 (após launch): Analisar SBCs do PTG — se fodder spike >50%, vender tudo imediatamente.",
        "SEG 08/06: Última oportunidade do 83+ Player Pick SBC. Vender restante do estoque.",
        "HOLD: Saka PTG e Vini Jr. PTG se você conseguir entrada abaixo de 30.000 e 38.000 coins "
        "respectivamente. Segurar até Copa começa (11 Jun).",
    ]
    for a in acoes:
        story.append(Paragraph(f"• {a}", styles["bullet"]))
    story.append(Spacer(1, 0.35 * cm))

    # ── DISCLAIMER ───────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1, color=CINZA_LINHA))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph(
        "DISCLAIMER: Este relatório é gerado automaticamente para fins educativos e de apoio a decisões "
        "de trading no EA FC 26 Ultimate Team. Preços de cartas são altamente voláteis e dependem de "
        "fatores como lançamentos de SBCs, promos ativas, horários de recompensas e comportamento da "
        "comunidade. Não existe garantia de lucro. Opere sempre dentro do seu budget disponível e nunca "
        "invista coins que não pode perder. Este relatório não é afiliado à EA Sports.",
        styles["disclaimer"]
    ))

    doc.build(story)
    print(f"PDF gerado: {CAMINHO_PDF}")


if __name__ == "__main__":
    build_pdf()
