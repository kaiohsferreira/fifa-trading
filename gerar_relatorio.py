#!/usr/bin/env python3
"""Gerador de relatório de trading EA FC 26 Ultimate Team."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime

# ── Constantes ─────────────────────────────────────────────────────────────────
REPORT_DT = datetime.datetime(2026, 6, 4, 8, 6)
FILENAME   = "relatorio-trading-2026-06-04-08h.pdf"
OUTPUT     = f"/home/user/fifa-trading/{FILENAME}"

GREEN_DARK  = colors.HexColor("#1a472a")
GREEN_MID   = colors.HexColor("#2d6a4f")
GREEN_LIGHT = colors.HexColor("#95d5b2")
GOLD        = colors.HexColor("#f4a261")
GOLD_DARK   = colors.HexColor("#e76f51")
BG_LIGHT    = colors.HexColor("#f0f7f4")
BG_TABLE    = colors.HexColor("#e8f5e9")
WHITE       = colors.white
GREY_TEXT   = colors.HexColor("#555555")
DARK_TEXT   = colors.HexColor("#1c1c1c")
RED_ALERT   = colors.HexColor("#c0392b")

# ── Estilos ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def s(name, **kw):
    return ParagraphStyle(name, parent=styles["Normal"], **kw)

TITLE_STYLE = s("titulo",
    fontSize=26, textColor=WHITE, fontName="Helvetica-Bold",
    alignment=TA_CENTER, spaceAfter=4)

SUBTITLE_STYLE = s("subtitulo",
    fontSize=12, textColor=GOLD, fontName="Helvetica-Bold",
    alignment=TA_CENTER, spaceAfter=2)

DATETIME_STYLE = s("dt",
    fontSize=10, textColor=GREEN_LIGHT, fontName="Helvetica",
    alignment=TA_CENTER, spaceAfter=0)

SECTION_STYLE = s("secao",
    fontSize=14, textColor=WHITE, fontName="Helvetica-Bold",
    backColor=GREEN_DARK, borderPad=6,
    spaceBefore=14, spaceAfter=6, leftIndent=-8, rightIndent=-8)

SUBSECTION_STYLE = s("subsecao",
    fontSize=11, textColor=GREEN_DARK, fontName="Helvetica-Bold",
    spaceBefore=8, spaceAfter=4)

BODY_STYLE = s("corpo",
    fontSize=9.5, textColor=DARK_TEXT, fontName="Helvetica",
    leading=14, alignment=TA_JUSTIFY, spaceAfter=4)

BULLET_STYLE = s("bullet",
    fontSize=9.5, textColor=DARK_TEXT, fontName="Helvetica",
    leading=14, leftIndent=14, bulletIndent=4, spaceAfter=3)

NOTE_STYLE = s("nota",
    fontSize=8.5, textColor=GREY_TEXT, fontName="Helvetica-Oblique",
    leading=12, alignment=TA_JUSTIFY, spaceAfter=4)

DISCLAIMER_STYLE = s("disclaimer",
    fontSize=8, textColor=GREY_TEXT, fontName="Helvetica-Oblique",
    leading=11, alignment=TA_JUSTIFY, borderPad=4)

RULE_NUM_STYLE = s("rulenum",
    fontSize=10, textColor=GOLD_DARK, fontName="Helvetica-Bold",
    leading=14)

RULE_TEXT_STYLE = s("ruletext",
    fontSize=9.5, textColor=DARK_TEXT, fontName="Helvetica",
    leading=14, spaceAfter=4)

FOOTER_STYLE = s("footer",
    fontSize=8, textColor=GREY_TEXT, fontName="Helvetica",
    alignment=TA_CENTER)


def section_header(text):
    return Paragraph(f"  {text}", SECTION_STYLE)


def header_bar(doc_width):
    """Cabeçalho verde escuro com título."""
    bar_data = [[
        Paragraph("EA FC 26 ULTIMATE TEAM", TITLE_STYLE),
    ]]
    bar_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
    ])
    return Table(bar_data, colWidths=[doc_width], style=bar_style)


def subtitle_bar(doc_width, dt_str):
    data = [
        [Paragraph("Relatório de Análise de Mercado & Oportunidades de Trading", SUBTITLE_STYLE)],
        [Paragraph(dt_str, DATETIME_STYLE)],
    ]
    style = TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), GREEN_MID),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
    ])
    return Table(data, colWidths=[doc_width], style=style)


def info_box(doc_width, items, bg=BG_LIGHT):
    rows = [[Paragraph(item, BODY_STYLE)] for item in items]
    st = TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), bg),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("GRID",         (0, 0), (-1, -1), 0.3, colors.HexColor("#ccddcc")),
    ])
    return Table(rows, colWidths=[doc_width], style=st)


# ── Tabela de Oportunidades ────────────────────────────────────────────────────
def opportunities_table(doc_width):
    col_w = [doc_width * p for p in [0.20, 0.07, 0.14, 0.11, 0.11, 0.10, 0.10, 0.17]]

    header = [
        Paragraph("<b>Jogador</b>", s("th", fontSize=8.5, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Rtg</b>",     s("th2", fontSize=8.5, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Clube / País</b>", s("th3", fontSize=8.5, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Compra (max)</b>", s("th4", fontSize=8.5, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Venda (alvo)</b>", s("th5", fontSize=8.5, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Lucro Bruto</b>", s("th6", fontSize=8.5, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Margem Liq.*</b>", s("th7", fontSize=8.5, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Estratégia</b>", s("th8", fontSize=8.5, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ]

    def row(jogador, rtg, clube, compra, venda, estrategia, bg=WHITE):
        lucro_bruto = venda - compra
        taxa = int(venda * 0.05)
        margem_liq = lucro_bruto - taxa

        cor_margem = colors.HexColor("#1a7f37") if margem_liq > 0 else RED_ALERT

        return [
            Paragraph(jogador, s(f"j{jogador}", fontSize=8.5, textColor=DARK_TEXT, fontName="Helvetica-Bold")),
            Paragraph(str(rtg),  s(f"r{jogador}", fontSize=8.5, textColor=GREEN_DARK, fontName="Helvetica-Bold", alignment=TA_CENTER)),
            Paragraph(clube,     s(f"c{jogador}", fontSize=8.5, textColor=GREY_TEXT)),
            Paragraph(f"{compra:,}c".replace(",", "."), s(f"cp{jogador}", fontSize=8.5, textColor=DARK_TEXT, alignment=TA_CENTER)),
            Paragraph(f"{venda:,}c".replace(",", "."), s(f"v{jogador}", fontSize=8.5, textColor=DARK_TEXT, alignment=TA_CENTER)),
            Paragraph(f"+{lucro_bruto:,}c".replace(",", "."), s(f"lb{jogador}", fontSize=8.5, textColor=GREEN_MID, fontName="Helvetica-Bold", alignment=TA_CENTER)),
            Paragraph(f"+{margem_liq:,}c".replace(",", "."), s(f"ml{jogador}", fontSize=8.5, textColor=cor_margem, fontName="Helvetica-Bold", alignment=TA_CENTER)),
            Paragraph(estrategia, s(f"e{jogador}", fontSize=7.8, textColor=GREY_TEXT)),
        ], bg

    data = [header]
    rows_data = [
        # SBC FODDER 83-84 (baixo risco, alto volume)
        ("Luka Modrić",       83, "Real Madrid / CRO",  750,  1_100, "SBC Fodder 83+ · comprar em massa hoje"),
        ("Iago Aspas",        83, "Celta Vigo / ESP",   750,  1_050, "Fodder 83+, alta liquidez, vender quinta"),
        ("Henrikh Mkhitaryan",83, "Inter Milão / ARM",  750,  1_050, "Fodder 83+, demanda SBC diária"),
        ("Manuel Neuer",      84, "Bayern München / GER", 800, 1_250, "Fodder 84+, SBC 10x84+ até 12/jun"),
        ("Lukaku",            84, "Roma / BEL",         800,  1_200, "Fodder 84+ upgrade SBC, alto volume"),
        ("Isco",              84, "Sevilla / ESP",      800,  1_200, "Fodder 84+, liquidez alta"),
        ("Wojciech Szczęsny", 84, "Barcelona / POL",    800,  1_200, "Fodder 84+, 10x upgrade SBC"),
        # 85 rated
        ("N'Golo Kanté",      85, "Al Ittihad / FRA",   950,  1_500, "Fodder 85+, demanda SBC diária"),
        ("Patrik Schick",     85, "Leverkusen / CZE",   950,  1_450, "3x 85+ upgrade SBC diário"),
        ("Manuela Giugliano", 85, "AS Roma / ITA",    1_000,  1_500, "Fodder feminino 85+, SBC barata"),
        # 86-87 rated
        ("Rubén Dias",        86, "Man City / POR",   2_200,  3_200, "Fodder 86+, icon upgrades SBC"),
        ("Vini Jr (Ouro Base)",87, "Real Madrid / BRA",3_500,  5_500, "Versão ouro base; PtG vai elevar preço"),
        # Thursday flip / Festival of Football antecipação
        ("Bukayo Saka",       87, "Arsenal / ING",    3_800,  5_800, "PtG release jun/5, Inglaterra forte"),
        ("Jamal Musiala",     87, "Bayern München / GER",3_200, 5_000, "PtG Alemanha · comprar ANTES do drop"),
        ("Christian Pulisic", 86, "AC Milão / EUA",   2_500,  4_000, "PtG EUA (sede Copa), demanda alta"),
    ]

    alt_bg = [WHITE, BG_TABLE]
    for i, (jogador, rtg, clube, compra, venda, estrategia) in enumerate(rows_data):
        r, bg = row(jogador, rtg, clube, compra, venda, estrategia, alt_bg[i % 2])
        data.append(r)

    table_style = TableStyle([
        # Cabeçalho
        ("BACKGROUND",   (0, 0), (-1, 0), GREEN_DARK),
        ("TEXTCOLOR",    (0, 0), (-1, 0), WHITE),
        ("TOPPADDING",    (0, 0), (-1, 0), 7),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
        # Linhas de dados
        ("TOPPADDING",    (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
        # Alternância de cor
        *[("BACKGROUND", (0, i + 1), (-1, i + 1), BG_TABLE if i % 2 == 1 else WHITE)
          for i in range(len(rows_data))],
        # Grid
        ("GRID",         (0, 0), (-1, -1), 0.5, colors.HexColor("#b2d8b2")),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        # Linhas separadoras de grupo
        ("LINEBELOW",    (0, 6),  (-1, 6),  1.0, GREEN_MID),   # após 84 rated
        ("LINEBELOW",    (0, 9),  (-1, 9),  1.0, GREEN_MID),   # após 85 rated
        ("LINEBELOW",    (0, 11), (-1, 11), 1.0, GREEN_MID),   # após 86-87 base
    ])

    return Table(data, colWidths=col_w, style=table_style, repeatRows=1)


# ── Tabela de Timing ───────────────────────────────────────────────────────────
def timing_table(doc_width):
    col_w = [doc_width * 0.18, doc_width * 0.22, doc_width * 0.22, doc_width * 0.38]
    header = [
        Paragraph("<b>Janela</b>",    s("t1", fontSize=9, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Quando</b>",    s("t2", fontSize=9, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Ação</b>",      s("t3", fontSize=9, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Motivo</b>",    s("t4", fontSize=9, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ]
    rows = [
        ["COMPRA HOJE", "Qui 04/jun · Agora", "Acumular 83-85 fodder", "Queda pré-evento; FoF começa amanhã"],
        ["DROP EVENT", "Sex 05/jun · 18h BST", "Vender 83-85 fodder", "Nova SBC lança, demanda sobe rapidamente"],
        ["PtG WAIT", "Sex 06 – Dom 07/jun", "Observar PtG, não comprar", "Preços inflados; aguardar estabilização"],
        ["PtG BUY",  "Seg/Ter 08-09/jun", "Comprar PtG de nações favoritas", "Preço caiu; Copa começa 11/jun"],
        ["UPGRADE", "Após partidas Copa", "Vender PtG com upgrade", "Cartas que avançaram sobem 30-80%"],
        ["FODDER DIÁRIO", "Todo dia 18-22h UTC", "Girar 83-85 rated", "Pico diário de demanda em SBCs"],
    ]
    data = [header]
    alt = [WHITE, BG_TABLE]
    for i, r in enumerate(rows):
        styled = [
            Paragraph(r[0], s(f"tw{i}", fontSize=8.5, textColor=GREEN_DARK, fontName="Helvetica-Bold", alignment=TA_CENTER)),
            Paragraph(r[1], s(f"tw2{i}", fontSize=8.5, textColor=DARK_TEXT, alignment=TA_CENTER)),
            Paragraph(r[2], s(f"tw3{i}", fontSize=8.5, textColor=DARK_TEXT)),
            Paragraph(r[3], s(f"tw4{i}", fontSize=8.5, textColor=GREY_TEXT)),
        ]
        data.append(styled)

    st = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), GREEN_MID),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        *[("BACKGROUND",  (0, i + 1), (-1, i + 1), alt[i % 2]) for i in range(len(rows))],
        ("GRID",          (0, 0), (-1, -1), 0.5, colors.HexColor("#b2d8b2")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ])
    return Table(data, colWidths=col_w, style=st, repeatRows=1)


# ── Tabela de Retorno ──────────────────────────────────────────────────────────
def return_table(doc_width):
    col_w = [doc_width * 0.22, doc_width * 0.26, doc_width * 0.26, doc_width * 0.26]
    header = [
        Paragraph("<b>Estratégia</b>", s("rt1", fontSize=9, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Investimento</b>", s("rt2", fontSize=9, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Cenário Conservador</b>", s("rt3", fontSize=9, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Cenário Otimista</b>", s("rt4", fontSize=9, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ]
    rows = [
        ["SBC Fodder\n83-84 rated",  "15.000 coins\n(~18 cartas)", "+2.700 coins (+18%)\nFodder a 1.100c, 5% taxa", "+4.500 coins (+30%)\nDemanda SBC sobe 40%"],
        ["SBC Fodder\n85 rated",     "10.000 coins\n(~10 cartas)", "+2.100 coins (+21%)\nVenda a 1.450c média", "+3.500 coins (+35%)\nSBC 3x85+ diário ativo"],
        ["Thursday Flip\nPtG Base",  "10.000 coins\n(~2-3 cartas)", "+3.200 coins (+32%)\nUpgrade 1 estágio Copa", "+8.000 coins (+80%)\nUpgrade 2+ estágios"],
        ["Evol. Invest.\n86-87 ouro", "5.000 coins\n(~2 cartas)",  "+1.500 coins (+30%)\nDemanda Evolution", "+3.000 coins (+60%)\nPtG + Evolution combo"],
        ["<b>TOTAL</b>",            "<b>40.000 coins</b>",         "<b>+9.500 coins (+24%)\nCapital final: 49.500</b>",
                                                                     "<b>+19.000 coins (+47%)\nCapital final: 59.000</b>"],
    ]
    data = [header]
    for i, r in enumerate(rows):
        is_total = i == len(rows) - 1
        fn = "Helvetica-Bold" if is_total else "Helvetica"
        tc = GREEN_DARK if is_total else DARK_TEXT
        bg = colors.HexColor("#d4edda") if is_total else (BG_TABLE if i % 2 == 1 else WHITE)
        data.append([
            Paragraph(r[0], s(f"rt_a{i}", fontSize=8.5, fontName=fn, textColor=tc)),
            Paragraph(r[1], s(f"rt_b{i}", fontSize=8.5, fontName=fn, textColor=tc, alignment=TA_CENTER)),
            Paragraph(r[2], s(f"rt_c{i}", fontSize=8.5, fontName=fn, textColor=GREEN_MID if is_total else GREY_TEXT)),
            Paragraph(r[3], s(f"rt_d{i}", fontSize=8.5, fontName=fn, textColor=GOLD_DARK if is_total else GREY_TEXT)),
        ])

    st = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), GREEN_DARK),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        *[("BACKGROUND",  (0, i + 1), (-1, i + 1),
           colors.HexColor("#d4edda") if i == len(rows) - 1 else (BG_TABLE if i % 2 == 1 else WHITE))
          for i in range(len(rows))],
        ("GRID",          (0, 0), (-1, -1), 0.5, colors.HexColor("#b2d8b2")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("LINEABOVE",     (0, len(rows)), (-1, len(rows)), 1.5, GREEN_DARK),
    ])
    return Table(data, colWidths=col_w, style=st, repeatRows=1)


# ── Regras de Ouro ─────────────────────────────────────────────────────────────
GOLDEN_RULES = [
    ("1", "LIMITE DE RISCO POR CARTA",
     "Nunca invista mais de 20% do budget total em uma única carta ou posição. "
     "Diversifique entre ratings (83-87) e estratégias (fodder + PtG + Evolution)."),
    ("2", "COMPRE NA QUEDA, VENDA NO PICO",
     "A janela ideal de compra é qui/sex de manhã (UTC) antes dos drops de conteúdo. "
     "Venda entre 18h-22h UTC quando a demanda por SBCs está no ápice."),
    ("3", "RESPEITE A TAXA DE 5%",
     "Sempre calcule lucro LÍQUIDO descontando 5% do preço de venda. "
     "Se a margem líquida for menor que 15%, a operação não compensa."),
    ("4", "NUNCA SEGURE POR EMOÇÃO",
     "Definiu o preço de venda? Coloque a carta no mercado e não altere. "
     "Greed mata trades. Se o mercado virar contra você, corte a perda."),
    ("5", "MONITORE EVENTOS ANTES DE INVESTIR PESADO",
     "Novas SBCs e promos mudam o mercado em horas. Confirme o conteúdo do "
     "evento antes de alocar mais de 10k coins em uma única categoria."),
    ("6", "INVISTA EM PATH TO GLORY COM CAUTELA",
     "Compre PtG apenas APÓS a estabilização de preço (48-72h do drop). "
     "Priorize nações com histórico forte na Copa: Brasil, França, Argentina, Espanha."),
    ("7", "USE O VOLUME A SEU FAVOR",
     "Prefira 15 cartas de 1k coin a 1 carta de 15k. Volume garante liquidez "
     "e reduz risco de travamento de capital em itens de baixa rotatividade."),
    ("8", "REGISTRE CADA TRADE",
     "Anote compra, venda, lucro/prejuízo de cada operação. "
     "Sem dados históricos você não sabe o que está funcionando."),
]


# ── Build PDF ──────────────────────────────────────────────────────────────────
def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=1.8 * cm,
        leftMargin=1.8 * cm,
        topMargin=1.5 * cm,
        bottomMargin=2.0 * cm,
    )

    usable_w = A4[0] - 3.6 * cm
    dt_str = REPORT_DT.strftime("Gerado em: %d/%m/%Y às %H:%M UTC  |  Budget: 40.000 coins  |  EA FC 26 FUT")

    story = []

    # ── CABEÇALHO ──────────────────────────────────────────────────────────────
    story.append(header_bar(usable_w))
    story.append(subtitle_bar(usable_w, dt_str))
    story.append(Spacer(1, 10))

    # ── CONTEXTO DE MERCADO ────────────────────────────────────────────────────
    story.append(section_header("1  CONTEXTO DE MERCADO · 04 JUN 2026"))
    story.append(Spacer(1, 4))

    ctx_items = [
        "<b>Evento Ativo:</b> Festival of Football (FoF) — lançamento AMANHÃ, 05/jun às 18h BST. "
        "É o maior evento de verão do EA FC 26, inspirado na Copa do Mundo FIFA 2026 (EUA/Canadá/México, "
        "estreia 11/jun). Duração total: 05/jun a 24/jul/2026.",

        "<b>Promo Inicial (05–19/jun) — PATH TO GLORY:</b> Cartas especiais de jogadores "
        "nacionais com upgrades dinâmicos conforme o desempenho real na Copa. "
        "Confirmados: Vinicius Jr (Brasil), Jamal Musiala (Alemanha), Bukayo Saka (Inglaterra), "
        "Christian Pulisic (EUA), Kevin De Bruyne (Bélgica), Frenkie de Jong (Holanda).",

        "<b>SBCs Ativas (dados 04/jun):</b>  "
        "• 10x 84+ Upgrade (válida até 12/jun, ~15.750 coins, max 3×/conta)  "
        "• 3x 85+ Upgrade (diária, reset 18h UTC)  "
        "• 1 de 3 x 83+ Player Pick (em rotação)",

        "<b>Bônus de Login:</b> Faça login entre 05/jun e 24/jul para receber ícone Pelé 93 OVR "
        "gratuito + 3 Evoluções 'Choose Your Journey'.",

        "<b>Tendência Geral:</b> O mercado está CAINDO hoje (qui, pré-evento). "
        "Traders estão liquidando cards para ter coins antes do drop de amanhã. "
        "Isso cria a melhor janela de COMPRA das próximas 2 semanas.",

        "<b>Preços de referência (04/jun):</b>  "
        "83 rated: ~750c  |  84 rated: ~750-800c  |  85 rated: ~950-1.000c  |  "
        "86 rated: ~2.200-3.000c  |  87 rated: ~3.200-5.500c",
    ]
    story.append(info_box(usable_w, ctx_items))
    story.append(Spacer(1, 10))

    # ── OPORTUNIDADES ──────────────────────────────────────────────────────────
    story.append(section_header("2  CARTAS RECOMENDADAS · OPORTUNIDADES DE COMPRA"))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "* Margem Líquida = Lucro Bruto menos 5% de taxa EA sobre o preço de venda. "
        "Cartas agrupadas por tier: 83-84 (fodder básico) · 85 (mid-tier) · 86-87 (investimento).",
        NOTE_STYLE))
    story.append(Spacer(1, 4))
    story.append(opportunities_table(usable_w))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>Alocação sugerida do budget:</b>  "
        "83-84 rated fodder: 15.000c  |  85 rated fodder: 10.000c  |  "
        "Thursday Flip / PtG base: 10.000c  |  Evolução 86-87: 5.000c",
        BODY_STYLE))
    story.append(Spacer(1, 10))

    # ── TIMING ────────────────────────────────────────────────────────────────
    story.append(section_header("3  ESTRATÉGIA DE TIMING"))
    story.append(Spacer(1, 4))
    story.append(timing_table(usable_w))
    story.append(Spacer(1, 6))

    story.append(info_box(usable_w, [
        "<b>Atenção Thursday Flip:</b> Hoje (qui 04/jun) é o penúltimo dia antes do "
        "drop do Festival of Football. O pico de liquidez de fodder ocorre entre "
        "18h-22h UTC de amanhã (sex 05/jun) quando a nova SBC do FoF for anunciada. "
        "Compre agora, venda amanhã à noite.",
        "<b>Path to Glory:</b> NÃO compre no lançamento (sex 05/jun às 18h BST). "
        "Aguarde a euforia passar (48-72h). Compre entre seg-ter 08-09/jun "
        "e segure até a Copa começar (11/jun) ou até upgrades individuais.",
    ], bg=colors.HexColor("#fff8e1")))
    story.append(Spacer(1, 10))

    # ── RETORNO 48H ──────────────────────────────────────────────────────────
    story.append(section_header("4  ESTIMATIVA DE RETORNO EM 48H"))
    story.append(Spacer(1, 4))
    story.append(return_table(usable_w))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "Premissas: preços de compra no nível atual (04/jun); venda após drop do "
        "Festival of Football (05-06/jun). Cenário conservador assume demanda +20% "
        "sobre o preço atual; otimista assume demanda +50% com SBC de alto rating ativa. "
        "Taxa EA de 5% descontada em TODAS as vendas.",
        NOTE_STYLE))
    story.append(Spacer(1, 10))

    # ── REGRAS DE OURO ────────────────────────────────────────────────────────
    story.append(section_header("5  8 REGRAS DE OURO DO TRADE"))
    story.append(Spacer(1, 6))

    rules_data = []
    for num, titulo, texto in GOLDEN_RULES:
        rule_row = [
            [
                Paragraph(num, s(f"rn{num}", fontSize=18, textColor=GOLD_DARK,
                                 fontName="Helvetica-Bold", alignment=TA_CENTER)),
            ],
            [
                Paragraph(f"<b>{titulo}</b>", s(f"rt_{num}", fontSize=9.5,
                          textColor=GREEN_DARK, fontName="Helvetica-Bold")),
                Paragraph(texto, s(f"rb_{num}", fontSize=9, textColor=DARK_TEXT,
                                   leading=13)),
            ],
        ]
        rules_data.append(rule_row)

    for i, (num, titulo, texto) in enumerate(GOLDEN_RULES):
        bg = BG_TABLE if i % 2 == 0 else WHITE
        inner = Table(
            [[
                Paragraph(num, s(f"n{i}", fontSize=20, textColor=GOLD_DARK,
                                 fontName="Helvetica-Bold", alignment=TA_CENTER)),
                [Paragraph(f"<b>{titulo}</b>", s(f"t{i}", fontSize=9.5,
                            textColor=GREEN_DARK, fontName="Helvetica-Bold",
                            spaceAfter=2)),
                 Paragraph(texto, s(f"b{i}", fontSize=9, textColor=DARK_TEXT, leading=13))],
            ]],
            colWidths=[usable_w * 0.07, usable_w * 0.93],
            style=TableStyle([
                ("BACKGROUND",   (0, 0), (-1, -1), bg),
                ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING",   (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
                ("LEFTPADDING",  (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("GRID",         (0, 0), (-1, -1), 0.3, colors.HexColor("#ccddcc")),
            ]),
        )
        story.append(inner)

    story.append(Spacer(1, 12))

    # ── DISCLAIMER ────────────────────────────────────────────────────────────
    story.append(HRFlowable(width=usable_w, thickness=1, color=GREEN_LIGHT))
    story.append(Spacer(1, 6))
    disc = Table([[Paragraph(
        "<b>DISCLAIMER:</b> Este relatório é gerado automaticamente com base em dados de mercado "
        "coletados de fontes públicas (FUTBIN, FUT.GG, TeamGullit, Reddit r/FIFA) e destina-se "
        "exclusivamente a fins informativos e educacionais. Preços do mercado FUT são altamente "
        "voláteis e podem variar significativamente em minutos. Nenhuma das informações aqui "
        "contidas constitui garantia de lucro. O trading em EA FC 26 envolve risco de perda de "
        "coins. Decida com base na sua própria análise e tolerância ao risco. "
        "EA Sports e FIFA são marcas registradas de seus respectivos proprietários.",
        DISCLAIMER_STYLE)]],
        colWidths=[usable_w],
        style=TableStyle([
            ("BACKGROUND",   (0, 0), (-1, -1), colors.HexColor("#f8f8f8")),
            ("TOPPADDING",   (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
            ("LEFTPADDING",  (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("BOX",          (0, 0), (-1, -1), 0.5, GREEN_LIGHT),
        ]),
    )
    story.append(disc)
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        f"Relatório gerado em {REPORT_DT.strftime('%d/%m/%Y às %H:%M UTC')} · "
        "EA FC 26 Ultimate Team Trading Report · github.com/kaiohsferreira/fifa-trading",
        FOOTER_STYLE))

    doc.build(story)
    print(f"PDF gerado: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
