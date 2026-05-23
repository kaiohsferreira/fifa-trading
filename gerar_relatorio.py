#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import PageBreak
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import os

# ── Cores da identidade visual ──────────────────────────────────────────────
VERDE_EA   = HexColor('#00D26A')
VERDE_DARK = HexColor('#00A352')
AZUL_DARK  = HexColor('#0D1B2A')
AZUL_MID   = HexColor('#1A2E44')
AZUL_LIGHT = HexColor('#1E3A5F')
CINZA_TEXTO= HexColor('#C8D6E5')
DOURADO    = HexColor('#FFD700')
VERMELHO   = HexColor('#E74C3C')
LARANJA    = HexColor('#F39C12')
BRANCO     = colors.white

# ── Dados do relatório ───────────────────────────────────────────────────────
REPORT_DATE = "23/05/2026 08:05 UTC"
PDF_NAME    = "relatorio-trading-2026-05-23-08h.pdf"

CARDS = [
    # (Jogador, Rating, Clube, Liga, Buy Low, Buy High, Sell, Margem Líq., Risco, Qtd Sug.)
    ("Manuel Neuer",        84, "Bayern Munich",      "Bundesliga",  700,  900, 1600, 615,  "Baixo",   12),
    ("Wojciech Szczesny",   84, "FC Barcelona",       "La Liga",     800,  980, 1700, 635,  "Baixo",   10),
    ("Isco",                84, "Sevilla FC",         "La Liga",     850, 1000, 1750, 663,  "Baixo",   10),
    ("Stefan de Vrij",      84, "Inter Milan",        "Serie A",     750,  900, 1600, 620,  "Baixo",   10),
    ("Alex Greenwood",      83, "Manchester City",    "Premier Lg.", 1100, 1400, 2100, 595,  "Médio",   8),
    ("Patrik Schick",       85, "Bayer Leverkusen",   "Bundesliga", 2000, 2500, 4000, 1300, "Médio",   5),
    ("Keira Walsh",         85, "FC Barcelona",       "Liga F",     1800, 2200, 3800, 1410, "Médio",   4),
    ("Phil Foden",          86, "Manchester City",    "Premier Lg.", 3000, 3800, 6500, 2375, "Alto",    2),
]

REGRAS = [
    ("1", "Nunca invista mais de 40% do budget em um único jogador.",
          "Diversificação protege seu capital de quedas inesperadas."),
    ("2", "Compre no piso, venda no pico — use o gráfico de preços do FUTBIN.",
          "Preços sobem antes de eventos e caem quando packs são abertos."),
    ("3", "Respeite a taxa de 5% da EA em todos os cálculos de margem.",
          "Ignorar a taxa transforma lucro em prejuízo invisível."),
    ("4", "Venda antes de 48h — nunca segure fodder durante virada de semana.",
          "Packs de recompensa do Weekend League inundam o mercado domingo à noite."),
    ("5", "Fique de olho nos SBCs novos toda quinta-feira às 19h (BST).",
          "Novos SBCs criam picos de demanda imediatos para cartas específicas."),
    ("6", "Use o filtro de 'Compra Imediata' ordenado por menor preço.",
          "Identifique cartas abaixo do mercado sem depender de leilões."),
    ("7", "Não entre em pânico com quedas — TOTS sempre se estabiliza em 48-72h.",
          "Paciência é a vantagem competitiva do trader disciplinado."),
    ("8", "Anote todas as transações: compra, venda, margem e horário.",
          "Dados históricos constroem intuição de mercado ao longo das semanas."),
]


