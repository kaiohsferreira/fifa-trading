#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

OUTPUT_FILE = "relatorio-trading-2026-06-05-20h.pdf"
REPORT_DATE = "05/06/2026 20:04"
REPORT_DATE_UTC = "05/06/2026 20:04 UTC"

# ─── Colours ──────────────────────────────────────────────────────────────────
GREEN_DARK  = colors.HexColor("#1a7a2e")
GREEN_MID   = colors.HexColor("#28a745")
GREEN_LIGHT = colors.HexColor("#d4edda")
GOLD        = colors.HexColor("#ffc107")
DARK_BG     = colors.HexColor("#1a1a2e")
CARD_BG     = colors.HexColor("#16213e")
WHITE       = colors.white
GREY_LIGHT  = colors.HexColor("#f8f9fa")
GREY_MID    = colors.HexColor("#dee2e6")
RED_DARK    = colors.HexColor("#c0392b")
ORANGE      = colors.HexColor("#e67e22")

# ─── Styles ───────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = S("ReportTitle",
    fontSize=26, leading=32, textColor=WHITE,
    alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=4)

subtitle_style = S("Subtitle",
    fontSize=13, leading=17, textColor=GOLD,
    alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=2)

datetime_style = S("DateTime",
    fontSize=10, leading=13, textColor=colors.HexColor("#adb5bd"),
    alignment=TA_CENTER, fontName="Helvetica", spaceAfter=2)

section_header = S("SectionHeader",
    fontSize=14, leading=18, textColor=WHITE,
    fontName="Helvetica-Bold", spaceAfter=6, spaceBefore=14,
    backColor=GREEN_DARK, leftIndent=-8, rightIndent=-8,
    borderPad=6)

sub_header = S("SubHeader",
    fontSize=11, leading=15, textColor=GREEN_DARK,
    fontName="Helvetica-Bold", spaceAfter=4, spaceBefore=8)

body_style = S("Body",
    fontSize=9.5, leading=14, textColor=colors.HexColor("#212529"),
    fontName="Helvetica", spaceAfter=4, alignment=TA_JUSTIFY)

bullet_style = S("Bullet",
    fontSize=9.5, leading=14, textColor=colors.HexColor("#212529"),
    fontName="Helvetica", spaceAfter=3, leftIndent=16,
    firstLineIndent=-10)

highlight_style = S("Highlight",
    fontSize=10, leading=14, textColor=DARK_BG,
    fontName="Helvetica-Bold", spaceAfter=3)

disclaimer_style = S("Disclaimer",
    fontSize=8, leading=11, textColor=colors.HexColor("#6c757d"),
    fontName="Helvetica", spaceAfter=3, alignment=TA_JUSTIFY)

