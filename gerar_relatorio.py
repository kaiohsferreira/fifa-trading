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
import os

# ── Paleta de cores ──────────────────────────────────────────────────────────
VERDE_ESCURO  = colors.HexColor("#0D3B1C")
VERDE_MEDIO   = colors.HexColor("#1A5C2E")
VERDE_CLARO   = colors.HexColor("#27AE60")
VERDE_NEON    = colors.HexColor("#39D353")
AMARELO       = colors.HexColor("#F1C40F")
LARANJA       = colors.HexColor("#E67E22")
VERMELHO      = colors.HexColor("#E74C3C")
BRANCO        = colors.white
CINZA_CLARO   = colors.HexColor("#F0F4F0")
CINZA_MEDIO   = colors.HexColor("#BDC3C7")
CINZA_ESCURO  = colors.HexColor("#2C3E50")

PDF_NAME = "relatorio-trading-2026-05-31-20h.pdf"
OUTPUT   = os.path.join(os.path.dirname(__file__), PDF_NAME)

DATE_STR = "31/05/2026 20:06"  # UTC


def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles["title_main"] = ParagraphStyle(
        "title_main",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=BRANCO,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    styles["title_sub"] = ParagraphStyle(
        "title_sub",
        fontName="Helvetica",
        fontSize=12,
        textColor=VERDE_NEON,
        alignment=TA_CENTER,
        spaceAfter=2,
    )
    styles["timestamp"] = ParagraphStyle(
        "timestamp",
        fontName="Helvetica-BoldOblique",
        fontSize=10,
        textColor=AMARELO,
        alignment=TA_CENTER,
        spaceAfter=6,
    )
    styles["section_header"] = ParagraphStyle(
        "section_header",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=BRANCO,
        spaceBefore=14,
        spaceAfter=6,
        leftIndent=6,
    )
    styles["body"] = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=CINZA_ESCURO,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
        leading=14,
    )
    styles["body_white"] = ParagraphStyle(
        "body_white",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=BRANCO,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
        leading=14,
    )
    styles["bullet"] = ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=CINZA_ESCURO,
        spaceAfter=3,
        leftIndent=14,
        bulletIndent=4,
        leading=14,
    )
    styles["highlight"] = ParagraphStyle(
        "highlight",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=VERDE_ESCURO,
        spaceAfter=3,
        leading=14,
    )
    styles["rule_num"] = ParagraphStyle(
        "rule_num",
        fontName="Helvetica-Bold",
        fontSize=10,
        textColor=AMARELO,
        spaceAfter=1,
        leading=13,
    )
    styles["rule_text"] = ParagraphStyle(
        "rule_text",
        fontName="Helvetica",
        fontSize=9,
        textColor=BRANCO,
        spaceAfter=5,
        leftIndent=16,
        leading=13,
        alignment=TA_JUSTIFY,
    )
    styles["disclaimer"] = ParagraphStyle(
        "disclaimer",
        fontName="Helvetica-Oblique",
        fontSize=7.5,
        textColor=CINZA_MEDIO,
        alignment=TA_JUSTIFY,
        leading=11,
    )
    styles["tag"] = ParagraphStyle(
        "tag",
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=BRANCO,
        alignment=TA_CENTER,
    )
    return styles


def colored_header(text, styles, bg=VERDE_ESCURO):
    tbl = Table(
        [[Paragraph(text, styles["section_header"])]],
        colWidths=[17.6 * cm],
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("ROUNDEDCORNERS", [4]),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
    ]))
    return tbl