def add_page_background(canvas_obj, doc):
    canvas_obj.saveState()
    # Fundo gradiente simulado
    canvas_obj.setFillColor(AZUL_DARK)
    canvas_obj.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # Faixa lateral esquerda decorativa
    canvas_obj.setFillColor(AZUL_MID)
    canvas_obj.rect(0, 0, 0.4*cm, A4[1], fill=1, stroke=0)
    canvas_obj.setFillColor(VERDE_EA)
    canvas_obj.rect(0, 0, 0.12*cm, A4[1], fill=1, stroke=0)
    # Rodapé
    canvas_obj.setFillColor(AZUL_MID)
    canvas_obj.rect(0, 0, A4[0], 1.2*cm, fill=1, stroke=0)
    canvas_obj.setFillColor(VERDE_EA)
    canvas_obj.rect(0, 1.18*cm, A4[0], 0.05*cm, fill=1, stroke=0)
    canvas_obj.setFont("Helvetica", 7)
    canvas_obj.setFillColor(CINZA_TEXTO)
    canvas_obj.drawCentredString(
        A4[0]/2, 0.45*cm,
        f"EA FC 26 Trading Report | {REPORT_DATE} | Uso exclusivo para fins de trading educacional"
    )
    canvas_obj.drawRightString(
        A4[0] - 1.2*cm, 0.45*cm,
        f"Pág. {doc.page}"
    )
    canvas_obj.restoreState()


def build_styles():
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'TitleMain', fontName='Helvetica-Bold', fontSize=22,
        textColor=VERDE_EA, alignment=TA_CENTER, spaceAfter=4,
        leading=26
    )
    subtitle_style = ParagraphStyle(
        'Subtitle', fontName='Helvetica', fontSize=11,
        textColor=CINZA_TEXTO, alignment=TA_CENTER, spaceAfter=2
    )
    section_style = ParagraphStyle(
        'SectionTitle', fontName='Helvetica-Bold', fontSize=13,
        textColor=VERDE_EA, spaceBefore=14, spaceAfter=6,
        borderPad=4
    )
    body_style = ParagraphStyle(
        'Body', fontName='Helvetica', fontSize=9,
        textColor=CINZA_TEXTO, leading=14, spaceAfter=4,
        alignment=TA_JUSTIFY
    )
    body_bold = ParagraphStyle(
        'BodyBold', fontName='Helvetica-Bold', fontSize=9,
        textColor=BRANCO, leading=14, spaceAfter=4
    )
    bullet_style = ParagraphStyle(
        'Bullet', fontName='Helvetica', fontSize=9,
        textColor=CINZA_TEXTO, leading=13, leftIndent=14,
        bulletIndent=4, spaceAfter=3
    )
    label_style = ParagraphStyle(
        'Label', fontName='Helvetica-Bold', fontSize=8,
        textColor=DOURADO
    )
    disclaimer_style = ParagraphStyle(
        'Disclaimer', fontName='Helvetica-Oblique', fontSize=7.5,
        textColor=HexColor('#8899AA'), alignment=TA_JUSTIFY, leading=11
    )
    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'section': section_style,
        'body': body_style,
        'body_bold': body_bold,
        'bullet': bullet_style,
        'label': label_style,
        'disclaimer': disclaimer_style,
    }


