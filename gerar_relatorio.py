#!/usr/bin/env python3
"""Gerador de relatório de trading EA FC 26 Ultimate Team."""

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
import os

FILENAME = "relatorio-trading-2026-05-28-14h.pdf"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), FILENAME)

# ── Paleta de cores ──────────────────────────────────────────────────────────
VERDE_EA    = colors.HexColor("#00C853")
VERDE_DARK  = colors.HexColor("#007E33")
PRETO       = colors.HexColor("#0D0D0D")
CINZA_BG    = colors.HexColor("#1A1A2E")
CINZA_LINHA = colors.HexColor("#16213E")
BRANCO      = colors.white
AMARELO     = colors.HexColor("#FFD600")
LARANJA     = colors.HexColor("#FF6D00")
VERMELHO    = colors.HexColor("#DD2C00")
AZUL_CLARO  = colors.HexColor("#82B1FF")

PAGE_W, PAGE_H = A4


def build_styles():
    base = getSampleStyleSheet()
    styles = {}

    styles["title"] = ParagraphStyle(
        "title",
        fontName="Helvetica-Bold",
        fontSize=26,
        textColor=VERDE_EA,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    styles["subtitle"] = ParagraphStyle(
        "subtitle",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=AMARELO,
        alignment=TA_CENTER,
        spaceAfter=2,
    )
    styles["datetime"] = ParagraphStyle(
        "datetime",
        fontName="Helvetica",
        fontSize=10,
        textColor=AZUL_CLARO,
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    styles["section"] = ParagraphStyle(
        "section",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=VERDE_EA,
        spaceBefore=14,
        spaceAfter=6,
        borderPadding=(0, 0, 3, 0),
    )
    styles["body"] = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=BRANCO,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
    )
    styles["bullet"] = ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=BRANCO,
        leading=14,
        leftIndent=12,
        spaceAfter=2,
        bulletIndent=4,
    )
    styles["rule_num"] = ParagraphStyle(
        "rule_num",
        fontName="Helvetica-Bold",
        fontSize=10,
        textColor=AMARELO,
        leading=14,
        spaceAfter=1,
    )
    styles["rule_text"] = ParagraphStyle(
        "rule_text",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=BRANCO,
        leading=13,
        leftIndent=16,
        spaceAfter=6,
    )
    styles["disclaimer"] = ParagraphStyle(
        "disclaimer",
        fontName="Helvetica-Oblique",
        fontSize=7.5,
        textColor=colors.HexColor("#888888"),
        leading=11,
        alignment=TA_JUSTIFY,
        spaceAfter=2,
    )
    styles["tag_green"] = ParagraphStyle(
        "tag_green",
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=VERDE_DARK,
        alignment=TA_CENTER,
    )
    styles["tag_red"] = ParagraphStyle(
        "tag_red",
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=VERMELHO,
        alignment=TA_CENTER,
    )
    return styles


