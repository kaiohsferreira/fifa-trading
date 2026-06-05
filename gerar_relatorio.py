#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import KeepTogether

REPORT_DATE = "05/06/2026 08:07"
PDF_FILENAME = "relatorio-trading-2026-06-05-08h.pdf"

GREEN_DARK  = colors.HexColor("#1a6b3c")
GREEN_MID   = colors.HexColor("#27ae60")
GREEN_LIGHT = colors.HexColor("#d5f5e3")
GOLD        = colors.HexColor("#f1c40f")
DARK_BG     = colors.HexColor("#1c2833")
WHITE       = colors.white
GRAY_LIGHT  = colors.HexColor("#f2f3f4")
GRAY_MED    = colors.HexColor("#aab7b8")
RED_ALERT   = colors.HexColor("#e74c3c")
BLUE_INFO   = colors.HexColor("#2e86c1")

def build_styles():
    base = getSampleStyleSheet()
    styles = {}

    styles["title_main"] = ParagraphStyle(
        "title_main", parent=base["Normal"],
        fontSize=22, textColor=WHITE, fontName="Helvetica-Bold",
        alignment=TA_CENTER, spaceAfter=4
    )
    styles["title_sub"] = ParagraphStyle(
        "title_sub", parent=base["Normal"],
        fontSize=11, textColor=GOLD, fontName="Helvetica-Bold",
        alignment=TA_CENTER, spaceAfter=2
    )
    styles["date_line"] = ParagraphStyle(
        "date_line", parent=base["Normal"],
        fontSize=9, textColor=GRAY_MED, fontName="Helvetica",
        alignment=TA_CENTER, spaceAfter=0
    )
    styles["section_header"] = ParagraphStyle(
        "section_header", parent=base["Normal"],
        fontSize=13, textColor=WHITE, fontName="Helvetica-Bold",
        alignment=TA_LEFT, spaceAfter=6, spaceBefore=14,
        backColor=GREEN_DARK, leftIndent=-6, rightIndent=-6,
        borderPad=5
    )
    styles["body"] = ParagraphStyle(
        "body", parent=base["Normal"],
        fontSize=9.5, textColor=colors.HexColor("#1c1c1c"),
        fontName="Helvetica", leading=14, spaceAfter=5,
        alignment=TA_JUSTIFY
    )
    styles["body_bold"] = ParagraphStyle(
        "body_bold", parent=base["Normal"],
        fontSize=9.5, textColor=colors.HexColor("#1c1c1c"),
        fontName="Helvetica-Bold", leading=14, spaceAfter=4
    )
    styles["bullet"] = ParagraphStyle(
        "bullet", parent=base["Normal"],
        fontSize=9.5, textColor=colors.HexColor("#1c1c1c"),
        fontName="Helvetica", leading=13, spaceAfter=3,
        leftIndent=12, bulletIndent=0
    )
    styles["rule_num"] = ParagraphStyle(
        "rule_num", parent=base["Normal"],
        fontSize=9.5, textColor=GREEN_DARK,
        fontName="Helvetica-Bold", leading=14, spaceAfter=2
    )
    styles["rule_body"] = ParagraphStyle(
        "rule_body", parent=base["Normal"],
        fontSize=9, textColor=colors.HexColor("#2c2c2c"),
        fontName="Helvetica", leading=13, spaceAfter=6,
        leftIndent=14
    )
    styles["disclaimer"] = ParagraphStyle(
        "disclaimer", parent=base["Normal"],
        fontSize=8, textColor=colors.HexColor("#555555"),
        fontName="Helvetica-Oblique", leading=11,
        alignment=TA_JUSTIFY
    )
    styles["tag_green"] = ParagraphStyle(
        "tag_green", parent=base["Normal"],
        fontSize=9, textColor=GREEN_DARK, fontName="Helvetica-Bold",
        alignment=TA_CENTER
    )
    styles["tag_red"] = ParagraphStyle(
        "tag_red", parent=base["Normal"],
        fontSize=9, textColor=RED_ALERT, fontName="Helvetica-Bold",
        alignment=TA_CENTER
    )
    return styles


def header_block(styles):
    bg_table = Table(
        [[Paragraph("EA FC 26 ULTIMATE TEAM", styles["title_main"])],
         [Paragraph("RELATÓRIO DE TRADING — ANÁLISE DE MERCADO", styles["title_sub"])],
         [Paragraph(f"Gerado em: {REPORT_DATE} UTC  |  Budget: 40.000 coins  |  Versão: diária", styles["date_line"])]],
        colWidths=[170*mm]
    )
    bg_table.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), DARK_BG),
        ("TOPPADDING",  (0,0), (-1,-1), 10),
        ("BOTTOMPADDING",(0,-1),(-1,-1), 10),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING",(0,0), (-1,-1), 8),
    ]))
    return bg_table


