#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import KeepTogether
import os

# ─── Configurações gerais ──────────────────────────────────────────────────────
REPORT_DATE_DISPLAY = "24/05/2026 20:09"
REPORT_DATE_FILE    = "2026-05-24-20h"
OUTPUT_FILE         = f"relatorio-trading-{REPORT_DATE_FILE}.pdf"
OUTPUT_PATH         = os.path.join(os.path.dirname(__file__), OUTPUT_FILE)

# ─── Paleta de cores (tema EA FC / verde-neon sobre escuro) ──────────────────
C_BG_DARK    = colors.HexColor("#0D1117")
C_GREEN      = colors.HexColor("#00FF87")
C_GREEN_DARK = colors.HexColor("#00C86B")
C_YELLOW     = colors.HexColor("#FFD700")
C_RED        = colors.HexColor("#FF4444")
C_BLUE       = colors.HexColor("#4D9FFF")
C_WHITE      = colors.HexColor("#FFFFFF")
C_LIGHT_GRAY = colors.HexColor("#C0C0C0")
C_MID_GRAY   = colors.HexColor("#808080")
C_DARK_GRAY  = colors.HexColor("#1E2530")
C_HEADER_BG  = colors.HexColor("#162032")
C_ROW_ALT    = colors.HexColor("#151B26")
C_ROW_NORM   = colors.HexColor("#0D1117")

PAGE_W, PAGE_H = A4
MARGIN = 1.8 * cm

# ─── Estilos ─────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def s(name, **kw):
    """Cria um ParagraphStyle sobre base 'Normal'."""
    return ParagraphStyle(name, parent=styles['Normal'], **kw)

S_TITLE = s("Title2",
    fontSize=26, leading=32, textColor=C_GREEN,
    fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=4)

S_SUBTITLE = s("Subtitle2",
    fontSize=13, leading=16, textColor=C_LIGHT_GRAY,
    fontName="Helvetica", alignment=TA_CENTER, spaceAfter=2)

S_DATE = s("Date2",
    fontSize=11, leading=14, textColor=C_YELLOW,
    fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=14)

S_SECTION = s("Section2",
    fontSize=14, leading=18, textColor=C_GREEN,
    fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=6)

S_SUBSECTION = s("Subsection2",
    fontSize=11, leading=14, textColor=C_YELLOW,
    fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=4)

S_BODY = s("Body2",
    fontSize=9, leading=13, textColor=C_LIGHT_GRAY,
    fontName="Helvetica", alignment=TA_JUSTIFY, spaceAfter=4)

S_BODY_BOLD = s("BodyBold2",
    fontSize=9, leading=13, textColor=C_WHITE,
    fontName="Helvetica-Bold", spaceAfter=4)

S_BULLET = s("Bullet2",
    fontSize=9, leading=13, textColor=C_LIGHT_GRAY,
    fontName="Helvetica", leftIndent=14, spaceAfter=3)

S_HIGHLIGHT = s("Highlight2",
    fontSize=9, leading=13, textColor=C_GREEN,
    fontName="Helvetica-Bold", spaceAfter=4)

S_DISCLAIMER = s("Disclaimer2",
    fontSize=7.5, leading=11, textColor=C_MID_GRAY,
    fontName="Helvetica", alignment=TA_JUSTIFY)

S_TABLE_HEADER = ParagraphStyle("TH",
    parent=styles['Normal'],
    fontSize=8, textColor=C_WHITE, fontName="Helvetica-Bold",
    alignment=TA_CENTER, leading=11)

S_TABLE_CELL = ParagraphStyle("TC",
    parent=styles['Normal'],
    fontSize=8, textColor=C_LIGHT_GRAY, fontName="Helvetica",
    alignment=TA_CENTER, leading=11)

S_TABLE_CELL_L = ParagraphStyle("TCL",
    parent=styles['Normal'],
    fontSize=8, textColor=C_LIGHT_GRAY, fontName="Helvetica",
    alignment=TA_LEFT, leading=11)

S_GREEN_CELL = ParagraphStyle("GC",
    parent=styles['Normal'],
    fontSize=8, textColor=C_GREEN, fontName="Helvetica-Bold",
    alignment=TA_CENTER, leading=11)

S_YELLOW_CELL = ParagraphStyle("YC",
    parent=styles['Normal'],
    fontSize=8, textColor=C_YELLOW, fontName="Helvetica-Bold",
    alignment=TA_CENTER, leading=11)

