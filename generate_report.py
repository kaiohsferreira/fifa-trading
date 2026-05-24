#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.graphics import renderPDF
from datetime import datetime

# ── Config ─────────────────────────────────────────────────────────────────
REPORT_DATE     = "24/05/2026 08:01"
REPORT_FILENAME = "relatorio-trading-2026-05-24-08h.pdf"
BUDGET          = 40_000

# ── Cores EA FC ─────────────────────────────────────────────────────────────
EA_GREEN   = colors.HexColor("#00D166")
EA_DARK    = colors.HexColor("#0A0A0A")
EA_GREY    = colors.HexColor("#1C1C1C")
EA_LGREY   = colors.HexColor("#2E2E2E")
EA_ACCENT  = colors.HexColor("#FFD700")
EA_RED     = colors.HexColor("#E83A3A")
EA_BLUE    = colors.HexColor("#4DB8FF")
EA_WHITE   = colors.HexColor("#F0F0F0")
TABLE_HEAD = colors.HexColor("#005C30")
TABLE_ALT  = colors.HexColor("#111111")
TABLE_NORM = colors.HexColor("#1A1A1A")

# ── Estilos ──────────────────────────────────────────────────────────────────
def build_styles():
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=EA_GREEN,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        fontName="Helvetica",
        fontSize=11,
        textColor=EA_ACCENT,
        alignment=TA_CENTER,
        spaceAfter=2,
    )
    date_style = ParagraphStyle(
        "DateStyle",
        fontName="Helvetica",
        fontSize=10,
        textColor=EA_WHITE,
        alignment=TA_CENTER,
        spaceAfter=0,
    )
    section_style = ParagraphStyle(
        "SectionStyle",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=EA_GREEN,
        spaceBefore=14,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "BodyStyle",
        fontName="Helvetica",
        fontSize=9,
        textColor=EA_WHITE,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
    )
    bullet_style = ParagraphStyle(
        "BulletStyle",
        fontName="Helvetica",
        fontSize=9,
        textColor=EA_WHITE,
        leading=14,
        leftIndent=14,
        spaceAfter=3,
    )
    gold_style = ParagraphStyle(
        "GoldStyle",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=EA_ACCENT,
        leading=14,
        leftIndent=14,
        spaceAfter=3,
    )
    disclaimer_style = ParagraphStyle(
        "DisclaimerStyle",
        fontName="Helvetica-Oblique",
        fontSize=8,
        textColor=colors.HexColor("#888888"),
        alignment=TA_CENTER,
        spaceAfter=2,
    )
    return {
        "title":      title_style,
        "subtitle":   subtitle_style,
        "date":       date_style,
        "section":    section_style,
        "body":       body_style,
        "bullet":     bullet_style,
        "gold":       gold_style,
        "disclaimer": disclaimer_style,
    }

# ── Cabeçalho de seção colorido ──────────────────────────────────────────────
def section_header(text, styles):
    return [
        HRFlowable(width="100%", thickness=1, color=EA_GREEN, spaceAfter=4),
        Paragraph(text, styles["section"]),
    ]

# ── Página de fundo escuro ────────────────────────────────────────────────────
def draw_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(EA_DARK)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # Faixa verde topo
    canvas.setFillColor(EA_GREEN)
    canvas.rect(0, A4[1] - 6, A4[0], 6, fill=1, stroke=0)
    # Faixa verde rodapé
    canvas.rect(0, 0, A4[0], 4, fill=1, stroke=0)
    # Número de página
    canvas.setFillColor(EA_GREY)
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(A4[0] - 1.5*cm, 0.6*cm,
                           f"Página {doc.page} | EA FC 26 Trading Report © {REPORT_DATE[:4]}")
    canvas.restoreState()