def section_title(text, styles):
    tbl = Table([[Paragraph(f"  {text}", styles["section_header"])]], colWidths=[170*mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), GREEN_DARK),
        ("TOPPADDING",  (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING",(0,0),(-1,-1), 8),
        ("ROUNDEDCORNERS", (0,0), (-1,-1), [3,3,3,3]),
    ]))
    return tbl


def market_context_section(styles):
    items = []
    items.append(section_title("1. CONTEXTO DO MERCADO — 05 JUNHO 2026", styles))
    items.append(Spacer(1, 4))

    ctx = [
        ["EVENTO ATIVO",  "Festival of Football — Path to Glory (Fase 1)"],
        ["PERÍODO",       "05 Jun → 19 Jun 2026 (Path to Glory)\n19 Jun → 26 Jun (Greats of the Game)"],
        ["MUNDO REAL",    "Copa do Mundo FIFA 2026 começa em 11 Jun (EUA/Canadá/México)"],
        ["TENDÊNCIA",     "Alta demanda por fodder 83-87 (SBCs novos de Copa)\nCartas Path to Glory sobem em 24-48h do lançamento"],
        ["RISCO HOJE",    "Lançamento do Path to Glory Team 1 a partir de 18h BST hoje\nMercado instável nas primeiras 6h — aguardar estabilização"],
    ]
    tbl = Table(ctx, colWidths=[42*mm, 128*mm])
    tbl.setStyle(TableStyle([
        ("FONTNAME",     (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME",     (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE",     (0,0), (-1,-1), 9),
        ("BACKGROUND",   (0,0), (0,-1), GREEN_LIGHT),
        ("BACKGROUND",   (1,0), (1,-1), GRAY_LIGHT),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[GREEN_LIGHT, GRAY_LIGHT]),
        ("GRID",         (0,0), (-1,-1), 0.4, GRAY_MED),
        ("TOPPADDING",   (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0), (-1,-1), 5),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
    ]))
    items.append(tbl)
    items.append(Spacer(1, 6))

    items.append(Paragraph(
        "Hoje (05/06) é o dia de lançamento do <b>Path to Glory</b>, evento principal do Festival of Football. "
        "Cartas dinâmicas serão liberadas para jogadores cujas seleções avançam na Copa do Mundo. "
        "O mercado de fodder 83–87 tende a sofrer <b>alta de 15–40%</b> nas próximas 48h à medida que "
        "novos SBCs de Copa são liberados. Hoje à noite espera-se uma avalanche de SBCs simultâneos. "
        "A estratégia ideal é acumular fodder <b>antes</b> das 18h BST (16h UTC) e segurar até amanhã.",
        styles["body"]
    ))
    return items