rule_style = S("Rule",
    fontSize=9.5, leading=14, textColor=colors.HexColor("#212529"),
    fontName="Helvetica", spaceAfter=5, leftIndent=20,
    firstLineIndent=-14)

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        rightMargin=1.8*cm, leftMargin=1.8*cm,
        topMargin=2*cm, bottomMargin=2*cm,
        title="Relatório de Trading EA FC 26",
        author="Agente de Mercado UT",
    )

    story = []

    # ── HEADER BLOCK ──────────────────────────────────────────────────────────
    header_data = [[
        Paragraph("⚽ RELATÓRIO DE TRADING", title_style),
    ]]
    header_table = Table(header_data, colWidths=[doc.width])
    header_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_BG),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ("ROUNDEDCORNERS", [6]),
    ]))
    story.append(header_table)

    sub_data = [[
        Paragraph("EA FC 26 Ultimate Team — Festival of Football 2026", subtitle_style),
    ]]
    sub_table = Table(sub_data, colWidths=[doc.width])
    sub_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_BG),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
    ]))
    story.append(sub_table)

    date_data = [[
        Paragraph(f"Gerado em: {REPORT_DATE_UTC}  |  Budget: 40.000 coins  |  Plataforma: PS5 / Xbox", datetime_style),
    ]]
    date_table = Table(date_data, colWidths=[doc.width])
    date_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
    ]))
    story.append(date_table)
    story.append(Spacer(1, 10))

    # ── SECTION 1: CONTEXTO DE MERCADO ────────────────────────────────────────
    story.append(section_header_box("1. CONTEXTO DO MERCADO ATUAL", doc))
    story.append(Spacer(1, 4))

    story.append(Paragraph('<b>Evento Ativo:</b> Festival of Football — Fase Path to Glory', sub_header))

    ctx_bullets = [
        ("🏆", "Festival of Football lançado HOJE (05/06/2026 às 19h BST). Mega-evento temático Copa do Mundo 2026 com 6 semanas de promos consecutivas."),
        ("⚡", "Path to Glory (PTG) ativo: 05/06 – 19/06. Cartas dinâmicas que upgradiam automaticamente toda quarta-feira conforme a seleção avança no Mundial."),
        ("🔥", "Shapeshifters começa em 12/06 (7 dias). Jogadores trocam de posição radicalmente — demanda por SBC alta e fodder vai valorizar MUITO antes do lançamento."),
        ("🎁", "Pelé 93 OVR gratuito (untradeable) para todos que logarem até 24/07. NÃO mexe no preço de cartas tradeáveis."),
        ("📉", "Mercado em queda nas primeiras 24-48h pós-lançamento de PTG: packs abertos → suply alto → preço de fodder baixo. MOMENTO IDEAL PARA COMPRAR."),
        ("⚽", "Copa do Mundo 2026 começa em 11/06. Jogadores de seleções fortes (Brasil, França, Argentina, Inglaterra, Espanha) terão upgrades semanais toda quarta-feira."),
        ("🚫", "TOTW encerrado no TOTW 30 (15/04). Sem novos drops de quinta-feira — foco total em PTG e Shapeshifters."),
        ("💡", "SBCs ativos relevantes: 10x 84+ Upgrade (expira 12/06), 1 of 3 83+ Nations Player Pick (expira 12/06), Grind Upgrade (3x), Provisions Upgrade."),
    ]
    for icon, text in ctx_bullets:
        story.append(Paragraph(f'{icon}  {text}', bullet_style))

    story.append(Spacer(1, 8))

    # ── TREND BOX ─────────────────────────────────────────────────────────────
    trend_data = [[
        Paragraph(
            '<b>TENDÊNCIA GERAL:</b> Mercado volátil e em QUEDA nos próximos 2 dias por abertura de packs. '
            'É o melhor momento do mês para comprar fodder barato. '
            'Shapeshifters (12/06) vai provocar spike de preços — comprar agora para vender em 7 dias.',
            body_style)
    ]]
    trend_table = Table(trend_data, colWidths=[doc.width])
    trend_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), GREEN_LIGHT),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("BOX",           (0, 0), (-1, -1), 1.5, GREEN_MID),
    ]))
    story.append(trend_table)
    story.append(Spacer(1, 10))

    # ── SECTION 2: TABELA DE OPORTUNIDADES ────────────────────────────────────
    story.append(section_header_box("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA", doc))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        'Todas as margens são calculadas após a taxa de 5% da EA (vendedor recebe 95% do preço de venda). '
        'Preços de referência: PS5 / Xbox — 05/06/2026.',
        body_style))
    story.append(Spacer(1, 6))

    # Table headers
    col_widths = [3.8*cm, 1.4*cm, 3.5*cm, 2.4*cm, 2.4*cm, 2.6*cm]
    table_header = [
        Paragraph('<b>Jogador</b>', ParagraphStyle("TH", fontSize=8.5, fontName="Helvetica-Bold",
                  textColor=WHITE, alignment=TA_CENTER)),
        Paragraph('<b>OVR</b>', ParagraphStyle("TH", fontSize=8.5, fontName="Helvetica-Bold",
                  textColor=WHITE, alignment=TA_CENTER)),
        Paragraph('<b>Clube / Seleção</b>', ParagraphStyle("TH", fontSize=8.5, fontName="Helvetica-Bold",
                  textColor=WHITE, alignment=TA_CENTER)),
        Paragraph('<b>Compra\n(máx.)</b>', ParagraphStyle("TH", fontSize=8.5, fontName="Helvetica-Bold",
                  textColor=WHITE, alignment=TA_CENTER)),
        Paragraph('<b>Venda\n(alvo)</b>', ParagraphStyle("TH", fontSize=8.5, fontName="Helvetica-Bold",
                  textColor=WHITE, alignment=TA_CENTER)),
        Paragraph('<b>Margem\nLíquida</b>', ParagraphStyle("TH", fontSize=8.5, fontName="Helvetica-Bold",
                  textColor=GOLD, alignment=TA_CENTER)),
    ]

    ps = ParagraphStyle("TC", fontSize=8, fontName="Helvetica",
                        textColor=colors.HexColor("#212529"), alignment=TA_CENTER, leading=11)
    ps_green = ParagraphStyle("TCG", fontSize=8.5, fontName="Helvetica-Bold",
                              textColor=GREEN_DARK, alignment=TA_CENTER, leading=11)
    ps_left = ParagraphStyle("TCL", fontSize=8, fontName="Helvetica",
                             textColor=colors.HexColor("#212529"), alignment=TA_LEFT, leading=11)

    # (Jogador, OVR, Clube/Seleção, Compra, Venda, Margem_líquida, nota_interna)
    players = [
        # ── SBC FODDER — FLIP PARA SHAPESHIFTERS ──
        ("Patrik Schick", "85", "Leverkusen / República Tcheca", "1.400", "2.200", "+690", "LIME"),
        ("Keira Walsh", "85", "Barcelona / Inglaterra", "1.300", "2.100", "+695", "LIME"),
        ("Manuela Giugliano", "85", "Roma / Itália", "1.200", "2.000", "+700", "LIME"),
        ("Sergej Milinković-Savić", "84", "Al-Hilal / Sérvia", "1.100", "1.900", "+705", "LIME"),
        ("Alex Greenwood", "84", "Man City / Inglaterra", "1.000", "1.750", "+663", "LIME"),
        ("Emily Fox", "84", "Arsenal / EUA", "1.000", "1.750", "+663", "LIME"),
        ("Giovanna Hoffmann", "83", "Wolfsburg / Alemanha", "900", "1.600", "+620", "LIME"),
        ("Perle Morroni", "83", "Lyon / França", "900", "1.600", "+620", "LIME"),
        # ── PATH TO GLORY — INVEST ANTES UPGRADES ──
        ("Cody Gakpo PTG", "95", "Liverpool / Holanda", "400.000", "600.000", "+170.000", "GOLD"),
        ("Alphonso Davies PTG", "95", "Bayern Munich / Canadá", "550.000", "800.000", "+210.000", "GOLD"),
        ("Ronald Araújo PTG", "94", "Barcelona / Uruguai", "680.000", "950.000", "+222.500", "GOLD"),
        # ── EVOLUTION FODDER — MERCADO CAÍDO ──
        ("Edinson Cavani EVO", "86", "SFC / Uruguai (evo base)", "3.500", "6.000", "+2.200", "ORANGE"),
        ("Adam Ounas EVO", "86", "Nice / Argélia (evo base)", "3.200", "5.500", "+2.025", "ORANGE"),
    ]

    table_data = [table_header]
    row_colors = []
    for i, (jogador, ovr, clube, compra, venda, margem, cat) in enumerate(players, start=1):
        row = [
            Paragraph(jogador, ps_left),
            Paragraph(ovr, ps),
            Paragraph(clube, ps_left),
            Paragraph(compra, ps),
            Paragraph(venda, ps),
            Paragraph(margem, ps_green),
        ]
        table_data.append(row)
        if cat == "LIME":
            row_colors.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#f0fff4")))
        elif cat == "GOLD":
            row_colors.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#fffde7")))
        elif cat == "ORANGE":
            row_colors.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#fff3e0")))

    tbl_style = [
        ("BACKGROUND",    (0, 0), (-1, 0), DARK_BG),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [GREY_LIGHT, WHITE]),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8.5),
        ("GRID",          (0, 0), (-1, -1), 0.5, GREY_MID),
        ("BOX",           (0, 0), (-1, -1), 1.5, GREEN_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ] + row_colors

    player_table = Table(table_data, colWidths=col_widths, repeatRows=1)
    player_table.setStyle(TableStyle(tbl_style))
    story.append(player_table)

    story.append(Spacer(1, 6))

    # Legend
    legend_data = [[
        Paragraph("🟢 Verde = SBC Fodder Flip (baixo risco, alta rotatividade)", disclaimer_style),
        Paragraph("🟡 Amarelo = Path to Glory invest (médio risco, alto retorno)", disclaimer_style),
        Paragraph("🟠 Laranja = Evolution card flip (médio risco)", disclaimer_style),
    ]]
    legend_table = Table(legend_data, colWidths=[doc.width/3]*3)
    legend_table.setStyle(TableStyle([
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
    ]))
    story.append(legend_table)
    story.append(Spacer(1, 10))

    # ── SECTION 3: ESTRATÉGIA DE TIMING ───────────────────────────────────────
    story.append(section_header_box("3. ESTRATÉGIA DE TIMING", doc))
    story.append(Spacer(1, 6))

    timing_data = [
        ["Período", "Ação", "Justificativa"],
        ["AGORA\n(05/06 – 06/06)", "COMPRAR fodder 83-85 OVR\nem massa", "Packs abertos → supply alto → preço em baixa. Janela de 24-48h mais barata do mês."],
        ["06/06 – 08/06\n(+48h PTG)", "COMPRAR PTG baratos\n(Gakpo, Davies, Araújo)", "Preços de PTG estabilizam 48-72h após o lançamento. Evitar comprar no dia 1."],
        ["08/06 – 11/06\n(Pré-Copa)", "SEGURAR tudo.\nMonitorar tracker", "Mundial começa 11/06. Mercado aquece com expectativa. Aguardar primeiro resultado."],
        ["11/06 – 12/06\n(Quarta pós-jogo)", "VENDER PTG de seleções\nque venceram rodada 1", "Upgrades processam na quarta. Vender antes do próximo jogo enquanto hype está alto."],
        ["12/06\n(Shapeshifters Day)", "VENDER todo o\nfodder 83-85 OVR", "Shapeshifters lança → SBCs aparecem → spike de 40-80% no preço do fodder. Janela de 30-60min."],
        ["12/06 – 19/06\n(durante PTG)", "Repetir ciclo\nfodder + PTG", "Novas SBCs aparecem a cada 2-3 dias. Monitorar futmind.com e futbin.com para agir rápido."],
    ]

    timing_col_widths = [2.8*cm, 3.8*cm, doc.width - 6.6*cm]
    ts_header_style = ParagraphStyle("TSH", fontSize=8.5, fontName="Helvetica-Bold",
                                      textColor=WHITE, alignment=TA_CENTER, leading=11)
    ts_body_style = ParagraphStyle("TSB", fontSize=8, fontName="Helvetica",
                                    textColor=colors.HexColor("#212529"), alignment=TA_LEFT, leading=11)
    ts_data_fmt = []
    for i, row in enumerate(timing_data):
        if i == 0:
            ts_data_fmt.append([Paragraph(c, ts_header_style) for c in row])
        else:
            ts_data_fmt.append([Paragraph(c, ts_body_style) for c in row])

    timing_table = Table(ts_data_fmt, colWidths=timing_col_widths, repeatRows=1)
    timing_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), DARK_BG),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [GREY_LIGHT, WHITE]),
        ("ALIGN",         (0, 0), (0, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",          (0, 0), (-1, -1), 0.5, GREY_MID),
        ("BOX",           (0, 0), (-1, -1), 1.5, GREEN_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 1), (-1, -1), 6),
        ("BACKGROUND",    (0, 1), (0, -1), colors.HexColor("#e8f5e9")),
        ("FONTNAME",      (0, 1), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 1), (0, -1), 8),
    ]))
    story.append(timing_table)
    story.append(Spacer(1, 10))

    # ── SECTION 4: ESTIMATIVA DE RETORNO 48H ──────────────────────────────────
    story.append(section_header_box("4. ESTIMATIVA DE RETORNO EM 48H", doc))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Budget disponível: 40.000 coins", sub_header))

    # Budget allocation
    alloc_data = [
        ["Estratégia", "Alocação", "Coins", "Cenário Conservador (+)", "Cenário Otimista (+)"],
        ["SBC Fodder Flip\n83-85 OVR", "50%", "20.000", "+6.000 a +8.000", "+10.000 a +14.000"],
        ["Path to Glory\nGakpo / Davies", "35%", "14.000", "+3.500 a +5.000", "+7.000 a +12.000"],
        ["Evolution Cards\n(evo base flip)", "15%", "6.000", "+1.500 a +2.500", "+3.000 a +5.000"],
        ["TOTAL", "100%", "40.000", "+11.000 a +15.500", "+20.000 a +31.000"],
    ]

    alloc_col_widths = [3.5*cm, 2.0*cm, 2.2*cm, 4.5*cm, 4.5*cm]
    alloc_header_s = ParagraphStyle("AH", fontSize=8.5, fontName="Helvetica-Bold",
                                     textColor=WHITE, alignment=TA_CENTER, leading=11)
    alloc_body_s = ParagraphStyle("AB", fontSize=8.5, fontName="Helvetica",
                                   textColor=colors.HexColor("#212529"), alignment=TA_CENTER, leading=11)
    alloc_body_left = ParagraphStyle("ABL", fontSize=8.5, fontName="Helvetica",
                                      textColor=colors.HexColor("#212529"), alignment=TA_LEFT, leading=11)
    alloc_bold_s = ParagraphStyle("ABS", fontSize=9, fontName="Helvetica-Bold",
                                   textColor=DARK_BG, alignment=TA_CENTER, leading=12)

    alloc_fmt = []
    for i, row in enumerate(alloc_data):
        if i == 0:
            alloc_fmt.append([Paragraph(c, alloc_header_s) for c in row])
        elif i == len(alloc_data) - 1:
            alloc_fmt.append([Paragraph(c, alloc_bold_s) for c in row])
        else:
            alloc_fmt.append([
                Paragraph(row[0], alloc_body_left),
                Paragraph(row[1], alloc_body_s),
                Paragraph(row[2], alloc_body_s),
                Paragraph(row[3], ParagraphStyle("ABG", fontSize=8.5, fontName="Helvetica",
                                                  textColor=GREEN_DARK, alignment=TA_CENTER, leading=11)),
                Paragraph(row[4], ParagraphStyle("ABO", fontSize=8.5, fontName="Helvetica-Bold",
                                                  textColor=GREEN_DARK, alignment=TA_CENTER, leading=11)),
            ])

    alloc_table = Table(alloc_fmt, colWidths=alloc_col_widths, repeatRows=1)
    alloc_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), DARK_BG),
        ("BACKGROUND",    (0, -1), (-1, -1), colors.HexColor("#1a7a2e")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [GREY_LIGHT, WHITE]),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",          (0, 0), (-1, -1), 0.5, GREY_MID),
        ("BOX",           (0, 0), (-1, -1), 1.5, GREEN_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("TEXTCOLOR",     (0, -1), (-1, -1), WHITE),
    ]))
    story.append(alloc_table)
    story.append(Spacer(1, 6))

    # Return summary box
    return_data = [[
        Paragraph(
            '<b>Retorno esperado em 48h:</b>  '
            'Conservador: +11.000 a +15.500 coins (27%-38%)  |  '
            'Otimista: +20.000 a +31.000 coins (50%-77%)<br/>'
            '<font color="#6c757d" size="8">*Cenário otimista assume Shapeshifters SBC pesado em 12/06 '
            'e Holanda + Canadá vencendo na Copa. Cenário conservador assume SBCs normais e 1 upgrade de PTG.</font>',
            body_style)
    ]]
    rt = Table(return_data, colWidths=[doc.width])
    rt.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), colors.HexColor("#e8f5e9")),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("BOX",           (0, 0), (-1, -1), 1.5, GREEN_MID),
    ]))
    story.append(rt)
    story.append(Spacer(1, 10))

    # ── SECTION 5: 8 REGRAS DE OURO ───────────────────────────────────────────
    story.append(section_header_box("5. AS 8 REGRAS DE OURO DO TRADE", doc))
    story.append(Spacer(1, 6))

    rules = [
        ("01", "NUNCA COMPRE NO HYPE DO LANÇAMENTO",
         "Os primeiros 24h de qualquer promo = preços inflados. Aguarde 48-72h para os preços estabilizarem."),
        ("02", "COMPRE NA QUINTA E DOMINGO",
         "Quinta = Rewards Rivals. Domingo = fim da Weekend League. Mais suply, menos demanda → preços caem. São as melhores janelas de compra."),
        ("03", "VENDA ANTES DO SPIKE MÁXIMO",
         "Venda quando o preço SUBIR, não quando atingir o pico. O pico é impossível de prever. Lucro realizado > lucro teórico."),
        ("04", "DIVERSIFIQUE — NUNCA ALL-IN",
         "Máximo 40-50% do budget em uma única estratégia. Distribua entre fodder (baixo risco), PTG (médio) e evolução (médio)."),
        ("05", "CALCULE SEMPRE A MARGEM COM 5% DE TAXA",
         "Preço de venda × 0.95 = coins que você recebe. Margem mínima aceitável: +15% sobre o preço de compra."),
        ("06", "USE FILTROS DE SNIPE NO WEB APP",
         "Configure filtro: OVR 83-85, Gold, preço máximo = seu alvo de compra. Compre abaixo do mercado e venda pelo preço de mercado."),
        ("07", "MONITORE LEAKS DE SBC",
         "Siga futmind.com, futbin.com e reddit r/FIFA. Quando um SBC pesado for anunciado, compre fodder ANTES — minutos fazem diferença."),
        ("08", "SEGURE CARDS PTG ATÉ QUARTA-FEIRA",
         "Upgrades de Path to Glory processam toda quarta-feira. Venda PTG de quinta a sábado, quando o hype do upgrade ainda está fresco."),
    ]

    rule_cols = [1.2*cm, 4.0*cm, doc.width - 5.2*cm]
    rule_rows = []
    num_s = ParagraphStyle("RN", fontSize=14, fontName="Helvetica-Bold",
                            textColor=GOLD, alignment=TA_CENTER, leading=18)
    rule_title_s = ParagraphStyle("RT", fontSize=9.5, fontName="Helvetica-Bold",
                                   textColor=GREEN_DARK, alignment=TA_LEFT, leading=13)
    rule_body_s = ParagraphStyle("RB", fontSize=9, fontName="Helvetica",
                                  textColor=colors.HexColor("#212529"), alignment=TA_JUSTIFY, leading=12)

    for num, title, desc in rules:
        rule_rows.append([
            Paragraph(num, num_s),
            Paragraph(title, rule_title_s),
            Paragraph(desc, rule_body_s),
        ])

    rules_table = Table(rule_rows, colWidths=rule_cols)
    rules_style = [
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",          (0, 0), (-1, -1), 0.4, GREY_MID),
        ("BOX",           (0, 0), (-1, -1), 1.5, GREEN_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("BACKGROUND",    (0, 0), (0, -1), DARK_BG),
    ]
    for i in range(len(rules)):
        bg = GREY_LIGHT if i % 2 == 0 else WHITE
        rules_style.append(("BACKGROUND", (1, i), (-1, i), bg))

    rules_table.setStyle(TableStyle(rules_style))
    story.append(rules_table)
    story.append(Spacer(1, 10))

    # ── SECTION 6: DISCLAIMER ─────────────────────────────────────────────────
    story.append(section_header_box("6. DISCLAIMER", doc))
    story.append(Spacer(1, 6))

    disclaimer_paragraphs = [
        "Este relatório foi gerado automaticamente por um agente de análise de mercado com base em dados coletados de fontes públicas (FUTBIN, FUT.GG, FUTMind, RealSport101, FIFAUTeam, ItemD2R, EZG e outras) em 05/06/2026.",
        "Os preços e margens apresentados são estimativas baseadas nas condições de mercado observadas no momento da geração do relatório. O mercado do EA FC 26 Ultimate Team é extremamente volátil e os preços podem variar significativamente em minutos.",
        "Investimentos em cartas de Path to Glory são de risco moderado-alto. O retorno depende diretamente do desempenho da seleção nacional no Mundial de 2026, que é imprevisível. Não há garantia de upgrades além do primeiro.",
        "O retorno estimado em 48h é uma projeção baseada em padrões históricos de mercado e nas condições atuais. Resultados reais podem ser superiores ou inferiores ao estimado. Nunca invista mais coins do que está disposto a perder.",
        "Este documento não constitui aconselhamento financeiro. É destinado exclusivamente ao entretenimento e à melhoria da experiência de jogo no EA FC 26 Ultimate Team. EA Sports, EA FC e Ultimate Team são marcas registradas da Electronic Arts Inc.",
    ]
    for para in disclaimer_paragraphs:
        story.append(Paragraph(para, disclaimer_style))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1, color=GREY_MID))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        f'Relatório gerado em {REPORT_DATE_UTC} — EA FC 26 Ultimate Team Trading Agent',
        ParagraphStyle("Footer", fontSize=7.5, fontName="Helvetica",
                       textColor=colors.HexColor("#adb5bd"), alignment=TA_CENTER)
    ))

    doc.build(story)
    print(f"PDF gerado: {OUTPUT_FILE}")


def section_header_box(text, doc):
    data = [[Paragraph(text, ParagraphStyle(
        "SHB", fontSize=12, fontName="Helvetica-Bold",
        textColor=WHITE, leading=16, alignment=TA_LEFT))]]
    t = Table(data, colWidths=[doc.width])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), GREEN_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("BOX",           (0, 0), (-1, -1), 0, GREEN_DARK),
    ]))
    return t


if __name__ == "__main__":
    build_pdf()