# ── Tabela principal de cartas ────────────────────────────────────────────────
def build_cards_table():
    headers = [
        "Jogador", "Rating", "Clube", "Compra\n(coins)",
        "Venda\n(coins)", "Lucro liq.\n(−5% EA)", "Estratégia"
    ]

    data = [
        # nome, rating, clube, compra, venda, notas
        ["Stanislav Lobotka",   "83", "Napoli",         "750",   "1.400",  "+600",  "SBC fodder semanal"],
        ["Giovanni Di Lorenzo", "83", "Napoli",         "750",   "1.350",  "+555",  "SBC fodder italiano"],
        ["Artem Dovbyk",        "83", "Roma",           "750",   "1.300",  "+485",  "ST fodder SBCs"],
        ["Dominik Szoboszlai",  "83", "Liverpool",      "750",   "1.450",  "+628",  "Premier League fodder"],
        ["Hugo Ekitike",        "83", "PSG",            "750",   "1.300",  "+485",  "Ligue 1 fodder"],
        ["Bradley Barcola",     "84", "PSG",            "800",   "1.600",  "+720",  "Ligue 1 – alta demanda"],
        ["Josko Gvardiol",      "84", "Man. City",      "800",   "1.550",  "+673",  "Def. PL fodder"],
        ["Moussa Diaby",        "84", "Al-Ittihad",     "800",   "1.500",  "+625",  "Fodder SBC mid-tier"],
        ["Fabián Ruiz",         "85", "PSG",            "900",   "2.000",  "+1.000","Top SBC 85-rated"],
        ["Marcus Thuram",       "85", "Inter Milan",    "900",   "1.900",  "+905",  "Serie A ST fodder"],
        ["Scott McTominay",     "85", "Napoli",         "900",   "1.900",  "+905",  "PL/IT dupla liga"],
        ["Hakan Çalhanoğlu",    "86", "Inter Milan",    "950",   "2.400",  "+1.330","CDM premium SBC"],
        ["Sandro Tonali",       "86", "Newcastle",      "950",   "2.300",  "+1.235","CDM PL demand"],
        ["Ibrahima Konaté",     "86", "Liverpool",      "1.000", "2.500",  "+1.375","CB PL – alta demanda"],
        ["Marc-André ter Stegen","86","Barcelona",      "950",   "2.200",  "+1.140","GK – demanda SBC"],
    ]

    # Calcula lucro real com -5% EA
    def calc_profit(compra_str, venda_str):
        compra = int(compra_str.replace(".", ""))
        venda  = int(venda_str.replace(".", ""))
        lucro  = int(venda * 0.95 - compra)
        return f"+{lucro:,}".replace(",", ".")

    table_data = [headers]
    for row in data:
        compra = row[3]
        venda  = row[4]
        lucro  = calc_profit(compra, venda)
        table_data.append([
            row[0], row[1], row[2], row[3], row[4], lucro, row[6]
        ])

    col_widths = [3.8*cm, 1.3*cm, 3.5*cm, 1.8*cm, 1.8*cm, 2.0*cm, 3.8*cm]

    style = TableStyle([
        # Cabeçalho
        ("BACKGROUND",   (0, 0), (-1, 0), TABLE_HEAD),
        ("TEXTCOLOR",    (0, 0), (-1, 0), EA_WHITE),
        ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0), 8),
        ("ALIGN",        (0, 0), (-1, 0), "CENTER"),
        ("VALIGN",       (0, 0), (-1, 0), "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, 0), 5),
        ("BOTTOMPADDING",(0, 0), (-1, 0), 5),
        # Linhas alternadas
        *[("BACKGROUND", (0, i), (-1, i), TABLE_ALT if i % 2 == 0 else TABLE_NORM)
          for i in range(1, len(table_data))],
        ("TEXTCOLOR",    (0, 1), (-1, -1), EA_WHITE),
        ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",     (0, 1), (-1, -1), 7.5),
        ("ALIGN",        (1, 1), (5, -1), "CENTER"),
        ("ALIGN",        (0, 1), (0, -1), "LEFT"),
        ("ALIGN",        (6, 1), (6, -1), "LEFT"),
        ("VALIGN",       (0, 1), (-1, -1), "MIDDLE"),
        ("TOPPADDING",   (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 1), (-1, -1), 4),
        # Coluna lucro em verde
        ("TEXTCOLOR",    (5, 1), (5, -1), EA_GREEN),
        ("FONTNAME",     (5, 1), (5, -1), "Helvetica-Bold"),
        # Grade
        ("GRID",         (0, 0), (-1, -1), 0.4, EA_LGREY),
        ("LINEBELOW",    (0, 0), (-1, 0),  1.2, EA_GREEN),
        ("ROWBACKGROUNDS",(0, 0), (-1, -1), [TABLE_HEAD]),
    ])

    return Table(table_data, colWidths=col_widths, style=style, repeatRows=1)

