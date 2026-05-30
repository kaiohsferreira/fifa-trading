#!/usr/bin/env python3
"""Gerador de relatório de trading EA FC 26 Ultimate Team"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak

# ─── Paleta ────────────────────────────────────────────────────────────────────
VERDE_ESCURO   = colors.HexColor("#0D3B1A")
VERDE_MEDIO    = colors.HexColor("#1A6B32")
VERDE_CLARO    = colors.HexColor("#2ECC71")
AMARELO        = colors.HexColor("#F1C40F")
LARANJA        = colors.HexColor("#E67E22")
VERMELHO       = colors.HexColor("#E74C3C")
CINZA_ESCURO   = colors.HexColor("#1C1C1C")
CINZA_MEDIO    = colors.HexColor("#2C2C2C")
CINZA_CLARO    = colors.HexColor("#3D3D3D")
BRANCO         = colors.HexColor("#FFFFFF")
BRANCO_SUAVE   = colors.HexColor("#F0F0F0")
AZUL_DESTAQUE  = colors.HexColor("#3498DB")

# ─── Estilos ────────────────────────────────────────────────────────────────────
def build_styles():
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=BRANCO,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        fontName="Helvetica",
        fontSize=11,
        textColor=VERDE_CLARO,
        alignment=TA_CENTER,
        spaceAfter=2,
    )
    date_style = ParagraphStyle(
        "DateStyle",
        fontName="Helvetica-Bold",
        fontSize=10,
        textColor=AMARELO,
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    section_style = ParagraphStyle(
        "SectionStyle",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=VERDE_CLARO,
        alignment=TA_LEFT,
        spaceBefore=10,
        spaceAfter=4,
        borderPad=4,
    )
    body_style = ParagraphStyle(
        "BodyStyle",
        fontName="Helvetica",
        fontSize=9,
        textColor=BRANCO_SUAVE,
        alignment=TA_JUSTIFY,
        spaceAfter=3,
        leading=14,
    )
    highlight_style = ParagraphStyle(
        "HighlightStyle",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=AMARELO,
        alignment=TA_LEFT,
        spaceAfter=3,
        leading=14,
    )
    disclaimer_style = ParagraphStyle(
        "DisclaimerStyle",
        fontName="Helvetica-Oblique",
        fontSize=7.5,
        textColor=colors.HexColor("#999999"),
        alignment=TA_JUSTIFY,
        spaceAfter=3,
        leading=11,
    )
    rules_header_style = ParagraphStyle(
        "RulesHeaderStyle",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=AMARELO,
        alignment=TA_LEFT,
        spaceAfter=2,
        leading=13,
    )
    rules_body_style = ParagraphStyle(
        "RulesBodyStyle",
        fontName="Helvetica",
        fontSize=8.5,
        textColor=BRANCO_SUAVE,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
        leading=13,
    )
    return {
        "title": title_style,
        "subtitle": subtitle_style,
        "date": date_style,
        "section": section_style,
        "body": body_style,
        "highlight": highlight_style,
        "disclaimer": disclaimer_style,
        "rules_header": rules_header_style,
        "rules_body": rules_body_style,
    }


# ─── Helpers ────────────────────────────────────────────────────────────────────
def hr(color=VERDE_MEDIO, thickness=0.8):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6, spaceBefore=2)


def section_title(text, styles):
    return [
        Spacer(1, 4*mm),
        Paragraph(f"▶  {text}", styles["section"]),
        hr(VERDE_MEDIO, 0.6),
    ]


# ─── Conteúdo ───────────────────────────────────────────────────────────────────
def build_content(styles):
    story = []

    # ── CABEÇALHO ──────────────────────────────────────────────────────────────
    header_data = [
        [Paragraph("⚽  EA FC 26 — RELATÓRIO DE TRADING", styles["title"])],
        [Paragraph("Ultimate Team · Análise de Mercado · Oportunidades de Investimento", styles["subtitle"])],
        [Paragraph("📅  Data: 30/05/2026  |  Hora: 14:06 UTC  |  Budget: 40.000 coins", styles["date"])],
    ]
    header_table = Table(header_data, colWidths=[170*mm])
    header_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), VERDE_ESCURO),
        ("TOPPADDING",   (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
        ("LEFTPADDING",  (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("ROUNDEDCORNERS", [4]),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 6*mm))

    # ── CONTEXTO DO MERCADO ────────────────────────────────────────────────────
    story += section_title("CONTEXTO DO MERCADO — 30/05/2026", styles)

    context_items = [
        ("🔥 Promo Ativa: Prime Heroes",
         "Lançada em 29/05/2026, traz versões lendárias de Heróis com rating 90+. "
         "Destaques: <b>Eden Hazard (96 OVR / LM)</b>, <b>Yaya Touré (96 OVR / CDM)</b> e "
         "<b>Jaap Stam (96 OVR / CB)</b>. Os SBCs do Prime Heroes exigem fodder de alta qualidade "
         "(83–88 rated), criando demanda imediata no mercado de cartas douradas."),

        ("📉 TOTS Ultimate Encerrado",
         "O Ultimate Team of the Season (última semana de TOTS) expirou em 29/05/2026. "
         "Com o fim dos packs do TOTS, jogadores que serviam como fodder estão com preços "
         "deprimidos — janela ideal para compra antecipada."),

        ("📅 Próxima Promo: Festival of Football",
         "Inicia em 05/06/2026 com <b>Path to Glory</b> (cartas ao vivo com Copa do Mundo). "
         "Demanda por fodder 83–87 rated deve aumentar significativamente na semana que vem, "
         "ampliando a janela de lucro das posições abertas hoje."),

        ("📦 SBC Ativa: 82+ Player Pick",
         "Disponível até 01/06/2026 às 18:00 UTC. Custo estimado de 1.800–2.100 coins/pick. "
         "Alta demanda por cartas 82–84 rated como base para a solução mais barata."),

        ("📊 Tendência Geral de Mercado",
         "Preços de 85–87 rated em mínimas pós-TOTS. Janela de compra aberta agora. "
         "Aceleração esperada a partir de domingo (31/05) com demanda pelos SBCs do Prime Heroes. "
         "O ciclo de quinta-feira (rewards de Rivals) já passou, criando excesso de oferta temporário."),
    ]

    for title_txt, desc_txt in context_items:
        row = [[
            Paragraph(f"<b>{title_txt}</b>", ParagraphStyle("ct", fontName="Helvetica-Bold",
                      fontSize=9, textColor=AMARELO, leading=13)),
            Paragraph(desc_txt, ParagraphStyle("cd", fontName="Helvetica",
                      fontSize=8.5, textColor=BRANCO_SUAVE, leading=13, alignment=TA_JUSTIFY)),
        ]]
        t = Table(row, colWidths=[55*mm, 115*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), CINZA_MEDIO),
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING",    (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING",   (0, 0), (-1, -1), 8),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
            ("ROWBACKGROUNDS",(0, 0), (-1, -1), [CINZA_MEDIO]),
            ("BOX",           (0, 0), (-1, -1), 0.5, VERDE_MEDIO),
            ("ROUNDEDCORNERS", [3]),
        ]))
        story.append(t)
        story.append(Spacer(1, 2*mm))

    # ── TABELA DE OPORTUNIDADES ────────────────────────────────────────────────
    story += section_title("TABELA DE CARTAS RECOMENDADAS", styles)

    story.append(Paragraph(
        "Jogadores com melhor relação risco/retorno para o budget de 40.000 coins. "
        "Margem líquida calculada após dedução da taxa EA de 5%. "
        "Preços baseados em dados de mercado de 30/05/2026.",
        ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=8,
                       textColor=colors.HexColor("#AAAAAA"), leading=12, spaceAfter=4)
    ))

    col_headers = ["Jogador", "OVR", "Clube", "Compra\n(coins)", "Venda\n(coins)", "Margem\nLíquida", "ROI\n(líq.)"]
    col_widths   = [38*mm, 12*mm, 36*mm, 22*mm, 22*mm, 22*mm, 18*mm]

    # (nome, ovr, clube, compra, venda)
    players = [
        ("Patrik Schick",      85, "Bayer Leverkusen",  800,   1_700),
        ("Fabián Ruiz",        85, "PSG",                850,   1_900),
        ("Daniel Carvajal",    85, "Real Madrid",        850,   1_850),
        ("Rúben Dias",         86, "Manchester City",    950,   2_200),
        ("Hakan Çalhanoğlu",   86, "Inter Milan",       1_000,  2_500),
        ("Ibrahima Konaté",    86, "Liverpool",          1_000,  2_350),
        ("Declan Rice",        87, "Arsenal",           1_600,  3_400),
        ("Cole Palmer",        87, "Chelsea",           1_600,  3_600),
    ]

    table_data = [col_headers]
    for name, ovr, club, buy, sell in players:
        net = round(sell * 0.95 - buy)
        roi = round((net / buy) * 100)
        roi_str = f"+{roi}%"
        net_str = f"+{net:,}".replace(",", ".")
        buy_str = f"{buy:,}".replace(",", ".")
        sell_str = f"{sell:,}".replace(",", ".")
        table_data.append([name, str(ovr), club, buy_str, sell_str, net_str, roi_str])

    opp_table = Table(table_data, colWidths=col_widths, repeatRows=1)
    opp_table.setStyle(TableStyle([
        # Header
        ("BACKGROUND",    (0, 0), (-1,  0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1,  0), AMARELO),
        ("FONTNAME",      (0, 0), (-1,  0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1,  0), 8),
        ("ALIGN",         (0, 0), (-1,  0), "CENTER"),
        ("VALIGN",        (0, 0), (-1,  0), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1,  0), 6),
        ("BOTTOMPADDING", (0, 0), (-1,  0), 6),
        # Rows
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 8),
        ("TEXTCOLOR",     (0, 1), (-1, -1), BRANCO_SUAVE),
        ("ALIGN",         (1, 1), (-1, -1), "CENTER"),
        ("ALIGN",         (0, 1), ( 0, -1), "LEFT"),
        ("ALIGN",         (2, 1), ( 2, -1), "LEFT"),
        ("VALIGN",        (0, 1), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        # Zebra
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_MEDIO, CINZA_CLARO]),
        # Destaque margem/roi
        ("TEXTCOLOR",     (5, 1), ( 5, -1), VERDE_CLARO),
        ("FONTNAME",      (5, 1), ( 5, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (6, 1), ( 6, -1), VERDE_CLARO),
        ("FONTNAME",      (6, 1), ( 6, -1), "Helvetica-Bold"),
        # Grid
        ("GRID",          (0, 0), (-1, -1), 0.4, VERDE_MEDIO),
        ("LINEBELOW",     (0, 0), (-1,  0), 1.2, VERDE_CLARO),
    ]))
    story.append(opp_table)

    # legenda abaixo da tabela
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "* Margem Líquida = Preço Venda × 0,95 − Preço Compra  |  ROI = Retorno sobre o investimento após taxa EA",
        ParagraphStyle("leg", fontName="Helvetica-Oblique", fontSize=7.5,
                       textColor=colors.HexColor("#888888"), leading=11, spaceAfter=2)
    ))

    # ── ESTRATÉGIA DE TIMING ──────────────────────────────────────────────────
    story += section_title("ESTRATÉGIA DE TIMING", styles)

    timing_rows = [
        ("🟢 AGORA\n30/05 – 14:00 UTC", VERDE_MEDIO,
         "Janela de compra ideal. Preços de fodder 85–87 rated em mínimas pós-TOTS + pós-Quinta-feira. "
         "Compre em lotes de 5–10 cartas por jogador. Distribua o budget: 40% em 85-rated (Schick/Ruiz/Carvajal), "
         "40% em 86-rated (Dias/Çalhanoğlu/Konaté) e 20% em 87-rated (Rice/Palmer)."),
        ("🟡 DOMINGO\n31/05 – 10:00 UTC", AMARELO,
         "Reavalie posições. Se cartas 87-rated já subiram ≥40%, venda metade da posição para garantir lucro. "
         "Monitore o surgimento de novos SBCs Prime Heroes — qualquer novo SBC com requisito 86+ dispara a demanda."),
        ("🔴 SEGUNDA-FEIRA\n01/06 – 18:00 UTC", LARANJA,
         "Expiry do SBC 82+ Player Pick (18:00 UTC). Antes do prazo, demanda por 82–84 rated aumenta. "
         "Venda os 85–87 rated restantes. Reinvista lucros em cartas 83-rated para o SBC final se ainda ativo."),
        ("🔵 JANELA EXTRA\n04/06 – pré-Festival", AZUL_DESTAQUE,
         "Antes do Festival of Football (05/06), cartas Premier League e La Liga 85-87 rated tendem a subir "
         "com especulação de Path to Glory. Posições não vendidas até segunda podem ser mantidas como "
         "investimento de médio prazo até 05/06."),
    ]

    for timing_label, label_color, timing_desc in timing_rows:
        row = [[
            Paragraph(timing_label, ParagraphStyle("tl", fontName="Helvetica-Bold",
                      fontSize=8, textColor=label_color, leading=12, alignment=TA_CENTER)),
            Paragraph(timing_desc, ParagraphStyle("td", fontName="Helvetica",
                      fontSize=8.5, textColor=BRANCO_SUAVE, leading=13, alignment=TA_JUSTIFY)),
        ]]
        t = Table(row, colWidths=[32*mm, 138*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (0,  0), CINZA_ESCURO),
            ("BACKGROUND",    (1, 0), (1,  0), CINZA_MEDIO),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LEFTPADDING",   (0, 0), (-1, -1), 8),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
            ("BOX",           (0, 0), (-1, -1), 0.5, VERDE_MEDIO),
            ("LINEBEFORE",    (1, 0), (1,  0), 1.5, label_color),
        ]))
        story.append(t)
        story.append(Spacer(1, 1.5*mm))

    # ── ESTIMATIVA DE RETORNO 48H ─────────────────────────────────────────────
    story += section_title("ESTIMATIVA DE RETORNO EM 48H", styles)

    strategy_rows = [
        ["Alocação", "85-rated (Schick/Ruiz/Carvajal)", "86-rated (Dias/Çalh./Konaté)", "87-rated (Rice/Palmer)"],
        ["Budget",   "16.000 coins (~19 cartas)",        "14.000 coins (~14 cartas)",    "10.000 coins (~6 cartas)"],
        ["Conserv.", "+5.500 coins  (+34%)",             "+5.200 coins  (+37%)",          "+3.800 coins  (+38%)"],
        ["Otimista", "+9.000 coins  (+56%)",             "+8.500 coins  (+61%)",          "+6.500 coins  (+65%)"],
    ]

    ret_table = Table(strategy_rows, colWidths=[28*mm, 48*mm, 52*mm, 42*mm])
    ret_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1,  0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1,  0), AMARELO),
        ("FONTNAME",      (0, 0), (-1,  0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("FONTNAME",      (0, 1), ( 0, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0, 1), ( 0, -1), BRANCO_SUAVE),
        ("TEXTCOLOR",     (1, 3), (-1,  3), VERDE_CLARO),
        ("FONTNAME",      (1, 3), (-1,  3), "Helvetica-Bold"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [CINZA_MEDIO, CINZA_CLARO, CINZA_MEDIO]),
        ("GRID",          (0, 0), (-1, -1), 0.4, VERDE_MEDIO),
        ("LINEBELOW",     (0, 0), (-1,  0), 1.2, VERDE_CLARO),
    ]))
    story.append(ret_table)

    # Resumo consolidado
    story.append(Spacer(1, 3*mm))
    summary_data = [
        [Paragraph("CONSOLIDADO 48H", ParagraphStyle("sh", fontName="Helvetica-Bold",
                   fontSize=9, textColor=AMARELO, alignment=TA_CENTER)),
         Paragraph("Conservador", ParagraphStyle("sl", fontName="Helvetica-Bold",
                   fontSize=9, textColor=BRANCO_SUAVE, alignment=TA_CENTER)),
         Paragraph("Otimista", ParagraphStyle("sl2", fontName="Helvetica-Bold",
                   fontSize=9, textColor=BRANCO_SUAVE, alignment=TA_CENTER))],
        [Paragraph("Total investido: 40.000 coins", ParagraphStyle("sv", fontName="Helvetica",
                   fontSize=8.5, textColor=BRANCO_SUAVE, alignment=TA_CENTER)),
         Paragraph("+14.500 coins\n(+36%)", ParagraphStyle("sc", fontName="Helvetica-Bold",
                   fontSize=11, textColor=VERDE_CLARO, alignment=TA_CENTER, leading=16)),
         Paragraph("+24.000 coins\n(+60%)", ParagraphStyle("so", fontName="Helvetica-Bold",
                   fontSize=11, textColor=AMARELO, alignment=TA_CENTER, leading=16))],
    ]
    sum_table = Table(summary_data, colWidths=[60*mm, 55*mm, 55*mm])
    sum_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), CINZA_ESCURO),
        ("BACKGROUND",    (1, 1), (1,  1),  CINZA_MEDIO),
        ("BACKGROUND",    (2, 1), (2,  1),  CINZA_MEDIO),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("BOX",           (0, 0), (-1, -1), 1.2, VERDE_CLARO),
        ("GRID",          (0, 0), (-1, -1), 0.4, VERDE_MEDIO),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("SPAN",          (0, 0), (0,  1)),
        ("LINEAFTER",     (0, 0), (0, -1), 0.8, VERDE_MEDIO),
    ]))
    story.append(sum_table)

    # ── 8 REGRAS DE OURO ─────────────────────────────────────────────────────
    story += section_title("8 REGRAS DE OURO DO TRADE", styles)

    rules = [
        ("1. Nunca invista 100% do budget em uma única carta.",
         "Diversifique em pelo menos 3–4 jogadores diferentes para diluir o risco de "
         "crash de preço ou bloqueio de price range."),
        ("2. Respeite o price range da EA.",
         "Antes de comprar, verifique o price range atual no FUTBIN/FUT.GG. "
         "Cartas próximas ao teto do range têm espaço limitado de valorização."),
        ("3. Compre na madrugada, venda no horário nobre.",
         "O pico de jogadores online é entre 18:00–22:00 UTC (Europa). "
         "Comprar fora do horário de pico garante melhores preços de entrada."),
        ("4. Monitore SBCs a cada 2–3 horas.",
         "Novos SBCs criam picos de demanda em minutos. Use FUTBIN e FUT.GG "
         "com notificações ativas para reagir rápido."),
        ("5. Nunca venda no lançamento de uma nova promo.",
         "Nos primeiros 30–60 minutos após um lançamento, os preços são instáveis. "
         "Aguarde a estabilização antes de colocar cartas à venda."),
        ("6. Defina stop-loss antes de comprar.",
         "Se uma carta cair 20% abaixo do preço de compra, venda imediatamente. "
         "Perder 20% é recuperável; perder 60% não é."),
        ("7. Nunca faça holding em véspera de fim de evento.",
         "Nas últimas 24h de uma promo, os preços de fodder colapsam com o excesso "
         "de oferta. Liquide posições com 48h de antecedência."),
        ("8. Registre todas as operações.",
         "Anote compra, venda, lucro/prejuízo por carta. Sem dados históricos, "
         "você repete os mesmos erros e não consegue otimizar a estratégia."),
    ]

    for rule_title, rule_desc in rules:
        row = [[
            Paragraph(rule_title, ParagraphStyle("rh", fontName="Helvetica-Bold",
                      fontSize=8.5, textColor=AMARELO, leading=13)),
            Paragraph(rule_desc, ParagraphStyle("rb", fontName="Helvetica",
                      fontSize=8.5, textColor=BRANCO_SUAVE, leading=13, alignment=TA_JUSTIFY)),
        ]]
        t = Table(row, colWidths=[65*mm, 105*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), CINZA_MEDIO),
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING",    (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING",   (0, 0), (-1, -1), 8),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
            ("BOX",           (0, 0), (-1, -1), 0.4, VERDE_MEDIO),
            ("LINEBEFORE",    (0, 0), (0,  0), 2.5, AMARELO),
        ]))
        story.append(t)
        story.append(Spacer(1, 1.5*mm))

    # ── DISCLAIMER ────────────────────────────────────────────────────────────
    story += section_title("DISCLAIMER", styles)

    disclaimer_text = (
        "Este relatório é gerado exclusivamente para fins informativos e educativos sobre trading no EA FC 26 Ultimate Team. "
        "As informações aqui contidas foram obtidas a partir de fontes públicas disponíveis na internet, incluindo FUTBIN, "
        "FUT.GG, Team Gullit, Sportskeeda, Dexerto e outros portais especializados no jogo. "
        "Nenhuma das informações presentes neste documento constitui conselho financeiro ou garantia de lucro. "
        "O mercado do FUT é volátil e imprevisível: preços podem variar drasticamente em minutos, bloqueios de price range "
        "podem ser aplicados pela EA a qualquer momento, e eventos inesperados podem alterar completamente o cenário de mercado. "
        "O autor/gerador deste relatório não se responsabiliza por perdas de coins decorrentes de decisões tomadas com base "
        "neste documento. Invista apenas o que você pode se dar ao luxo de perder dentro do jogo. "
        "EA Sports FC 26, Ultimate Team e todos os nomes relacionados são marcas registradas da Electronic Arts Inc. "
        "Este relatório não tem afiliação oficial com a EA Sports."
    )
    story.append(Paragraph(disclaimer_text, styles["disclaimer"]))

    # ── RODAPÉ ────────────────────────────────────────────────────────────────
    story.append(Spacer(1, 4*mm))
    story.append(hr(VERDE_MEDIO, 0.5))
    footer_data = [[
        Paragraph("⚽ EA FC 26 Trading Bot · github.com/kaiohsferreira/fifa-trading",
                  ParagraphStyle("ft", fontName="Helvetica", fontSize=7,
                                 textColor=colors.HexColor("#666666"), alignment=TA_CENTER)),
        Paragraph("Gerado em 30/05/2026 às 14:06 UTC",
                  ParagraphStyle("ftd", fontName="Helvetica", fontSize=7,
                                 textColor=colors.HexColor("#666666"), alignment=TA_CENTER)),
    ]]
    ft = Table(footer_data, colWidths=[100*mm, 70*mm])
    ft.setStyle(TableStyle([
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(ft)

    return story


# ─── Main ────────────────────────────────────────────────────────────────────────
def main():
    filename = "relatorio-trading-2026-05-30-14h.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=18*mm,
        rightMargin=18*mm,
        topMargin=16*mm,
        bottomMargin=14*mm,
        title="Relatório de Trading EA FC 26 — 30/05/2026",
        author="EA FC 26 Trading Bot",
    )

    styles = build_styles()

    def background_canvas(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(CINZA_ESCURO)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.restoreState()

    story = build_content(styles)
    doc.build(story, onFirstPage=background_canvas, onLaterPages=background_canvas)
    print(f"PDF gerado: {filename}")


if __name__ == "__main__":
    main()