def build_header(styles):
    elems = []
    elems.append(Spacer(1, 0.5*cm))

    # Badge / logo text
    badge_data = [["EA FC 26 · ULTIMATE TEAM"]]
    badge_tbl = Table(badge_data, colWidths=[10*cm])
    badge_tbl.setStyle(TableStyle([
        ('BACKGROUND',   (0,0), (-1,-1), VERDE_DARK),
        ('TEXTCOLOR',    (0,0), (-1,-1), BRANCO),
        ('FONTNAME',     (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE',     (0,0), (-1,-1), 9),
        ('ALIGN',        (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING',   (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',(0,0), (-1,-1), 5),
        ('ROUNDEDCORNERS', [4,4,4,4]),
    ]))
    # Center badge
    badge_wrap = Table([[badge_tbl]], colWidths=[17*cm])
    badge_wrap.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER')]))
    elems.append(badge_wrap)
    elems.append(Spacer(1, 0.3*cm))

    elems.append(Paragraph("RELATÓRIO DE ANÁLISE DE MERCADO", styles['title']))
    elems.append(Paragraph("Gerado em: " + REPORT_DATE, styles['subtitle']))
    elems.append(Spacer(1, 0.2*cm))
    elems.append(HRFlowable(width="100%", thickness=1.5, color=VERDE_EA, spaceAfter=8))
    return elems


def build_market_context(styles):
    elems = []
    elems.append(Paragraph("1. CONTEXTO DE MERCADO — MOMENTO ATUAL", styles['section']))

    # Info boxes top row
    ctx_data = [
        [
            Paragraph("<b>EVENTO ATIVO</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("<b>FASE DO MERCADO</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("<b>BUDGET DISPONÍVEL</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        ],
        [
            Paragraph("🏆 Ultimate TOTS\n(desde 22/05)", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=10, textColor=VERDE_EA, alignment=TA_CENTER, leading=14)),
            Paragraph("📉 Pós-Crash\nEstabilização", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=10, textColor=LARANJA, alignment=TA_CENTER, leading=14)),
            Paragraph("💰 40.000 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=10, textColor=BRANCO, alignment=TA_CENTER, leading=14)),
        ],
    ]
    ctx_tbl = Table(ctx_data, colWidths=[5.5*cm, 5.5*cm, 5.5*cm])
    ctx_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (0,0), AZUL_MID),
        ('BACKGROUND',    (1,0), (1,0), AZUL_MID),
        ('BACKGROUND',    (2,0), (2,0), AZUL_MID),
        ('BACKGROUND',    (0,1), (0,1), HexColor('#0D2A1B')),
        ('BACKGROUND',    (1,1), (1,1), HexColor('#2A1D0D')),
        ('BACKGROUND',    (2,1), (2,1), AZUL_LIGHT),
        ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('GRID',          (0,0), (-1,-1), 0.5, HexColor('#2A3F55')),
        ('ROUNDEDCORNERS', [4,4,4,4]),
    ]))
    elems.append(ctx_tbl)
    elems.append(Spacer(1, 0.4*cm))

    body_text = [
        ("<b>Ultimate TOTS (22/05 – 29/05):</b> O maior evento do ano chegou ontem. "
         "Jogadores como Messi, Ronaldo, Mbappé e Haaland receberam cartas com ratings acima de 96. "
         "A abertura massiva de packs causou o <b>crash pós-TOTS</b> — fase ideal para compras estratégicas."),
        "",
        ("<b>La Liga TOTS SBC</b> expira em <b>26/05 (terça-feira)</b>. Restam apenas ~3 dias de demanda "
         "ativa por fodder da La Liga (cartas 84-86 da La Liga sobem nas próximas 24-48h)."),
        "",
        ("<b>End of Era SBCs ativos:</b> Mohamed Salah (EoE) e Gianluigi Buffon (Trophy Titans ICON) "
         "estão drenando cartas 83-87 do mercado. Isso sustenta os preços de fodder mesmo pós-crash."),
        "",
        ("<b>Timing atual (sábado manhã):</b> Preços no fundo do crash. "
         "Weekend League começa hoje — jogadores vão <b>comprar jogadores</b> para montar times, "
         "causando alta de 15-30% nos preços nas próximas 12-18h."),
    ]

    for line in body_text:
        if line:
            elems.append(Paragraph(line, styles['body']))
        else:
            elems.append(Spacer(1, 0.15*cm))

    elems.append(HRFlowable(width="100%", thickness=0.5, color=AZUL_LIGHT, spaceAfter=4))
    return elems


def build_cards_table(styles):
    elems = []
    elems.append(Paragraph("2. CARTAS RECOMENDADAS PARA COMPRA", styles['section']))

    disclaimer_tbl = Paragraph(
        "* Margem líquida calculada após taxa de 5% da EA. Preços baseados em dados de 23/05/2026 às 08h UTC "
        "— verifique sempre no FUTBIN/FUT.GG antes de executar. Qtd. Sug. = quantidade recomendada para o budget de 40k.",
        ParagraphStyle('', fontName='Helvetica-Oblique', fontSize=7, textColor=CINZA_TEXTO, leading=10)
    )

    # Header
    header = [
        Paragraph("JOGADOR", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph("OVR", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph("CLUBE / LIGA", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph("COMPRA\n(coins)", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph("VENDA\n(coins)", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph("MARGEM\nLÍQ.*", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph("RISCO", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph("QTD.\nSUG.", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
    ]

    risco_cores = {"Baixo": VERDE_EA, "Médio": LARANJA, "Alto": VERMELHO}

    table_data = [header]
    for i, (name, rat, clube, liga, b_low, b_high, sell, margin, risk, qty) in enumerate(CARDS):
        buy_str   = f"{b_low:,}–{b_high:,}".replace(",", ".")
        sell_str  = f"{sell:,}".replace(",", ".")
        margin_str= f"+{margin:,}".replace(",", ".")
        risk_color= risco_cores.get(risk, BRANCO)
        row_bg    = HexColor('#0F2035') if i % 2 == 0 else AZUL_LIGHT

        row = [
            Paragraph(f"<b>{name}</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8.5, textColor=BRANCO)),
            Paragraph(f"<b>{rat}</b>",  ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=VERDE_EA, alignment=TA_CENTER)),
            Paragraph(f"{clube}\n<font size='7' color='#8899AA'>{liga}</font>",
                      ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, leading=11)),
            Paragraph(buy_str,   ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph(sell_str,  ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=VERDE_EA, alignment=TA_CENTER)),
            Paragraph(margin_str,ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph(f"<b>{risk}</b>",ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=risk_color, alignment=TA_CENTER)),
            Paragraph(str(qty),  ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=BRANCO, alignment=TA_CENTER)),
        ]
        table_data.append(row)

    col_widths = [4.0*cm, 1.2*cm, 3.2*cm, 2.5*cm, 2.0*cm, 2.0*cm, 1.6*cm, 1.2*cm]
    tbl = Table(table_data, colWidths=col_widths, repeatRows=1)

    row_styles = [
        ('BACKGROUND',    (0,0), (-1,0),  AZUL_MID),
        ('GRID',          (0,0), (-1,-1), 0.4, HexColor('#1A3050')),
        ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING',   (0,0), (-1,-1), 5),
        ('RIGHTPADDING',  (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor('#0F2035'), AZUL_LIGHT]),
    ]
    tbl.setStyle(TableStyle(row_styles))

    elems.append(tbl)
    elems.append(Spacer(1, 0.2*cm))
    elems.append(disclaimer_tbl)
    elems.append(Spacer(1, 0.3*cm))
    elems.append(HRFlowable(width="100%", thickness=0.5, color=AZUL_LIGHT, spaceAfter=4))
    return elems


def build_allocation(styles):
    elems = []
    elems.append(Paragraph("3. ALOCAÇÃO DO BUDGET (40.000 coins)", styles['section']))

    alloc_data = [
        [
            Paragraph("ESTRATÉGIA", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("INVESTIMENTO", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("QTD. CARTAS", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("RETORNO EST.", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("% BUDGET", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        ],
        [
            Paragraph("SBC Fodder 84-rated\n(Neuer, Isco, De Vrij, Szczesny)", ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, leading=11)),
            Paragraph("16.000 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=BRANCO, alignment=TA_CENTER)),
            Paragraph("~19 cartas", ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph("+8.000–11.000", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=VERDE_EA, alignment=TA_CENTER)),
            Paragraph("40%", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=LARANJA, alignment=TA_CENTER)),
        ],
        [
            Paragraph("SBC Fodder 85-rated\n(Schick, Keira Walsh)", ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, leading=11)),
            Paragraph("12.000 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=BRANCO, alignment=TA_CENTER)),
            Paragraph("~5 cartas", ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph("+7.500–9.000", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=VERDE_EA, alignment=TA_CENTER)),
            Paragraph("30%", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=LARANJA, alignment=TA_CENTER)),
        ],
        [
            Paragraph("Mid-Tier Promo (86-rated)\n(Phil Foden + 1 outro)", ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, leading=11)),
            Paragraph("8.000 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=BRANCO, alignment=TA_CENTER)),
            Paragraph("~2 cartas", ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph("+4.750–6.500", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=VERDE_EA, alignment=TA_CENTER)),
            Paragraph("20%", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=LARANJA, alignment=TA_CENTER)),
        ],
        [
            Paragraph("Reserva (liquidez)", ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO)),
            Paragraph("4.000 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=BRANCO, alignment=TA_CENTER)),
            Paragraph("—", ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph("Proteção de capital", ParagraphStyle('', fontName='Helvetica-Oblique', fontSize=8, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph("10%", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
        ],
        [
            Paragraph("<b>TOTAL</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=DOURADO)),
            Paragraph("<b>40.000 coins</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("<b>~26 cartas</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("<b>+20.250–26.500</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=VERDE_EA, alignment=TA_CENTER)),
            Paragraph("<b>100%</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=DOURADO, alignment=TA_CENTER)),
        ],
    ]

    col_widths = [5.5*cm, 2.8*cm, 2.4*cm, 3.2*cm, 2.2*cm]
    tbl = Table(alloc_data, colWidths=col_widths)
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),   AZUL_MID),
        ('BACKGROUND',    (0,-1),(-1,-1),  HexColor('#0D2A1B')),
        ('ROWBACKGROUNDS',(0,1), (-1,-2),  [HexColor('#0F2035'), AZUL_LIGHT]),
        ('GRID',          (0,0), (-1,-1),  0.4, HexColor('#1A3050')),
        ('ALIGN',         (0,0), (-1,-1),  'CENTER'),
        ('VALIGN',        (0,0), (-1,-1),  'MIDDLE'),
        ('TOPPADDING',    (0,0), (-1,-1),  7),
        ('BOTTOMPADDING', (0,0), (-1,-1),  7),
        ('LEFTPADDING',   (0,0), (-1,-1),  5),
    ]))
    elems.append(tbl)
    elems.append(Spacer(1, 0.3*cm))
    elems.append(HRFlowable(width="100%", thickness=0.5, color=AZUL_LIGHT, spaceAfter=4))
    return elems


def build_timing(styles):
    elems = []
    elems.append(Paragraph("4. ESTRATÉGIA DE TIMING — PRÓXIMAS 48 HORAS", styles['section']))

    timeline = [
        ("SAB 23/05\n08h–12h", "COMPRAR",   VERDE_EA,  "Preços no fundo do crash pós-TOTS. Janela de compra ideal para 84–85 rated. "
                                                          "Weekend League começa hoje — equipes serão montadas ao longo do dia."),
        ("SAB 23/05\n14h–22h", "SEGURAR",   LARANJA,   "Mercado em estabilização. Preços começam a subir conforme jogadores buscam "
                                                          "completar SBCs e montar times para o Weekend League."),
        ("DOM 24/05\n08h–18h", "VENDER",    VERDE_EA,  "Pico de demanda por fodder. Jogadores montam times e completam SBCs antes "
                                                          "do encerramento do Weekend League. Preços de 84–85 rated no topo semanal."),
        ("DOM 24/05\n20h–00h", "CAUTELA",   VERMELHO,  "Recompensas do Weekend League serão abertas. Packs inundam o mercado — "
                                                          "preços caem. Venda ANTES das 20h BST (21h BRT)."),
        ("SEG 25/05\n08h–14h", "REAVALI.",  LARANJA,   "La Liga TOTS SBC expira em 26/05. Demanda específica por cartas La Liga "
                                                          "(Isco, Szczesny). Oportunidade para novo ciclo com cartas La Liga."),
    ]

    time_data = [[
        Paragraph("HORÁRIO", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph("AÇÃO", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph("DESCRIÇÃO", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
    ]]

    for hora, acao, cor, desc in timeline:
        time_data.append([
            Paragraph(hora, ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=CINZA_TEXTO, alignment=TA_CENTER, leading=11)),
            Paragraph(f"<b>{acao}</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=cor, alignment=TA_CENTER)),
            Paragraph(desc, ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, leading=11)),
        ])

    tbl = Table(time_data, colWidths=[2.5*cm, 2.2*cm, 12.0*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),  (-1,0),  AZUL_MID),
        ('ROWBACKGROUNDS',(0,1),  (-1,-1), [HexColor('#0F2035'), AZUL_LIGHT]),
        ('GRID',          (0,0),  (-1,-1), 0.4, HexColor('#1A3050')),
        ('ALIGN',         (0,0),  (-1,-1), 'CENTER'),
        ('VALIGN',        (0,0),  (-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0),  (-1,-1), 7),
        ('BOTTOMPADDING', (0,0),  (-1,-1), 7),
    ]))
    elems.append(tbl)
    elems.append(Spacer(1, 0.3*cm))
    elems.append(HRFlowable(width="100%", thickness=0.5, color=AZUL_LIGHT, spaceAfter=4))
    return elems


def build_returns(styles):
    elems = []
    elems.append(Paragraph("5. ESTIMATIVA DE RETORNO EM 48 HORAS", styles['section']))

    scenario_data = [
        [
            Paragraph("CENÁRIO", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("PRESSUPOSTO", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("RETORNO BRUTO", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("LUCRO LÍQUIDO", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("CAPITAL FINAL", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("ROI", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=8, textColor=DOURADO, alignment=TA_CENTER)),
        ],
        [
            Paragraph("🔴 Pessimista", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=VERMELHO)),
            Paragraph("Venda com 10% abaixo\ndo alvo (mercado lento)",
                      ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, leading=11, alignment=TA_CENTER)),
            Paragraph("48.200 coins", ParagraphStyle('', fontName='Helvetica', fontSize=9, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph("+8.200 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=LARANJA, alignment=TA_CENTER)),
            Paragraph("48.200 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph("+20,5%", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=LARANJA, alignment=TA_CENTER)),
        ],
        [
            Paragraph("🟡 Conservador", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=LARANJA)),
            Paragraph("Venda nos preços\nalvo definidos",
                      ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, leading=11, alignment=TA_CENTER)),
            Paragraph("59.200 coins", ParagraphStyle('', fontName='Helvetica', fontSize=9, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph("+20.250 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=VERDE_EA, alignment=TA_CENTER)),
            Paragraph("60.250 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=VERDE_EA, alignment=TA_CENTER)),
            Paragraph("+50,6%", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=VERDE_EA, alignment=TA_CENTER)),
        ],
        [
            Paragraph("🟢 Otimista", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=VERDE_EA)),
            Paragraph("Spike de SBC + WL\nEoE Salah em alta",
                      ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, leading=11, alignment=TA_CENTER)),
            Paragraph("65.000 coins", ParagraphStyle('', fontName='Helvetica', fontSize=9, textColor=CINZA_TEXTO, alignment=TA_CENTER)),
            Paragraph("+26.500 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("66.500 coins", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=DOURADO, alignment=TA_CENTER)),
            Paragraph("+66,3%", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=DOURADO, alignment=TA_CENTER)),
        ],
    ]

    tbl = Table(scenario_data, colWidths=[2.8*cm, 4.0*cm, 2.7*cm, 2.7*cm, 2.7*cm, 1.8*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),  (-1,0),  AZUL_MID),
        ('BACKGROUND',    (0,1),  (-1,1),  HexColor('#2A1010')),
        ('BACKGROUND',    (0,2),  (-1,2),  HexColor('#1A2A10')),
        ('BACKGROUND',    (0,3),  (-1,3),  HexColor('#0D2A1B')),
        ('GRID',          (0,0),  (-1,-1), 0.4, HexColor('#1A3050')),
        ('ALIGN',         (0,0),  (-1,-1), 'CENTER'),
        ('VALIGN',        (0,0),  (-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0),  (-1,-1), 8),
        ('BOTTOMPADDING', (0,0),  (-1,-1), 8),
    ]))
    elems.append(tbl)
    elems.append(Spacer(1, 0.3*cm))
    elems.append(HRFlowable(width="100%", thickness=0.5, color=AZUL_LIGHT, spaceAfter=4))
    return elems


def build_golden_rules(styles):
    elems = []
    elems.append(Paragraph("6. 8 REGRAS DE OURO DO TRADE", styles['section']))

    for num, regra, detalhe in REGRAS:
        rule_data = [[
            Paragraph(f"<b>{num}</b>", ParagraphStyle('', fontName='Helvetica-Bold', fontSize=14,
                      textColor=VERDE_EA, alignment=TA_CENTER)),
            [
                Paragraph(f"<b>{regra}</b>",
                          ParagraphStyle('', fontName='Helvetica-Bold', fontSize=9, textColor=BRANCO, leading=12)),
                Paragraph(detalhe,
                          ParagraphStyle('', fontName='Helvetica', fontSize=8, textColor=CINZA_TEXTO, leading=11)),
            ],
        ]]
        rule_tbl = Table(rule_data, colWidths=[1.2*cm, 15.5*cm])
        rule_tbl.setStyle(TableStyle([
            ('BACKGROUND',    (0,0), (0,0), AZUL_MID),
            ('BACKGROUND',    (1,0), (1,0), HexColor('#0F2035')),
            ('ALIGN',         (0,0), (0,0), 'CENTER'),
            ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING',    (0,0), (-1,-1), 7),
            ('BOTTOMPADDING', (0,0), (-1,-1), 7),
            ('LEFTPADDING',   (1,0), (1,0), 10),
            ('BOX',           (0,0), (-1,-1), 0.5, HexColor('#1A3050')),
        ]))
        elems.append(rule_tbl)
        elems.append(Spacer(1, 0.2*cm))

    elems.append(HRFlowable(width="100%", thickness=0.5, color=AZUL_LIGHT, spaceAfter=4))
    return elems


def build_disclaimer(styles):
    elems = []
    elems.append(Spacer(1, 0.2*cm))
    disc_box = Table([[
        Paragraph(
            "<b>⚠ DISCLAIMER:</b> Este relatório é gerado automaticamente para fins educacionais e de auxílio "
            "a decisões de trading no EA FC 26 Ultimate Team. Os preços e margens são estimativas baseadas "
            "em dados históricos e tendências de mercado — não constituem garantia de lucro. O mercado do "
            "FUT é volátil e pode mudar rapidamente. Invista apenas o que está disposto a perder. "
            "Este conteúdo não tem afiliação oficial com a EA Sports. Sempre confirme os preços em tempo "
            "real no FUTBIN (futbin.com) ou FUT.GG (fut.gg) antes de executar qualquer operação.",
            styles['disclaimer']
        )
    ]], colWidths=[16.7*cm])
    disc_box.setStyle(TableStyle([
        ('BACKGROUND',  (0,0), (-1,-1), HexColor('#0A1520')),
        ('BOX',         (0,0), (-1,-1), 0.5, HexColor('#2A3F55')),
        ('TOPPADDING',  (0,0), (-1,-1), 8),
        ('BOTTOMPADDING',(0,0),(-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING',(0,0), (-1,-1), 10),
    ]))
    elems.append(disc_box)
    return elems


def generate_pdf():
    output_path = os.path.join(os.path.dirname(__file__), PDF_NAME)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=1.2*cm,
        leftMargin=1.2*cm,
        topMargin=1.0*cm,
        bottomMargin=1.8*cm,
    )

    styles = build_styles()
    story  = []

    story += build_header(styles)
    story += build_market_context(styles)
    story += build_cards_table(styles)
    story += build_allocation(styles)
    story += build_timing(styles)
    story += build_returns(styles)
    story += build_golden_rules(styles)
    story += build_disclaimer(styles)

    doc.build(story, onFirstPage=add_page_background, onLaterPages=add_page_background)
    print(f"PDF gerado: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_pdf()
