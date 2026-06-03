#!/usr/bin/env python3
"""Gerador de relatório de trading EA FC 26 Ultimate Team."""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak

REPORT_DATE = "03/06/2026 20:06"
PDF_FILENAME = "relatorio-trading-2026-06-03-20h.pdf"

# ─── Paleta de cores ────────────────────────────────────────────────────────
EA_GREEN   = colors.HexColor("#00B04F")
EA_DARK    = colors.HexColor("#0D0D0D")
EA_GOLD    = colors.HexColor("#F5A623")
EA_BLUE    = colors.HexColor("#0E3B6E")
EA_LIGHT   = colors.HexColor("#F2F2F2")
EA_RED     = colors.HexColor("#C0392B")
EA_WHITE   = colors.white
ROW_ALT    = colors.HexColor("#E8F5EE")


def build_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title", parent=base["Title"],
            fontSize=22, textColor=EA_WHITE, alignment=TA_CENTER,
            spaceAfter=4, fontName="Helvetica-Bold"
        ),
        "subtitle": ParagraphStyle(
            "subtitle", parent=base["Normal"],
            fontSize=11, textColor=EA_GOLD, alignment=TA_CENTER,
            spaceAfter=2, fontName="Helvetica-Bold"
        ),
        "date_style": ParagraphStyle(
            "date_style", parent=base["Normal"],
            fontSize=10, textColor=EA_LIGHT, alignment=TA_CENTER,
            spaceAfter=0, fontName="Helvetica"
        ),
        "section": ParagraphStyle(
            "section", parent=base["Heading2"],
            fontSize=13, textColor=EA_WHITE, fontName="Helvetica-Bold",
            backColor=EA_BLUE, leftIndent=-8, rightIndent=-8,
            spaceBefore=10, spaceAfter=4,
            borderPad=4
        ),
        "body": ParagraphStyle(
            "body", parent=base["Normal"],
            fontSize=9.5, textColor=EA_DARK, fontName="Helvetica",
            spaceAfter=4, leading=14
        ),
        "body_j": ParagraphStyle(
            "body_j", parent=base["Normal"],
            fontSize=9.5, textColor=EA_DARK, fontName="Helvetica",
            spaceAfter=4, leading=14, alignment=TA_JUSTIFY
        ),
        "bold": ParagraphStyle(
            "bold", parent=base["Normal"],
            fontSize=9.5, textColor=EA_DARK, fontName="Helvetica-Bold",
            spaceAfter=2
        ),
        "bullet": ParagraphStyle(
            "bullet", parent=base["Normal"],
            fontSize=9.5, textColor=EA_DARK, fontName="Helvetica",
            leftIndent=16, spaceAfter=3, leading=14,
            bulletIndent=6
        ),
        "disclaimer": ParagraphStyle(
            "disclaimer", parent=base["Normal"],
            fontSize=8, textColor=colors.HexColor("#666666"),
            fontName="Helvetica", spaceAfter=4, leading=11,
            alignment=TA_JUSTIFY
        ),
        "gold_rule": ParagraphStyle(
            "gold_rule", parent=base["Normal"],
            fontSize=9.5, textColor=EA_DARK, fontName="Helvetica",
            leftIndent=20, spaceAfter=5, leading=14,
            bulletIndent=6
        ),
    }


def section_header(text, styles):
    return Paragraph(f"<font color='#FFFFFF'><b>  {text}</b></font>", styles["section"])


