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
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import PageBreak

OUTPUT = "relatorio-trading-2026-05-21-20h.pdf"

# ── Cores ──────────────────────────────────────────────────────────────────
VERDE_ESCURO   = colors.HexColor("#1a5c2e")
VERDE_MEDIO    = colors.HexColor("#28a745")
VERDE_CLARO    = colors.HexColor("#d4edda")
OURO           = colors.HexColor("#c8a200")
CINZA_ESCURO   = colors.HexColor("#2c2c2c")
CINZA_CLARO    = colors.HexColor("#f8f9fa")
CINZA_LINHA    = colors.HexColor("#dee2e6")
LARANJA        = colors.HexColor("#fd7e14")
VERMELHO       = colors.HexColor("#dc3545")
BRANCO         = colors.white
PRETO          = colors.black

def build_styles():
    base = getSampleStyleSheet()

    def s(name, **kw):
        return ParagraphStyle(name, **kw)

    return {
        "titulo": s("titulo",
            fontSize=24, fontName="Helvetica-Bold",
            textColor=BRANCO, alignment=TA_CENTER, spaceAfter=4),
        "subtitulo": s("subtitulo",
            fontSize=13, fontName="Helvetica-Bold",
            textColor=OURO, alignment=TA_CENTER, spaceAfter=2),
        "data": s("data",
            fontSize=10, fontName="Helvetica",
            textColor=VERDE_CLARO, alignment=TA_CENTER, spaceAfter=0),
        "section": s("section",
            fontSize=13, fontName="Helvetica-Bold",
            textColor=BRANCO, backColor=VERDE_ESCURO,
            leftIndent=8, rightIndent=8, spaceBefore=14, spaceAfter=6,
            borderPad=5),
        "body": s("body",
            fontSize=9.5, fontName="Helvetica",
            textColor=CINZA_ESCURO, alignment=TA_JUSTIFY,
            spaceBefore=3, spaceAfter=3, leading=14),
        "body_bold": s("body_bold",
            fontSize=9.5, fontName="Helvetica-Bold",
            textColor=CINZA_ESCURO, spaceBefore=2, spaceAfter=2, leading=14),
        "bullet": s("bullet",
            fontSize=9.5, fontName="Helvetica",
            textColor=CINZA_ESCURO, leftIndent=14,
            spaceBefore=2, spaceAfter=2, leading=14),
        "disclaimer": s("disclaimer",
            fontSize=8, fontName="Helvetica-Oblique",
            textColor=colors.HexColor("#666666"), alignment=TA_JUSTIFY,
            leading=12),
        "header_cell": s("header_cell",
            fontSize=8.5, fontName="Helvetica-Bold",
            textColor=BRANCO, alignment=TA_CENTER),
        "cell": s("cell",
            fontSize=8.2, fontName="Helvetica",
            textColor=CINZA_ESCURO, alignment=TA_CENTER, leading=11),
        "cell_left": s("cell_left",
            fontSize=8.2, fontName="Helvetica-Bold",
            textColor=CINZA_ESCURO, alignment=TA_LEFT, leading=11),
        "retorno_titulo": s("retorno_titulo",
            fontSize=10, fontName="Helvetica-Bold",
            textColor=VERDE_ESCURO, spaceBefore=4, spaceAfter=2),
        "regra_num": s("regra_num",
            fontSize=22, fontName="Helvetica-Bold",
            textColor=OURO, alignment=TA_CENTER),
        "regra_txt": s("regra_txt",
            fontSize=9, fontName="Helvetica",
            textColor=CINZA_ESCURO, alignment=TA_LEFT, leading=12),
        "aviso": s("aviso",
            fontSize=9, fontName="Helvetica-Bold",
            textColor=LARANJA, alignment=TA_CENTER, spaceAfter=4),
    }