def header_footer(canvas, doc):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(CINZA_BG)
    canvas.rect(0, PAGE_H - 30, PAGE_W, 30, fill=1, stroke=0)
    canvas.setFillColor(VERDE_EA)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 19,
                             "EA FC 26 ULTIMATE TEAM — RELATÓRIO DE TRADING DIÁRIO")
    # Footer bar
    canvas.setFillColor(CINZA_BG)
    canvas.rect(0, 0, PAGE_W, 22, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(2 * cm, 8,
                      "Gerado por Market Analyst Bot | Apenas para uso educacional")
    canvas.drawRightString(PAGE_W - 2 * cm, 8, f"Página {doc.page}")
    canvas.restoreState()


def make_table_header():
    return [
        "Jogador", "Rat.", "Clube / Liga", "Posição",
        "Compra\n(coins)", "Venda\n(coins)", "Margem\nLíquida", "Horizon."
    ]


def make_cards_data():
    """
    Dados de mercado baseados em pesquisa de 28/05/2026.
    Margem líquida = venda * 0.95 - compra (após taxa EA de 5%).
    """
    cards = [
        # (Jogador, Rat, Clube/Liga, Pos, Compra, Venda, Horizonte)
        ("Modric",         83, "LA Galaxy / MLS",    "CM",  750,   1_400,  "48h"),
        ("Mkhitaryan",     83, "Inter / Serie A",    "CAM", 750,   1_350,  "48h"),
        ("Brandt",         83, "Dortmund / Bundesl.","CAM", 750,   1_350,  "48h"),
        ("Lukaku",         84, "Roma / Serie A",     "ST",  750,   1_600,  "48h"),
        ("Grimaldo",       84, "Leverkusen / Bund.", "LB",  750,   1_550,  "48h"),
        ("Pickford",       84, "Everton / PL",       "GK",  750,   1_500,  "48h"),
        ("Thuram M.",      85, "Inter / Serie A",    "ST",  1_500, 2_800,  "48h"),
        ("Mbeumo",         85, "Brentford / PL",     "RW",  1_500, 2_600,  "24h"),
        ("Dybala",         86, "Roma / Serie A",     "CAM", 6_500, 10_500, "48h"),
        ("Ona Battle",     86, "Barcelona / NWSL",   "RW",  6_500, 10_000, "48h"),
        ("Jonathan Tah",   87, "Bayern / Bundesl.",  "CB",  10_000,15_500, "48h"),
        ("Jan Oblak",      88, "Atletico / LaLiga",  "GK",  13_000,19_500, "48h"),
        ("B. Saka (base)", 88, "Arsenal / PL",       "RM",  14_000,20_000, "Thu"),
        ("Lewandowski",    88, "Barcelona / LaLiga", "ST",  13_500,19_000, "48h"),
    ]

    rows = []
    for jogador, rat, clube, pos, compra, venda, horiz in cards:
        margem_liq = int(venda * 0.95 - compra)
        margem_pct = round((margem_liq / compra) * 100, 1)
        rows.append([
            jogador, str(rat), clube, pos,
            f"{compra:,}".replace(",", "."),
            f"{venda:,}".replace(",", "."),
            f"+{margem_liq:,}\n({margem_pct}%)".replace(",", "."),
            horiz
        ])
    return rows


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=2.2 * cm,
        bottomMargin=1.8 * cm,
    )

    S = build_styles()
    story = []

    # ── CAPA / CABEÇALHO ────────────────────────────────────────────────────
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph("⚽ RELATÓRIO DE TRADING", S["title"]))
    story.append(Paragraph("EA FC 26 Ultimate Team — Análise de Mercado", S["subtitle"]))
    story.append(Paragraph("28/05/2026  14:08 UTC", S["datetime"]))
    story.append(HRFlowable(width="100%", thickness=2, color=VERDE_EA, spaceAfter=10))

    # ── CONTEXTO DE MERCADO ─────────────────────────────────────────────────
    story.append(Paragraph("📊 CONTEXTO DO MERCADO", S["section"]))

    ctx_data = [
        ["EVENTO ATIVO",   "Ultimate TOTS — Semana Final  (22/05 – 29/05/2026)"],
        ["STATUS",         "Último dia de Ultimate TOTS — conteúdo expira amanhã"],
        ["PRÓXIMO EVENTO", "Festival of Football / Path to Glory  (05/06/2026)"],
        ["SBCs ATIVOS",    "End of an Era (Salah 96, Bernardo Silva 93, Stones 91)\n"
                           "UCL Final Showdown (Ben White 90, Lee Kang In 90)"],
        ["UCL FINAL",      "Arsenal × PSG — 30/05/2026 (Budapest) — RTTF upgrades"],
        ["TENDÊNCIA",      "Mercado em queda por abertura massiva de packs TOTS\n"
                           "→ JANELA IDEAL DE COMPRA para fodder e meta cards"],
    ]
    ctx_table = Table(ctx_data, colWidths=[3.8 * cm, 12.8 * cm])
    ctx_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (0, -1), CINZA_LINHA),
        ("BACKGROUND",   (1, 0), (1, -1), colors.HexColor("#0F0F1E")),
        ("TEXTCOLOR",    (0, 0), (0, -1), VERDE_EA),
        ("TEXTCOLOR",    (1, 0), (1, -1), BRANCO),
        ("FONTNAME",     (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME",     (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE",     (0, 0), (-1, -1), 8.5),
        ("LEADING",      (0, 0), (-1, -1), 13),
        ("ROWBACKGROUNDS",(0, 0), (-1, -1),
         [colors.HexColor("#0F0F1E"), colors.HexColor("#131325")]),
        ("GRID",         (0, 0), (-1, -1), 0.4, colors.HexColor("#333355")),
        ("VALIGN",       (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("LEFTPADDING",  (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.append(ctx_table)
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph(
        "O mercado de EA FC 26 está em plena queda pós-TOTS. A abertura massiva de packs durante "
        "a semana do Ultimate TOTS gerou excesso de oferta de cartas gold 83-88, derrubando preços "
        "30-60% abaixo da média histórica. Essa janela de compra é temporária: com o fim do TOTS "
        "em 29/05 e o início do Festival of Football em 05/06, a demanda por SBC fodder voltará "
        "a subir rapidamente, especialmente cartas 84-87 para os novos SBCs do Path to Glory. "
        "Além disso, a Final da UCL (Arsenal × PSG, 30/05) pode gerar spikes em RTTF cards.",
        S["body"]
    ))

    # ── TABELA DE CARTAS ────────────────────────────────────────────────────
    story.append(Paragraph("🃏 CARTAS RECOMENDADAS (Budget: 40.000 coins)", S["section"]))
    story.append(Paragraph(
        "Preços baseados em pesquisa de mercado de 28/05/2026. "
        "Margem líquida já descontada a taxa EA de 5% sobre o preço de venda. "
        "Compre em lotes nas próximas 6-12h enquanto o mercado está deprimido.",
        S["body"]
    ))

    header = make_table_header()
    rows   = make_cards_data()
    table_data = [header] + rows

    col_w = [3.5, 1.2, 3.8, 1.6, 2.0, 2.0, 2.2, 1.5]
    col_w = [w * cm for w in col_w]

    tbl = Table(table_data, colWidths=col_w, repeatRows=1)

    # Estilos base
    tbl_style = [
        # Cabeçalho
        ("BACKGROUND",    (0, 0), (-1, 0),  VERDE_DARK),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0),  8),
        ("ALIGN",         (0, 0), (-1, 0),  "CENTER"),
        ("VALIGN",        (0, 0), (-1, 0),  "MIDDLE"),
        # Corpo
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 8),
        ("ALIGN",         (0, 1), (0, -1),  "LEFT"),
        ("ALIGN",         (1, 1), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 1), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1),
         [colors.HexColor("#0A0A1A"), colors.HexColor("#111122")]),
        ("TEXTCOLOR",     (0, 1), (1, -1),  BRANCO),
        ("TEXTCOLOR",     (2, 1), (3, -1),  colors.HexColor("#AAAACC")),
        ("TEXTCOLOR",     (4, 1), (4, -1),  AZUL_CLARO),
        ("TEXTCOLOR",     (5, 1), (5, -1),  AMARELO),
        ("TEXTCOLOR",     (6, 1), (6, -1),  VERDE_EA),
        ("TEXTCOLOR",     (7, 1), (7, -1),  LARANJA),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#2A2A4A")),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]
    # Highlight melhores oportunidades (87-88 rated)
    for i, row in enumerate(rows, start=1):
        if row[1] in ("87", "88"):
            tbl_style.append(("BACKGROUND", (0, i), (-1, i),
                               colors.HexColor("#0D1F0D")))
    tbl.setStyle(TableStyle(tbl_style))
    story.append(tbl)
    story.append(Spacer(1, 0.2 * cm))

    # Legenda
    legenda_data = [
        [Paragraph("● Branco = 83-86 rated (fodder rápido)", S["body"]),
         Paragraph("● Verde escuro = 87-88 rated (maior margem, 2-3 dias)", S["body"])],
    ]
    leg_tbl = Table(legenda_data, colWidths=[8.5 * cm, 8.5 * cm])
    leg_tbl.setStyle(TableStyle([
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#AAAAAA")),
        ("FONTSIZE",  (0, 0), (-1, -1), 8),
        ("TOPPADDING",(0, 0), (-1, -1), 0),
    ]))
    story.append(leg_tbl)

    # ── ESTRATÉGIA DE TIMING ─────────────────────────────────────────────────
    story.append(Paragraph("⏱ ESTRATÉGIA DE TIMING", S["section"]))

    timing = [
        ["QUANDO",        "AÇÃO",                          "MOTIVO"],
        ["Agora\n(14h UTC)",
         "COMPRAR fodder 83-85 em lote\n(gaste 8-12k coins)",
         "Mercado no fundo pós-TOTS"],
        ["Hoje 18h-22h UTC",
         "COMPRAR 1-2x Dybala 86 e Tah 87",
         "Antes do drop de quinta-feira"],
        ["29/05 — 18h BST\n(Thursday drop)",
         "VENDER 70% do fodder 83-85\nListar Dybala e Tah",
         "Pico de demanda pós-conteúdo novo"],
        ["30/05 — UCL Final",
         "OBSERVAR Arsenal RTTF cards\nVender se Arsenal vencer",
         "Ben White, Saka RTTF spike esperado"],
        ["31/05 – 02/06",
         "Vender remainder e realociar\npara cartas Path to Glory",
         "Preparar novo ciclo Festival"],
    ]
    timing_tbl = Table(timing, colWidths=[3.5 * cm, 6.0 * cm, 7.3 * cm])
    timing_tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  VERDE_DARK),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  BRANCO),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  8.5),
        ("ALIGN",        (0, 0), (-1, 0),  "CENTER"),
        ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",     (0, 1), (-1, -1), 8.5),
        ("TEXTCOLOR",    (0, 1), (0, -1),  AMARELO),
        ("TEXTCOLOR",    (1, 1), (1, -1),  VERDE_EA),
        ("TEXTCOLOR",    (2, 1), (2, -1),  colors.HexColor("#CCCCCC")),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1),
         [colors.HexColor("#0A0A1A"), colors.HexColor("#111122")]),
        ("GRID",         (0, 0), (-1, -1), 0.4, colors.HexColor("#2A2A4A")),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",        (0, 1), (0, -1),  "CENTER"),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("LEFTPADDING",  (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(timing_tbl)
    story.append(Spacer(1, 0.3 * cm))

    # ── ESTIMATIVA DE RETORNO ────────────────────────────────────────────────
    story.append(Paragraph("💰 ESTIMATIVA DE RETORNO EM 48H", S["section"]))

    ret_data = [
        ["CENÁRIO", "ESTRATÉGIA", "INVESTIMENTO", "RETORNO BRUTO", "LUCRO LÍQUIDO", "ROI"],
        ["Conservador",
         "Fodder 83-84 apenas\n(30-40 cartas)",
         "9.000 coins",
         "14.000 coins",
         "+4.700 coins",
         "52%"],
        ["Moderado",
         "Fodder 83-85 + Dybala 86\n(1 cópia)",
         "20.000 coins",
         "32.000 coins",
         "+10.500 coins",
         "53%"],
        ["Otimista",
         "Fodder 83-87 + Oblak 88\n+ Lewandowski 88",
         "38.000 coins",
         "61.000 coins",
         "+19.000 coins",
         "50%"],
    ]
    ret_tbl = Table(ret_data, colWidths=[2.4, 4.5, 2.8, 2.8, 2.8, 1.5])
    ret_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  VERDE_DARK),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0),  8),
        ("ALIGN",         (0, 0), (-1, 0),  "CENTER"),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 8.5),
        ("ALIGN",         (0, 1), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        # Linha conservador
        ("BACKGROUND",    (0, 1), (-1, 1),  colors.HexColor("#0A1A0A")),
        ("TEXTCOLOR",     (0, 1), (-1, 1),  colors.HexColor("#BBDDBB")),
        # Linha moderado
        ("BACKGROUND",    (0, 2), (-1, 2),  colors.HexColor("#0D1A0A")),
        ("TEXTCOLOR",     (0, 2), (-1, 2),  VERDE_EA),
        # Linha otimista
        ("BACKGROUND",    (0, 3), (-1, 3),  colors.HexColor("#1A1200")),
        ("TEXTCOLOR",     (0, 3), (-1, 3),  AMARELO),
        ("FONTNAME",      (0, 3), (-1, 3),  "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#2A2A4A")),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    # Ajusta colWidths para cm
    ret_tbl._argW = [w * cm for w in [2.4, 4.5, 2.8, 2.8, 2.8, 1.5]]
    story.append(ret_tbl)
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph(
        "<b>Nota:</b> Cenário otimista pressupõe spike do Thursday drop em 29/05 e "
        "valorização dos meta cards pós-Final UCL. Cenário conservador assume sell "
        "gradual sem evento catalisador adicional. Valores líquidos já descontam "
        "taxa EA de 5% aplicada sobre cada transação de venda.",
        S["body"]
    ))

    # ── 8 REGRAS DE OURO ────────────────────────────────────────────────────
    story.append(Paragraph("🏆 8 REGRAS DE OURO DO TRADE", S["section"]))

    rules = [
        ("1", "Nunca invista mais de 60% do budget em um único ativo.",
         "Diversificação protege contra quedas inesperadas (novo promo, patch de preços, bug EA)."),
        ("2", "Compre na queda, venda no pico de demanda SBC.",
         "O melhor momento de compra é DURANTE o promo/TOTS. O melhor de venda é nas primeiras "
         "3h após novo SBC/drop de quinta."),
        ("3", "Monitore futbin.com a cada 2-3 horas.",
         "Preços de fodder mudam rapidamente. Um spike de 1.500 → 2.500 em 2h é comum."),
        ("4", "Sempre liste a 150-200 coins abaixo do mínimo atual.",
         "Garante venda rápida e evita que cards fiquem presos no mercado por 24h+."),
        ("5", "Nunca venda na sexta-feira à tarde.",
         "Sexta é momento de conteúdo novo + abertura de packs. Mercado fica instável. "
         "Prefira vender quinta à noite ou domingo."),
        ("6", "Respeite a taxa EA de 5%.",
         "Todo cálculo de lucro deve subtrair os 5% antes. Muitos traders perdem por ignorar "
         "essa taxa em trades de alto volume."),
        ("7", "Tenha sempre 20-30% do budget em coins líquidos.",
         "Para aproveitar oportunidades inesperadas (SBC urgente, player dropa 40% sem motivo)."),
        ("8", "Jamais persiga losses — se o mercado virou, saia.",
         "Se um investimento caiu 25%+ e não há catalisador de alta, realize o prejuízo "
         "e realoque. Coins líquidos valem mais que cards depreciando."),
    ]

    for num, titulo, desc in rules:
        story.append(Paragraph(f"REGRA #{num} — {titulo}", S["rule_num"]))
        story.append(Paragraph(desc, S["rule_text"]))

    # ── DISCLAIMER ───────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1,
                             color=colors.HexColor("#333333"), spaceBefore=10, spaceAfter=6))
    story.append(Paragraph("⚠ DISCLAIMER", S["section"]))
    story.append(Paragraph(
        "Este relatório é produzido exclusivamente para fins educacionais e informativos sobre o "
        "mercado virtual do jogo EA FC 26 Ultimate Team. As previsões de preço e retorno são "
        "baseadas em dados históricos de mercado e tendências observadas; NÃO constituem garantia "
        "de lucro. O mercado do EA FC Ultimate Team é altamente volátil e pode ser afetado por "
        "patches, mudanças de preço range, novos eventos, bugs e decisões da Electronic Arts sem "
        "aviso prévio. Opere com responsabilidade e nunca arrisque mais coins do que pode perder. "
        "Este documento não tem afiliação com Electronic Arts Inc.",
        S["disclaimer"]
    ))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"PDF gerado: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
