#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak
from datetime import datetime

# ─── Configurações ────────────────────────────────────────────────────────────
REPORT_DATETIME = "25/05/2026 08:05"
PDF_FILENAME = "relatorio-trading-2026-05-25-08h.pdf"

# Paleta de cores EA FC / Verde-escuro
VERDE_ESCURO   = colors.HexColor("#0a4d29")
VERDE_MEDIO    = colors.HexColor("#1a7a3e")
VERDE_CLARO    = colors.HexColor("#2ecc71")
DOURADO        = colors.HexColor("#f5c518")
AMARELO_ALERTA = colors.HexColor("#f39c12")
VERMELHO       = colors.HexColor("#e74c3c")
CINZA_ESCURO   = colors.HexColor("#1c1c1c")
CINZA_MEDIO    = colors.HexColor("#2d2d2d")
CINZA_CLARO    = colors.HexColor("#f5f5f5")
BRANCO         = colors.white

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_FILENAME,
        pagesize=A4,
        leftMargin=1.5*cm,
        rightMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm,
    )

    styles = getSampleStyleSheet()

    # ── Estilos personalizados ────────────────────────────────────────────────
    titulo_estilo = ParagraphStyle(
        "TituloPrincipal",
        parent=styles["Title"],
        fontSize=22,
        textColor=BRANCO,
        backColor=VERDE_ESCURO,
        alignment=TA_CENTER,
        spaceAfter=4,
        spaceBefore=4,
        fontName="Helvetica-Bold",
        borderPad=8,
    )

    subtitulo_estilo = ParagraphStyle(
        "Subtitulo",
        parent=styles["Normal"],
        fontSize=12,
        textColor=DOURADO,
        alignment=TA_CENTER,
        spaceAfter=2,
        fontName="Helvetica-Bold",
    )

    data_estilo = ParagraphStyle(
        "DataHora",
        parent=styles["Normal"],
        fontSize=10,
        textColor=CINZA_ESCURO,
        alignment=TA_CENTER,
        spaceAfter=10,
        fontName="Helvetica",
    )

    secao_titulo = ParagraphStyle(
        "SecaoTitulo",
        parent=styles["Heading1"],
        fontSize=13,
        textColor=BRANCO,
        backColor=VERDE_MEDIO,
        alignment=TA_LEFT,
        spaceAfter=6,
        spaceBefore=14,
        fontName="Helvetica-Bold",
        leftIndent=-4,
        borderPad=6,
    )

    subsecao_titulo = ParagraphStyle(
        "SubsecaoTitulo",
        parent=styles["Heading2"],
        fontSize=11,
        textColor=VERDE_ESCURO,
        alignment=TA_LEFT,
        spaceAfter=4,
        spaceBefore=8,
        fontName="Helvetica-Bold",
    )

    corpo = ParagraphStyle(
        "Corpo",
        parent=styles["Normal"],
        fontSize=9.5,
        textColor=CINZA_ESCURO,
        alignment=TA_JUSTIFY,
        spaceAfter=5,
        leading=14,
        fontName="Helvetica",
    )

    bullet_estilo = ParagraphStyle(
        "Bullet",
        parent=styles["Normal"],
        fontSize=9.5,
        textColor=CINZA_ESCURO,
        alignment=TA_LEFT,
        leftIndent=14,
        bulletIndent=4,
        spaceAfter=3,
        leading=14,
        fontName="Helvetica",
    )

    alerta_estilo = ParagraphStyle(
        "Alerta",
        parent=styles["Normal"],
        fontSize=9,
        textColor=CINZA_ESCURO,
        backColor=colors.HexColor("#fff9e6"),
        alignment=TA_JUSTIFY,
        spaceAfter=5,
        leading=13,
        fontName="Helvetica",
        borderPad=6,
        borderWidth=1,
        borderColor=AMARELO_ALERTA,
    )

    disclaimer_estilo = ParagraphStyle(
        "Disclaimer",
        parent=styles["Normal"],
        fontSize=8,
        textColor=colors.HexColor("#777777"),
        alignment=TA_JUSTIFY,
        spaceAfter=4,
        leading=12,
        fontName="Helvetica",
    )

    regra_titulo_estilo = ParagraphStyle(
        "RegraTitulo",
        parent=styles["Normal"],
        fontSize=9.5,
        textColor=DOURADO,
        fontName="Helvetica-Bold",
        spaceAfter=1,
    )

    # ── Montagem do conteúdo ──────────────────────────────────────────────────
    story = []

    # ── CABEÇALHO ─────────────────────────────────────────────────────────────
    story.append(Paragraph("⚽  EA FC 26 — RELATÓRIO DE TRADING", titulo_estilo))
    story.append(Paragraph("Ultimate Team | Análise de Mercado Diária", subtitulo_estilo))
    story.append(Paragraph(f"Gerado em: {REPORT_DATETIME} UTC  |  Budget: 40.000 coins  |  Meta: +30-50% em 48h", data_estilo))
    story.append(HRFlowable(width="100%", thickness=2, color=DOURADO, spaceAfter=10))

    # ── SEÇÃO 1: CONTEXTO DO MERCADO ──────────────────────────────────────────
    story.append(Paragraph("1. CONTEXTO DO MERCADO — 25/05/2026", secao_titulo))

    story.append(Paragraph(
        "O mercado do EA FC 26 Ultimate Team encontra-se em fase <b>TOTS Ultimate (Team of the Season)</b>, "
        "o maior evento do ano. O Ultimate TOTS foi lançado em 22 de maio de 2026 e permanece ativo até "
        "<b>29 de maio de 2026</b>. Paralelamente, os SBCs <b>End of an Era</b> estão sendo liberados "
        "gradativamente (Salah 96 OVR, Griezmann 94 OVR, Robertson 93 OVR), criando picos de demanda "
        "por fodder de rating médio e alto.",
        corpo
    ))

    story.append(Paragraph(
        "Com a chegada iminente do <b>World Cup Mode</b> (2 jun. 2026) e promos como "
        "<b>Shapeshifters</b> (12 jun.), <b>Path to Glory</b> e <b>Greats of the Game</b> (26 jun.), "
        "o mercado está prestes a entrar em nova fase de alta demanda por SBC fodder. "
        "Esta é a janela ideal para acumular cards baratos antes da valorização.",
        corpo
    ))

    context_data = [
        ["INDICADOR", "STATUS", "IMPACTO NO MERCADO"],
        ["Evento Ativo",      "TOTS Ultimate (até 29/05)",    "🔴 Picos de preço em TOTS cards"],
        ["SBCs End of an Era", "Ativos (Salah, Griezmann...)", "🟡 Alta demanda por fodder 86-89"],
        ["Fodder 85-87 OVR",  "Próximo ao preço de descarte", "🟢 Oportunidade de compra"],
        ["Fodder 90-92 OVR",  "Nunca esteve tão barato",      "🟢 Investimento de médio prazo"],
        ["Próxima promo",     "World Cup (02/06)",            "📈 Catalisador de valorização"],
        ["Thursday flip",    "Recompensas: toda quinta",      "🟢 Janela de compra recorrente"],
    ]
    context_table = Table(context_data, colWidths=[5*cm, 6*cm, 6.2*cm])
    context_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  VERDE_ESCURO),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  BRANCO),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  9),
        ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("FONTSIZE",     (0, 1), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",         (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
    ]))
    story.append(context_table)
    story.append(Spacer(1, 10))

    # ── SEÇÃO 2: TABELA DE OPORTUNIDADES ──────────────────────────────────────
    story.append(Paragraph("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA/VENDA", secao_titulo))

    story.append(Paragraph(
        "As oportunidades abaixo foram selecionadas considerando o contexto de TOTS + End of an Era SBCs ativos. "
        "Preços baseados em dados de FUTBIN e FUT.GG (25/05/2026). "
        "<b>Margem líquida já descontada a taxa EA de 5%.</b>",
        corpo
    ))

    # Tabela principal de cartas
    header = [
        "JOGADOR", "OVR", "CLUBE", "COMPRA\n(coins)", "VENDA\n(coins)", "MARGEM\nLÍQUIDA", "QTDE\nSUGERIDA", "ESTRATÉGIA"
    ]

    cards_data = [
        # [nome, ovr, clube, compra, venda, margem_liquida, qtde, estrategia]
        ["Carvajal",         "85", "Real Madrid",    "1.100", "1.600", "+452",   "10x", "SBC Fodder TOTS"],
        ["De Gea",           "85", "Man. United",    "1.150", "1.700", "+462",   "10x", "SBC Fodder TOTS"],
        ["Griezmann",        "85", "Atlético Madrid","1.200", "1.750", "+463",   "8x",  "Fodder / End of Era"],
        ["Foden",            "85", "Man. City",      "1.200", "1.700", "+415",   "8x",  "SBC Fodder TOTS"],
        ["Dani Olmo",        "85", "Barcelona",      "1.200", "1.750", "+463",   "8x",  "SBC Fodder TOTS"],
        ["Konaté",           "86", "Liverpool",      "1.200", "1.900", "+605",   "8x",  "Fodder / End of Era"],
        ["Tonali",           "86", "Newcastle",      "1.300", "2.000", "+600",   "8x",  "SBC Fodder demand"],
        ["Alexander-Arnold", "86", "Liverpool",      "1.400", "2.100", "+595",   "6x",  "Fodder linkagem ENG"],
        ["Nuno Mendes",      "86", "PSG",            "1.300", "2.000", "+600",   "6x",  "SBC Fodder TOTS"],
        ["Çalhanoğlu",       "86", "Internazionale", "1.400", "2.100", "+595",   "6x",  "SBC Fodder Serie A"],
        ["Kvaratskhelia",    "87", "PSG",            "1.900", "2.900", "+855",   "5x",  "Fodder / End of Era"],
        ["Kerr",             "88", "Chelsea",        "1.600", "2.700", "+965",   "4x",  "Womens SBC spike"],
        ["Katoto",           "88", "Arsenal",        "1.600", "2.600", "+870",   "4x",  "Womens SBC spike"],
        ["Kimmich",          "89", "Bayern Munich",  "4.600", "6.500", "+1.575", "3x",  "SBC premium fodder"],
        ["Rodri",            "90", "Man. City",      "5.500", "8.000", "+2.100", "2x",  "World Cup SBC prep"],
    ]

    table_header = [header]
    table_rows = table_header + cards_data

    col_widths = [3.4*cm, 1.1*cm, 3.4*cm, 1.7*cm, 1.7*cm, 1.9*cm, 1.7*cm, 3.2*cm]
    main_table = Table(table_rows, colWidths=col_widths, repeatRows=1)

    main_style = TableStyle([
        # Cabeçalho
        ("BACKGROUND",   (0, 0), (-1, 0),  VERDE_ESCURO),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  DOURADO),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  8),
        ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        # Corpo
        ("FONTSIZE",     (0, 1), (-1, -1), 8),
        ("FONTNAME",     (0, 1), (0, -1),  "Helvetica-Bold"),  # nome em negrito
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        # Coluna margem em verde
        ("TEXTCOLOR",    (5, 1), (5, -1),  VERDE_MEDIO),
        ("FONTNAME",     (5, 1), (5, -1),  "Helvetica-Bold"),
        # Grid
        ("GRID",         (0, 0), (-1, -1), 0.4, colors.HexColor("#bbbbbb")),
        ("TOPPADDING",   (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
        # Highlight linhas 90 OVR+
        ("BACKGROUND",   (0, 14), (-1, 14), colors.HexColor("#fff3cd")),
        ("BACKGROUND",   (0, 15), (-1, 15), colors.HexColor("#fff3cd")),
    ])
    main_table.setStyle(main_style)
    story.append(main_table)

    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "⚠️  <b>Nota:</b> Preços podem variar ±15% conforme horário e plataforma (PS5/Xbox/PC). "
        "Sempre confira os valores atuais em FUTBIN ou FUT.GG antes de executar. "
        "Margem líquida = (preço de venda × 0,95) − preço de compra.",
        alerta_estilo
    ))

    # ── SEÇÃO 3: ESTRATÉGIA DE TIMING ─────────────────────────────────────────
    story.append(Paragraph("3. ESTRATÉGIA DE TIMING", secao_titulo))

    timing_data = [
        ["QUANDO",              "AÇÃO",                     "MOTIVO"],
        ["Segunda-feira\n07h-09h UTC", "COMPRAR fodder 85-87",   "Mercado esvaziado, preços baixos"],
        ["Quinta-feira\n17h-19h UTC",  "COMPRAR — Thursday Flip", "Rewards Div. Rivals abertos = oferta alta"],
        ["Quinta-feira\n23h-01h UTC",  "VENDER — Thursday Flip",  "Pico de demanda pós-rewards"],
        ["Sexta-feira\n10h-12h UTC",   "COMPRAR 88-90 fodder",    "Crash pós-packs = preços no fundo"],
        ["Sábado\n12h-18h UTC",        "VENDER fodder 85-88",     "Peak de jogadores no mercado"],
        ["Domingo\n20h-23h UTC",       "COMPRAR meta players",    "Queda pós-WL, antes da segunda-feira"],
        ["Lançamento SBC\n(qualquer)",  "VENDER fodder acumulado", "Pico de demanda = melhor margem"],
        ["01-02/Jun (World Cup)", "VENDER 90-92 OVR cards",  "Catalisador de valorização forte"],
    ]

    timing_table = Table(timing_data, colWidths=[4.5*cm, 5.5*cm, 7.2*cm])
    timing_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  VERDE_MEDIO),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  BRANCO),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  9),
        ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("FONTSIZE",     (0, 1), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",         (0, 0), (-1, -1), 0.4, colors.HexColor("#cccccc")),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        # Linha World Cup destaque
        ("BACKGROUND",   (0, 8), (-1, 8), colors.HexColor("#fff3cd")),
        ("FONTNAME",     (0, 8), (-1, 8), "Helvetica-Bold"),
    ]))
    story.append(timing_table)
    story.append(Spacer(1, 8))

    # ── SEÇÃO 4: PLANO DE ALOCAÇÃO DO BUDGET ─────────────────────────────────
    story.append(Paragraph("4. PLANO DE ALOCAÇÃO DO BUDGET (40.000 coins)", secao_titulo))

    alloc_data = [
        ["ESTRATÉGIA",               "ALOCAÇÃO", "COINS", "OBJETIVO"],
        ["SBC Fodder 85-87 OVR",     "40%",      "16.000",  "Vender no próximo SBC grande"],
        ["Thursday Flip",            "25%",      "10.000",  "Lucro rápido 24-48h"],
        ["Investimento 88-90 OVR",   "25%",      "10.000",  "World Cup promo (01-10 Jun)"],
        ["Reserva de emergência",    "10%",      "4.000",   "Aproveitar sniping e oportunidades"],
    ]
    alloc_table = Table(alloc_data, colWidths=[5.5*cm, 2.5*cm, 2.8*cm, 6.4*cm])
    alloc_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  VERDE_ESCURO),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  DOURADO),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  9),
        ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("FONTSIZE",     (0, 1), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",         (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("TOPPADDING",   (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 6),
        # Reserva em vermelho
        ("BACKGROUND",   (0, 4), (-1, 4), colors.HexColor("#fdecea")),
    ]))
    story.append(alloc_table)
    story.append(Spacer(1, 8))

    # ── SEÇÃO 5: ESTIMATIVA DE RETORNO EM 48h ────────────────────────────────
    story.append(Paragraph("5. ESTIMATIVA DE RETORNO EM 48h", secao_titulo))

    retorno_data = [
        ["CENÁRIO",        "RETORNO (%)", "LUCRO ESTIMADO", "CAPITAL FINAL", "CONDIÇÃO"],
        ["Conservador",    "+18%",        "+7.200 coins",    "47.200 coins", "Mercado estável, 1 SBC médio"],
        ["Moderado",       "+30%",        "+12.000 coins",   "52.000 coins", "1 SBC grande + Thursday flip"],
        ["Otimista",       "+50%",        "+20.000 coins",   "60.000 coins", "Vários SBCs + World Cup leak"],
        ["Agressivo",      "+70%",        "+28.000 coins",   "68.000 coins", "World Cup + sniping intenso"],
    ]
    retorno_table = Table(retorno_data, colWidths=[2.8*cm, 2.5*cm, 3.2*cm, 3.2*cm, 5.5*cm])
    retorno_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  VERDE_ESCURO),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  BRANCO),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  9),
        ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("FONTSIZE",     (0, 1), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",         (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("TOPPADDING",   (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 6),
        # Conservador: azul claro
        ("TEXTCOLOR",    (1, 1), (1, 1),  colors.HexColor("#2980b9")),
        # Moderado: verde
        ("TEXTCOLOR",    (1, 2), (1, 2),  VERDE_MEDIO),
        # Otimista: verde escuro bold
        ("TEXTCOLOR",    (1, 3), (1, 3),  VERDE_ESCURO),
        ("FONTNAME",     (0, 3), (-1, 3), "Helvetica-Bold"),
        # Agressivo: dourado
        ("BACKGROUND",   (0, 4), (-1, 4), colors.HexColor("#fff9e6")),
        ("TEXTCOLOR",    (1, 4), (1, 4),  DOURADO),
        ("FONTNAME",     (0, 4), (-1, 4), "Helvetica-Bold"),
    ]))
    story.append(retorno_table)

    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "💡 <b>Foco recomendado:</b> Cenário Moderado (+30%) é o mais realista para o momento, "
        "com a combinação de Thursday flip + 1 SBC grande esperado nos próximos 2 dias. "
        "O cenário Otimista (+50%) é alcançável se o World Cup Mode for lançado antes do previsto "
        "e trouxer SBCs de 88-90 OVR com alta demanda.",
        alerta_estilo
    ))

    # ── SEÇÃO 6: ANÁLISE DETALHADA POR ESTRATÉGIA ────────────────────────────
    story.append(Paragraph("6. ANÁLISE DETALHADA POR ESTRATÉGIA", secao_titulo))

    story.append(Paragraph("A) SBC Fodder Flipping (83-88 OVR)", subsecao_titulo))
    story.append(Paragraph(
        "Durante o TOTS, o mercado vive um <b>crash de preços para cards 85-88 OVR</b> — esses jogadores "
        "aparecem em packs com frequência muito maior, derrubando os preços para próximo do descarte. "
        "A janela ideal para comprar em massa é agora (25-27 maio). A venda deve ocorrer assim que "
        "um SBC grande for anunciado (ex: End of an Era — Griezmann 94 OVR ainda ativo até 06/06). "
        "Cards com liga Premier League e La Liga costumam ter pico de demanda mais rápido, pois "
        "são usados para completar requisitos de liga/nação nas SBCs.",
        corpo
    ))
    story.append(Paragraph(
        "<b>Exemplos práticos de compra imediata:</b> Comprar 10× Carvajal (85, Real Madrid) a 1.100 "
        "= 11.000 coins investidos. Se vender a 1.600 (após SBC): receita 16.000 × 0,95 = 15.200. "
        "Lucro líquido: <b>+4.200 coins</b> (+38%). Mesma lógica para Konaté 86 e Kvaratskhelia 87.",
        corpo
    ))

    story.append(Paragraph("B) Thursday Flip — Janela Recorrente", subsecao_titulo))
    story.append(Paragraph(
        "Toda <b>quinta-feira às 17h BST (16h UTC)</b>, as recompensas de Division Rivals são distribuídas. "
        "Isso causa uma inundação de cards no mercado → preços caem drasticamente na janela 17h-20h. "
        "A estratégia: <b>comprar cards meta 86-88 OVR na quinta à tarde</b> (quando estão baratos) "
        "e vender entre quinta à noite e sexta de manhã, quando os preços se normalizam. "
        "Tip: focar em cards populares da Premier League (Alexander-Arnold, Foden, Konaté) pois "
        "têm maior liquidez e voltam ao preço mais rapidamente.",
        corpo
    ))

    story.append(Paragraph("C) Investimento Antecipado para World Cup Promo", subsecao_titulo))
    story.append(Paragraph(
        "O <b>World Cup Mode</b> chega em 02/06/2026, seguido por promos como Shapeshifters (12/06), "
        "Path to Glory e Greats of the Game (26/06). Historicamente, esses eventos trazem SBCs "
        "que exigem fodder de <b>88-92 OVR</b> — exatamente o que está baratíssimo agora durante o TOTS. "
        "Cards como Kimmich (89), Rodri (90) e eventuais TOTS de 91-92 OVR próximos ao preço de descarte "
        "são investimentos de baixíssimo risco e alto potencial de retorno (50-100% em 15-30 dias). "
        "Atenção: esses cards precisam de maior capital e liquidez mais lenta — use apenas parte do budget.",
        corpo
    ))

    # ── SEÇÃO 7: REGRAS DE OURO ───────────────────────────────────────────────
    story.append(Paragraph("7. AS 8 REGRAS DE OURO DO TRADE", secao_titulo))

    regras = [
        ("📊  REGRA 1 — Pesquise antes de comprar",
         "Nunca compre sem verificar o preço atual em FUTBIN ou FUT.GG. "
         "O mercado muda em minutos. Um bom trade começa com informação correta."),
        ("💰  REGRA 2 — Respeite a taxa de 5% da EA",
         "Todo preço de venda deve ser calculado com desconto de 5%. "
         "Se vender a 2.000, recebe 1.900. Sempre calcule a margem líquida antes de comprar."),
        ("📦  REGRA 3 — Não concentre em um único jogador",
         "Diversifique. Compre no máximo 10-12 unidades do mesmo card. "
         "Se o mercado mudar, você consegue absorver o impacto sem travar o capital."),
        ("⏱  REGRA 4 — Timing é tudo",
         "Quinta (rewards), domingo à noite e segunda cedo são os melhores momentos para comprar. "
         "Sábado à tarde e logo após SBCs são os melhores momentos para vender."),
        ("🚫  REGRA 5 — Nunca compre no pico",
         "Nas primeiras horas de lançamento de uma promo ou SBC, os preços explodem. "
         "Espere 2-4 horas para a euforia baixar antes de comprar."),
        ("🎯  REGRA 6 — Tenha um preço de saída definido",
         "Antes de comprar, defina: 'Vou vender a X coins'. "
         "Se o mercado não chegar lá em 48h, reavalie e aceite lucro menor se necessário."),
        ("💎  REGRA 7 — Acumule fodder durante promos grandes",
         "TOTS, Team of the Year e Futties são momentos de crash de fodder. "
         "Compre 85-90 OVR barato agora, venda durante os SBCs das promos seguintes."),
        ("🧠  REGRA 8 — Emocional zero, dados sempre",
         "Não se apegue a cards. Se o preço caiu e não vai voltar, venda e corte o prejuízo. "
         "Capital travado é pior do que uma pequena perda. Discipline beats emotion."),
    ]

    for titulo, descricao in regras:
        story.append(KeepTogether([
            Paragraph(titulo, regra_titulo_estilo),
            Paragraph(descricao, corpo),
            Spacer(1, 4),
        ]))

    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cccccc"), spaceAfter=8))

    # ── FONTES E FERRAMENTAS ──────────────────────────────────────────────────
    story.append(Paragraph("8. FERRAMENTAS E FONTES RECOMENDADAS", secao_titulo))

    tools_data = [
        ["FERRAMENTA",       "URL",                     "USO"],
        ["FUTBIN",           "futbin.com",              "Preços, SBC calculator, price ranges"],
        ["FUT.GG",           "fut.gg",                  "Preços, evolutions, rating combinations"],
        ["FUTWIZ",           "futwiz.com",              "Cheapest by rating, player database"],
        ["Team Gullit",      "teamgullit.com",          "Trading methods, promo calendar"],
        ["SuperCoinsy",      "supercoinsy.com",         "Budget players, market analysis"],
        ["EA FC Official",   "ea.com/games/ea-sports-fc", "Eventos oficiais, TOTS news"],
        ["Reddit r/FIFA",    "reddit.com/r/FIFA",       "Trading tips, community insights"],
    ]
    tools_table = Table(tools_data, colWidths=[3.5*cm, 5*cm, 8.7*cm])
    tools_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  VERDE_ESCURO),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  BRANCO),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  9),
        ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("FONTSIZE",     (0, 1), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CINZA_CLARO, BRANCO]),
        ("GRID",         (0, 0), (-1, -1), 0.4, colors.HexColor("#cccccc")),
        ("TOPPADDING",   (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
    ]))
    story.append(tools_table)
    story.append(Spacer(1, 12))

    # ── DISCLAIMER ────────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cccccc"), spaceAfter=6))
    story.append(Paragraph("DISCLAIMER", ParagraphStyle(
        "DisclaimerTitulo", parent=styles["Normal"],
        fontSize=9, fontName="Helvetica-Bold", textColor=colors.HexColor("#555555"),
        spaceAfter=3,
    )))
    story.append(Paragraph(
        "Este relatório é gerado com fins educacionais e informativos para trading no EA FC 26 Ultimate Team. "
        "Os preços apresentados são estimativas baseadas em dados públicos de FUTBIN, FUT.GG, FUTWIZ e outras "
        "fontes abertas na data de geração do documento. O mercado do FUT é altamente volátil e os preços "
        "podem variar significativamente em minutos. Não há garantia de lucro. Trade com responsabilidade. "
        "EA SPORTS FC™ é marca registrada da Electronic Arts Inc. Este relatório não tem afiliação "
        "oficial com a EA Sports. Sempre verifique os preços atuais antes de executar qualquer operação.",
        disclaimer_estilo
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        f"Relatório gerado em {REPORT_DATETIME} UTC — EA FC 26 Ultimate Team Trading Analysis",
        ParagraphStyle("Footer", parent=styles["Normal"],
                       fontSize=8, fontName="Helvetica", textColor=colors.HexColor("#999999"),
                       alignment=TA_CENTER)
    ))

    doc.build(story)
    print(f"✅ PDF gerado com sucesso: {PDF_FILENAME}")

if __name__ == "__main__":
    build_pdf()
