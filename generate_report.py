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
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
import os

# ─── Configuração ────────────────────────────────────────────────────────────
REPORT_DATE = "01/06/2026"
REPORT_TIME = "14:07"
REPORT_DATETIME = f"{REPORT_DATE} {REPORT_TIME}"
OUTPUT_FILE = "relatorio-trading-2026-06-01-14h.pdf"

# ─── Cores ───────────────────────────────────────────────────────────────────
GREEN_DARK   = colors.HexColor("#1a7a1a")
GREEN_MED    = colors.HexColor("#28a745")
GREEN_LIGHT  = colors.HexColor("#d4edda")
GOLD         = colors.HexColor("#f0c040")
GOLD_DARK    = colors.HexColor("#c8960c")
DARK_BG      = colors.HexColor("#0d1117")
DARK_CARD    = colors.HexColor("#161b22")
DARK_BORDER  = colors.HexColor("#21262d")
TEXT_WHITE   = colors.HexColor("#e6edf3")
TEXT_GREY    = colors.HexColor("#8b949e")
RED_WARN     = colors.HexColor("#da3633")
BLUE_INFO    = colors.HexColor("#1f6feb")
BLUE_LIGHT   = colors.HexColor("#dbeafe")

# ─── Estilo personalizado ────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles['title'] = ParagraphStyle(
        'Title',
        fontSize=22,
        textColor=GOLD,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    styles['subtitle'] = ParagraphStyle(
        'Subtitle',
        fontSize=11,
        textColor=TEXT_GREY,
        fontName='Helvetica',
        alignment=TA_CENTER,
        spaceAfter=2,
    )
    styles['section'] = ParagraphStyle(
        'Section',
        fontSize=13,
        textColor=GOLD,
        fontName='Helvetica-Bold',
        spaceBefore=14,
        spaceAfter=6,
        borderPad=4,
    )
    styles['body'] = ParagraphStyle(
        'Body',
        fontSize=9,
        textColor=colors.HexColor("#1a1a1a"),
        fontName='Helvetica',
        leading=14,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
    )
    styles['body_bold'] = ParagraphStyle(
        'BodyBold',
        fontSize=9,
        textColor=colors.HexColor("#1a1a1a"),
        fontName='Helvetica-Bold',
        leading=14,
        spaceAfter=4,
    )
    styles['tag_green'] = ParagraphStyle(
        'TagGreen',
        fontSize=8,
        textColor=GREEN_DARK,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER,
    )
    styles['tag_gold'] = ParagraphStyle(
        'TagGold',
        fontSize=8,
        textColor=GOLD_DARK,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER,
    )
    styles['tag_blue'] = ParagraphStyle(
        'TagBlue',
        fontSize=8,
        textColor=BLUE_INFO,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER,
    )
    styles['disclaimer'] = ParagraphStyle(
        'Disclaimer',
        fontSize=7.5,
        textColor=TEXT_GREY,
        fontName='Helvetica-Oblique',
        leading=11,
        alignment=TA_JUSTIFY,
    )
    styles['rule_num'] = ParagraphStyle(
        'RuleNum',
        fontSize=10,
        textColor=GOLD,
        fontName='Helvetica-Bold',
        leading=14,
    )
    styles['rule_text'] = ParagraphStyle(
        'RuleText',
        fontSize=9,
        textColor=colors.HexColor("#1a1a1a"),
        fontName='Helvetica',
        leading=13,
        spaceAfter=3,
    )
    styles['center_bold'] = ParagraphStyle(
        'CenterBold',
        fontSize=10,
        textColor=colors.HexColor("#1a1a1a"),
        fontName='Helvetica-Bold',
        alignment=TA_CENTER,
        leading=14,
    )
    styles['small'] = ParagraphStyle(
        'Small',
        fontSize=8,
        textColor=TEXT_GREY,
        fontName='Helvetica',
        leading=11,
        alignment=TA_CENTER,
    )

    return styles


def hr(color=GOLD_DARK, thickness=0.8):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6, spaceBefore=6)