def build_pdf():
    s = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
    )
    W = 17.6 * cm
    story = []

    # ── CABEÇALHO ─────────────────────────────────────────────────────────────
    header_tbl = Table(
        [[
            Paragraph("⚽ EA FC 26 ULTIMATE TEAM", s["title_main"]),
        ]],
        colWidths=[W],
    )
    header_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), VERDE_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
    ]))

    sub_tbl = Table(
        [[Paragraph("RELATÓRIO DE ANÁLISE DE MERCADO — TRADING DIÁRIO", s["title_sub"])]],
        colWidths=[W],
    )
    sub_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), VERDE_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))

    date_tbl = Table(
        [[Paragraph(f"Data/Hora do Relatório: {DATE_STR} UTC", s["timestamp"])]],
        colWidths=[W],
    )
    date_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), VERDE_MEDIO),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))

    story += [header_tbl, sub_tbl, date_tbl, Spacer(1, 10)]

    # ── PILLS ────────────────────────────────────────────────────────────────
    pills_data = [[
        Paragraph("💰 Budget: 40.000 coins", s["tag"]),
        Paragraph("📅 Momento: Pós-TOTS | Pré-Festival", s["tag"]),
        Paragraph("🎯 Meta: +15-40% em 48h", s["tag"]),
    ]]
    pills_tbl = Table(pills_data, colWidths=[5.5 * cm, 7.1 * cm, 5 * cm])
    pills_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), VERDE_CLARO),
        ("BACKGROUND", (1, 0), (1, 0), LARANJA),
        ("BACKGROUND", (2, 0), (2, 0), AMARELO),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("TEXTCOLOR", (0, 0), (-1, -1), BRANCO),
        ("TEXTCOLOR", (2, 0), (2, 0), CINZA_ESCURO),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("ROUNDEDCORNERS", [4]),
        ("COLPADDING",  (0, 0), (-1, -1), 4),
    ]))
    story += [pills_tbl, Spacer(1, 12)]

    # ── 1. CONTEXTO DE MERCADO ────────────────────────────────────────────────
    story.append(colored_header("1. CONTEXTO DO MERCADO — 31 MAI 2026", s))
    story.append(Spacer(1, 6))

    ctx_rows = [
        ["Evento Ativo", "Pós-TOTS (Team of the Season encerrado em 29/05). Mercado em fase de recuperação. Próximo grande evento: Festival of Football — Path to Glory, com início em 05/06/2026."],
        ["Tendência Geral", "Preços de fodder (83-88) estão no piso histórico após flood de packs do TOTS. Janela de compra agressiva aberta agora. Recuperação esperada a partir de quinta-feira (04/06) conforme demanda de SBCs pré-Festival aumenta."],
        ["Catalisador Iminente", "Path to Glory (05/06): cartas LIVE do Mundial 2026 que evoluem conforme o país avança. Alta demanda por jogadores de seleções fortes (Brasil, França, Argentina, Alemanha). Neymar retorna ao FUT via convocação brasileira."],
        ["Timing Chave", "Hoje (Dom 31/05): comprar fodder e pré-investimentos. Qua-Qui (03-04/06): vender fodder nos picos de SBC. Sex (05/06): potencial spike de cartas ligadas ao Mundial."],
        ["Risk Level", "MODERADO. Pós-TOTS é uma das janelas de trading mais previsíveis do calendário FUT."],
    ]
    ctx_col_widths = [4.5 * cm, 13.1 * cm]
    ctx_tbl = Table(ctx_rows, colWidths=ctx_col_widths)
    ctx_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, -1), VERDE_ESCURO),
        ("BACKGROUND",    (1, 0), (1, -1), CINZA_CLARO),
        ("ROWBACKGROUNDS",(1, 0), (1, -1), [CINZA_CLARO, BRANCO]),
        ("TEXTCOLOR",     (0, 0), (0, -1), BRANCO),
        ("TEXTCOLOR",     (1, 0), (1, -1), CINZA_ESCURO),
        ("FONTNAME",      (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME",      (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8.5),
        ("ALIGN",         (0, 0), (0, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("GRID",          (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
    ]))
    story += [ctx_tbl, Spacer(1, 12)]

    # ── 2. TABELA DE CARTAS RECOMENDADAS ─────────────────────────────────────
    story.append(colored_header("2. CARTAS RECOMENDADAS — COMPRAR AGORA", s))
    story.append(Spacer(1, 6))

    header_row = [
        Paragraph("JOGADOR", s["tag"]),
        Paragraph("OVR", s["tag"]),
        Paragraph("CLUBE", s["tag"]),
        Paragraph("COMPRA\n(coins)", s["tag"]),
        Paragraph("VENDA\n(coins)", s["tag"]),
        Paragraph("MARGEM\nLÍQ. (5%)", s["tag"]),
        Paragraph("ESTRATÉGIA", s["tag"]),
    ]

    # margem = venda * 0.95 - compra
    cards = [
        # nome, ovr, clube, compra, venda, estrategia
        ("Luka Modric",        "83", "Real Madrid",      800,   1_050, "SBC Fodder — La Liga"),
        ("Romelu Lukaku",      "84", "AS Roma",           800,   1_050, "SBC Fodder — Serie A"),
        ("Isco",               "84", "Real Betis",        800,   1_050, "SBC Fodder — La Liga"),
        ("Scott McTominay",    "85", "Napoli",            850,   1_150, "SBC Fodder — Serie A"),
        ("Stefan de Vrij",     "84", "Inter Milan",       800,   1_050, "SBC Fodder — Serie A"),
        ("Olivier Giroud",     "85", "AC Milan",          850,   1_150, "SBC Fodder — Serie A"),
        ("Ona Battle",         "86", "FC Barcelona",    6_500,   8_500, "Evolução + pre-Festival"),
        ("Jonathan Tah",       "87", "Bayer Leverkusen",10_000, 14_200, "Pre-Festival — Alemanha"),
    ]

    def margem(compra, venda):
        return int(venda * 0.95 - compra)

    card_rows = []
    for nome, ovr, clube, compra, venda, strat in cards:
        m = margem(compra, venda)
        cor_m = VERDE_CLARO if m > 0 else VERMELHO
        card_rows.append([
            Paragraph(nome, ParagraphStyle("cn", fontName="Helvetica-Bold", fontSize=8, textColor=CINZA_ESCURO, leading=10)),
            Paragraph(ovr,  ParagraphStyle("ov", fontName="Helvetica-Bold", fontSize=9, textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=11)),
            Paragraph(clube, ParagraphStyle("cl", fontName="Helvetica", fontSize=7.5, textColor=CINZA_ESCURO, leading=10)),
            Paragraph(f"{compra:,}".replace(",", "."),
                      ParagraphStyle("pr", fontName="Helvetica-Bold", fontSize=8.5, textColor=LARANJA, alignment=TA_CENTER, leading=11)),
            Paragraph(f"{venda:,}".replace(",", "."),
                      ParagraphStyle("vd", fontName="Helvetica-Bold", fontSize=8.5, textColor=VERDE_CLARO, alignment=TA_CENTER, leading=11)),
            Paragraph(f"+{m:,}".replace(",", "."),
                      ParagraphStyle("mg", fontName="Helvetica-Bold", fontSize=8.5, textColor=cor_m, alignment=TA_CENTER, leading=11)),
            Paragraph(strat, ParagraphStyle("st", fontName="Helvetica", fontSize=7.5, textColor=CINZA_ESCURO, leading=10)),
        ])

    full_table = [header_row] + card_rows
    col_w = [3.5*cm, 1.2*cm, 3.2*cm, 2*cm, 2*cm, 2.2*cm, 3.5*cm]
    cards_tbl = Table(full_table, colWidths=col_w, repeatRows=1)
    cards_tbl.setStyle(TableStyle([
        # Header
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 8),
        ("ALIGN",         (0, 0), (-1, 0), "CENTER"),
        # Row alternation
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        # General
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
        ("GRID",          (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
        ("LINEBELOW",     (0, 0), (-1, 0), 1.5, VERDE_CLARO),
    ]))
    story += [cards_tbl, Spacer(1, 5)]

    nota = Paragraph(
        "* Margem Líquida já descontada a taxa de 5% da EA sobre o valor de venda. "
        "Preços estimados com base em dados de mercado de 31/05/2026 — verifique em tempo real no FUTBIN/FUT.GG antes de operar.",
        ParagraphStyle("nota", fontName="Helvetica-Oblique", fontSize=7.5, textColor=CINZA_ESCURO, leading=10)
    )
    story += [nota, Spacer(1, 12)]

    # ── 3. ALOCAÇÃO DO BUDGET ─────────────────────────────────────────────────
    story.append(colored_header("3. ALOCAÇÃO SUGERIDA DO BUDGET (40.000 coins)", s))
    story.append(Spacer(1, 6))

    alloc_data = [
        [Paragraph("FATIA", s["tag"]), Paragraph("VALOR", s["tag"]),
         Paragraph("ESTRATÉGIA", s["tag"]), Paragraph("RISCO", s["tag"])],
        ["SBC Fodder (83-86)", "16.000 coins", "Mass flip: 83-85 rated — comprar ~20 cartas a 800-850, vender 1.000-1.150", "BAIXO"],
        ["Mid-Tier (86-87)", "14.000 coins", "1x Jonathan Tah (87 OVR) + 1x Ona Battle (86 OVR) — hold até 05/06", "MÉDIO"],
        ["Pré-Festival Reserve", "6.000 coins", "Aguardar leaks do Path to Glory (sai ~03/06) para snipe de jogadores do Mundial", "MÉDIO"],
        ["Caixa Livre", "4.000 coins", "Liquidez para oportunidades de snipe e emergências", "—"],
    ]
    alloc_col_w = [4*cm, 3*cm, 7.6*cm, 3*cm]
    alloc_tbl = Table(alloc_data, colWidths=alloc_col_w, repeatRows=1)
    alloc_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_MEDIO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8.5),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("TEXTCOLOR",     (0, 1), (-1, -1), CINZA_ESCURO),
        ("FONTNAME",      (0, 1), (0, -1), "Helvetica-Bold"),
        ("ALIGN",         (1, 0), (1, -1), "CENTER"),
        ("ALIGN",         (3, 0), (3, -1), "CENTER"),
        ("FONTNAME",      (3, 1), (3, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (3, 1), (3, 1), VERMELHO),
        ("TEXTCOLOR",     (3, 2), (3, 3), LARANJA),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("GRID",          (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
        ("LINEBELOW",     (0, 0), (-1, 0), 1.2, VERDE_NEON),
    ]))
    story += [alloc_tbl, Spacer(1, 12)]

    # ── 4. TIMING ─────────────────────────────────────────────────────────────
    story.append(colored_header("4. ESTRATÉGIA DE TIMING — QUANDO COMPRAR E VENDER", s))
    story.append(Spacer(1, 6))

    timing_rows = [
        [Paragraph("DATA", s["tag"]), Paragraph("HORÁRIO (UTC)", s["tag"]),
         Paragraph("AÇÃO", s["tag"]), Paragraph("MOTIVO", s["tag"])],
        ["Dom 31/05 — AGORA", "20:00–23:59", "COMPRAR fodder 83-85 + Tah + Ona Battle",
         "Piso pós-TOTS. Liquidez alta, preços no mínimo histórico."],
        ["Seg 01/06", "06:00–09:00", "COMPRAR fodder adicional se ainda disponível",
         "Madrugada BR = menor oferta, preços ligeiramente mais altos → vender sobrando de domingo."],
        ["Ter 02/06", "18:00–22:00", "VENDER 50% do fodder 83-85",
         "Demanda sobe antes do meio da semana. Pico de SBC grinders."],
        ["Qua-Qui 03-04/06", "17:00–21:00", "VENDER restante do fodder + monitorar leaks Path to Glory",
         "SBC-rush quinta. Leaks do Path to Glory elevam demanda por fodder das nações do Mundial."],
        ["Sex 05/06", "17:00–19:00", "REALIZAR lucro nas cartas mid-tier (Tah, Ona Battle)",
         "Lançamento do Path to Glory = spike de preços. Vender antes do pico se possível."],
    ]
    timing_col_w = [3.5*cm, 2.8*cm, 6.3*cm, 5*cm]
    timing_tbl = Table(timing_rows, colWidths=timing_col_w, repeatRows=1)
    timing_tbl.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",      (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",       (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",       (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("FONTNAME",       (0, 1), (0, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",      (0, 1), (-1, -1), CINZA_ESCURO),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 5),
        ("LEFTPADDING",    (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",   (0, 0), (-1, -1), 6),
        ("GRID",           (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
        ("LINEBELOW",      (0, 0), (-1, 0), 1.2, AMARELO),
    ]))
    story += [timing_tbl, Spacer(1, 12)]

    # ── 5. ESTIMATIVA DE RETORNO ──────────────────────────────────────────────
    story.append(colored_header("5. ESTIMATIVA DE RETORNO EM 48H (ATÉ 02/06/2026)", s))
    story.append(Spacer(1, 6))

    ret_data = [
        [Paragraph("CENÁRIO", s["tag"]), Paragraph("RETORNO ESTIMADO", s["tag"]),
         Paragraph("RESULTADO (coins)", s["tag"]), Paragraph("PREMISSA", s["tag"])],
        ["🟢 Otimista",    "+35–40%",   "+14.000 a +16.000",
         "Leak do Path to Glory antes de sex. SBCs novos no meio da semana. Mercado recupera rápido."],
        ["🟡 Conservador", "+15–20%",   "+6.000 a +8.000",
         "Fodder vende com margem normal. Tah e Ona Battle sobem 20-30%. Sem catalisador extra."],
        ["🔴 Pessimista",  "+5–8%",     "+2.000 a +3.200",
         "Mercado lento, SBCs fracos. Apenas fodder 83-84 vendido com margem mínima."],
    ]
    ret_col_w = [3.2*cm, 3.2*cm, 4*cm, 7.2*cm]
    ret_tbl = Table(ret_data, colWidths=ret_col_w, repeatRows=1)
    ret_tbl.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",      (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",       (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",       (0, 0), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#D5F5E3"), colors.HexColor("#FEF9E7"), colors.HexColor("#FDEDEC")]),
        ("FONTNAME",       (0, 1), (1, -1), "Helvetica-Bold"),
        ("FONTNAME",       (3, 1), (3, -1), "Helvetica"),
        ("TEXTCOLOR",      (1, 1), (2, 1), VERDE_CLARO),
        ("TEXTCOLOR",      (1, 2), (2, 2), LARANJA),
        ("TEXTCOLOR",      (1, 3), (2, 3), VERMELHO),
        ("TEXTCOLOR",      (3, 1), (3, -1), CINZA_ESCURO),
        ("ALIGN",          (1, 0), (2, -1), "CENTER"),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",     (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 7),
        ("LEFTPADDING",    (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",   (0, 0), (-1, -1), 8),
        ("GRID",           (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
        ("LINEBELOW",      (0, 0), (-1, 0), 1.2, VERDE_NEON),
    ]))
    story += [ret_tbl, Spacer(1, 12)]

    # ── 6. 8 REGRAS DE OURO ───────────────────────────────────────────────────
    story.append(colored_header("6. 8 REGRAS DE OURO DO TRADE", s))
    story.append(Spacer(1, 4))

    regras = [
        ("1", "NUNCA opere sem verificar o preço em tempo real (FUTBIN ou FUT.GG) — preços mudam em minutos."),
        ("2", "Respeite o preço de compra máximo. Se não encontrar na faixa indicada, não compre. Paciência > pressa."),
        ("3", "Venda em lotes de 5-10 cartas para não derrubar o próprio mercado."),
        ("4", "Mantenha sempre 10% do budget em caixa livre para sniping e emergências."),
        ("5", "Não entre em pânico durante quedas. Pós-TOTS é queda saudável — é a HORA de comprar, não vender."),
        ("6", "Siga os leaks com disciplina: cartas ligadas ao Mundial 2026 vão subir com o Path to Glory (05/06)."),
        ("7", "Evite comprar em horários de pico (18h-22h BR) — concorrência alta sobe os preços. Prefira madrugada."),
        ("8", "Registre cada operação: compra, venda, lucro. Sem controle, não há crescimento consistente de capital."),
    ]

    rules_box_data = [[Paragraph(f"Regra {n}º — {txt}", s["body_white"])] for n, txt in regras]
    rules_box = Table(rules_box_data, colWidths=[W])
    rules_box.setStyle(TableStyle([
        ("BACKGROUND",     (0, 0), (-1, -1), VERDE_ESCURO),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [VERDE_ESCURO, VERDE_MEDIO]),
        ("TOPPADDING",     (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 6),
        ("LEFTPADDING",    (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",   (0, 0), (-1, -1), 12),
        ("LINEBELOW",      (0, 0), (-1, -2), 0.3, VERDE_NEON),
    ]))
    story += [rules_box, Spacer(1, 14)]

    # ── DISCLAIMER ────────────────────────────────────────────────────────────
    story.append(HRFlowable(width=W, thickness=0.5, color=CINZA_MEDIO))
    story.append(Spacer(1, 6))
    disc = (
        "DISCLAIMER: Este relatório é gerado automaticamente com fins educativos e de entretenimento. "
        "As análises e recomendações baseiam-se em dados públicos de mercado do EA FC 26 Ultimate Team "
        "e em padrões históricos de trading. Não há garantia de lucro. O mercado FUT pode variar "
        "drasticamente devido a atualizações de jogo, promos surpresa e comportamento da comunidade. "
        "Invista apenas o que você está disposto a arriscar. Este conteúdo não constitui conselho financeiro."
        " EA SPORTS FC™ e Ultimate Team™ são marcas registradas da Electronic Arts Inc."
    )
    story.append(Paragraph(disc, s["disclaimer"]))
    story.append(Spacer(1, 4))
    footer = Paragraph(
        f"Gerado em {DATE_STR} UTC | Repositório: kaiohsferreira/fifa-trading",
        ParagraphStyle("footer", fontName="Helvetica", fontSize=7, textColor=CINZA_MEDIO, alignment=TA_CENTER)
    )
    story.append(footer)

    doc.build(story)
    print(f"PDF gerado: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