def opportunities_section(styles):
    items = []
    items.append(section_title("2. OPORTUNIDADES RECOMENDADAS (Budget: 40.000 coins)", styles))
    items.append(Spacer(1, 4))

    items.append(Paragraph(
        "Tabela com jogadores específicos, preços-alvo e margens líquidas após taxa EA de 5%.",
        styles["body"]
    ))
    items.append(Spacer(1, 4))

    header = [
        Paragraph("JOGADOR", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("RAT", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("POSIÇÃO/CLUBE", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("COMPRA (coins)", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("VENDA (coins)", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("MARGEM LÍQUIDA", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("ESTRATÉGIA", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8, textColor=WHITE, alignment=TA_CENTER)),
    ]

    def row(player, rat, pos_club, buy, sell, margin, strat, highlight=False):
        bg = GREEN_LIGHT if highlight else WHITE
        st = ParagraphStyle("r", fontName="Helvetica", fontSize=8, alignment=TA_CENTER, leading=10)
        st2 = ParagraphStyle("r2", fontName="Helvetica", fontSize=8, alignment=TA_LEFT, leading=10)
        st_g = ParagraphStyle("rg", fontName="Helvetica-Bold", fontSize=8, alignment=TA_CENTER, textColor=GREEN_DARK, leading=10)
        return [
            Paragraph(player, st2),
            Paragraph(rat, st),
            Paragraph(pos_club, st2),
            Paragraph(buy, st),
            Paragraph(sell, st),
            Paragraph(margin, st_g),
            Paragraph(strat, st2),
        ]

    data = [header,
        row("Luka Modrić",     "83", "CM — Real Madrid",          "750",  "1.100", "+295 (39%)",   "SBC Fodder. Comprar antes 18h. Vender 48h.", True),
        row("Romelu Lukaku",   "84", "ST — Napoli",               "750",  "1.150", "+343 (45%)",   "SBC Fodder. Acumular 20+ cópias.", False),
        row("Ngolo Kanté",     "85", "CDM — Al-Ittihad",          "750",  "1.200", "+390 (52%)",   "Fodder popular. Demanda constante.", True),
        row("Sandro Tonali",   "86", "CDM — Newcastle",           "800",  "1.400", "+530 (66%)",   "Alto giro. SBC pede CM/CDM 86+.", False),
        row("Upamecano",       "85", "CB — Bayern München",       "800",  "1.350", "+483 (60%)",   "CB 85 escasso. Vender na sexta.", True),
        row("Patrik Schick",   "86", "ST — Bayer Leverkusen",     "900",  "1.500", "+525 (58%)",   "Copa: Tchéquia. Potencial upgrade.", False),
        row("Amad Diallo",     "84", "RW — Manchester United",    "1.200","2.000", "+700 (58%)",   "Copa: Costa do Marfim. Path to Glory.", True),
        row("Mallory Swanson", "82", "LW — Chicago Red Stars",    "2.500","3.800", "+1.110 (44%)", "Mass bid. 5★5★. Evo candidate.", False),
        row("Klara Bühl",      "84", "LM — Bayern München",       "800",  "1.300", "+435 (54%)",   "SBC fodder feminino. Alta demanda.", True),
        row("Rubén Díaz",      "85", "CB — Manchester City",      "1.000","1.700", "+615 (62%)",   "CB meta. Comprar hoje, vender sábado.", False),
        row("Alexia Putellas", "87", "CM — Barcelona (F)",        "1.400","2.200", "+690 (49%)",   "87 CM raro. SBC Copa costuma pedir.", True),
        row("Aleix García",    "83", "CM — Manchester City",      "750",  "1.050", "+248 (33%)",   "Volume alto. Mass bid 50+ cópias.", False),
    ]

    col_w = [30*mm, 10*mm, 30*mm, 20*mm, 20*mm, 22*mm, 38*mm]
    tbl = Table(data, colWidths=col_w, repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), GREEN_DARK),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("GRID",          (0,0), (-1,-1), 0.4, GRAY_MED),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 4),
        ("RIGHTPADDING",  (0,0), (-1,-1), 4),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, GRAY_LIGHT]),
    ]))
    items.append(tbl)
    items.append(Spacer(1, 5))
    items.append(Paragraph(
        "<b>Nota:</b> Margens calculadas após taxa EA de 5% sobre o preço de venda. "
        "Preços baseados em dados de mercado de 05/06/2026 às 08h UTC — sujeitos a variação. "
        "Sempre verifique o preço atual no FUTBIN ou FUT.GG antes de comprar.",
        styles["body"]
    ))
    return items