def header_banner(st):
    """Faixa de cabeçalho superior."""
    data = [
        [Paragraph("⚽  EA FC 26 ULTIMATE TEAM", st["titulo"])],
        [Paragraph("Relatório Diário de Trading — Análise de Mercado", st["subtitulo"])],
        [Paragraph("21/05/2026  20:09 UTC  |  Budget: 40.000 coins  |  Operador: kaiohsferreira", st["data"])],
    ]
    t = Table(data, colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, -1), VERDE_ESCURO),
        ("TOPPADDING",  (0, 0), (-1, 0), 14),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 12),
        ("LEFTPADDING",  (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return t

def section_title(text, st):
    return Paragraph(f"▌  {text}", st["section"])

def build_market_context(st, elements):
    elements.append(Spacer(1, 0.3*cm))
    elements.append(section_title("1. CONTEXTO DO MERCADO — 21/05/2026", st))

    ctx = [
        ("PROMO ATIVA", "Ultimate TOTS (Team of the Season) — estreia AMANHÃ, 22/05 às 18h BST (19h BRT). "
         "Evento mais importante do ano. Cartas TOTS 90–99 OVR disponíveis via packs, SBCs e objetivos."),
        ("END OF AN ERA SBCs", "SBCs confirmados via leak: Salah 95 OVR, Griezmann 94 OVR, "
         "Bernardo Silva 93 OVR, Goretzka 92 OVR e Robertson 92 OVR. Previsão de lançamento junto com o Ultimate TOTS."),
        ("FODDER ULTRA-BARATO", "Cartas 83–85 rated estão próximas do discard (~750–1.500 coins). "
         "Pior momento do ano para vendas de fodder, MAS o melhor para compras em massa antes dos SBCs End of an Era."),
        ("WEEK 5 TOTS UPGRADE SBC", "Expira 22/05. Custo ~26.350 coins, recompensa ~40.030 coins (ROI positivo). "
         "Se tiver fodder suficiente, vale completar HOJE."),
        ("TOTS CRAFTING UPGRADE", "Ativo até 29/05. Custo ~3.000 coins por tentativa. Repeatable infinitamente."),
        ("TENDÊNCIA GERAL", "Fodder em baixa histórica → compre agora. Preços de TOTS players disparam nas primeiras 48h "
         "→ aguarde 2–3 dias para comprar. Melhor janela de venda: sexta-feira antes do FUT Champions."),
    ]

    for label, text in ctx:
        row = Table(
            [[Paragraph(label, ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=8.5,
                                               textColor=VERDE_ESCURO, alignment=TA_LEFT)),
              Paragraph(text, st["body"])]],
            colWidths=[3.5*cm, 13.5*cm]
        )
        row.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("LINEBELOW", (0, 0), (-1, -1), 0.5, CINZA_LINHA),
        ]))
        elements.append(row)