def section_header(text, styles):
    return [
        hr(GOLD_DARK, 1.2),
        Paragraph(f"▶  {text}", styles['section']),
        hr(GOLD_DARK, 0.5),
    ]


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        rightMargin=1.8*cm,
        leftMargin=1.8*cm,
        topMargin=2*cm,
        bottomMargin=2*cm,
        title="Relatório de Trading EA FC 26",
        author="EA FC 26 Market Analyst",
    )

    styles = build_styles()
    story = []

    # ── CABEÇALHO ──────────────────────────────────────────────────────────
    story.append(Paragraph("EA FC 26 ULTIMATE TEAM", styles['title']))
    story.append(Paragraph("RELATÓRIO DE ANÁLISE DE MERCADO", styles['subtitle']))
    story.append(Paragraph(f"Gerado em: {REPORT_DATETIME} UTC  |  Budget: 40.000 coins", styles['subtitle']))
    story.append(Spacer(1, 0.3*cm))

    # Badge de evento ativo
    event_table = Table(
        [[Paragraph("🏆  FESTIVAL OF FOOTBALL ATIVO  |  PATH TO GLORY  |  WORLD CUP 2026", styles['tag_gold'])]],
        colWidths=[16*cm],
    )
    event_table.setStyle(TableStyle([
        ('BACKGROUND',  (0, 0), (-1, -1), colors.HexColor("#fff3cd")),
        ('ROUNDEDCORNERS', [4]),
        ('BOX',         (0, 0), (-1, -1), 1.2, GOLD_DARK),
        ('TOPPADDING',  (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0,0), (-1, -1), 6),
    ]))
    story.append(event_table)
    story.append(Spacer(1, 0.4*cm))

    # ── 1. CONTEXTO DE MERCADO ─────────────────────────────────────────────
    story.extend(section_header("1. CONTEXTO DO MERCADO", styles))

    context_data = [
        ["EVENTO",       "Festival of Football — Path to Glory (05/06 a 19/06/2026)"],
        ["PROMO ATIVA",  "World Cup 2026 Path to Glory: cartas dinâmicas com upgrades por desempenho nacional"],
        ["PRÓXIMO EVENTO","Greats of the Game — 19/06 (ICONs: Kempes, Rivellino)"],
        ["TENDÊNCIA",    "Mercado aquecido; SBCs do Path to Glory elevam demanda por fodder 83-87"],
        ["ATENÇÃO",      "EVO Undo ativo desde 04/06 → cards tradeable voltam ao mercado → oportunidade!"],
        ["THURSDAY",     "Rewards do Rivals saem quinta-feira → pico de oferta → BUY WINDOW"],
    ]
    ctx_table = Table(context_data, colWidths=[4*cm, 11.4*cm])
    ctx_table.setStyle(TableStyle([
        ('FONTNAME',    (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME',    (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE',    (0, 0), (-1, -1), 8.5),
        ('TEXTCOLOR',   (0, 0), (0, -1), GREEN_DARK),
        ('TEXTCOLOR',   (1, 0), (1, -1), colors.HexColor("#1a1a1a")),
        ('BACKGROUND',  (0, 0), (-1, 0), GREEN_LIGHT),
        ('BACKGROUND',  (0, 2), (-1, 2), GREEN_LIGHT),
        ('BACKGROUND',  (0, 4), (-1, 4), GREEN_LIGHT),
        ('GRID',        (0, 0), (-1, -1), 0.4, colors.HexColor("#c3e6cb")),
        ('TOPPADDING',  (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING',(0,0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(ctx_table)
    story.append(Spacer(1, 0.3*cm))

    # ── 2. TABELA DE OPORTUNIDADES ─────────────────────────────────────────
    story.extend(section_header("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA", styles))

    story.append(Paragraph(
        "Jogadores específicos selecionados com base em preço de mercado (console), utilidade em SBCs ativos e "
        "potencial de valorização durante o Path to Glory. Margem calculada após taxa EA de 5%.",
        styles['body']
    ))
    story.append(Spacer(1, 0.2*cm))

    headers = [
        Paragraph("JOGADOR", styles['body_bold']),
        Paragraph("RTG", styles['body_bold']),
        Paragraph("CLUBE", styles['body_bold']),
        Paragraph("COMPRA\n(coins)", styles['body_bold']),
        Paragraph("VENDA\n(coins)", styles['body_bold']),
        Paragraph("MARGEM\nLÍQUIDA", styles['body_bold']),
        Paragraph("ESTRATÉGIA", styles['body_bold']),
    ]

    card_data = [
        # [Jogador, Rating, Clube, Compra, Venda, Margem, Estratégia]
        ["Jonathan Tah",       "87", "Bayer Leverkusen", "9.500",  "13.500", "+2.825",  "SBC fodder alto"],
        ["Niklas Süle",        "86", "Borussia Dortmund","2.800",  "4.200",  "+1.190",  "SBC 85-86 rated"],
        ["Patrik Schick",      "85", "Bayer Leverkusen", "1.000",  "1.800",  "+710",    "Fodder volume"],
        ["Gerard Moreno",      "85", "Villarreal",       "900",    "1.700",  "+715",    "Fodder volume"],
        ["Rúben Dias",         "88", "Manchester City",  "12.000", "18.000", "+5.100",  "Path to Glory link"],
        ["Kevin De Bruyne",    "88", "Manchester City",  "15.000", "22.000", "+5.900",  "PTG valorização"],
        ["Gavi",               "86", "Barcelona",        "3.500",  "5.800",  "+2.010",  "SBC La Liga link"],
        ["Sergej Milinković",  "85", "Al-Hilal",         "800",    "1.500",  "+625",    "Fodder volume"],
        ["Marcus Thuram",      "86", "Inter Milan",      "3.200",  "5.000",  "+1.550",  "PTG France SBC"],
        ["Lautaro Martínez",   "88", "Inter Milan",      "11.000", "16.500", "+4.675",  "PTG Argentina"],
        ["Omar Marmoush",      "86", "Manchester City",  "4.500",  "7.000",  "+2.150",  "PTG Egypt/upgrd"],
        ["Keira Walsh",        "85", "Barcelona (W)",    "700",    "1.400",  "+630",    "Fodder budget"],
    ]

    table_rows = [headers]
    for row in card_data:
        table_rows.append([
            Paragraph(row[0], styles['body']),
            Paragraph(row[1], styles['center_bold']),
            Paragraph(row[2], styles['body']),
            Paragraph(row[3], styles['body']),
            Paragraph(row[4], styles['body']),
            Paragraph(row[5], styles['tag_green']),
            Paragraph(row[6], styles['body']),
        ])

    col_widths = [3.6*cm, 1.0*cm, 3.2*cm, 1.8*cm, 1.8*cm, 1.7*cm, 3.5*cm]
    card_table = Table(table_rows, colWidths=col_widths, repeatRows=1)

    row_colors = []
    for i in range(1, len(table_rows)):
        bg = colors.white if i % 2 == 1 else colors.HexColor("#f0f7f0")
        row_colors.append(('BACKGROUND', (0, i), (-1, i), bg))

    card_table.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), GREEN_DARK),
        ('TEXTCOLOR',     (0, 0), (-1, 0), colors.white),
        ('FONTNAME',      (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE',      (0, 0), (-1, 0), 8),
        ('ALIGN',         (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID',          (0, 0), (-1, -1), 0.4, colors.HexColor("#c3e6cb")),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f7f0")]),
    ] + row_colors))

    story.append(card_table)
    story.append(Spacer(1, 0.2*cm))

    note = Paragraph(
        "* Margem líquida = (Preço Venda × 0,95) − Preço Compra. Preços baseados em console (PS5/Xbox) em 01/06/2026 às 14h UTC.",
        styles['disclaimer']
    )
    story.append(note)

    # ── 3. ESTRATÉGIA DE TIMING ────────────────────────────────────────────
    story.extend(section_header("3. ESTRATÉGIA DE TIMING", styles))

    timing_data = [
        ["JANELA",              "AÇÃO",                                                "MOTIVO"],
        ["Qui 14h–18h UTC",     "COMPRAR fodder 83–86 rated em volume",                "Rivals Rewards → mercado inundado → preços mínimos"],
        ["Qui 18h–Sex 12h",     "COMPRAR Path to Glory específicos (De Bruyne, Dias)",  "Preços baixos antes dos jogos Copa do Mundo"],
        ["Sex–Sab (durante WC)","VENDER PTG em alta se seleção avançar",               "Vitória = upgrade da carta = valorização imediata"],
        ["Sex 15h–20h UTC",     "VENDER fodder comprado quinta",                       "Novos SBCs sexta elevam demanda por fodder"],
        ["Sab 10h–14h UTC",     "VENDER stocks restantes (Weekend League)",            "WL players pagam mais por fodder barato"],
        ["Dom noite",           "Reinvestir lucros em novo ciclo Thu buy",             "Preparar posição para próxima semana"],
    ]

    timing_table = Table(timing_data, colWidths=[3.5*cm, 6.2*cm, 5.9*cm])
    timing_table.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), colors.HexColor("#1a4a8a")),
        ('TEXTCOLOR',     (0, 0), (-1, 0), colors.white),
        ('FONTNAME',      (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME',      (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE',      (0, 0), (-1, -1), 8),
        ('TEXTCOLOR',     (0, 1), (0, -1), BLUE_INFO),
        ('GRID',          (0, 0), (-1, -1), 0.4, colors.HexColor("#bee3f8")),
        ('BACKGROUND',    (0, 1), (-1, 1), BLUE_LIGHT),
        ('BACKGROUND',    (0, 3), (-1, 3), BLUE_LIGHT),
        ('BACKGROUND',    (0, 5), (-1, 5), BLUE_LIGHT),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('ALIGN',         (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(timing_table)

    # ── 4. ESTIMATIVA DE RETORNO ───────────────────────────────────────────
    story.extend(section_header("4. ESTIMATIVA DE RETORNO EM 48H", styles))

    story.append(Paragraph(
        "Budget: 40.000 coins  |  Estratégia mista: 60% fodder flipping + 30% PTG investment + 10% reserva",
        styles['body_bold']
    ))
    story.append(Spacer(1, 0.2*cm))

    retorno_data = [
        ["CENÁRIO",          "ALOCAÇÃO FODDER", "ALOCAÇÃO PTG",  "RETORNO BRUTO",  "RETORNO LÍQUIDO", "CAPITAL FINAL"],
        ["Conservador 📉",   "24.000 coins",    "12.000 coins",  "+7.200 coins",   "+6.300 coins",    "46.300 coins"],
        ["Moderado  📊",     "24.000 coins",    "12.000 coins",  "+11.500 coins",  "+10.100 coins",   "50.100 coins"],
        ["Otimista  🚀",     "24.000 coins",    "12.000 coins",  "+16.800 coins",  "+14.700 coins",   "54.700 coins"],
    ]

    ret_table = Table(retorno_data, colWidths=[2.6*cm, 2.6*cm, 2.6*cm, 2.6*cm, 2.8*cm, 3.0*cm])
    ret_table.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), GREEN_DARK),
        ('TEXTCOLOR',     (0, 0), (-1, 0), colors.white),
        ('FONTNAME',      (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME',      (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE',      (0, 0), (-1, -1), 8),
        ('ALIGN',         (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID',          (0, 0), (-1, -1), 0.4, colors.HexColor("#c3e6cb")),
        ('BACKGROUND',    (0, 1), (-1, 1), colors.HexColor("#fff3cd")),
        ('BACKGROUND',    (0, 2), (-1, 2), GREEN_LIGHT),
        ('BACKGROUND',    (0, 3), (-1, 3), colors.HexColor("#d4edda")),
        ('TEXTCOLOR',     (5, 1), (5, 3), GREEN_DARK),
        ('FONTNAME',      (5, 1), (5, 3), 'Helvetica-Bold'),
        ('TOPPADDING',    (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(ret_table)
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph(
        "Conservador: sem SBCs novos na janela. Moderado: 1-2 SBCs médios liberados. "
        "Otimista: SBC grande (86+ rated squad) + vitória de seleção PTG no WC.",
        styles['disclaimer']
    ))

    # ── 5. OPORTUNIDADE ESPECIAL — EVO UNDO ───────────────────────────────
    story.extend(section_header("5. OPORTUNIDADE ESPECIAL — EVO UNDO (NOVIDADE)", styles))

    evo_text = (
        "<b>O que é:</b> Desde 04/06/2026, o EVO Undo permite resetar qualquer Evolução aplicada a uma carta. "
        "Se a carta era tradeable antes da evolução, ela retorna como tradeable e pode ser vendida novamente.<br/><br/>"
        "<b>Oportunidade de trading:</b> Jogadores que aplicaram evoluções em cartas baratas (83-85 OVR) e "
        "agora possuem cartas evolved de 88-90 OVR podem desistir da evo, retornando a carta base ao mercado. "
        "Isso cria uma janela de compra de cartas base 83-85 com preços deprimidos.<br/><br/>"
        "<b>Ação recomendada:</b> Comprar cartas 83-85 de jogadores populares para evo (ex: Gerard Moreno 85, "
        "Patrik Schick 85, Niklas Süle 86) nas próximas 24h enquanto o mercado se ajusta. "
        "Vender como fodder nos SBCs de Path to Glory que exigem rated squads."
    )
    story.append(Paragraph(evo_text, styles['body']))

    # ── 6. 8 REGRAS DE OURO DO TRADE ──────────────────────────────────────
    story.extend(section_header("6. 8 REGRAS DE OURO DO TRADE", styles))

    rules = [
        ("1", "NUNCA segure fodder por mais de 48h",
         "O mercado de fodder é volátil. Se o SBC que você esperava não sair, saia da posição com breakeven ou pequena perda."),
        ("2", "Compre na OFERTA, não na demanda",
         "Quinta após rewards e domingo noite são as melhores janelas de compra. Evite comprar durante picos de SBC."),
        ("3", "Respeite a taxa EA de 5%",
         "Sempre calcule: lucro real = (preço venda × 0,95) − preço compra. Nunca confunda margem bruta com líquida."),
        ("4", "Diversifique por rating e tipo",
         "Misture fodder 83-85 (volume, baixo risco) com 1-2 PTG investments (alto retorno, maior risco). Nunca 100% em um só tipo."),
        ("5", "Siga o calendário de SBCs",
         "Cada novo SBC que exige 85+ rated squad = spike de preço em 24h. Tenha seu stock pronto ANTES do drop."),
        ("6", "Fuja de price ranges artificiais",
         "Quando a EA impõe price ranges, o mercado trava. Evite cartas com range ativo — prefira cards fora do range."),
        ("7", "Não invista em PTG antes do primeiro jogo da seleção",
         "Compre PTG ANTES do jogo. Se a seleção ganhar, a carta valoriza. Se perder, o preço cai. Timing é tudo."),
        ("8", "Mantenha sempre 20% de reserva",
         "Nunca invista 100% do budget. Os 20% de reserva (8.000 coins) são para aproveitar oportunidades inesperadas."),
    ]

    rules_data = []
    for num, title, desc in rules:
        rules_data.append([
            Paragraph(num, styles['rule_num']),
            [Paragraph(f"<b>{title}</b>", styles['rule_text']),
             Paragraph(desc, styles['rule_text'])],
        ])

    rules_table = Table(rules_data, colWidths=[0.8*cm, 14.8*cm])
    rules_table.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('BACKGROUND',    (0, 0), (0, -1), colors.HexColor("#fff3cd")),
        ('GRID',          (0, 0), (-1, -1), 0.3, colors.HexColor("#e9ecef")),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1),
         [colors.white, colors.HexColor("#f8f9fa")] * 4),
    ]))
    story.append(rules_table)

    # ── 7. DISCLAIMER ─────────────────────────────────────────────────────
    story.extend(section_header("7. DISCLAIMER", styles))

    disclaimer_text = (
        "Este relatório é gerado de forma automatizada com base em dados públicos de mercado disponíveis em "
        "01/06/2026 às 14:07 UTC, provenientes de fontes como FUTBIN, FUT.GG, FUTWIZ, TeamGullit e Reddit. "
        "As estimativas de preço e margem são aproximações baseadas em médias de mercado e podem variar "
        "significativamente em função de eventos do jogo, novas liberações de SBC/promos pela EA Sports, "
        "desempenho de seleções no Mundial 2026 e flutuações naturais de oferta e demanda. "
        "O trading em Ultimate Team envolve riscos inerentes, incluindo a possibilidade de perda total do "
        "capital investido. Este documento NÃO constitui recomendação financeira ou garantia de lucro. "
        "O usuário é inteiramente responsável por suas decisões de trade. A EA Sports pode alterar "
        "price ranges, regras de mercado ou disponibilidade de cartas a qualquer momento sem aviso prévio. "
        "Compra e venda de FUT coins com terceiros viola os Termos de Serviço da EA Sports."
    )
    story.append(Paragraph(disclaimer_text, styles['disclaimer']))

    # ── RODAPÉ ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.5*cm))
    story.append(hr(TEXT_GREY, 0.5))
    story.append(Paragraph(
        f"EA FC 26 Ultimate Team — Market Analysis Report  |  {REPORT_DATETIME} UTC  |  Budget: 40.000 coins",
        styles['small']
    ))
    story.append(Paragraph(
        "Gerado automaticamente por agente de análise de mercado  |  github.com/kaiohsferreira/fifa-trading",
        styles['small']
    ))

    doc.build(story)
    print(f"PDF gerado: {OUTPUT_FILE}")
    return OUTPUT_FILE


if __name__ == "__main__":
    build_pdf()