S_RED_CELL = ParagraphStyle("RC",
    parent=styles['Normal'],
    fontSize=8, textColor=C_RED, fontName="Helvetica-Bold",
    alignment=TA_CENTER, leading=11)


# ─── Funções auxiliares ───────────────────────────────────────────────────────
def hr(color=C_GREEN, thickness=1):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6)

def sp(h=0.3):
    return Spacer(1, h * cm)

def p(text, style=S_BODY):
    return Paragraph(text, style)

def bullet(text, icon="▸"):
    return Paragraph(f"{icon}  {text}", S_BULLET)


# ─── Conteúdo ─────────────────────────────────────────────────────────────────
def build_story():
    story = []

    # ══════════════════════════════════════════════════
    # HEADER
    # ══════════════════════════════════════════════════
    story.append(sp(0.5))
    story.append(p("⚽  EA FC 26 ULTIMATE TEAM", S_TITLE))
    story.append(p("RELATÓRIO DIÁRIO DE TRADING", S_SUBTITLE))
    story.append(p(f"📅  {REPORT_DATE_DISPLAY} UTC", S_DATE))
    story.append(hr(C_GREEN, 2))
    story.append(sp(0.2))

    # ══════════════════════════════════════════════════
    # 1. CONTEXTO DO MERCADO
    # ══════════════════════════════════════════════════
    story.append(p("1. CONTEXTO DO MERCADO", S_SECTION))
    story.append(hr(C_GREEN_DARK, 0.5))

    story.append(p(
        "<b>Evento Ativo Principal:</b> <font color='#00FF87'>ULTIMATE TOTS</font> "
        "(Team of the Season Definitivo) — lançado em 22/05/2026 às 18h BST, "
        "permanece em packs até <b>29/05/2026</b>. Este é o evento final da temporada, "
        "reunindo os melhores TOTS de todas as ligas em um único pack release.",
        S_BODY))

    story.append(p(
        "Junto ao Ultimate TOTS, foram lançadas <b>End of an Era SBCs</b> para jogadores "
        "icônicos como <b>Mohamed Salah (95 OVR)</b>, Bernardo Silva (93), John Stones (91), "
        "Andrew Robertson, Antoine Griezmann e Leon Goretzka — além da <b>Trophy Titans ICON SBC "
        "(Gianluigi Buffon)</b> e Showdowns ligados à Final da UEFA Champions League.",
        S_BODY))

    story.append(p(
        "Também está ativa a <b>TOTS Career Path Evolution</b> (gratuita, iniciada em 15/05/2026), "
        "que permite evoluir jogadores de rating mais baixo adicionando o TOTS Trait.",
        S_BODY))

    story.append(sp(0.3))
    story.append(p("📊 Tendências do Mercado Agora:", S_SUBSECTION))

    trends = [
        ["Tendência", "Status", "Impacto no Trader"],
        ["Fodder 83–86 OVR", "⬇ Preços baixos", "Oportunidade de compra"],
        ["Fodder 87–88 OVR", "⬇ Temporariamente baixo", "Acumular antes da alta"],
        ["TOTS 90–92 OVR", "⬇ Mercado saturado", "Comprar melhores cards do ano"],
        ["Evolutions elegíveis", "↗ Demanda crescente", "Investir em cartas elegíveis"],
        ["End of an Era SBCs", "⬆ Alta demanda fodder", "Fodder 85+ sobe em breve"],
        ["Pack opening", "⬆ Volume alto", "Oferta grande agora → preços caem"],
    ]

    trend_table = Table(trends, colWidths=[5.2*cm, 4.2*cm, 7.6*cm])
    trend_table.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),   C_HEADER_BG),
        ('TEXTCOLOR',     (0,0), (-1,0),   C_GREEN),
        ('FONTNAME',      (0,0), (-1,0),   'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,0),   8),
        ('ALIGN',         (0,0), (-1,-1),  'CENTER'),
        ('VALIGN',        (0,0), (-1,-1),  'MIDDLE'),
        ('FONTNAME',      (0,1), (-1,-1),  'Helvetica'),
        ('FONTSIZE',      (0,1), (-1,-1),  8),
        ('TEXTCOLOR',     (0,1), (-1,-1),  C_LIGHT_GRAY),
        ('ROWBACKGROUNDS',(0,1), (-1,-1),  [C_ROW_NORM, C_ROW_ALT]),
        ('GRID',          (0,0), (-1,-1),  0.4, colors.HexColor("#2A3545")),
        ('TOPPADDING',    (0,0), (-1,-1),  4),
        ('BOTTOMPADDING', (0,0), (-1,-1),  4),
        ('LEFTPADDING',   (0,0), (-1,-1),  6),
        ('RIGHTPADDING',  (0,0), (-1,-1),  6),
    ]))
    story.append(trend_table)
    story.append(sp(0.4))

    # ══════════════════════════════════════════════════
    # 2. TABELA DE OPORTUNIDADES
    # ══════════════════════════════════════════════════
    story.append(p("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA", S_SECTION))
    story.append(hr(C_GREEN_DARK, 0.5))
    story.append(p(
        "Budget disponível: <b><font color='#FFD700'>40.000 coins</font></b>  |  "
        "Taxa EA: 5%  |  Horizonte: próximas 48h",
        S_BODY_BOLD))
    story.append(sp(0.2))

    # Cabeçalho
    header = [
        Paragraph("Jogador", S_TABLE_HEADER),
        Paragraph("OVR", S_TABLE_HEADER),
        Paragraph("Clube", S_TABLE_HEADER),
        Paragraph("Compra\n(coins)", S_TABLE_HEADER),
        Paragraph("Venda\n(coins)", S_TABLE_HEADER),
        Paragraph("Margem\nLíquida", S_TABLE_HEADER),
        Paragraph("Qtd\nRec.", S_TABLE_HEADER),
        Paragraph("Estratégia", S_TABLE_HEADER),
    ]

    # Dados — (nome, ovr, clube, compra, venda, margem, qtd, estrategia)
    # margem = venda * 0.95 - compra
    cards = [
        # Fodder 86
        ("Ibrahima Konaté",      "86", "Liverpool FC",       1200, 1700,  None, "12", "SBC Fodder / End of Era"),
        ("Sandro Tonali",        "86", "Newcastle Utd",      1300, 1800,  None, "10", "SBC Fodder / End of Era"),
        ("Nuno Mendes",          "86", "Paris SG",           1300, 1800,  None, "10", "SBC Fodder / End of Era"),
        ("İlkay Gündoğan",       "86", "FC Barcelona",       1400, 1900,  None,  "8", "SBC Fodder / Sell Fri"),
        # Fodder 87
        ("Lucy Bronze",          "87", "FC Barcelona",       1700, 2500,  None,  "8", "Fodder 87 / Thu Flip"),
        ("Sam Kerr",             "87", "Chelsea FC",         1700, 2500,  None,  "8", "Fodder 87 / Thu Flip"),
        ("Rose Lavelle",         "87", "NJ/NY Gotham FC",    1800, 2600,  None,  "6", "Fodder 87 / Thu Flip"),
        # Fodder 88
        ("Irene Paredes",        "88", "FC Barcelona",       2900, 4200,  None,  "4", "Fodder 88 / High Demand"),
        ("Erin Endler",          "88", "PSG (feminino)",     2900, 4200,  None,  "4", "Fodder 88 / High Demand"),
        ("Bukayo Saka",          "88", "Arsenal FC",         2900, 4300,  None,  "3", "Fodder 88 / SBC Alta"),
        # Evolutions
        ("Lamine Yamal (base)",  "82", "FC Barcelona",        950, 1600,  None,  "8", "Evo TOTS Career Path"),
        ("Kobbie Mainoo (base)", "81", "Man. United",          850, 1500,  None, "10", "Evo TOTS Career Path"),
        # TOTS meta barato
        ("TOTS 90-OVR genérico", "90", "Vários",             3500, 5200,  None,  "4", "FUT Champs spike"),
    ]

    rows = [header]
    for (nome, ovr, clube, compra, venda, _, qtd, estrategia) in cards:
        margem = round(venda * 0.95 - compra)
        pct = round(margem / compra * 100)
        cor_margem = S_GREEN_CELL if margem > 0 else S_RED_CELL
        rows.append([
            Paragraph(nome, S_TABLE_CELL_L),
            Paragraph(ovr, S_TABLE_CELL),
            Paragraph(clube, S_TABLE_CELL_L),
            Paragraph(f"{compra:,}".replace(",", "."), S_YELLOW_CELL),
            Paragraph(f"{venda:,}".replace(",", "."), S_TABLE_CELL),
            Paragraph(f"{margem:,}".replace(",", ".") + f"\n(+{pct}%)", cor_margem),
            Paragraph(qtd, S_TABLE_CELL),
            Paragraph(estrategia, S_TABLE_CELL_L),
        ])

    col_widths = [3.8*cm, 1.2*cm, 3.5*cm, 1.9*cm, 1.9*cm, 2.0*cm, 1.3*cm, 3.4*cm]
    main_table = Table(rows, colWidths=col_widths, repeatRows=1)
    main_table.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),   C_HEADER_BG),
        ('LINEBELOW',     (0,0), (-1,0),   1.5, C_GREEN),
        ('ALIGN',         (0,0), (-1,-1),  'CENTER'),
        ('VALIGN',        (0,0), (-1,-1),  'MIDDLE'),
        ('ROWBACKGROUNDS',(0,1), (-1,-1),  [C_ROW_NORM, C_ROW_ALT]),
        ('GRID',          (0,0), (-1,-1),  0.3, colors.HexColor("#2A3545")),
        ('TOPPADDING',    (0,0), (-1,-1),  4),
        ('BOTTOMPADDING', (0,0), (-1,-1),  4),
        ('LEFTPADDING',   (0,0), (-1,-1),  4),
        ('RIGHTPADDING',  (0,0), (-1,-1),  4),
        # Linha separadora entre seções
        ('LINEBELOW',     (0,3),  (-1,3),  0.8, C_BLUE),
        ('LINEBELOW',     (0,6),  (-1,6),  0.8, C_BLUE),
        ('LINEBELOW',     (0,9),  (-1,9),  0.8, C_BLUE),
        ('LINEBELOW',     (0,11), (-1,11), 0.8, C_BLUE),
    ]))
    story.append(main_table)
    story.append(sp(0.3))

    story.append(p(
        "⚠️  <i>Preços estimados com base em dados públicos de FUTBIN e FUT.GG para 24/05/2026. "
        "Verifique sempre o mercado ao vivo antes de executar.</i>",
        S_DISCLAIMER))
    story.append(sp(0.4))

    # ══════════════════════════════════════════════════
    # 3. ALOCAÇÃO DO BUDGET
    # ══════════════════════════════════════════════════
    story.append(p("3. ALOCAÇÃO DO BUDGET — 40.000 COINS", S_SECTION))
    story.append(hr(C_GREEN_DARK, 0.5))

    budget_data = [
        ["Categoria", "Investimento (coins)", "Qtd Aprox.", "Objetivo"],
        ["Fodder 86 OVR",     "12.000",  "~9 cartas",  "SBC End of Era / Alta demanda"],
        ["Fodder 87 OVR",     "12.000",  "~7 cartas",  "Thursday Flip / SBC spike"],
        ["Fodder 88 OVR",     "10.000",  "~3 cartas",  "Alta margem, risco médio"],
        ["Evo elegíveis",      "4.000",  "~5 cartas",  "TOTS Career Path Evolution"],
        ["Reserva líquida",    "2.000",  "—",          "Oportunidades imediatas"],
        ["TOTAL",             "40.000",  "~24 cartas", ""],
    ]

    budget_table = Table(budget_data, colWidths=[4.5*cm, 4.0*cm, 3.2*cm, 7.3*cm])
    budget_table.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),  (-1,0),  C_HEADER_BG),
        ('TEXTCOLOR',     (0,0),  (-1,0),  C_GREEN),
        ('FONTNAME',      (0,0),  (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0),  (-1,-1), 8),
        ('ALIGN',         (0,0),  (-1,-1), 'CENTER'),
        ('VALIGN',        (0,0),  (-1,-1), 'MIDDLE'),
        ('FONTNAME',      (0,1),  (-1,-1), 'Helvetica'),
        ('TEXTCOLOR',     (0,1),  (-1,-1), C_LIGHT_GRAY),
        ('ROWBACKGROUNDS',(0,1),  (-1,-2), [C_ROW_NORM, C_ROW_ALT]),
        ('BACKGROUND',    (0,-1), (-1,-1), colors.HexColor("#1A2E20")),
        ('TEXTCOLOR',     (0,-1), (-1,-1), C_GREEN),
        ('FONTNAME',      (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('GRID',          (0,0),  (-1,-1), 0.4, colors.HexColor("#2A3545")),
        ('LINEABOVE',     (0,-1), (-1,-1), 1.2, C_GREEN),
        ('TOPPADDING',    (0,0),  (-1,-1), 4),
        ('BOTTOMPADDING', (0,0),  (-1,-1), 4),
        ('LEFTPADDING',   (0,0),  (-1,-1), 6),
        ('RIGHTPADDING',  (0,0),  (-1,-1), 6),
    ]))
    story.append(budget_table)
    story.append(sp(0.4))

    # ══════════════════════════════════════════════════
    # 4. ESTRATÉGIA DE TIMING
    # ══════════════════════════════════════════════════
    story.append(p("4. ESTRATÉGIA DE TIMING", S_SECTION))
    story.append(hr(C_GREEN_DARK, 0.5))

    timing = [
        ["Horário / Dia", "Ação Recomendada", "Justificativa"],
        ["Dom 24/05 — AGORA\n20h–23h UTC",
         "COMPRAR fodder 86–88\ne cartas Evo elegíveis",
         "Domingo à noite = menor volume de jogadores online → preços no chão"],
        ["Seg–Ter 25–26/05\n06h–10h UTC",
         "MONITORAR preços;\nbuy more se cair mais",
         "Madrugada EU = oportunidade de snipe no mercado ocidental"],
        ["Qua 27/05\nqualquer hora",
         "Preparar listas de venda;\nnão vender ainda",
         "Meio de semana = demanda menor, aguardar pico"],
        ["Qui 28/05\n17h–20h UTC",
         "VENDER fodder 86–87\ndepois dos Rivals Rewards",
         "Thursday Flip clássico: Rivals Rewards liberam coins → players compram fodder"],
        ["Sex 29/05\n15h–19h UTC",
         "VENDER restante do fodder\ne cartas 88+ antes de FUT Champs",
         "Pico semanal: jogadores otimizam time para FUT Champs. TOTS encerra hoje!"],
        ["Sáb–Dom 30–31/05\napós FUT Champs",
         "COMPRAR TOTS 90–92 OVR\nse mercado crashar forte",
         "Pós-FUT Champs = panic selling. Melhor preço do ano para cartas TOTS top"],
    ]

    timing_table = Table(timing, colWidths=[4.0*cm, 5.0*cm, 10.0*cm])
    timing_table.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),   C_HEADER_BG),
        ('TEXTCOLOR',     (0,0), (-1,0),   C_GREEN),
        ('FONTNAME',      (0,0), (-1,0),   'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1),  7.5),
        ('ALIGN',         (0,0), (0,-1),   'CENTER'),
        ('ALIGN',         (1,0), (2,-1),   'LEFT'),
        ('VALIGN',        (0,0), (-1,-1),  'MIDDLE'),
        ('FONTNAME',      (0,1), (-1,-1),  'Helvetica'),
        ('TEXTCOLOR',     (0,1), (0,-1),   C_YELLOW),
        ('FONTNAME',      (0,1), (0,-1),   'Helvetica-Bold'),
        ('TEXTCOLOR',     (1,1), (1,-1),   C_GREEN),
        ('FONTNAME',      (1,1), (1,-1),   'Helvetica-Bold'),
        ('TEXTCOLOR',     (2,1), (2,-1),   C_LIGHT_GRAY),
        ('ROWBACKGROUNDS',(0,1), (-1,-1),  [C_ROW_NORM, C_ROW_ALT]),
        ('GRID',          (0,0), (-1,-1),  0.4, colors.HexColor("#2A3545")),
        ('TOPPADDING',    (0,0), (-1,-1),  5),
        ('BOTTOMPADDING', (0,0), (-1,-1),  5),
        ('LEFTPADDING',   (0,0), (-1,-1),  6),
        ('RIGHTPADDING',  (0,0), (-1,-1),  6),
    ]))
    story.append(timing_table)
    story.append(sp(0.4))

    # ══════════════════════════════════════════════════
    # 5. ESTIMATIVA DE RETORNO 48H
    # ══════════════════════════════════════════════════
    story.append(p("5. ESTIMATIVA DE RETORNO EM 48H", S_SECTION))
    story.append(hr(C_GREEN_DARK, 0.5))

    ret_data = [
        ["Cenário", "Capital Inicial", "Retorno Estimado", "Capital Final", "Lucro Líquido", "ROI"],
        ["🐢 Conservador",  "40.000", "+5.500",  "45.500", "5.500",  "+13,8%"],
        ["⚖️  Moderado",    "40.000", "+9.000",  "49.000", "9.000",  "+22,5%"],
        ["🚀 Otimista",     "40.000", "+15.000", "55.000", "15.000", "+37,5%"],
    ]

    ret_table = Table(ret_data, colWidths=[3.8*cm, 3.2*cm, 3.5*cm, 3.2*cm, 3.2*cm, 2.1*cm])
    ret_table.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),   C_HEADER_BG),
        ('TEXTCOLOR',     (0,0), (-1,0),   C_GREEN),
        ('FONTNAME',      (0,0), (-1,0),   'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1),  8),
        ('ALIGN',         (0,0), (-1,-1),  'CENTER'),
        ('VALIGN',        (0,0), (-1,-1),  'MIDDLE'),
        ('FONTNAME',      (0,1), (-1,-1),  'Helvetica'),
        ('TEXTCOLOR',     (0,1), (-1,-1),  C_LIGHT_GRAY),
        ('TEXTCOLOR',     (0,1), (0,-1),   C_WHITE),
        ('FONTNAME',      (0,1), (0,-1),   'Helvetica-Bold'),
        ('TEXTCOLOR',     (4,1), (5,-1),   C_GREEN),
        ('FONTNAME',      (4,1), (5,-1),   'Helvetica-Bold'),
        ('ROWBACKGROUNDS',(0,1), (-1,-1),  [C_ROW_NORM, C_ROW_ALT]),
        ('GRID',          (0,0), (-1,-1),  0.4, colors.HexColor("#2A3545")),
        ('TOPPADDING',    (0,0), (-1,-1),  5),
        ('BOTTOMPADDING', (0,0), (-1,-1),  5),
    ]))
    story.append(ret_table)
    story.append(sp(0.2))

    story.append(p(
        "<b>Premissas do cenário conservador:</b> venda de 70% das cartas nos alvos mínimos, "
        "30% abaixo do alvo por undersell. "
        "<b>Otimista:</b> venda 100% nos alvos, Thursday Flip funciona perfeitamente e "
        "fodder 87–88 sobe 40%+ antes de sexta com SBCs activos.",
        S_BODY))
    story.append(sp(0.4))

    # ══════════════════════════════════════════════════
    # 6. NOTAS ESPECIAIS — ULTIMATE TOTS WEEK
    # ══════════════════════════════════════════════════
    story.append(p("6. NOTAS ESPECIAIS — SEMANA ULTIMATE TOTS", S_SECTION))
    story.append(hr(C_GREEN_DARK, 0.5))

    story.append(p(
        "Esta é a última semana de promoção da temporada 2025/2026. "
        "O mercado está em modo de <b><font color='#FF4444'>maximum crash</font></b>: "
        "há 60 cartas TOTS em packs simultaneamente, incluindo versões 96–97 OVR de "
        "Mbappé, Messi, Lamine Yamal e outros. O volume de pack-opening é o maior do ano.",
        S_BODY))

    notes = [
        "<b>End of an Era Salah (95 OVR)</b> — SBC requer ~36 squads e ~1,2M de coins em fodder total. "
        "Esse SBC sozinho consome toneladas de fodder 85+ ao longo da semana.",
        "<b>TOTS Career Path Evolution</b> — gratuita, aumenta demanda por cartas base baratas "
        "(75–82 OVR) elegíveis. Procure versões base de Lamine Yamal, Kobbie Mainoo, "
        "Nico Williams e similar.",
        "<b>Champions League Final (31/05)</b> — possível Showdown SBC de última hora lançado "
        "na quinta/sexta-feira. Mantenha ~5.000 coins de reserva para reagir rápido.",
        "<b>Pós-TOTS (a partir de 29/05)</b> — mercado entra em modo 'end of season'. "
        "Cartas TOTS 90–92 OVR que hoje custam 3.000–5.000 são os melhores investimentos "
        "para quem joga até julho (FC 27 announcements).",
        "<b>Domingo à noite (AGORA)</b> é historicamente o melhor momento de compra da semana: "
        "traders europeus dormindo, americanos começando a vender. Janela de 2–3h.",
    ]

    for note in notes:
        story.append(bullet(note, "◆"))

    story.append(sp(0.4))

    # ══════════════════════════════════════════════════
    # 7. 8 REGRAS DE OURO DO TRADE
    # ══════════════════════════════════════════════════
    story.append(p("7. AS 8 REGRAS DE OURO DO TRADE", S_SECTION))
    story.append(hr(C_GREEN_DARK, 0.5))

    rules = [
        ("01", "NUNCA abra packs com coins",
         "A expected value de packs é sempre negativa para o trader. Cada pack aberto "
         "é capital destruído. Use coins exclusivamente no transfer market."),
        ("02", "Sempre aplique a taxa de 5%",
         "EA cobra 5% de tax na venda. Calcule sempre: Lucro = (Preço Venda × 0,95) – Preço Compra. "
         "Qualquer trade que ignore isso queima margem."),
        ("03", "Diversifique — nunca all-in",
         "Espalhe o budget por ao menos 3 categorias de cards. Concentrar em uma única "
         "carta/rating é o maior erro de traders iniciantes."),
        ("04", "Conheça os horários de pico",
         "Preços sobem sexta/sábado (FUT Champs) e caem domingo/segunda (supply alta). "
         "Compre nos vales, venda nos picos — consistentemente."),
        ("05", "Thursday Flip é sagrado",
         "Toda quinta-feira, após as Rivals Rewards (~17h UTC), o mercado floodeia com coins "
         "frescos. Fodder e meta cards sobem 10–30% nas 4h seguintes. Esteja pronto."),
        ("06", "Snipe com paciência — não com pressa",
         "Defina um preço-alvo de buy e espere. Use filtros de preço no Transfer Market. "
         "Um snipe certo vale mais que 10 compras medianas."),
        ("07", "Nunca venda no pânico",
         "Se um evento crashar seu investimento, analise o porquê antes de vender. "
         "Crashes de TOTS são temporários — fodder sempre volta com próximos SBCs."),
        ("08", "Reinvista 80% do lucro, proteja 20%",
         "Ao lucrar, reserve 20% como floor de segurança. Os 80% restantes reinvestidos "
         "com compound growth fazem seu capital dobrar em 1–2 semanas de trading ativo."),
    ]

    for num, titulo, desc in rules:
        rule_data = [[
            Paragraph(num, ParagraphStyle("RNum", parent=styles['Normal'],
                fontSize=16, textColor=C_GREEN, fontName="Helvetica-Bold",
                alignment=TA_CENTER, leading=18)),
            [Paragraph(titulo, S_BODY_BOLD), Paragraph(desc, S_BODY)]
        ]]
        rule_table = Table(rule_data, colWidths=[1.5*cm, 17.5*cm])
        rule_table.setStyle(TableStyle([
            ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
            ('BACKGROUND',    (0,0), (0,0),   C_DARK_GRAY),
            ('BACKGROUND',    (1,0), (1,0),   C_ROW_ALT),
            ('LINEABOVE',     (0,0), (-1,0),  0.4, colors.HexColor("#2A3545")),
            ('LINEBELOW',     (0,0), (-1,0),  0.4, colors.HexColor("#2A3545")),
            ('TOPPADDING',    (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING',   (0,0), (-1,-1), 8),
            ('RIGHTPADDING',  (0,0), (-1,-1), 8),
        ]))
        story.append(rule_table)

    story.append(sp(0.5))

    # ══════════════════════════════════════════════════
    # 8. RESUMO EXECUTIVO
    # ══════════════════════════════════════════════════
    story.append(p("8. RESUMO EXECUTIVO — AÇÃO IMEDIATA", S_SECTION))
    story.append(hr(C_GREEN_DARK, 0.5))

    summary_data = [
        ["🎯 COMPRAR AGORA (Dom 24/05, 20h–23h UTC)", ""],
        ["Ação", "Detalhe"],
        ["Comprar 9 cartas 86 OVR (Konaté, Tonali, Nuno Mendes…)",
         "~12.000 coins — fodder máxima demanda"],
        ["Comprar 7 cartas 87 OVR (Bronze, Kerr, Lavelle…)",
         "~12.000 coins — Thursday Flip"],
        ["Comprar 3 cartas 88 OVR (Paredes, Endler, Saka…)",
         "~10.000 coins — margem alta"],
        ["Comprar 5 cartas Evo elegíveis 81–82 OVR",
         "~4.000 coins — TOTS Career Path"],
        ["Manter 2.000 coins de reserva",
         "Snipe oportunidades e CL Final SBC"],
    ]

    sum_table = Table(summary_data, colWidths=[11.0*cm, 8.0*cm])
    sum_table.setStyle(TableStyle([
        ('SPAN',          (0,0), (-1,0)),
        ('BACKGROUND',    (0,0), (-1,0),   colors.HexColor("#1A2E20")),
        ('TEXTCOLOR',     (0,0), (-1,0),   C_GREEN),
        ('FONTNAME',      (0,0), (-1,0),   'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,0),   9),
        ('ALIGN',         (0,0), (-1,0),   'CENTER'),
        ('BACKGROUND',    (0,1), (-1,1),   C_HEADER_BG),
        ('TEXTCOLOR',     (0,1), (-1,1),   C_GREEN),
        ('FONTNAME',      (0,1), (-1,1),   'Helvetica-Bold'),
        ('FONTSIZE',      (0,1), (-1,-1),  8),
        ('FONTNAME',      (0,2), (0,-1),   'Helvetica-Bold'),
        ('TEXTCOLOR',     (0,2), (0,-1),   C_WHITE),
        ('TEXTCOLOR',     (1,2), (1,-1),   C_YELLOW),
        ('ROWBACKGROUNDS',(0,2), (-1,-1),  [C_ROW_NORM, C_ROW_ALT]),
        ('GRID',          (0,0), (-1,-1),  0.4, colors.HexColor("#2A3545")),
        ('ALIGN',         (0,0), (-1,-1),  'LEFT'),
        ('TOPPADDING',    (0,0), (-1,-1),  5),
        ('BOTTOMPADDING', (0,0), (-1,-1),  5),
        ('LEFTPADDING',   (0,0), (-1,-1),  8),
        ('RIGHTPADDING',  (0,0), (-1,-1),  8),
    ]))
    story.append(sum_table)
    story.append(sp(0.5))

    # ══════════════════════════════════════════════════
    # 9. DISCLAIMER
    # ══════════════════════════════════════════════════
    story.append(hr(C_MID_GRAY, 0.5))
    story.append(sp(0.2))
    story.append(p("⚠️  DISCLAIMER", S_SUBSECTION))
    story.append(p(
        "Este relatório é produzido exclusivamente para fins educacionais e de entretenimento. "
        "Os preços, margens e estimativas de retorno apresentados são baseados em dados públicos "
        "de FUTBIN.com, FUT.GG, Teamgullit.com e outras fontes de acesso livre disponíveis em "
        "24/05/2026. O mercado do EA FC 26 Ultimate Team é altamente volátil e pode mudar "
        "drasticamente em minutos após novos eventos, patches ou anúncios da EA Sports. "
        "O autor não se responsabiliza por perdas decorrentes de decisões de trading baseadas "
        "neste documento. Sempre verifique os preços ao vivo antes de realizar qualquer transação. "
        "Trading de coins é feito inteiramente dentro do jogo e não envolve dinheiro real.",
        S_DISCLAIMER))

    story.append(sp(0.2))
    story.append(p(
        f"Relatório gerado automaticamente em {REPORT_DATE_DISPLAY} UTC  |  "
        "Repositório: github.com/kaiohsferreira/fifa-trading",
        ParagraphStyle("Footer", parent=styles['Normal'],
            fontSize=7, textColor=C_MID_GRAY, fontName="Helvetica",
            alignment=TA_CENTER)))

    return story


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="Relatório Trading EA FC 26",
        author="FIFA Trading Bot",
        subject="Análise de Mercado Ultimate Team"
    )

    # Fundo escuro em cada página
    def page_bg(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(C_BG_DARK)
        canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        # Barra verde no topo
        canvas.setFillColor(C_GREEN)
        canvas.rect(0, PAGE_H - 0.35*cm, PAGE_W, 0.35*cm, fill=1, stroke=0)
        # Barra verde no rodapé
        canvas.rect(0, 0, PAGE_W, 0.25*cm, fill=1, stroke=0)
        canvas.restoreState()

    story = build_story()
    doc.build(story, onFirstPage=page_bg, onLaterPages=page_bg)
    print(f"PDF gerado: {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    main()