def build_cards_table(st, elements):
    elements.append(Spacer(1, 0.3*cm))
    elements.append(section_title("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA", st))
    elements.append(Spacer(1, 0.15*cm))

    headers = ["Jogador", "Rat.", "Clube / Liga", "Compra\n(coins)", "Venda\n(coins)", "Lucro\n(–5% EA)", "Estratégia"]

    rows = [
        # [Jogador, Rat, Clube, Compra, Venda, Lucro, Estratégia]
        ["Luka Modrić",         "83", "Real Madrid / LaLiga",     "750",    "1.400",  "+580",  "Fodder End of an Era SBC"],
        ["Iago Aspas",          "83", "Celta Vigo / LaLiga",      "750",    "1.300",  "+485",  "Fodder SBC LaLiga"],
        ["Mateo Kovačić",       "83", "Man City / Premier L.",    "750",    "1.400",  "+580",  "Fodder End of an Era SBC"],
        ["Romelu Lukaku",       "84", "Roma / Serie A",           "800",    "1.600",  "+720",  "Fodder SBC Serie A"],
        ["Alejandro Grimaldo",  "84", "Leverkusen / Bundesliga",  "800",    "1.700",  "+815",  "Fodder End of an Era SBC"],
        ["Rúben Neves",         "84", "Al Hilal / Saudi Pro L.",  "800",    "1.500",  "+625",  "Fodder SBC genérico 84+"],
        ["William Saliba",      "84", "Arsenal / Premier L.",     "800",    "1.600",  "+720",  "Fodder SBC Premier League"],
        ["Federico Dimarco",    "85", "Inter / Serie A",          "1.350",  "2.800",  "+1.310","Fodder SBC 85+ Serie A"],
        ["Nico Schlotterbeck",  "85", "Dortmund / Bundesliga",    "1.300",  "2.600",  "+1.170","Fodder SBC Bundesliga"],
        ["Marcus Thuram",       "85", "Inter / Serie A",          "1.500",  "3.000",  "+1.350","Fodder SBC 85+ ofensivo"],
        ["Youssouf Fofana",     "85", "Real Madrid / LaLiga",     "1.300",  "2.700",  "+1.265","Fodder SBC 85+ LaLiga"],
        ["Alejandro Balde",     "86", "Barcelona / LaLiga",       "1.600",  "3.800",  "+1.910","Fodder SBC 86+ LaLiga"],
        ["Leandro Trossard",    "86", "Arsenal / Premier L.",     "1.700",  "3.900",  "+1.995","Fodder SBC 86+ Premier"],
        ["Granit Xhaka",        "86", "Leverkusen / Bundesliga",  "1.600",  "3.700",  "+1.815","Fodder SBC 86+ Bundesliga"],
        ["Lamine Yamal TOTS",   "95", "Barcelona / LaLiga",       "250k*",  "280k*",  "+16k*", "Comprar após queda D+2/D+3"],
    ]

    col_widths = [3.4*cm, 0.8*cm, 3.6*cm, 1.7*cm, 1.7*cm, 1.7*cm, 4.1*cm]

    table_data = [[Paragraph(h, st["header_cell"]) for h in headers]]
    for i, row in enumerate(rows):
        styled = []
        for j, cell in enumerate(row):
            if j == 0:
                styled.append(Paragraph(cell, st["cell_left"]))
            elif j == 5:
                color = VERDE_MEDIO if not cell.startswith("–") else VERMELHO
                p = ParagraphStyle("p_lucro", fontName="Helvetica-Bold", fontSize=8.2,
                                   textColor=color, alignment=TA_CENTER, leading=11)
                styled.append(Paragraph(cell, p))
            else:
                styled.append(Paragraph(cell, st["cell"]))
        table_data.append(styled)

    t = Table(table_data, colWidths=col_widths, repeatRows=1)

    style = [
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 8.5),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("GRID",          (0, 0), (-1, -1), 0.4, CINZA_LINHA),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        # última linha (Yamal TOTS) destaque especial
        ("BACKGROUND",    (0, len(rows)), (-1, len(rows)), colors.HexColor("#fff3cd")),
        ("FONTNAME",      (0, len(rows)), (-1, len(rows)), "Helvetica-Bold"),
    ]
    t.setStyle(TableStyle(style))
    elements.append(t)

    elements.append(Spacer(1, 0.2*cm))
    elements.append(Paragraph(
        "* Lamine Yamal TOTS: preço estimado com base em leaks e cartas similares. "
        "NÃO comprar no D+0/D+1. Aguardar queda D+2 ou D+3 pós-lançamento. "
        "Valores de fodder (750–1.600 coins) são preços de abertura no mercado — "
        "use a ferramenta de Cheapest SBC do FUTBIN para confirmar antes de comprar.",
        st["disclaimer"]))