def build_pdf():
    doc = SimpleDocTemplate(
        PDF_FILENAME,
        pagesize=A4,
        rightMargin=18*mm, leftMargin=18*mm,
        topMargin=14*mm, bottomMargin=14*mm,
        title="Relatório de Trading EA FC 26",
        author="Market Analysis Bot"
    )

    styles = build_styles()
    story = []

    # ── CABEÇALHO ─────────────────────────────────────────────────────────
    header_data = [
        [Paragraph("EA FC 26 ULTIMATE TEAM", styles["title"])],
        [Paragraph("RELATÓRIO DIÁRIO DE TRADING", styles["subtitle"])],
        [Paragraph(f"Data/Hora do Relatório: {REPORT_DATE} UTC", styles["date_style"])],
    ]
    header_table = Table(header_data, colWidths=[174*mm])
    header_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), EA_DARK),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 2), (-1, 2), 12),
        ("LEFTPADDING",  (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("LINEBELOW", (0, 2), (-1, 2), 2, EA_GREEN),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 6*mm))

    # ── 1. CONTEXTO DO MERCADO ──────────────────────────────────────────
    story.append(section_header("1. CONTEXTO DO MERCADO — 03/06/2026", styles))
    story.append(Spacer(1, 2*mm))

    ctx_items = [
        ("<b>Festival of Football (Ativo: 05/06 → 24/07/2026):</b> "
         "EA Sports lançou o maior evento do ano coincidindo com a Copa do Mundo FIFA 2026. "
         "A campanha envolve múltiplas promos encadeadas, pacotes temáticos e recompensas login diário. "
         "O mercado está em aquecimento pré-evento — comprar antes do pico é a estratégia correta."),
        ("<b>Path to Glory — Promo ATIVA (05/06 → 19/06):</b> "
         "Cartas especiais de jogadores da Copa do Mundo que SOBEM DE RATING conforme as seleções avançam. "
         "Confirmados: Vini Jr (Brasil), Musiala (Alemanha), Saka (Inglaterra), Pulisic (EUA), Raúl Jiménez (México). "
         "Cada vitória da seleção = upgrade da carta. Alto potencial especulativo."),
        ("<b>Shapeshifters (Ativo: 12/06 → 10/07):</b> "
         "Jogadores com posições trocadas e boosts de atributos. "
         "Aumenta a demanda por fodder de nível médio (83-87) para SBCs de troca de posição."),
        ("<b>Greats of the Game (Previsto: 19/06 → 26/06):</b> "
         "ICONs Rivellino e Mario Kempes chegam via SBC — esses SBCs exigem fodder 85-87 em grande volume. "
         "<b>Comprar fodder AGORA é a jogada pré-lançamento mais segura.</b>"),
        ("<b>Pelé ICON 93 OVR — Login gratuito (05/06 → 24/07):</b> "
         "Sem SBC, sem moedas. Apenas login. Não impacta demanda de fodder diretamente, "
         "mas mantém jogadores ativos no FUT aumentando o volume geral de negociação."),
        ("<b>Evo Reset System (Ativo desde 04/06):</b> "
         "EA liberou o reset de Evolutions em cartas tradeable. Cartas evoluídas voltam a poder ser "
         "listadas no mercado. Cria oportunidades em jogadores com potencial de evolução barato."),
        ("<b>Copa do Mundo começa em 11/06:</b> "
         "Jogos reais impactam cartas Path to Glory. Seleções favoritas (Brasil, França, Argentina, "
         "Alemanha, Portugal) têm cartas com maior potencial de valorização."),
    ]
    for item in ctx_items:
        story.append(Paragraph(f"• {item}", styles["bullet"]))

    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(
        "<b>Tendência Geral:</b> Mercado em fase de ALTA. Demanda por fodder deve subir "
        "acentuadamente de 05/06 a 26/06 com o encadeamento de SBCs. "
        "Janela de compra: <b>AGORA (03/06)</b>. Janela de venda: <b>06/06 a 10/06 e 19/06 a 22/06</b>.",
        styles["body_j"]
    ))
    story.append(Spacer(1, 4*mm))

    # ── 2. TABELA DE OPORTUNIDADES ───────────────────────────────────────
    story.append(section_header("2. CARTAS RECOMENDADAS — BUDGET ATÉ 40.000 COINS", styles))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "Tabela com preços de compra e venda estimados. "
        "<b>Margem líquida</b> já desconta a taxa EA de 5% sobre o preço de venda.",
        styles["body"]
    ))
    story.append(Spacer(1, 2*mm))

    # Cabeçalho da tabela
    col_headers = [
        Paragraph("<b>Jogador</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
                  fontSize=8.5, textColor=EA_WHITE, alignment=TA_CENTER)),
        Paragraph("<b>OVR</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
                  fontSize=8.5, textColor=EA_WHITE, alignment=TA_CENTER)),
        Paragraph("<b>Clube / Liga</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
                  fontSize=8.5, textColor=EA_WHITE, alignment=TA_CENTER)),
        Paragraph("<b>Tipo de Carta</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
                  fontSize=8.5, textColor=EA_WHITE, alignment=TA_CENTER)),
        Paragraph("<b>Comprar até</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
                  fontSize=8.5, textColor=EA_WHITE, alignment=TA_CENTER)),
        Paragraph("<b>Vender em</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
                  fontSize=8.5, textColor=EA_WHITE, alignment=TA_CENTER)),
        Paragraph("<b>Margem Líq.</b>", ParagraphStyle("th", fontName="Helvetica-Bold",
                  fontSize=8.5, textColor=EA_WHITE, alignment=TA_CENTER)),
    ]

    cell_style = ParagraphStyle("td", fontName="Helvetica", fontSize=8.5,
                                textColor=EA_DARK, alignment=TA_CENTER)
    cell_bold  = ParagraphStyle("td_b", fontName="Helvetica-Bold", fontSize=8.5,
                                textColor=EA_DARK, alignment=TA_CENTER)
    cell_green = ParagraphStyle("td_g", fontName="Helvetica-Bold", fontSize=8.5,
                                textColor=EA_GREEN, alignment=TA_CENTER)
    cell_gold  = ParagraphStyle("td_gold", fontName="Helvetica-Bold", fontSize=8.5,
                                textColor=colors.HexColor("#8B6914"), alignment=TA_CENTER)

    # (Jogador, OVR, Clube/Liga, Tipo, Comprar, Vender, Margem)
    # Margem = Venda * 0.95 - Compra
    players = [
        ("Modric", "83", "Al-Qadsiah / Saudi Pro", "Gold Rare", "800", "1.600", "+720"),
        ("Iago Aspas", "83", "Celta Vigo / La Liga", "Gold Rare", "800", "1.600", "+720"),
        ("Kovacic", "83", "Man City / Premier", "Gold Rare", "800", "1.500", "+625"),
        ("Mane", "83", "Al-Nassr / Saudi Pro", "800", "800", "1.600", "+720"),
        ("Trossard", "83", "Arsenal / Premier", "Gold Rare", "800", "1.600", "+720"),
        ("Neuer", "84", "Bayern / Bundesliga", "Gold Rare", "900", "1.800", "+810"),
        ("Lukaku", "84", "Roma / Serie A", "Gold Rare", "900", "1.900", "+905"),
        ("Grimaldo", "84", "Bayer Lev. / Bundesliga", "Gold Rare", "1.000", "2.000", "+900"),
        ("De Paul", "84", "Atlético Madrid / La Liga", "Gold Rare", "900", "1.800", "+810"),
        ("Partey", "84", "Arsenal / Premier", "Gold Rare", "900", "1.900", "+905"),
        ("Patrik Schick", "85", "B. Leverkusen / Bundesliga", "Gold Rare", "1.300", "2.600", "+1.170"),
        ("Manuela Giugliano", "85", "Roma / Serie F", "Gold Rare", "1.200", "2.500", "+1.175"),
        ("Alex Greenwood", "85", "Man City W / FAWSL", "Gold Rare", "1.100", "2.300", "+1.085"),
        ("Ruben Dias", "86", "Man City / Premier", "Gold Rare", "1.800", "3.500", "+1.525"),
        ("Klara Bühl", "86", "Bayern F / Frauen-Bund.", "Gold Rare", "1.700", "3.400", "+1.530"),
        ("Vinicius Jr", "87", "Real Madrid / La Liga", "Gold Rare", "3.000", "5.500", "+2.225"),
        ("Bukayo Saka", "87", "Arsenal / Premier", "Gold Rare", "3.200", "5.800", "+2.310"),
        ("Jamal Musiala", "87", "Bayern / Bundesliga", "Gold Rare", "3.000", "5.600", "+2.320"),
    ]

    rows = [col_headers]
    for i, p in enumerate(players):
        bg = ROW_ALT if i % 2 == 0 else EA_WHITE
        row = [
            Paragraph(p[0], cell_bold),
            Paragraph(p[1], cell_style),
            Paragraph(p[2], cell_style),
            Paragraph(p[3], cell_style),
            Paragraph(f"{p[4]} c", cell_style),
            Paragraph(f"{p[5]} c", cell_style),
            Paragraph(f"{p[6]} c", cell_green),
        ]
        rows.append(row)

    col_widths = [36*mm, 12*mm, 40*mm, 22*mm, 20*mm, 20*mm, 20*mm]
    tbl = Table(rows, colWidths=col_widths, repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  EA_BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ROW_ALT, EA_WHITE]),
        ("GRID",         (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
        ("LINEBELOW",    (0, 0), (-1, 0),  1.5, EA_GREEN),
        ("LINEBELOW",    (0, -1),(-1, -1), 1,   EA_BLUE),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "<i>* Preços estimados com base em dados históricos e tendências do mercado atual. "
        "Margem líquida = (Preço de Venda × 0,95) − Preço de Compra. Verifique sempre no FUTBIN antes de comprar.</i>",
        styles["disclaimer"]
    ))
    story.append(Spacer(1, 4*mm))

    # ── 3. ESTRATÉGIA DE TIMING ──────────────────────────────────────────
    story.append(section_header("3. ESTRATÉGIA DE TIMING", styles))
    story.append(Spacer(1, 2*mm))

    timing_blocks = [
        ("COMPRAR AGORA (03/06 — hoje):",
         [
             "Cartas 83-84 Gold Rare abaixo de 1.000 coins — mercado ainda em estado pré-evento, oferta alta.",
             "Cartas 85-86 Gold Rare entre 1.100 e 1.900 coins — janela pré-Festival of Football.",
             "Vini Jr, Musiala e Saka 87 OVR entre 2.800 e 3.200 coins — Path to Glory começa em 05/06.",
             "Evitar compras acima dos tetos indicados na tabela. Paciência = lucro.",
         ]),
        ("SEGURAR (04–05/06):",
         [
             "Não vender nas horas que antecedem o lançamento do Festival of Football (05/06 18h BST).",
             "Preços de fodder sobem com o anúncio dos SBCs temáticos. Aguardar confirmação dos requisitos.",
             "Monitorar Path to Glory Team 1 para ajustar posição em Vini Jr / Saka / Musiala.",
         ]),
        ("VENDER — Janela 1 (06/06 → 10/06):",
         [
             "Primeiras 48-72h após abertura do evento: SBCs novos = demanda máxima.",
             "83-84: alvo 1.500-1.800 coins. 85-86: alvo 2.400-3.500 coins.",
             "Vender em lotes pequenos (5-10 cartas) para não saturar o mercado.",
         ]),
        ("VENDER — Janela 2 (19/06 → 22/06):",
         [
             "Greats of the Game entra em 19/06 com ICONs Rivellino e Kempes via SBC.",
             "SBCs de ICON clássico exigem 85-87 Gold Rare em grandes volumes.",
             "Cartas 85-87 devem pico nesta janela. Alvo: 85 OVR > 2.800 coins, 87 OVR > 5.500 coins.",
         ]),
        ("THURSDAY FLIP (toda semana):",
         [
             "Quinta-feira: recompensas de Rivals caem → supply aumenta → preços despencam (comprar).",
             "Sexta-feira 18h BST → Domingo 18h BST: demanda FUT Champs → preços sobem (vender).",
             "Foco em cartas 85-87 com boa liquidez (jogadores de ligas TOP 5).",
         ]),
    ]

    for title, bullets in timing_blocks:
        story.append(Paragraph(f"<b>{title}</b>", styles["bold"]))
        for b in bullets:
            story.append(Paragraph(f"→  {b}", styles["bullet"]))
        story.append(Spacer(1, 2*mm))

    story.append(Spacer(1, 2*mm))

    # ── 4. ESTIMATIVA DE RETORNO EM 48H ─────────────────────────────────
    story.append(section_header("4. ESTIMATIVA DE RETORNO EM 48H", styles))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "<b>Budget inicial: 40.000 coins</b>  |  Horizonte: 48 horas (comprar hoje, vender 05-06/06)",
        styles["bold"]
    ))
    story.append(Spacer(1, 2*mm))

    # Tabela de retorno
    ret_headers = ["Cenário", "Estratégia", "Cartas Compradas", "Capital Final", "Lucro Líquido", "ROI"]
    ret_data_raw = [
        ("Conservador",
         "50% em fodder 83-84\n+ 50% em fodder 85-86",
         "~30 cartas 83-84 (800c)\n+ ~10 cartas 85-86 (2.000c)",
         "52.400 coins",
         "+12.400 coins",
         "+31%"),
        ("Moderado",
         "40% em 83-84\n+ 40% em 85-86\n+ 20% em Saka/Musiala",
         "~15 cartas 83-84\n+ ~7 cartas 85-86\n+ 2 cartas 87 OVR",
         "58.000 coins",
         "+18.000 coins",
         "+45%"),
        ("Otimista",
         "30% fodder 83-84\n+ 40% fodder 85-87\n+ 30% Saka/Vini Jr (hold PtG)",
         "~10 cartas 83-84\n+ ~7 cartas 85-86\n+ 3 cartas 87 OVR",
         "66.000 coins",
         "+26.000 coins",
         "+65%"),
    ]

    ret_style_h = ParagraphStyle("rh", fontName="Helvetica-Bold", fontSize=8.5,
                                 textColor=EA_WHITE, alignment=TA_CENTER)
    ret_style   = ParagraphStyle("rc", fontName="Helvetica", fontSize=8,
                                 textColor=EA_DARK, alignment=TA_CENTER, leading=12)
    ret_bold    = ParagraphStyle("rb", fontName="Helvetica-Bold", fontSize=8.5,
                                 textColor=EA_DARK, alignment=TA_CENTER)
    ret_green   = ParagraphStyle("rg", fontName="Helvetica-Bold", fontSize=9,
                                 textColor=EA_GREEN, alignment=TA_CENTER)

    ret_rows = [[Paragraph(h, ret_style_h) for h in ret_headers]]
    scenario_colors = [
        colors.HexColor("#EAF4FF"),  # conservador
        colors.HexColor("#FFF8E6"),  # moderado
        colors.HexColor("#EAFAF1"),  # otimista
    ]
    for i, r in enumerate(ret_data_raw):
        row = [
            Paragraph(r[0], ret_bold),
            Paragraph(r[1].replace("\n", "<br/>"), ret_style),
            Paragraph(r[2].replace("\n", "<br/>"), ret_style),
            Paragraph(r[3], ret_bold),
            Paragraph(r[4], ret_green),
            Paragraph(r[5], ret_green),
        ]
        ret_rows.append(row)

    ret_col_widths = [26*mm, 40*mm, 46*mm, 26*mm, 22*mm, 14*mm]
    ret_tbl = Table(ret_rows, colWidths=ret_col_widths, repeatRows=1)
    ret_tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  EA_BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [
            colors.HexColor("#EAF4FF"),
            colors.HexColor("#FFF8E6"),
            colors.HexColor("#EAFAF1"),
        ]),
        ("GRID",         (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 6),
        ("LINEBELOW",    (0, 0), (-1, 0),  1.5, EA_GREEN),
    ]))
    story.append(ret_tbl)
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "<i>* Projeções baseadas em padrões históricos de preços durante promos de Copa do Mundo no FUT. "
        "Cenário otimista pressupõe Brasil e Inglaterra nos quartos de final. Nunca garantido.</i>",
        styles["disclaimer"]
    ))
    story.append(Spacer(1, 4*mm))

    # ── 5. 8 REGRAS DE OURO ──────────────────────────────────────────────
    story.append(section_header("5. AS 8 REGRAS DE OURO DO TRADE", styles))
    story.append(Spacer(1, 2*mm))

    regras = [
        ("01", "NUNCA compre acima do teto indicado.",
         "Pagar 10% a mais destrói a margem. Seja paciente — o mercado sempre oferece o preço certo."),
        ("02", "Venda em lotes pequenos.",
         "Colocar 30 cartas iguais ao mesmo tempo satura o mercado e derruba o preço. Máximo 5-8 por vez."),
        ("03", "Compre na quinta, venda no sábado.",
         "Rewards de Rivals toda quinta = oferta alta = preços baixos. FUT Champs no fim de semana = demanda alta."),
        ("04", "Monitore os SBCs antes de comprar.",
         "Fodder só vale quando há SBCs ativos. Confirme no FUTBIN antes de fazer posição grande."),
        ("05", "Nunca coloque todo o budget numa única carta.",
         "Diversifique em pelo menos 3-5 tipos diferentes. Um SBC cancelado pode travar todo seu capital."),
        ("06", "Respeite o horário de pico.",
         "Mercado mais ativo: 18h-22h BST (19h-23h BRT). Fora desse horário, spreads maiores e menos liquidez."),
        ("07", "Path to Glory = especulação, não garantia.",
         "Cards sobem SOMENTE se a seleção avançar. Não aposte mais de 20% do budget nessa estratégia."),
        ("08", "Use o FUTBIN Price Range para não ser bloqueado.",
         "EA bloqueia transações fora do price range. Sempre confira o limite superior antes de listar."),
    ]

    for num, titulo, desc in regras:
        rule_data = [[
            Paragraph(f"<b>{num}</b>", ParagraphStyle("rn", fontName="Helvetica-Bold",
                      fontSize=18, textColor=EA_GOLD, alignment=TA_CENTER)),
            Paragraph(f"<b>{titulo}</b><br/><font size=9>{desc}</font>",
                      ParagraphStyle("rt", fontName="Helvetica", fontSize=9.5,
                                     textColor=EA_DARK, leading=14))
        ]]
        rule_tbl = Table(rule_data, colWidths=[14*mm, 156*mm])
        rule_tbl.setStyle(TableStyle([
            ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING",  (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING",   (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
            ("LINEBELOW",    (0, 0), (-1, -1), 0.5, colors.HexColor("#DDDDDD")),
            ("BACKGROUND",   (0, 0), (0, 0),  EA_DARK),
        ]))
        story.append(rule_tbl)

    story.append(Spacer(1, 5*mm))

    # ── 6. DISCLAIMER ─────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1, color=EA_BLUE))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph("<b>DISCLAIMER</b>", styles["bold"]))
    story.append(Paragraph(
        "Este relatório foi gerado por um sistema automatizado de análise de mercado com base em dados "
        "públicos disponíveis em FUTBIN, FUT.GG, TeamGullit, Reddit e fontes jornalísticas especializadas. "
        "Os preços indicados são estimativas baseadas em médias históricas e tendências observadas; "
        "<b>não constituem garantia de lucro</b>. O mercado do EA FC 26 Ultimate Team é volátil e pode "
        "ser impactado por decisões da EA Sports (patches, ajustes de price ranges, SBCs cancelados) "
        "sem aviso prévio. Invista apenas o valor que está disposto a arriscar. O autor não se "
        "responsabiliza por perdas decorrentes das estratégias aqui descritas. "
        "Verifique sempre os preços em tempo real antes de executar qualquer transação.",
        styles["disclaimer"]
    ))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        f"Relatório gerado em {REPORT_DATE} UTC  |  EA FC 26 Trading Analysis System  |  "
        "Budget Referência: 40.000 coins",
        ParagraphStyle("footer", fontName="Helvetica", fontSize=8,
                       textColor=colors.HexColor("#999999"), alignment=TA_CENTER)
    ))

    doc.build(story)
    print(f"PDF gerado: {PDF_FILENAME}")


if __name__ == "__main__":
    build_pdf()