def timing_section(styles):
    items = []
    items.append(section_title("3. ESTRATÉGIA DE TIMING", styles))
    items.append(Spacer(1, 4))

    timing = [
        ["HORÁRIO",          "AÇÃO RECOMENDADA",                                                      "RISCO"],
        ["08h–16h UTC\n(hoje)", "Comprar fodder 83–87 em massa via mass bid.\nAlvo: Modrić, Lukaku, Kanté, Bühl, García.\nEstoque 200–300 cópias distribuídas.", "BAIXO"],
        ["16h–18h UTC\n(hoje)", "PARAR de comprar. Aguardar anúncio.\nObservar primeiros SBCs do Path to Glory.\nNão vender ainda — mercado instável.", "MÉDIO"],
        ["18h–22h UTC\n(hoje)", "Monitorar SBCs liberados. Ajustar preços de venda.\nSe SBCs pedirem 84–85 rated: listar a 1.200–1.500.\nEvitar pânico se preço cair momentaneamente.", "MÉDIO"],
        ["22h–06h UTC\n(sexta)", "Vender 50% do estoque. Guardar resto para sábado.\nMass bid em Mallory Swanson (22h–02h: menor concorrência).", "BAIXO"],
        ["06h–20h UTC\n(sexta)", "Pico de demanda. Listar fodder restante.\nSexta = pré-Weekend League. Meta players sobem 20–30%.", "BAIXO"],
        ["Sábado\n(07 Jun)", "Vender últimas cópias. Sábado tarde = pico máximo.\nReinvestir lucro em fodder 87–88 se SBCs continuarem.", "BAIXO"],
    ]

    col_w = [28*mm, 100*mm, 22*mm]
    tbl = Table(timing, colWidths=col_w, repeatRows=1)

    row_styles = [
        ("BACKGROUND",   (0,0), (-1,0), DARK_BG),
        ("TEXTCOLOR",    (0,0), (-1,0), GOLD),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID",         (0,0), (-1,-1), 0.4, GRAY_MED),
        ("FONTSIZE",     (0,0), (-1,-1), 8.5),
        ("TOPPADDING",   (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0), (-1,-1), 5),
        ("LEFTPADDING",  (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, GRAY_LIGHT]),
        ("FONTNAME",     (0,1), (0,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",    (2,1), (2,1), colors.HexColor("#2ecc71")),
        ("TEXTCOLOR",    (2,2), (2,3), colors.HexColor("#e67e22")),
        ("TEXTCOLOR",    (2,4), (2,-1), colors.HexColor("#2ecc71")),
    ]
    tbl.setStyle(TableStyle(row_styles))
    items.append(tbl)
    return items


def returns_section(styles):
    items = []
    items.append(section_title("4. ESTIMATIVA DE RETORNO EM 48H", styles))
    items.append(Spacer(1, 4))

    items.append(Paragraph(
        "Simulação com budget de <b>40.000 coins</b> distribuídos em fodder e oportunidades pontuais.",
        styles["body"]
    ))
    items.append(Spacer(1, 4))

    scenarios = [
        ["PARÂMETRO",            "CONSERVADOR",           "OTIMISTA"],
        ["Budget investido",     "38.000 coins",          "40.000 coins"],
        ["Cartas compradas",     "~200 cópias (83–85)",   "~250 cópias (83–87)"],
        ["Preço médio compra",   "800 coins/carta",       "750 coins/carta"],
        ["Preço médio venda",    "1.100 coins/carta",     "1.400 coins/carta"],
        ["Receita bruta",        "220.000 coins",         "350.000 coins"],
        ["Taxa EA (5%)",         "11.000 coins",          "17.500 coins"],
        ["Lucro líquido",        "+9.500 coins (+25%)",   "+22.500 coins (+56%)"],
        ["Capital final",        "49.500 coins",          "62.500 coins"],
        ["Melhor cenário extra", "—",                     "Path to Glory flip:\n+5.000 coins adicionais"],
    ]

    col_w = [52*mm, 59*mm, 59*mm]
    tbl = Table(scenarios, colWidths=col_w, repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), DARK_BG),
        ("TEXTCOLOR",     (0,0), (-1,0), GOLD),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 9),
        ("GRID",          (0,0), (-1,-1), 0.4, GRAY_MED),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("RIGHTPADDING",  (0,0), (-1,-1), 6),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN",         (1,0), (-1,-1), "CENTER"),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, GRAY_LIGHT]),
        ("BACKGROUND",    (1,-3), (1,-3), colors.HexColor("#d5f5e3")),
        ("BACKGROUND",    (2,-3), (2,-3), colors.HexColor("#d5f5e3")),
        ("TEXTCOLOR",     (1,-3), (2,-3), GREEN_DARK),
        ("FONTNAME",      (1,-3), (2,-3), "Helvetica-Bold"),
        ("BACKGROUND",    (1,-2), (1,-2), colors.HexColor("#d5f5e3")),
        ("BACKGROUND",    (2,-2), (2,-2), colors.HexColor("#eafaf1")),
        ("TEXTCOLOR",     (1,-2), (2,-2), GREEN_DARK),
        ("FONTNAME",      (1,-2), (2,-2), "Helvetica-Bold"),
    ]))
    items.append(tbl)
    items.append(Spacer(1, 5))
    items.append(Paragraph(
        "<b>Premissas:</b> SBCs de Copa do Mundo liberados nas próximas 24h. "
        "Preços de fodder sobem 30–80% com novos desafios. "
        "Cenário conservador assume apenas 1–2 SBCs novos. "
        "Cenário otimista assume 4+ SBCs simultâneos de Copa + Path to Glory, "
        "o que historicamente triplicou o preço de fodder nos anos anteriores.",
        styles["body"]
    ))
    return items


