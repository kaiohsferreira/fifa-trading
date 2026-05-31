#!/usr/bin/env python3
"""Generate EA FC 26 trading analysis PDF report."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime, timezone
import os

# ── Constants ────────────────────────────────────────────────────────────────
REPORT_DT = datetime(2026, 5, 31, 14, 6, tzinfo=timezone.utc)
FILENAME   = f"relatorio-trading-{REPORT_DT.strftime('%Y-%m-%d-%Hh')}.pdf"
OUTPUT     = os.path.join(os.path.dirname(__file__), FILENAME)

GREEN   = colors.HexColor("#1a7a1a")
DARK_G  = colors.HexColor("#0d4d0d")
GOLD    = colors.HexColor("#c8a400")
LIGHT_G = colors.HexColor("#e8f5e9")
HEADER  = colors.HexColor("#155724")
WHITE   = colors.white
GRAY    = colors.HexColor("#555555")
LIGHT_Y = colors.HexColor("#fffde7")
RED_D   = colors.HexColor("#b71c1c")

PAGE_W, PAGE_H = A4

# ── Style helpers ─────────────────────────────────────────────────────────────
base_styles = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = S("title",
    fontName="Helvetica-Bold", fontSize=22, textColor=WHITE,
    alignment=TA_CENTER, spaceAfter=4)

subtitle_style = S("subtitle",
    fontName="Helvetica-Bold", fontSize=13, textColor=GOLD,
    alignment=TA_CENTER, spaceAfter=2)

meta_style = S("meta",
    fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#cccccc"),
    alignment=TA_CENTER, spaceAfter=0)

section_style = S("section",
    fontName="Helvetica-Bold", fontSize=13, textColor=HEADER,
    spaceBefore=14, spaceAfter=6,
    borderPad=4, borderColor=GREEN, borderWidth=0)

body_style = S("body",
    fontName="Helvetica", fontSize=10, textColor=colors.black,
    leading=15, alignment=TA_JUSTIFY, spaceAfter=4)

bullet_style = S("bullet",
    fontName="Helvetica", fontSize=10, textColor=colors.black,
    leading=14, leftIndent=16, spaceAfter=3)

bold_body = S("bold_body",
    fontName="Helvetica-Bold", fontSize=10, textColor=colors.black,
    leading=14, spaceAfter=2)

disclaimer_style = S("disclaimer",
    fontName="Helvetica-Oblique", fontSize=8, textColor=GRAY,
    alignment=TA_JUSTIFY, leading=11)

label_style = S("label",
    fontName="Helvetica-Bold", fontSize=9, textColor=WHITE,
    alignment=TA_CENTER)

# ── Table style builder ───────────────────────────────────────────────────────
def tbl_style(col_widths, header_color=DARK_G, alt_color=LIGHT_G):
    return TableStyle([
        ("BACKGROUND",  (0, 0), (-1, 0),  header_color),
        ("TEXTCOLOR",   (0, 0), (-1, 0),  WHITE),
        ("FONTNAME",    (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, 0),  9),
        ("ALIGN",       (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
        ("FONTNAME",    (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",    (0, 1), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, alt_color]),
        ("GRID",        (0, 0), (-1, -1), 0.4, colors.HexColor("#aaaaaa")),
        ("TOPPADDING",  (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",(0, 0), (-1, -1), 5),
    ])

# ── Data ──────────────────────────────────────────────────────────────────────
# Columns: Jogador | Rating | Clube | Posição | Compra (coins) | Venda (coins) | Margem Líq.
cards = [
    ["Jogador",        "OVR", "Clube",           "Pos.", "Compra\n(coins)", "Venda\n(coins)", "Margem\nLíq.*"],
    # 86-rated fodder
    ["Konaté",         "86",  "Liverpool",        "CB",  "950",            "2.400",          "+1.330"],
    ["Olise",          "86",  "Bayern Munich",    "RM",  "950",            "2.200",          "+1.140"],
    ["Ona Batlle",     "86",  "FC Barcelona",     "RB",  "950",            "2.100",          "+1.045"],
    ["Courtois",       "86",  "Real Madrid",      "GK",  "1.100",          "2.500",          "+1.275"],
    # 87-rated fodder
    ["Jonathan Tah",   "87",  "Real Madrid",      "CB",  "1.600",          "4.200",          "+2.390"],
    ["Mac Allister",   "87",  "Liverpool",        "CM",  "1.500",          "4.000",          "+2.300"],
    ["David Raya",     "87",  "Arsenal",          "GK",  "1.700",          "4.500",          "+2.575"],
    # 88-rated fodder
    ["Gabriel",        "88",  "Arsenal",          "CB",  "3.000",          "7.500",          "+4.125"],
    ["Irene Paredes",  "88",  "FC Barcelona",     "CB",  "2.700",          "7.000",          "+3.950"],
    ["Endler",         "88",  "FC Barcelona",     "GK",  "3.000",          "6.800",          "+3.460"],
    # 83/84 bulk fodder
    ["Rüdiger",        "85",  "Real Madrid",      "CB",  "1.800",          "3.500",          "+1.525"],
    ["Marquinhos",     "85",  "Paris SG",         "CB",  "1.800",          "3.500",          "+1.525"],
    ["Donnarumma",     "86",  "Paris SG",         "GK",  "1.000",          "2.300",          "+1.185"],
]

col_widths = [3.3*cm, 1.1*cm, 3.3*cm, 1.1*cm, 2.0*cm, 2.0*cm, 2.0*cm]

# ── Budget allocation ─────────────────────────────────────────────────────────
budget_data = [
    ["Estratégia",                                    "Coins Alocados", "Qtd. Cartas", "Objetivo"],
    ["Fodder 86-rated (Konaté, Olise, Ona Batlle)",   "9.500",          "10",          "Vender Jun 5-6"],
    ["Fodder 87-rated (Tah, Mac Allister, Raya)",     "14.400",         "9",           "Vender Jun 5-6"],
    ["Fodder 88-rated (Gabriel, Paredes)",            "11.700",         "4",           "Vender Jun 5-7"],
    ["Reserva (Thursday flip + emergências)",         "4.400",          "—",           "Flexível"],
    ["TOTAL",                                         "40.000",         "23",          ""],
]

# ── Content builder ───────────────────────────────────────────────────────────
def header_block():
    """Green banner header."""
    header_tbl = Table(
        [[Paragraph("EA FC 26 ULTIMATE TEAM", title_style)],
         [Paragraph("Relatório Diário de Trading — SBC Fodder & Promo Flipping", subtitle_style)],
         [Paragraph(f"Data: {REPORT_DT.strftime('%d/%m/%Y %H:%M')} UTC  |  Budget: 40.000 coins  |  Meta: +20K–48K em 48h", meta_style)]],
        colWidths=[PAGE_W - 4*cm]
    )
    header_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_G),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]))
    return header_tbl


def section(title):
    bar = Table(
        [[Paragraph(f"▌ {title}", S("sh", fontName="Helvetica-Bold", fontSize=12,
                                     textColor=WHITE, spaceAfter=0))]],
        colWidths=[PAGE_W - 4*cm]
    )
    bar.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
    ]))
    return bar


def badge(text, bg=GOLD, fg=colors.black):
    b = Table([[Paragraph(text, S("b", fontName="Helvetica-Bold", fontSize=9,
                                   textColor=fg, spaceAfter=0))]],
              colWidths=[None])
    b.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
    ]))
    return b


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm,
        title="EA FC 26 — Relatório de Trading",
        author="Trading Bot — EA FC 26 UT",
    )

    story = []

    # ── HEADER ────────────────────────────────────────────────────────────────
    story.append(header_block())
    story.append(Spacer(1, 0.4*cm))

    # ── 1. CONTEXTO DE MERCADO ─────────────────────────────────────────────────
    story.append(section("1. CONTEXTO DE MERCADO — 31/05/2026"))
    story.append(Spacer(1, 0.25*cm))

    context_rows = [
        ["Promo Ativa",     "Prime Heroes (desde 29/05) — Eden Hazard 96, Yaya Touré, De Rossi, Jaap Stam, M. Richards"],
        ["Próximo Evento",  "Festival of Football — Path to Glory começa 05/06/2026 (17:00 BST)"],
        ["World's Game Upd.", "04/06 — EVO Undo/Reset chega ao mercado → cartas evo voltam a ser tradáveis"],
        ["Thursday Flip",   "05/06 (qui) = Drop de Rivals + lançamento FoF → janela de ouro para comprar barato"],
        ["Tendência Geral",  "Mercado em LOW entre promos → COMPRA AGORA, VENDE NO PICO do Festival"],
    ]
    ctx_tbl = Table(context_rows, colWidths=[3.8*cm, PAGE_W - 4*cm - 3.8*cm])
    ctx_tbl.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (0, -1), DARK_G),
        ("TEXTCOLOR",   (0, 0), (0, -1), GOLD),
        ("FONTNAME",    (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, -1), 9),
        ("FONTNAME",    (1, 0), (1, -1), "Helvetica"),
        ("TEXTCOLOR",   (1, 0), (1, -1), colors.black),
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.HexColor("#f4f4f4"), WHITE]),
        ("GRID",        (0, 0), (-1, -1), 0.3, colors.HexColor("#bbbbbb")),
        ("TOPPADDING",  (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",(0, 0), (-1, -1), 6),
    ]))
    story.append(ctx_tbl)
    story.append(Spacer(1, 0.1*cm))

    story.append(Paragraph(
        "⚡ <b>Janela crítica:</b> Estamos a 5 dias do Festival of Football. "
        "O mercado está em depressão pós-TOTS e pré-FoF — momento ideal para comprar fodder barato "
        "e vender no pico quando os SBCs do Path to Glory forem lançados em 05/06.",
        S("alert", fontName="Helvetica", fontSize=9.5, textColor=RED_D,
          leading=13, backColor=LIGHT_Y, borderPad=8,
          leftIndent=6, rightIndent=6, spaceAfter=4)
    ))
    story.append(Spacer(1, 0.3*cm))

    # ── 2. TABELA DE CARTAS RECOMENDADAS ──────────────────────────────────────
    story.append(section("2. CARTAS RECOMENDADAS — Fodder Flipping 86–88 OVR"))
    story.append(Spacer(1, 0.25*cm))

    story.append(Paragraph(
        "Selecione jogadores nesta faixa de rating (86–88) que servem como <b>fodder premium</b> para SBCs "
        "de alto nível. Com o Path to Glory chegando em 05/06, a demanda por esses ratings dispara.",
        body_style))
    story.append(Spacer(1, 0.2*cm))

    cards_tbl = Table(cards, colWidths=col_widths)
    st = tbl_style(col_widths)
    # Highlight 88-rated rows
    for i in [9, 10, 11]:
        st.add("BACKGROUND", (0, i), (-1, i), colors.HexColor("#d4edda"))
    # Color the margin column green for all data rows
    for i in range(1, len(cards)):
        st.add("TEXTCOLOR", (6, i), (6, i), colors.HexColor("#1a5c1a"))
        st.add("FONTNAME",  (6, i), (6, i), "Helvetica-Bold")
    cards_tbl.setStyle(st)
    story.append(cards_tbl)

    story.append(Paragraph(
        "* <i>Margem líquida = Preço de venda × 0,95 − Preço de compra (taxa EA de 5% já descontada). "
        "Preços baseados em médias de mercado de 31/05/2026 — sujeito a variação.</i>",
        S("note", fontName="Helvetica-Oblique", fontSize=7.5, textColor=GRAY,
          leading=10, spaceAfter=2)))
    story.append(Spacer(1, 0.35*cm))

    # ── 3. ALOCAÇÃO DO BUDGET ─────────────────────────────────────────────────
    story.append(section("3. ALOCAÇÃO DO BUDGET — 40.000 Coins"))
    story.append(Spacer(1, 0.25*cm))

    b_tbl = Table(budget_data,
                  colWidths=[6.8*cm, 2.6*cm, 2.2*cm, PAGE_W - 4*cm - 11.6*cm])
    bs = tbl_style([])
    bs.add("BACKGROUND", (0, len(budget_data)-1), (-1, -1), DARK_G)
    bs.add("TEXTCOLOR",  (0, len(budget_data)-1), (-1, -1), GOLD)
    bs.add("FONTNAME",   (0, len(budget_data)-1), (-1, -1), "Helvetica-Bold")
    b_tbl.setStyle(bs)
    story.append(b_tbl)
    story.append(Spacer(1, 0.35*cm))

    # ── 4. ESTRATÉGIA DE TIMING ───────────────────────────────────────────────
    story.append(section("4. ESTRATÉGIA DE TIMING — Quando Comprar e Vender"))
    story.append(Spacer(1, 0.25*cm))

    timing_rows = [
        ["Data / Hora (UTC)",          "Ação",      "Detalhe"],
        ["31/05 — AGORA (14:00)",       "🟢 COMPRAR", "Mercado em low pós-TOTS. Compre fodder 86-88 rated nos mínimos."],
        ["31/05 – 01/06 (00:00-06:00)", "🟢 COMPRAR", "Madrugada UTC = menor volume → preços ainda mais baixos."],
        ["02/06 – 03/06 (weekend)",     "⏸ AGUARDAR", "Fim de semana = mais packs abertos → preços podem cair mais. Boa janela extra."],
        ["04/06 (quinta, 17:00 UTC)",   "🟡 ATENÇÃO",  "EVO Reset live. Rivals rewards → preços caem. Compra last-minute de fodder."],
        ["05/06 (sex, 17:00 UTC)",      "🔴 VENDER",   "Festival of Football + Path to Glory ao vivo. SBCs novos → PICO de demanda de fodder."],
        ["06/06 – 07/06",               "🔴 VENDER",   "Venda o restante. Demanda sustentada pelos SBCs e investidores entrando tarde."],
    ]
    t_tbl = Table(timing_rows, colWidths=[4.0*cm, 2.5*cm, PAGE_W - 4*cm - 6.5*cm])
    ts = tbl_style([])
    ts.add("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#e8f5e9"))
    ts.add("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#e8f5e9"))
    ts.add("BACKGROUND", (0, 5), (-1, 5), colors.HexColor("#ffebee"))
    ts.add("BACKGROUND", (0, 6), (-1, 6), colors.HexColor("#ffebee"))
    ts.add("ALIGN",      (0, 0), (0, -1), "LEFT")
    ts.add("ALIGN",      (2, 0), (2, -1), "LEFT")
    t_tbl.setStyle(ts)
    story.append(t_tbl)
    story.append(Spacer(1, 0.35*cm))

    # ── 5. RETORNO ESTIMADO EM 48H ────────────────────────────────────────────
    story.append(section("5. ESTIMATIVA DE RETORNO EM 48H"))
    story.append(Spacer(1, 0.25*cm))

    ret_rows = [
        ["Cenário",        "Capital Inicial", "Retorno Estimado", "Capital Final",  "ROI"],
        ["🟡 Conservador",  "40.000",          "+12.000 – +18.000","52.000 – 58.000", "30% – 45%"],
        ["🟢 Otimista",     "40.000",          "+22.000 – +36.000","62.000 – 76.000", "55% – 90%"],
        ["📊 Base Case",    "40.000",          "+15.000 – +25.000","55.000 – 65.000", "37% – 62%"],
    ]
    r_tbl = Table(ret_rows, colWidths=[3.0*cm, 2.5*cm, 3.8*cm, 3.8*cm, 2.1*cm])
    rs = tbl_style([])
    rs.add("BACKGROUND", (0, 1), (-1, 1), LIGHT_Y)
    rs.add("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#e8f5e9"))
    rs.add("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#e3f2fd"))
    rs.add("FONTNAME",   (0, 1), (-1, -1), "Helvetica-Bold")
    rs.add("TEXTCOLOR",  (4, 2), (4, 2), colors.HexColor("#1a7a1a"))
    r_tbl.setStyle(rs)
    story.append(r_tbl)

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>Premissas:</b> Compra ao preço-alvo indicado · Venda no pico de demanda do Path to Glory "
        "(05–06/06) · 5% de taxa EA descontada · Sem crashes inesperados de mercado · Sem ban de conta.",
        S("pre", fontName="Helvetica-Oblique", fontSize=8, textColor=GRAY, leading=11)))
    story.append(Spacer(1, 0.35*cm))

    # ── 6. ESTRATÉGIAS ADICIONAIS ─────────────────────────────────────────────
    story.append(section("6. ESTRATÉGIAS ADICIONAIS"))
    story.append(Spacer(1, 0.25*cm))

    extras = [
        ("Thursday Flip",
         "Em 04/06 (quinta), os rewards de Division Rivals são liberados → inundação de cartas no mercado. "
         "Use os 4.400 coins reservados para comprar fodder 85–86 com desconto extra e venda em 24–48h."),
        ("EVO Reset Play (04/06)",
         "A atualização 'World's Game' (04/06) habilita o EVO Undo/Reset. Cartas que eram "
         "não-tradeable após receberem Evoluções voltam a ser vendáveis → pode gerar pico de oferta "
         "em algumas cartas e escassez em outras. Monitore o mercado das 17:00–18:00 UTC do dia 04/06."),
        ("Festival of Football — Path to Glory Live Upgrades",
         "Jogadores cujos países passam nas fases da Copa do Mundo (verão 2026) recebem upgrades "
         "automáticos de rating. Identifique jogadores baratos de seleções fortes (França, Brasil, "
         "Argentina, Espanha, Inglaterra) na faixa 82–84 OVR para investir ANTES do torneio iniciar."),
    ]
    for title_e, body_e in extras:
        story.append(Paragraph(f"<b>▶ {title_e}</b>", bold_body))
        story.append(Paragraph(body_e, bullet_style))
        story.append(Spacer(1, 0.1*cm))
    story.append(Spacer(1, 0.2*cm))

    # ── 7. 8 REGRAS DE OURO ───────────────────────────────────────────────────
    story.append(section("7. AS 8 REGRAS DE OURO DO TRADE"))
    story.append(Spacer(1, 0.25*cm))

    rules = [
        ("1", "Nunca investir mais de 60% do budget em uma única estratégia.",
              "Diversifique entre 86, 87 e 88-rated fodder."),
        ("2", "Compre no mínimo — venda no pico.",
              "Madrugada UTC e pós-rewards são os melhores momentos para comprar."),
        ("3", "Respeite a taxa de 5% da EA.",
              "Só venda se o lucro líquido (pós-taxa) for positivo. Calcule SEMPRE antes."),
        ("4", "Defina stop-loss mental.",
              "Se o preço cair 30% do seu preço de compra, reavalie antes de segurar ou cortar."),
        ("5", "Nunca compre em pânico de alta.",
              "Se o preço já subiu 50%+, a oportunidade passou. Espere o próximo ciclo."),
        ("6", "Fique atento aos leaks de SBC.",
              "Leaks de SBCs no Twitter/Reddit costumam aparecer horas antes do lançamento — sinal de entrada."),
        ("7", "Não segure cartas por mais de 72h sem plano.",
              "Mercado de FUT é volátil. Se não vendeu em 3 dias, revise o preço ou corte o prejuízo."),
        ("8", "Registre todas as operações.",
              "Anote compra, venda e margem de cada carta. Sem dados, não há aprendizado."),
    ]

    rules_data = [["#", "Regra", "Dica Prática"]] + [[r[0], r[1], r[2]] for r in rules]
    r_tbl2 = Table(rules_data, colWidths=[0.7*cm, 6.3*cm, PAGE_W - 4*cm - 7.0*cm])
    rs2 = tbl_style([])
    for i in range(1, len(rules_data)):
        rs2.add("ALIGN",    (0, i), (0, i), "CENTER")
        rs2.add("FONTNAME", (0, i), (0, i), "Helvetica-Bold")
        rs2.add("TEXTCOLOR",(0, i), (0, i), DARK_G)
        rs2.add("FONTNAME", (1, i), (1, i), "Helvetica-Bold")
        rs2.add("ALIGN",    (1, i), (2, i), "LEFT")
    r_tbl2.setStyle(rs2)
    story.append(r_tbl2)
    story.append(Spacer(1, 0.35*cm))

    # ── DISCLAIMER ────────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=0.5, color=GRAY))
    story.append(Spacer(1, 0.1*cm))
    story.append(Paragraph(
        "<b>DISCLAIMER:</b> Este relatório é gerado com fins educativos e informativos sobre mecânicas de "
        "mercado do EA FC 26 Ultimate Team. Os preços de cartas mencionados são estimativas baseadas em "
        "dados históricos e tendências de mercado — não constituem garantia de lucro. O mercado FUT é "
        "altamente volátil e pode sofrer alterações imediatas devido a patches, mudanças de price range "
        "pela EA, leaks ou eventos inesperados. Negocie com responsabilidade e dentro dos Termos de "
        "Serviço da EA Sports. O autor não se responsabiliza por perdas financeiras decorrentes do uso "
        "deste relatório.",
        disclaimer_style))
    story.append(Spacer(1, 0.1*cm))
    story.append(Paragraph(
        f"Gerado em: {REPORT_DT.strftime('%d/%m/%Y %H:%M')} UTC  |  EA FC 26 Ultimate Team Market Analysis",
        S("foot", fontName="Helvetica", fontSize=7.5, textColor=GRAY, alignment=TA_CENTER)))

    doc.build(story)
    return OUTPUT


if __name__ == "__main__":
    path = build_pdf()
    print(f"PDF gerado: {path}")