def build_timing(st, elements):
    elements.append(Spacer(1, 0.3*cm))
    elements.append(section_title("3. ESTRATÉGIA DE TIMING", st))

    timeline = [
        ("AGORA (21/05 — noite)", OURO,
         "• Compre fodder 83–86 rated em massa enquanto preços estão no piso histórico.\n"
         "• Meta: acumular 30–40 cartas de fodder com o budget de 40k coins.\n"
         "• Foco em cartas 84–85 de LaLiga, Bundesliga, Premier League e Serie A "
         "(mais usadas nos SBCs End of an Era).\n"
         "• Complete o Week 5 TOTS Upgrade SBC se tiver fodder sobrando (expira amanhã)."),
        ("AMANHÃ (22/05 — manhã/tarde)", VERDE_MEDIO,
         "• Evite comprar cartas TOTS nas primeiras horas — preços inflados.\n"
         "• Continue comprando fodder se ainda houver coins disponíveis.\n"
         "• Monitore os SBCs End of an Era assim que saírem (a partir das 18h BST / 19h BRT).\n"
         "• Venda fodder quando a demanda pelos SBCs subir (espere +20–30% de valorização)."),
        ("D+2 / D+3 (23–24/05)", VERDE_ESCURO,
         "• Janela ideal para comprar cartas TOTS midrange após a queda de preço.\n"
         "• Fodder que não foi vendido: use no TOTS Crafting Upgrade SBC (custo ~3k, válido até 29/05).\n"
         "• Avalie cartas de Evolução elegíveis para investimento de longo prazo (82–83 rated sub-1k)."),
        ("SEXTA-FEIRA (23/05)", LARANJA,
         "• MELHOR JANELA DE VENDA da semana — todos buscam melhorar o time para o FUT Champions.\n"
         "• Venda cartas TOTS e cartas valorizadas antes das 18h (pico de demanda).\n"
         "• Não segure cartas valiosas no fim de semana — preços caem após o rush de FUT Champs."),
    ]

    for title, color, text in timeline:
        box_data = [[
            Paragraph(title, ParagraphStyle("tt", fontName="Helvetica-Bold", fontSize=9,
                                             textColor=BRANCO, alignment=TA_LEFT)),
        ]]
        box = Table(box_data, colWidths=[17*cm])
        box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), color),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ]))
        elements.append(box)

        lines = text.split("\n")
        for line in lines:
            elements.append(Paragraph(line, st["bullet"]))
        elements.append(Spacer(1, 0.1*cm))