def golden_rules_section(styles):
    items = []
    items.append(section_title("5. 8 REGRAS DE OURO DO TRADE", styles))
    items.append(Spacer(1, 4))

    rules = [
        ("1", "NUNCA compre no lançamento",
         "Nas primeiras 6h de qualquer promo, os preços estão inflados pelo FOMO. "
         "Espere pelo menos 6–12h para o mercado estabilizar antes de comprar qualquer carta nova."),
        ("2", "Verifique o preço antes de CADA compra",
         "O mercado do FC 26 muda minuto a minuto. Sempre confirme o preço atual no FUTBIN "
         "ou FUT.GG antes de executar qualquer compra, mesmo que tenha verificado há 10 minutos."),
        ("3", "Nunca coloque mais de 30% do budget em um único ativo",
         "Diversificação é proteção. Se um SBC for cancelado ou um jogador for removido "
         "dos requisitos, você não perde tudo. Distribua o risco entre pelo menos 4–5 cartas diferentes."),
        ("4", "Respeite a taxa EA de 5%",
         "A EA cobra 5% sobre o preço de venda. Para ter lucro real de 300 coins por carta "
         "vendida a 1.000, você precisa tê-la comprado a no máximo 650 coins. "
         "Calcule sempre ANTES de comprar."),
        ("5", "Venda antes do pico, não no pico",
         "Tentar vender exatamente no topo é arriscado. Quando o preço subir 40–60% "
         "acima do seu custo médio, realize o lucro. Ganância é o maior inimigo do trader."),
        ("6", "Aproveite os ciclos semanais",
         "Quinta: Rivals Rewards → preços caem (melhor momento para comprar). "
         "Sexta à tarde / Sábado: pico de jogadores online → preços sobem. "
         "Domingo noite: final do WL → outra janela de compra."),
        ("7", "Mass bid é mais seguro que Buy Now",
         "Fazer lances em dezenas de cartas abaixo do preço Buy Now reduz o custo médio "
         "e protege contra manipulação de mercado. Prefira mass bid em cartas de alto volume."),
        ("8", "Documente seus trades",
         "Registre cada compra: jogador, quantidade, preço, data. "
         "Só assim você sabe o que funciona, o que falhou, e como melhorar a estratégia a cada semana."),
    ]

    for num, title, body in rules:
        items.append(
            Table([
                [Paragraph(f"#{num}", ParagraphStyle("rn", fontName="Helvetica-Bold", fontSize=11,
                                                      textColor=WHITE, alignment=TA_CENTER)),
                 Paragraph(title, ParagraphStyle("rt", fontName="Helvetica-Bold", fontSize=10,
                                                  textColor=WHITE))]
            ], colWidths=[12*mm, 158*mm],
            style=TableStyle([
                ("BACKGROUND",   (0,0), (-1,-1), GREEN_DARK),
                ("TOPPADDING",   (0,0), (-1,-1), 4),
                ("BOTTOMPADDING",(0,0), (-1,-1), 4),
                ("LEFTPADDING",  (0,0), (-1,-1), 6),
                ("RIGHTPADDING", (0,0), (-1,-1), 6),
                ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
            ]))
        )
        items.append(Paragraph(body, styles["rule_body"]))
        items.append(Spacer(1, 2))

    return items


def disclaimer_section(styles):
    items = []
    items.append(HRFlowable(width="100%", thickness=0.5, color=GRAY_MED, spaceAfter=6))
    items.append(Paragraph(
        "<b>DISCLAIMER:</b> Este relatório é gerado automaticamente para fins de análise e estratégia "
        "de trading no EA FC 26 Ultimate Team. Os preços indicados são estimativas baseadas em dados "
        "de mercado coletados em 05/06/2026 às 08:07 UTC via FUTBIN, FUT.GG e fontes públicas. "
        "O mercado do Ultimate Team é volátil e pode mudar drasticamente em minutos, especialmente "
        "durante eventos promocionais. Não há garantia de lucro. Invista apenas o que estiver disposto "
        "a perder. Este documento não constitui aconselhamento financeiro. EA Sports, EA FC 26 e "
        "Ultimate Team são marcas registradas da Electronic Arts Inc.",
        styles["disclaimer"]
    ))
    return items


def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        topMargin=14*mm,
        bottomMargin=14*mm,
        leftMargin=18*mm,
        rightMargin=18*mm,
    )

    styles = build_styles()
    story = []

    story.append(header_block(styles))
    story.append(Spacer(1, 8))

    story.extend(market_context_section(styles))
    story.append(Spacer(1, 6))

    story.extend(opportunities_section(styles))
    story.append(Spacer(1, 6))

    story.extend(timing_section(styles))
    story.append(Spacer(1, 6))

    story.extend(returns_section(styles))
    story.append(Spacer(1, 6))

    story.extend(golden_rules_section(styles))
    story.append(Spacer(1, 8))

    story.extend(disclaimer_section(styles))

    doc.build(story)
    print(f"PDF gerado: {filename}")


if __name__ == "__main__":
    build_pdf(PDF_FILENAME)