# ── Tabela resumo de retorno ──────────────────────────────────────────────────
def build_return_table():
    headers = ["Cenário", "Estratégia", "Capital Inicial", "Retorno Est.", "Capital Final"]
    data = [
        headers,
        ["Conservador 24h", "SBC Fodder 83-84 × 20 unid.", "40.000", "+15%",  "46.000"],
        ["Moderado 24h",    "SBC Fodder 84-86 misto × 15", "40.000", "+22%",  "48.800"],
        ["Conservador 48h", "SBC Fodder + TOTS crash buy",  "40.000", "+30%",  "52.000"],
        ["Otimista 48h",    "Multi-tier + Evolução + flip",  "40.000", "+55%",  "62.000"],
    ]
    col_widths = [3.5*cm, 6.5*cm, 3.0*cm, 2.5*cm, 3.0*cm]
    style = TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0), TABLE_HEAD),
        ("TEXTCOLOR",    (0, 0), (-1, 0), EA_WHITE),
        ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0), 8.5),
        ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        *[("BACKGROUND", (0, i), (-1, i), TABLE_ALT if i % 2 == 0 else TABLE_NORM)
          for i in range(1, len(data))],
        ("TEXTCOLOR",    (0, 1), (-1, -1), EA_WHITE),
        ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",     (0, 1), (-1, -1), 8),
        ("TEXTCOLOR",    (3, 1), (3, -1), EA_GREEN),
        ("FONTNAME",     (3, 1), (3, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",    (4, 1), (4, -1), EA_ACCENT),
        ("FONTNAME",     (4, 1), (4, -1), "Helvetica-Bold"),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("GRID",         (0, 0), (-1, -1), 0.4, EA_LGREY),
        ("LINEBELOW",    (0, 0), (-1, 0),  1.2, EA_GREEN),
    ])
    return Table(data, colWidths=col_widths, style=style)