def build_return_estimate(st, elements):
    elements.append(Spacer(1, 0.3*cm))
    elements.append(section_title("4. ESTIMATIVA DE RETORNO EM 48H", st))
    elements.append(Spacer(1, 0.15*cm))

    scenarios = [
        {
            "label": "CENÁRIO CONSERVADOR",
            "color": VERDE_MEDIO,
            "items": [
                ("Budget investido em fodder", "35.000 coins"),
                ("Cartas compradas (média 1.000/unid.)", "~35 cartas"),
                ("Preço médio de venda pós-SBC (–5% EA)", "1.600 coins/carta"),
                ("Receita bruta estimada", "56.000 coins"),
                ("Lucro líquido estimado", "+21.000 coins (+60%)"),
                ("Capital final", "~61.000 coins"),
            ],
            "nota": "Considera valorização moderada de 60–70% no fodder após lançamento dos End of an Era SBCs."
        },
        {
            "label": "CENÁRIO OTIMISTA",
            "color": OURO,
            "items": [
                ("Budget investido em fodder", "38.000 coins"),
                ("Cartas compradas (média 950/unid.)", "~40 cartas"),
                ("Preço médio de venda pós-SBC (–5% EA)", "2.200 coins/carta"),
                ("Receita bruta estimada", "88.000 coins"),
                ("Lucro líquido estimado", "+50.000 coins (+132%)"),
                ("Capital final", "~88.000 coins"),
            ],
            "nota": "Considera demanda alta pelos SBCs e sell-out de fodder na sexta-feira antes do FUT Champions."
        },
    ]

    scenario_tables = []
    for sc in scenarios:
        header = Table(
            [[Paragraph(sc["label"], ParagraphStyle("sc_h", fontName="Helvetica-Bold",
                                                     fontSize=10, textColor=BRANCO, alignment=TA_CENTER))]],
            colWidths=[8*cm]
        )
        header.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), sc["color"]),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))

        rows_sc = []
        for k, v in sc["items"]:
            is_lucro = "Lucro" in k or "Capital" in k
            key_style = ParagraphStyle("k", fontName="Helvetica", fontSize=8.5,
                                        textColor=CINZA_ESCURO, alignment=TA_LEFT)
            val_style = ParagraphStyle("v", fontName="Helvetica-Bold", fontSize=8.5,
                                        textColor=VERDE_ESCURO if is_lucro else CINZA_ESCURO,
                                        alignment=TA_RIGHT)
            rows_sc.append([Paragraph(k, key_style), Paragraph(v, val_style)])

        detail = Table(rows_sc, colWidths=[5*cm, 3*cm])
        detail.setStyle(TableStyle([
            ("GRID",           (0, 0), (-1, -1), 0.3, CINZA_LINHA),
            ("ROWBACKGROUNDS", (0, 0), (-1, -1), [BRANCO, CINZA_CLARO]),
            ("TOPPADDING",     (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING",  (0, 0), (-1, -1), 4),
            ("LEFTPADDING",    (0, 0), (-1, -1), 6),
            ("RIGHTPADDING",   (0, 0), (-1, -1), 6),
        ]))

        nota_p = Paragraph(f"ℹ {sc['nota']}", ParagraphStyle("nota_sc",
            fontName="Helvetica-Oblique", fontSize=7.5,
            textColor=colors.HexColor("#555555"), alignment=TA_LEFT, leading=10))

        scenario_tables.append([header])
        scenario_tables.append([detail])
        scenario_tables.append([nota_p])
        scenario_tables.append([Spacer(1, 0.2*cm)])

    # Lado a lado
    from reportlab.platypus import KeepTogether

    left_items = []
    right_items = []

    for idx, sc in enumerate(scenarios):
        header = Table(
            [[Paragraph(sc["label"], ParagraphStyle("sc_h2", fontName="Helvetica-Bold",
                                                     fontSize=9.5, textColor=BRANCO, alignment=TA_CENTER))]],
            colWidths=[8*cm]
        )
        header.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), sc["color"]),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))

        rows_sc = []
        for k, v in sc["items"]:
            is_lucro = "Lucro" in k or "Capital" in k
            key_style = ParagraphStyle("k2", fontName="Helvetica", fontSize=8,
                                        textColor=CINZA_ESCURO, alignment=TA_LEFT)
            val_style = ParagraphStyle("v2", fontName="Helvetica-Bold", fontSize=8,
                                        textColor=VERDE_ESCURO if is_lucro else CINZA_ESCURO,
                                        alignment=TA_RIGHT)
            rows_sc.append([Paragraph(k, key_style), Paragraph(v, val_style)])

        detail = Table(rows_sc, colWidths=[4.8*cm, 3.2*cm])
        detail.setStyle(TableStyle([
            ("GRID",           (0, 0), (-1, -1), 0.3, CINZA_LINHA),
            ("ROWBACKGROUNDS", (0, 0), (-1, -1), [BRANCO, CINZA_CLARO]),
            ("TOPPADDING",     (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING",  (0, 0), (-1, -1), 4),
            ("LEFTPADDING",    (0, 0), (-1, -1), 6),
            ("RIGHTPADDING",   (0, 0), (-1, -1), 6),
        ]))

        nota_p = Paragraph(f"ℹ {sc['nota']}", ParagraphStyle("nota_sc2",
            fontName="Helvetica-Oblique", fontSize=7.5,
            textColor=colors.HexColor("#555555"), alignment=TA_LEFT, leading=10))

        target = left_items if idx == 0 else right_items
        target.append(header)
        target.append(detail)
        target.append(Spacer(1, 0.1*cm))
        target.append(nota_p)

    combined = Table(
        [[left_items, right_items]],
        colWidths=[8.5*cm, 8.5*cm]
    )
    combined.setStyle(TableStyle([
        ("VALIGN",       (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",  (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING",   (0, 0), (-1, -1), 0),
    ]))
    elements.append(combined)


def build_golden_rules(st, elements):
    elements.append(Spacer(1, 0.4*cm))
    elements.append(section_title("5. 8 REGRAS DE OURO DO TRADE", st))
    elements.append(Spacer(1, 0.15*cm))

    rules = [
        ("1", "Nunca compre no pico", "Preços disparam nas primeiras 24h após lançamento de promo. Aguarde a queda natural de D+2/D+3."),
        ("2", "Compre na quinta-feira", "A queda de recompensas do Rivals quinta-feira aumenta a oferta e derruba preços — hora de comprar em massa."),
        ("3", "Venda na sexta-feira", "O rush do FUT Champions cria a maior demanda da semana — venda antes das 18h de sexta."),
        ("4", "Calcule sempre a taxa EA", "Todo lucro bruto perde 5% na venda. Nunca faça o cálculo sem descontar essa taxa."),
        ("5", "Diversifique o fodder", "Não aposte tudo em uma liga — SBCs pedem diferentes ligas. Mantenha fodder de LaLiga, Premier, Bundesliga e Serie A."),
        ("6", "Monitore o FUTBIN antes de vender", "Sempre confira o preço médio das últimas 6h antes de listar uma carta — preços mudam rápido durante promos."),
        ("7", "Nunca segure com emoção", "Defina seu alvo de venda antes de comprar. Se atingiu, venda. Não espere por mais — o mercado é imprevisível."),
        ("8", "Reserve 20% como reserva", "Nunca invista 100% do budget. Guarde 8.000 coins para oportunidades de snipe e emergências."),
    ]

    rule_rows = []
    for num, title, desc in rules:
        num_cell = Paragraph(num, ParagraphStyle("rn", fontName="Helvetica-Bold",
                                                   fontSize=20, textColor=OURO,
                                                   alignment=TA_CENTER))
        title_p = Paragraph(title, ParagraphStyle("rt", fontName="Helvetica-Bold",
                                                    fontSize=9.5, textColor=VERDE_ESCURO))
        desc_p  = Paragraph(desc, ParagraphStyle("rd", fontName="Helvetica",
                                                   fontSize=8.5, textColor=CINZA_ESCURO, leading=12))
        text_cell = Table([[title_p], [desc_p]], colWidths=[14*cm])
        text_cell.setStyle(TableStyle([
            ("LEFTPADDING",  (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING",   (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 1),
        ]))
        rule_rows.append([num_cell, text_cell])

    rule_table = Table(rule_rows, colWidths=[1.5*cm, 15.5*cm])
    rule_table.setStyle(TableStyle([
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("LINEBELOW",      (0, 0), (-1, -1), 0.4, CINZA_LINHA),
        ("TOPPADDING",     (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 6),
        ("LEFTPADDING",    (1, 0), (-1, -1), 8),
    ]))
    elements.append(rule_table)


def build_disclaimer(st, elements):
    elements.append(Spacer(1, 0.5*cm))
    elements.append(HRFlowable(width="100%", thickness=1, color=CINZA_LINHA))
    elements.append(Spacer(1, 0.15*cm))

    elements.append(Paragraph(
        "⚠  AVISO IMPORTANTE",
        st["aviso"]))

    elements.append(Paragraph(
        "Este relatório é gerado automaticamente com base em dados públicos de comunidades FUT "
        "(FUTBIN, FUT.GG, TeamGullit, Reddit) e possui fins exclusivamente informativos. "
        "Os preços indicados são estimativas baseadas em dados históricos e tendências de mercado "
        "— não constituem garantia de lucro. O mercado de EA FC Ultimate Team é volátil e pode "
        "mudar em minutos após lançamentos de promos ou patches. "
        "Invista apenas o que pode perder. Nunca aposte todo o budget em uma única estratégia. "
        "Fontes: futbin.com · fut.gg · teamgullit.com · khelnow.com · fifaultimateteam.it",
        st["disclaimer"]))

    elements.append(Spacer(1, 0.2*cm))
    elements.append(Paragraph(
        "Relatório gerado em 21/05/2026 às 20:09 UTC  |  github.com/kaiohsferreira/fifa-trading",
        ParagraphStyle("footer", fontName="Helvetica", fontSize=7.5,
                        textColor=colors.HexColor("#999999"), alignment=TA_CENTER)))


def main():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        title="EA FC 26 — Relatório de Trading 21/05/2026",
        author="kaiohsferreira",
        subject="FUT Trading Analysis",
    )

    st = build_styles()
    elements = []

    elements.append(header_banner(st))

    build_market_context(st, elements)
    build_cards_table(st, elements)
    build_timing(st, elements)
    build_return_estimate(st, elements)
    build_golden_rules(st, elements)
    build_disclaimer(st, elements)

    doc.build(elements)
    print(f"PDF gerado: {OUTPUT}")


if __name__ == "__main__":
    main()
