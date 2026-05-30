#!/usr/bin/env python3
"""Gerador de relatório diário de trading EA FC 26 Ultimate Team."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ── Configuração ──────────────────────────────────────────────────────────────
DATA_HORA   = "30/05/2026 08:06"
DATA_HORA_FILE = "2026-05-30-08h"
OUTPUT_FILE = f"relatorio-trading-{DATA_HORA_FILE}.pdf"

# Paleta de cores EA FC
COR_VERDE   = colors.HexColor("#00D600")
COR_VERDE_E = colors.HexColor("#009900")
COR_AZUL    = colors.HexColor("#0E1A2B")
COR_OURO    = colors.HexColor("#C9A84C")
COR_CINZA_C = colors.HexColor("#F5F5F5")
COR_CINZA_E = colors.HexColor("#333333")
COR_BORDA   = colors.HexColor("#222222")
COR_AMARELO = colors.HexColor("#FFD700")
COR_VERMELHO= colors.HexColor("#CC0000")
COR_LARANJA = colors.HexColor("#E86A00")
BRANCO      = colors.white

def build_styles():
    base = getSampleStyleSheet()

    titulo = ParagraphStyle(
        "Titulo",
        parent=base["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=COR_VERDE,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    subtitulo = ParagraphStyle(
        "Subtitulo",
        parent=base["Normal"],
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=COR_OURO,
        alignment=TA_CENTER,
        spaceAfter=2,
    )
    data_hora = ParagraphStyle(
        "DataHora",
        parent=base["Normal"],
        fontName="Helvetica",
        fontSize=10,
        textColor=BRANCO,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    secao = ParagraphStyle(
        "Secao",
        parent=base["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=COR_VERDE,
        spaceBefore=14,
        spaceAfter=6,
        borderPad=4,
    )
    corpo = ParagraphStyle(
        "Corpo",
        parent=base["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        textColor=COR_CINZA_E,
        leading=15,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=base["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        textColor=COR_CINZA_E,
        leading=15,
        leftIndent=16,
        spaceAfter=3,
    )
    negrito = ParagraphStyle(
        "Negrito",
        parent=base["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=COR_CINZA_E,
        leading=15,
        spaceAfter=4,
    )
    aviso = ParagraphStyle(
        "Aviso",
        parent=base["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=8,
        textColor=colors.HexColor("#666666"),
        leading=12,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
    )
    regra_titulo = ParagraphStyle(
        "RegraTitulo",
        parent=base["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=COR_OURO,
        leading=14,
        leftIndent=8,
    )
    return {
        "titulo": titulo, "subtitulo": subtitulo, "data_hora": data_hora,
        "secao": secao, "corpo": corpo, "bullet": bullet,
        "negrito": negrito, "aviso": aviso, "regra_titulo": regra_titulo,
    }


def header_banner(styles):
    """Cria o cabeçalho visual do relatório."""
    banner_data = [
        [Paragraph("⚽  EA FC 26 ULTIMATE TEAM — RELATÓRIO DE TRADING", styles["titulo"])],
        [Paragraph("Análise de Mercado · Oportunidades de Compra e Venda · Estratégia 48h", styles["subtitulo"])],
        [Paragraph(f"Data e Hora do Relatório: {DATA_HORA} UTC", styles["data_hora"])],
    ]
    banner = Table(banner_data, colWidths=[17 * cm])
    banner.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, -1), COR_AZUL),
        ("TOPPADDING",  (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 10),
        ("LEFTPADDING",  (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("ROUNDEDCORNERS", [8]),
    ]))
    return banner


def secao_contexto(styles):
    elementos = []
    elementos.append(Paragraph("1. CONTEXTO DO MERCADO — 30/05/2026", styles["secao"]))
    elementos.append(HRFlowable(width="100%", thickness=1, color=COR_VERDE, spaceAfter=6))

    ctx = [
        ("<b>Evento Principal:</b> TOTS (Team of the Season) encerrado em 29/05/2026. "
         "A janela de transição pós-TOTS é historicamente o melhor período para comprar "
         "fodder e cartas gold baratas antes da próxima grande promo."),

        ("<b>Próxima Promo Confirmada:</b> Festival of Football — <b>Path to Glory</b> "
         "começa em <b>05/06/2026 às 18h BST</b> (Cartas Live vinculadas à Copa do Mundo 2026). "
         "Esta é a maior promo do ano e vai gerar demanda massiva por SBCs e fodder."),

        ("<b>Copa do Mundo FIFA 2026:</b> Começa em 11/06/2026 (EUA/Canadá/México). "
         "O Path to Glory terá cartas de jogadores internacionais que sobem de rating "
         "conforme suas seleções avançam no torneio — enorme potencial de valorização."),

        ("<b>SBCs Ativos Agora:</b> Berbatov Showdown 91-rated (expira 31/05 às 18h30 UTC), "
         "Scott Prime Heroes 94-rated, Scott Showdown 91-rated. Estes SBCs aumentam a "
         "demanda por fodder neste final de semana."),

        ("<b>Tendência Geral:</b> Mercado em transição/queda pós-TOTS. Preços de cartas "
         "gold 83-87 rated estão nas mínimas sazonais. Janela de compra aberta "
         "até ~04/06 para maximizar retorno com Path to Glory."),
    ]
    for t in ctx:
        elementos.append(Paragraph(f"• {t}", styles["bullet"]))
        elementos.append(Spacer(1, 3))
    return elementos


def secao_oportunidades(styles):
    elementos = []
    elementos.append(Paragraph("2. OPORTUNIDADES DE COMPRA — BUDGET: 40.000 COINS", styles["secao"]))
    elementos.append(HRFlowable(width="100%", thickness=1, color=COR_VERDE, spaceAfter=6))

    nota = ("<b>Nota metodológica:</b> Preços estimados com base em dados FUTBIN/FUT.GG "
            "para PC/PS/Xbox em 30/05/2026. A margem líquida já desconta a taxa de 5% da EA. "
            "Compre em lotes de no máximo 10-15 cartas da mesma carta para reduzir risco de mercado.")
    elementos.append(Paragraph(nota, styles["corpo"]))
    elementos.append(Spacer(1, 6))

    # Cabeçalho da tabela
    headers = [
        Paragraph("<b>Jogador</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Rating</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Clube / Liga</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Comprar (max)</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Vender (alvo)</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Margem Líq.</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
        Paragraph("<b>Estratégia / Timing</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER)),
    ]

    st_cell = ParagraphStyle("cell", fontName="Helvetica", fontSize=8, textColor=COR_CINZA_E, alignment=TA_CENTER, leading=11)
    st_cell_l = ParagraphStyle("celll", fontName="Helvetica", fontSize=7.8, textColor=COR_CINZA_E, alignment=TA_LEFT, leading=10)

    def c(txt): return Paragraph(txt, st_cell)
    def cl(txt): return Paragraph(txt, st_cell_l)
    def cb(txt):
        s = ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=8, textColor=COR_CINZA_E, alignment=TA_CENTER, leading=11)
        return Paragraph(txt, s)

    dados = [
        # Fodder 83-rated — comprar em massa para SBCs do Path to Glory
        [cb("João Gomes"), c("83"), cl("Wolverhampton\nPremier League"), c("900"), c("1.600"), c("✅ +620"), cl("SBC fodder PL\nVender 05-07/06")],
        [cb("Dwight McNeil"), c("83"), cl("Everton\nPremier League"), c("850"), c("1.500"), c("✅ +575"), cl("SBC fodder PL\nVender 05-07/06")],
        [cb("Ansu Fati"), c("84"), cl("Barcelona\nLa Liga"), c("1.300"), c("2.200"), c("✅ +790"), cl("SBC fodder LaLiga\nVender 05-07/06")],
        [cb("Raphaël Guerreiro"), c("84"), cl("Bayern Munich\nBundesliga"), c("1.200"), c("2.000"), c("✅ +700"), cl("SBC fodder BL\nVender 05-07/06")],
        [cb("Carlos Soler"), c("84"), cl("PSG\nLigue 1"), c("1.100"), c("1.900"), c("✅ +705"), cl("SBC fodder L1\nVender 05-07/06")],
        # 85-86 rated
        [cb("Granit Xhaka"), c("86"), cl("Bayer Leverkusen\nBundesliga"), c("2.500"), c("4.200"), c("✅ +1.490"), cl("SBC alto custo\nVender 06-08/06")],
        [cb("Marcus Thuram"), c("85"), cl("Inter Milan\nSerie A"), c("2.000"), c("3.400"), c("✅ +1.230"), cl("Inter + França WC\nVender 05-08/06")],
        [cb("Jonathan Tah"), c("87"), cl("Bayern Munich\nBundesliga"), c("4.500"), c("7.500"), c("✅ +2.625"), cl("SBC 87-rated\nVender 06-09/06")],
        # Investimento Evolução
        [cb("Ismaïla Sarr"), c("83"), cl("Crystal Palace\nPremier League"), c("1.100"), c("3.500"), c("🚀 +2.225"), cl("EVO candidate\nVender pós-EVO")],
        # Path to Glory pre-invest
        [cb("Wout Weghorst"), c("83"), cl("Hoffenheim\nBundesliga"), c("850"), c("2.800"), c("🚀 +1.810"), cl("Holanda WC 2026\nVender 05-10/06")],
        [cb("Guido Rodriguez"), c("84"), cl("Real Betis\nLa Liga"), c("1.200"), c("3.000"), c("🚀 +1.650"), cl("Argentina WC 2026\nVender 05-10/06")],
        # Thursday flipping
        [cb("Fodder 83 PL (lote)"), c("83"), cl("Mix Premier League\nVários Clubes"), c("750"), c("1.400"), c("✅ +580"), cl("Comprar Qui/Dom\nVender Sáb/Sex")],
    ]

    table_data = [headers] + dados
    col_widths = [3.2*cm, 1.4*cm, 3.0*cm, 2.0*cm, 2.0*cm, 2.0*cm, 3.4*cm]

    tabela = Table(table_data, colWidths=col_widths, repeatRows=1)
    tabela.setStyle(TableStyle([
        # Header
        ("BACKGROUND",    (0, 0), (-1, 0), COR_AZUL),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 8.5),
        ("ALIGN",         (0, 0), (-1, 0), "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, 0), 7),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
        # Rows
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 8),
        ("ALIGN",         (0, 1), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        # Alternating rows
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, COR_CINZA_C]),
        # Grid
        ("GRID",          (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("LINEBELOW",     (0, 0), (-1, 0), 2, COR_VERDE),
        ("ROUNDEDCORNERS", [4]),
    ]))

    elementos.append(tabela)

    # Legenda
    elementos.append(Spacer(1, 6))
    leg = ("✅ = Operação de baixo risco (fodder/SBC flip)   "
           "🚀 = Investimento especulativo (maior retorno, maior risco)   "
           "Margem Líq. = lucro por carta após 5% de taxa EA")
    elementos.append(Paragraph(leg, styles["aviso"]))
    return elementos


def secao_estrategia(styles):
    elementos = []
    elementos.append(Paragraph("3. ESTRATÉGIA DE TIMING", styles["secao"]))
    elementos.append(HRFlowable(width="100%", thickness=1, color=COR_VERDE, spaceAfter=6))

    timing = [
        ("<b>AGORA — Sáb 30/05 (manhã):</b> Janela de compra ideal. Mercado pós-TOTS com "
         "preços nas mínimas. Compre fodder 83-84 em lotes de 10-15 cartas. "
         "Priorize Premier League e La Liga (maior demanda em SBCs)."),

        ("<b>Dom 31/05 (até 18h30 UTC):</b> SBC Berbatov Showdown expira — "
         "demanda aguda por fodder nas horas finais. Venda parte do estoque já comprado "
         "se os preços subirem 40%+. Valorize cartas BL e PL."),

        ("<b>Seg 01/06 — Qua 04/06:</b> Mantenha posição. Mercado calmo antes do Path to Glory. "
         "Reabasteça estoque se os preços voltarem à base. "
         "Compre jogadores internacionais (Brasil, França, Espanha, Inglaterra) com perfil "
         "para Path to Glory a preços gold-base."),

        ("<b>Qui 04/06 (Rivals Rewards):</b> Dia de recompensas do Division Rivals — mercado "
         "inunda de cartas. Compre mais fodder e cartas internacionais que caírem abaixo do "
         "valor intrínseco. Não venda neste dia."),

        ("<b>Sex 05/06 — 18h BST (Path to Glory lança):</b> VENDA! "
         "Este é o pico de demanda. Preços de fodder e cartas internacionais "
         "disparam nas primeiras 12-24h do Path to Glory. "
         "Liste suas cartas 15-20 min antes do lançamento para capturar o pico."),

        ("<b>Sáb 06/06 — Dom 07/06 (Weekend League):</b> Segunda janela de venda. "
         "Cartas 85-87 rated tendem a se valorizar ainda mais com demanda de SBCs "
         "e time building para a WL. Liquide evolução candidates neste período."),
    ]
    for t in timing:
        elementos.append(Paragraph(f"▶ {t}", styles["bullet"]))
        elementos.append(Spacer(1, 4))
    return elementos


def secao_alocacao(styles):
    elementos = []
    elementos.append(Paragraph("4. ALOCAÇÃO DO BUDGET — 40.000 COINS", styles["secao"]))
    elementos.append(HRFlowable(width="100%", thickness=1, color=COR_VERDE, spaceAfter=6))

    alloc_data = [
        [Paragraph("<b>Segmento</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>Coins</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>% Budget</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>Qtd. Estimada de Cartas</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER))],
        ["Fodder 83-84 (SBC flip)", "18.000", "45%", "~18 cartas @ 1.000 avg"],
        ["Fodder 85-87 (SBC alto custo)", "10.000", "25%", "~4 cartas @ 2.500 avg"],
        ["Investimento Path to Glory (internacionais)", "6.000", "15%", "~5 cartas @ 1.200 avg"],
        ["Candidatos a Evolução", "4.000", "10%", "~3 cartas @ 1.300 avg"],
        ["Reserva (liquidez / oportunidades)", "2.000", "5%", "Caixa livre"],
        [Paragraph("<b>TOTAL</b>", ParagraphStyle("tb", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>40.000</b>", ParagraphStyle("tb", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>100%</b>", ParagraphStyle("tb", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>~30 cartas</b>", ParagraphStyle("tb", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER))],
    ]

    t = Table(alloc_data, colWidths=[5.5*cm, 2.5*cm, 2.5*cm, 6.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), COR_AZUL),
        ("BACKGROUND",    (0, -1), (-1, -1), COR_VERDE_E),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("TEXTCOLOR",     (0, -1), (-1, -1), BRANCO),
        ("FONTNAME",      (0, 1), (-1, -2), "Helvetica"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [BRANCO, COR_CINZA_C]),
        ("GRID",          (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("LINEBELOW",     (0, 0), (-1, 0), 2, COR_VERDE),
    ]))
    elementos.append(t)
    return elementos


def secao_retorno(styles):
    elementos = []
    elementos.append(Paragraph("5. ESTIMATIVA DE RETORNO EM 48H", styles["secao"]))
    elementos.append(HRFlowable(width="100%", thickness=1, color=COR_VERDE, spaceAfter=6))

    ret_data = [
        [Paragraph("<b>Cenário</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>Retorno Bruto</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>Taxa EA (5%)</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>Lucro Líquido</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>ROI</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER)),
         Paragraph("<b>Portfolio Final</b>", ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO, alignment=TA_CENTER))],
        ["🟡 Conservador\n(spike +60%)", "64.000", "−3.200", "+20.800", "52%", "60.800"],
        ["🟢 Base\n(spike +90%)", "76.000", "−3.800", "+32.200", "80%", "72.200"],
        ["🚀 Otimista\n(spike +140%)", "96.000", "−4.800", "+51.200", "128%", "91.200"],
    ]

    t = Table(ret_data, colWidths=[3.4*cm, 2.5*cm, 2.5*cm, 2.5*cm, 1.8*cm, 3.3*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), COR_AZUL),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, COR_CINZA_C]),
        ("GRID",          (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("LINEBELOW",     (0, 0), (-1, 0), 2, COR_VERDE),
        # Destaque lucro líquido
        ("TEXTCOLOR",     (3, 1), (3, -1), COR_VERDE_E),
        ("FONTNAME",      (3, 1), (3, -1), "Helvetica-Bold"),
    ]))
    elementos.append(t)

    elementos.append(Spacer(1, 6))
    hip = ("<b>Hipóteses:</b> Budget inicial de 40.000 coins. Cenário Conservador assume que "
           "apenas o fodder 83-84 sobe 60% durante Path to Glory. Cenário Base inclui "
           "valorização de 85-87 e internacionais. Cenário Otimista reflete spike total "
           "do mercado nas primeiras 24h do Path to Glory (comportamento histórico de promos "
           "similares como TOTY e TOTS launch week). Todos os valores já deduzem 5% de taxa EA.")
    elementos.append(Paragraph(hip, styles["corpo"]))
    return elementos


def secao_regras(styles):
    elementos = []
    elementos.append(Paragraph("6. 8 REGRAS DE OURO DO TRADE", styles["secao"]))
    elementos.append(HRFlowable(width="100%", thickness=1, color=COR_OURO, spaceAfter=6))

    regras = [
        ("01", "COMPRE ANTES, VENDA NA HYPE",
         "Nunca compre na hora do pico. Acumule cartas 24-48h antes de promos e venda "
         "nas primeiras horas do lançamento, quando a demanda explode e os preços atingem máximas."),

        ("02", "DIVERSIFIQUE POR LIGA",
         "Distribua o budget entre Premier League, La Liga, Bundesliga e Serie A. "
         "Nunca concentre mais de 40% do portfolio numa única liga — SBCs variam de requisitos."),

        ("03", "LOTES MÁXIMOS DE 10-15 CARTAS",
         "Comprar mais de 15 cartas do mesmo jogador aumenta o risco de mercado. "
         "Se todos tentarem vender ao mesmo tempo, o preço despenca. Diversifique os nomes."),

        ("04", "RESPEITE A TAXA DE 5%",
         "Sempre calcule o lucro líquido descontando 5% do preço de venda. "
         "Uma carta comprada a 1.000 e vendida a 1.400 rende apenas 330 coins, não 400."),

        ("05", "QUINTA = DIA DE COMPRA",
         "Toda quinta-feira (Division Rivals Rewards) o mercado é inundado de cartas. "
         "Use esse dia para reabastecer estoque a preços mínimos. Nunca venda às quintas."),

        ("06", "NUNCA ENTRE EM PÂNICO",
         "Se o mercado cair depois que você comprou, não venda no prejuízo. "
         "Cartas de fodder têm floor price pelo SBC demand — aguarde a recuperação."),

        ("07", "ACOMPANHE FUTBIN E FUT.GG",
         "Monitore gráficos de preço em tempo real. Se uma carta subiu +80% e o gráfico "
         "mostra estabilização ou queda, venda imediatamente — não espere mais."),

        ("08", "MANTENHA 5-10% DE RESERVA",
         "Sempre mantenha um caixa mínimo livre para aproveitar oportunidades inesperadas "
         "(promoção surpresa de SBC, queda de preço de carta premium, etc.)."),
    ]

    for num, titulo, desc in regras:
        regra_data = [
            [Paragraph(f"<b>#{num}</b>", ParagraphStyle("rnum", fontName="Helvetica-Bold",
              fontSize=13, textColor=COR_OURO, alignment=TA_CENTER)),
             Paragraph(f"<b>{titulo}</b>", ParagraphStyle("rtit", fontName="Helvetica-Bold",
               fontSize=10, textColor=COR_AZUL, alignment=TA_LEFT)),
             Paragraph(desc, ParagraphStyle("rdesc", fontName="Helvetica",
               fontSize=8.5, textColor=COR_CINZA_E, alignment=TA_JUSTIFY, leading=12))],
        ]
        t = Table(regra_data, colWidths=[1.2*cm, 3.5*cm, 12.3*cm])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (0, -1), COR_AZUL),
            ("BACKGROUND",    (1, 0), (-1, -1), COR_CINZA_C),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LEFTPADDING",   (0, 0), (-1, -1), 6),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
            ("GRID",          (0, 0), (-1, -1), 0.5, colors.HexColor("#DDDDDD")),
            ("LINEBELOW",     (0, 0), (-1, 0), 0.5, COR_VERDE),
        ]))
        elementos.append(t)
        elementos.append(Spacer(1, 4))
    return elementos


def secao_disclaimer(styles):
    elementos = []
    elementos.append(Paragraph("DISCLAIMER", styles["secao"]))
    elementos.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#AAAAAA"), spaceAfter=6))

    disc = (
        "Este relatório foi gerado automaticamente com fins informativos e educativos sobre "
        "estratégias de trading no mercado virtual do EA FC 26 Ultimate Team. "
        "Os preços indicados são estimativas baseadas em dados históricos e tendências de mercado "
        "coletados de fontes públicas (FUTBIN, FUT.GG, Team Gullit, Reddit). "
        "O mercado do FUT é altamente volátil e imprevisível — resultados passados não garantem "
        "retornos futuros. Nenhum valor mencionado deve ser interpretado como garantia de lucro. "
        "O trading no Ultimate Team envolve risco de perda total do capital investido. "
        "Verifique sempre os preços em tempo real antes de realizar qualquer transação. "
        "Este relatório não tem afiliação com a Electronic Arts Inc. ou a FIFA."
    )
    elementos.append(Paragraph(disc, styles["aviso"]))

    rodape = Paragraph(
        f"Gerado em {DATA_HORA} UTC  |  EA FC 26 Trading Intelligence  |  Budget: 40.000 coins  |  v1.0",
        ParagraphStyle("rodape", fontName="Helvetica-Oblique", fontSize=7.5,
                       textColor=colors.HexColor("#999999"), alignment=TA_CENTER)
    )
    elementos.append(Spacer(1, 8))
    elementos.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CCCCCC"), spaceAfter=4))
    elementos.append(rodape)
    return elementos


def gerar_pdf():
    output_path = os.path.join(os.path.dirname(__file__), OUTPUT_FILE)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm,
        title="Relatório de Trading EA FC 26",
        author="EA FC 26 Trading Intelligence",
    )

    styles = build_styles()
    story = []

    # Cabeçalho
    story.append(header_banner(styles))
    story.append(Spacer(1, 12))

    # Seções
    story.extend(secao_contexto(styles))
    story.append(Spacer(1, 8))

    story.extend(secao_oportunidades(styles))
    story.append(Spacer(1, 8))

    story.extend(secao_estrategia(styles))
    story.append(Spacer(1, 8))

    story.extend(secao_alocacao(styles))
    story.append(Spacer(1, 8))

    story.extend(secao_retorno(styles))
    story.append(Spacer(1, 8))

    story.extend(secao_regras(styles))
    story.append(Spacer(1, 8))

    story.extend(secao_disclaimer(styles))

    doc.build(story)
    print(f"PDF gerado: {output_path}")
    return output_path


if __name__ == "__main__":
    gerar_pdf()