# ── Conteúdo do PDF ───────────────────────────────────────────────────────────
def build_content(styles):
    story = []

    # ── HEADER BLOCK ─────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph("⚽  EA FC 26 ULTIMATE TEAM", styles["title"]))
    story.append(Paragraph("RELATÓRIO DIÁRIO DE TRADING", styles["subtitle"]))
    story.append(Paragraph(f"Gerado em: {REPORT_DATE} UTC", styles["date"]))
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width="100%", thickness=2, color=EA_GREEN, spaceAfter=8))

    # ── 1. CONTEXTO DO MERCADO ────────────────────────────────────────────────
    story += section_header("1. CONTEXTO DO MERCADO — 24 MAI 2026", styles)

    story.append(Paragraph(
        "<b><font color='#FFD700'>🏆 ULTIMATE TOTS ativo</font></b> – Lançado em 22/05/2026 às 18h BST, "
        "o Ultimate TOTS traz 38 cartas com ratings de <b>92 a 97</b> (Messi, Ronaldo, Mbappé, Haaland, "
        "Modric). Esta é a última semana de promoção da temporada, com impacto maciço no mercado.",
        styles["body"]
    ))
    story.append(Paragraph(
        "<b><font color='#4DB8FF'>📉 MARKET CRASH EM CURSO</font></b> – Com a abertura em massa de "
        "pacotes durante o Ultimate TOTS, o mercado está inundado de cartas 83-88 rated. Preços de "
        "fodder em <b>mínimas históricas</b> — janela ideal para compra.",
        styles["body"]
    ))
    story.append(Paragraph(
        "<b><font color='#00D166'>📋 SBCs ATIVOS</font></b> – End of an Era SBCs em curso "
        "(Salah 96, Griezmann 94, Robertson 93). Exigem fodder 83-86 em grandes quantidades, "
        "criando pressão de demanda contínua durante toda a semana.",
        styles["body"]
    ))

    events_data = [
        ["Evento",         "Status",     "Impacto no Mercado"],
        ["Ultimate TOTS",  "🟢 ATIVO",   "Crash de 83-88 rated; alta procura de SBC"],
        ["End of an Era",  "🟢 ATIVO",   "Demanda de fodder 83-86 para unlock"],
        ["RTTF (UEFA)",    "🟢 ATIVO",   "Cartas dinâmicas — buy antes das partidas"],
        ["Path to Glory",  "🟢 ATIVO",   "Upgrades baseados em ligas domésticas"],
        ["Fantasy FC",     "🟡 EXPIRA 29/05","Últimos dias — liquide posições"],
    ]
    tbl = Table(events_data,
                colWidths=[4.5*cm, 2.5*cm, 11.5*cm],
                style=TableStyle([
                    ("BACKGROUND",  (0,0),(-1,0), TABLE_HEAD),
                    ("TEXTCOLOR",   (0,0),(-1,0), EA_WHITE),
                    ("FONTNAME",    (0,0),(-1,0), "Helvetica-Bold"),
                    ("FONTSIZE",    (0,0),(-1,-1), 8),
                    ("ALIGN",       (0,0),(-1,-1), "CENTER"),
                    ("VALIGN",      (0,0),(-1,-1), "MIDDLE"),
                    *[("BACKGROUND",(0,i),(-1,i), TABLE_ALT if i%2==0 else TABLE_NORM)
                      for i in range(1, len(events_data))],
                    ("TEXTCOLOR",   (0,1),(-1,-1), EA_WHITE),
                    ("TOPPADDING",  (0,0),(-1,-1), 4),
                    ("BOTTOMPADDING",(0,0),(-1,-1), 4),
                    ("GRID",        (0,0),(-1,-1), 0.4, EA_LGREY),
                    ("LINEBELOW",   (0,0),(-1,0),  1.2, EA_GREEN),
                ]))
    story.append(tbl)
    story.append(Spacer(1, 0.3*cm))

    # ── 2. TABELA DE CARTAS RECOMENDADAS ─────────────────────────────────────
    story += section_header("2. CARTAS RECOMENDADAS — BUDGET: 40.000 coins", styles)
    story.append(Paragraph(
        "Preços baseados em dados de <b>FUTBIN / FUT.GG</b> às 08:01 UTC. "
        "Lucro líquido já descontado a taxa de <b>5% EA</b>. "
        "Priorize cartas em <b>mínimos de mercado</b> (crash pós-TOTS pack-opening).",
        styles["body"]
    ))
    story.append(Spacer(1, 0.2*cm))
    story.append(build_cards_table())
    story.append(Spacer(1, 0.3*cm))

    # ── 3. ESTRATÉGIA DE TIMING ───────────────────────────────────────────────
    story += section_header("3. ESTRATÉGIA DE TIMING", styles)

    timing_data = [
        ["Janela",              "Ação",       "Detalhes"],
        ["Dom 24/05 – 08h-14h", "🛒 COMPRAR", "Máximo pack-opening weekend; preços no fundo"],
        ["Dom 24/05 – 19h-23h", "📦 SEGURAR", "Demanda SBC noturna começa a subir"],
        ["Seg 25/05 – 09h-12h", "💰 VENDER",  "Pico de SBC completion antes do reset semanal"],
        ["Qui 28/05 – 13h",     "🛒 COMPRAR", "Rivals Rewards despejam cartas; preços caem"],
        ["Sex 29/05 – 17h-21h", "💰 VENDER",  "Champs Weekend pré-compra; demanda máxima"],
        ["Sex 29/05 – 18h+",    "⚠️ ATENÇÃO", "Fantasy FC expira; liquidar posições restantes"],
    ]
    tbl2 = Table(timing_data,
                 colWidths=[4.0*cm, 2.8*cm, 11.7*cm],
                 style=TableStyle([
                     ("BACKGROUND",  (0,0),(-1,0), TABLE_HEAD),
                     ("TEXTCOLOR",   (0,0),(-1,0), EA_WHITE),
                     ("FONTNAME",    (0,0),(-1,0), "Helvetica-Bold"),
                     ("FONTSIZE",    (0,0),(-1,-1), 8),
                     ("ALIGN",       (1,0),(1,-1), "CENTER"),
                     ("ALIGN",       (0,0),(0,-1), "CENTER"),
                     ("ALIGN",       (2,0),(2,-1), "LEFT"),
                     ("VALIGN",      (0,0),(-1,-1), "MIDDLE"),
                     *[("BACKGROUND",(0,i),(-1,i), TABLE_ALT if i%2==0 else TABLE_NORM)
                       for i in range(1, len(timing_data))],
                     ("TEXTCOLOR",   (0,1),(-1,-1), EA_WHITE),
                     ("TOPPADDING",  (0,0),(-1,-1), 4),
                     ("BOTTOMPADDING",(0,0),(-1,-1), 4),
                     ("GRID",        (0,0),(-1,-1), 0.4, EA_LGREY),
                     ("LINEBELOW",   (0,0),(-1,0),  1.2, EA_GREEN),
                 ]))
    story.append(tbl2)
    story.append(Spacer(1, 0.3*cm))

    # ── 4. RETORNO ESTIMADO 48H ───────────────────────────────────────────────
    story += section_header("4. ESTIMATIVA DE RETORNO EM 48H", styles)
    story.append(Paragraph(
        "Projeções baseadas em market trends históricos do TOTS + análise de SBC demand atual. "
        "Capital inicial: <b>40.000 coins</b>. Todos os valores em coins (após taxa EA de 5%).",
        styles["body"]
    ))
    story.append(Spacer(1, 0.2*cm))
    story.append(build_return_table())
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "💡 <b>Recomendação:</b> Alocar <b>60% do budget (24.000 coins)</b> em 83-84 rated fodder "
        "(mass buy) e <b>40% (16.000 coins)</b> em 85-86 rated premium fodder para SBCs End of an Era.",
        styles["body"]
    ))

    # ── 5. ESTRATÉGIAS DETALHADAS ─────────────────────────────────────────────
    story += section_header("5. ESTRATÉGIAS DETALHADAS", styles)

    story.append(Paragraph("<b><font color='#FFD700'>🔄 SBC Fodder Flipping (principal estratégia)</font></b>", styles["body"]))
    for item in [
        "Compre em <b>massa</b> 83-84 rated cards a 750 coins (mínimo TOTS crash)",
        "Alvo: 20–30 cartas por sessão de compra (total: ~15.000-20.000 coins)",
        "Venda unitária a 1.300–1.500 coins durante picos de SBC demand (noite/Seg)",
        "Lucro líquido por carta: ~500-650 coins | Retorno potencial: 10.000-15.000 coins",
        "Repita o ciclo: crash (Dom manhã) → venda (Dom noite/Seg manhã)",
    ]:
        story.append(Paragraph(f"  ▸ {item}", styles["bullet"]))

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("<b><font color='#4DB8FF'>📈 Evolution Card Investing</font></b>", styles["body"]))
    for item in [
        "Identifique jogadores 83-84 rated elegíveis para próximas Evolutions",
        "Compre antes do anúncio oficial (vazamentos surgem Qua/Qui)",
        "Preço médio de saída: 2x–3x o valor de compra após anúncio",
        "Exemplo: card a 750 → 1.800-2.200 após ser elegível para Evolution",
    ]:
        story.append(Paragraph(f"  ▸ {item}", styles["bullet"]))

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("<b><font color='#00D166'>📊 Thursday Flipping (Rivals Rewards)</font></b>", styles["body"]))
    for item in [
        "Quinta-feira 13h UTC: Rivals Rewards despejados → preços caem 15-25%",
        "Compre 85-86 rated cards durante a janela de crash (13h-16h)",
        "Venda na noite de Sexta (17h-22h UTC) quando demanda do Champs sobe",
        "Margem esperada: +20-30% em 24-48h com risco moderado",
    ]:
        story.append(Paragraph(f"  ▸ {item}", styles["bullet"]))

    # ── 6. DISTRIBUIÇÃO DO BUDGET ─────────────────────────────────────────────
    story += section_header("6. DISTRIBUIÇÃO DO BUDGET (40.000 coins)", styles)

    budget_data = [
        ["Estratégia",           "Alocação", "Coins", "Objetivo"],
        ["SBC Fodder 83-84",     "50%",      "20.000","Mass flip durante SBC rush"],
        ["SBC Fodder 85-86",     "30%",      "12.000","End of Era + premium SBCs"],
        ["Evolution Investing",  "10%",      "4.000", "Cards elegíveis pré-anúncio"],
        ["Reserva / Oportunidade","10%",     "4.000", "Deals inesperados / RTTF"],
    ]
    tbl3 = Table(budget_data,
                 colWidths=[4.5*cm, 2.5*cm, 2.5*cm, 9.0*cm],
                 style=TableStyle([
                     ("BACKGROUND",  (0,0),(-1,0), TABLE_HEAD),
                     ("TEXTCOLOR",   (0,0),(-1,0), EA_WHITE),
                     ("FONTNAME",    (0,0),(-1,0), "Helvetica-Bold"),
                     ("FONTSIZE",    (0,0),(-1,-1), 8.5),
                     ("ALIGN",       (1,0),(2,-1), "CENTER"),
                     ("ALIGN",       (0,0),(0,-1), "LEFT"),
                     ("ALIGN",       (3,0),(3,-1), "LEFT"),
                     ("VALIGN",      (0,0),(-1,-1), "MIDDLE"),
                     *[("BACKGROUND",(0,i),(-1,i), TABLE_ALT if i%2==0 else TABLE_NORM)
                       for i in range(1, len(budget_data))],
                     ("TEXTCOLOR",   (0,1),(-1,-1), EA_WHITE),
                     ("TEXTCOLOR",   (2,1),(2,-1), EA_ACCENT),
                     ("FONTNAME",    (2,1),(2,-1), "Helvetica-Bold"),
                     ("TOPPADDING",  (0,0),(-1,-1), 5),
                     ("BOTTOMPADDING",(0,0),(-1,-1), 5),
                     ("GRID",        (0,0),(-1,-1), 0.4, EA_LGREY),
                     ("LINEBELOW",   (0,0),(-1,0),  1.2, EA_GREEN),
                 ]))
    story.append(tbl3)
    story.append(Spacer(1, 0.3*cm))

    # ── 7. 8 REGRAS DE OURO DO TRADE ─────────────────────────────────────────
    story += section_header("7. ⭐ 8 REGRAS DE OURO DO TRADE", styles)

    rules = [
        ("1", "NUNCA compre na alta",
         "Após anúncio de SBC, aguarde 30-60 min para os preços normalizarem antes de comprar fodder."),
        ("2", "VENDA antes do pico máximo",
         "Não seja ganancioso: se atingiu +40% de lucro, venda. O mercado pode reverter a qualquer momento."),
        ("3", "DIVERSIFIQUE o portfólio",
         "Não concentre todo o budget em um único jogador ou rating. Distribua o risco."),
        ("4", "ESTUDE os horários de mercado",
         "Manhãs de domingo = preços mais baixos (pack opening). Noite de sexta = preços mais altos."),
        ("5", "RESPEITE a taxa EA de 5%",
         "Nunca calcule seu lucro sem descontar 5% do valor de venda. Isso define sua margem real."),
        ("6", "MONITORE vazamentos",
         "Siga @FUT_Alerts e fut.gg/news para Evolution e SBC leaks — antecipe o mercado 2-3h."),
        ("7", "EVITE cartas de nicho",
         "Priorize ligas populares (PL, La Liga, Serie A). Cartas exóticas têm menor liquidez."),
        ("8", "DEFINA stop-loss",
         "Se uma carta cair 30% do preço de compra, venda e assuma o prejuízo. Não segure 'esperando'."),
    ]

    for num, title, desc in rules:
        story.append(Paragraph(
            f'<font color="#FFD700"><b>Regra {num}:</b></font> '
            f'<font color="#00D166"><b>{title}</b></font> — {desc}',
            styles["bullet"]
        ))
        story.append(Spacer(1, 0.1*cm))

    story.append(Spacer(1, 0.3*cm))

    # ── 8. DISCLAIMER ─────────────────────────────────────────────────────────
    story += section_header("8. DISCLAIMER", styles)
    story.append(Paragraph(
        "Este relatório é gerado automaticamente com base em dados públicos de mercado "
        "(FUTBIN, FUT.GG, TeamGullit, Reddit) e tem caráter exclusivamente informativo. "
        "Preços de cartas em EA FC 26 Ultimate Team são altamente voláteis e podem variar "
        "significativamente em minutos. O autor não garante lucros e não se responsabiliza "
        "por perdas de coins resultantes de decisões de trading baseadas neste documento. "
        "Este relatório NÃO é aconselhamento financeiro. "
        "EA SPORTS, EA FC e Ultimate Team são marcas registradas da Electronic Arts Inc.",
        styles["disclaimer"]
    ))
    story.append(Spacer(1, 0.2*cm))
    story.append(HRFlowable(width="100%", thickness=1, color=EA_GREEN))
    story.append(Spacer(1, 0.1*cm))
    story.append(Paragraph(
        f"Relatório gerado em {REPORT_DATE} UTC  |  Budget: {BUDGET:,} coins  |  "
        "Fonte: FUTBIN · FUT.GG · TeamGullit · Reddit · OperationSports",
        styles["disclaimer"]
    ))

    return story

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    doc = SimpleDocTemplate(
        REPORT_FILENAME,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.2*cm,
        bottomMargin=1.5*cm,
    )

    styles  = build_styles()
    content = build_content(styles)

    doc.build(content, onFirstPage=draw_background, onLaterPages=draw_background)
    print(f"✅ PDF gerado: {REPORT_FILENAME}")

if __name__ == "__main__":
    main()
