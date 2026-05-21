#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import KeepTogether
import datetime

DATA_RELATORIO = "2026-05-21"
NOME_ARQUIVO = f"relatorio-trading-{DATA_RELATORIO}.pdf"

VERDE_ESCURO  = colors.HexColor("#1B5E20")
VERDE_MEDIO   = colors.HexColor("#2E7D32")
VERDE_CLARO   = colors.HexColor("#4CAF50")
VERDE_FUNDO   = colors.HexColor("#E8F5E9")
VERDE_LINHA   = colors.HexColor("#A5D6A7")
AMARELO       = colors.HexColor("#F9A825")
AMARELO_FUNDO = colors.HexColor("#FFF9C4")
CINZA_ESCURO  = colors.HexColor("#212121")
CINZA_MEDIO   = colors.HexColor("#424242")
CINZA_CLARO   = colors.HexColor("#F5F5F5")
BRANCO        = colors.white
PRETO         = colors.black
VERMELHO      = colors.HexColor("#C62828")

def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "TituloRelatorio",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=BRANCO,
        alignment=TA_CENTER,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        "SubtituloRelatorio",
        fontName="Helvetica",
        fontSize=12,
        textColor=VERDE_LINHA,
        alignment=TA_CENTER,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        "DataRelatorio",
        fontName="Helvetica-Bold",
        fontSize=10,
        textColor=AMARELO,
        alignment=TA_CENTER,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        "SecaoTitulo",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=BRANCO,
        alignment=TA_LEFT,
        spaceAfter=6,
        spaceBefore=4,
        leftIndent=8,
    ))
    styles.add(ParagraphStyle(
        "Corpo",
        fontName="Helvetica",
        fontSize=9,
        textColor=CINZA_ESCURO,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
        leading=14,
    ))
    styles.add(ParagraphStyle(
        "CorpoNegrito",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=CINZA_ESCURO,
        alignment=TA_LEFT,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        "BulletItem",
        fontName="Helvetica",
        fontSize=9,
        textColor=CINZA_ESCURO,
        leftIndent=14,
        spaceAfter=3,
        leading=13,
    ))
    styles.add(ParagraphStyle(
        "Disclaimer",
        fontName="Helvetica-Oblique",
        fontSize=7.5,
        textColor=colors.HexColor("#757575"),
        alignment=TA_JUSTIFY,
        spaceAfter=2,
        leading=11,
    ))
    styles.add(ParagraphStyle(
        "TableHeader",
        fontName="Helvetica-Bold",
        fontSize=7.5,
        textColor=BRANCO,
        alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        "TableCell",
        fontName="Helvetica",
        fontSize=7.5,
        textColor=CINZA_ESCURO,
        alignment=TA_CENTER,
        leading=10,
    ))
    styles.add(ParagraphStyle(
        "TableCellLeft",
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=CINZA_ESCURO,
        alignment=TA_LEFT,
        leading=10,
    ))
    styles.add(ParagraphStyle(
        "Regra",
        fontName="Helvetica",
        fontSize=9,
        textColor=CINZA_ESCURO,
        spaceAfter=5,
        leading=13,
        leftIndent=6,
    ))
    return styles


def secao_header(titulo, styles):
    """Retorna uma tabela com fundo verde escuro como cabeçalho de seção."""
    p = Paragraph(titulo, styles["SecaoTitulo"])
    t = Table([[p]], colWidths=[19 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), VERDE_MEDIO),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("ROUNDEDCORNERS", [4, 4, 4, 4]),
    ]))
    return t


def build_cabecalho(styles):
    items = []

    # Banner principal
    titulo_p  = Paragraph("EA FC 26 ULTIMATE TEAM", styles["TituloRelatorio"])
    subtitulo_p = Paragraph("Relatório de Trading — Análise Diária de Mercado", styles["SubtituloRelatorio"])
    data_p    = Paragraph(f"Data: {DATA_RELATORIO}  |  Budget: 40.000 coins  |  Meta: SBC Fodder Flipping + Evo Investing", styles["DataRelatorio"])

    banner = Table(
        [[titulo_p], [subtitulo_p], [data_p]],
        colWidths=[19 * cm],
    )
    banner.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), VERDE_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
        ("BOTTOMPADDING", (0, 2), (-1, 2), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
    ]))
    items.append(banner)
    items.append(Spacer(1, 0.4 * cm))
    return items


def build_contexto(styles):
    items = []
    items.append(secao_header("📅  1. CONTEXTO DO MERCADO — 21/05/2026", styles))
    items.append(Spacer(1, 0.25 * cm))

    # Caixa de destaque: evento ativo
    evento_lines = [
        Paragraph("<b>🔥 EVENTO ATIVO: PRÉ-LANÇAMENTO ULTIMATE TOTS</b>", styles["CorpoNegrito"]),
        Paragraph(
            "O <b>Ultimate Team of the Season (Ultimate TOTS)</b> é lançado amanhã, <b>22/05/2026 às 14h00 (BRT)</b>. "
            "Este é o evento mais aguardado do ano — e a última grande janela de lucro antes do encerramento da temporada. "
            "Alongside TOTS, <b>End of Era SBCs</b> de Salah, Griezmann, Bernardo Silva, Goretzka e Robertson serão ativados.",
            styles["Corpo"]
        ),
    ]
    caixa_evento = Table([[col] for col in evento_lines], colWidths=[18.4 * cm])
    caixa_evento.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), AMARELO_FUNDO),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("BOX",           (0, 0), (-1, -1), 1, AMARELO),
    ]))
    items.append(caixa_evento)
    items.append(Spacer(1, 0.3 * cm))

    contexto_texto = [
        ("<b>Situação atual do mercado:</b> Os rewards do Weekend League e do Squad Battles inundaram "
         "o mercado com cartas 84-87 OVR, derrubando os preços para mínimas históricas. Cartas 86 OVR "
         "estão sendo vendidas a <b>700–1.500 coins</b> — perto do preço de descarte. Essa janela "
         "de compra só se fecha quando os SBCs do Ultimate TOTS abrirem."),

        ("<b>Tendência geral:</b> Alta iminente em todas as cartas fodder 83-88 OVR nas próximas 24-48h. "
         "SBCs de End of Era exigem squads completos de alto rating, o que cria picos de demanda abruptos. "
         "Players que estão baratos hoje valem 2-3× mais durante o rush de SBC."),

        ("<b>Oportunidade chave:</b> Comprar fodder HOJE (quinta-feira) nas primeiras horas da manhã "
         "quando o mercado está saturado de supply e vender AMANHÃ (sexta) após 15h00 BRT, "
         "quando os SBCs do Ultimate TOTS liberarem demanda reprimida."),
    ]
    for t in contexto_texto:
        items.append(Paragraph(t, styles["Corpo"]))
    items.append(Spacer(1, 0.2 * cm))
    return items


def build_tabela_recomendacoes(styles):
    items = []
    items.append(secao_header("📊  2. CARTAS RECOMENDADAS PARA COMPRA", styles))
    items.append(Spacer(1, 0.25 * cm))

    # Cabeçalho da tabela
    headers = [
        Paragraph("Jogador", styles["TableHeader"]),
        Paragraph("OVR", styles["TableHeader"]),
        Paragraph("Clube", styles["TableHeader"]),
        Paragraph("Liga", styles["TableHeader"]),
        Paragraph("Comprar\n(coins)", styles["TableHeader"]),
        Paragraph("Vender\n(coins)", styles["TableHeader"]),
        Paragraph("Margem\nLíq. (5%)", styles["TableHeader"]),
        Paragraph("Melhor\nHorário\nCompra (BRT)", styles["TableHeader"]),
        Paragraph("Melhor\nHorário\nVenda (BRT)", styles["TableHeader"]),
    ]

    TC = styles["TableCell"]
    TL = styles["TableCellLeft"]

    # Dados: [jogador, ovr, clube, liga, compra, venda, margem, h_compra, h_venda]
    jogadores = [
        ("Grimaldo",       "84", "B. Leverkusen",  "Bundesliga",  "750–900",  "1.700–2.200",  "+890",  "07:00–10:00",  "Sex 15:00–19:00"),
        ("Rodrigo De Paul","84", "Atlético Madrid", "La Liga",    "750–900",  "1.700–2.200",  "+890",  "07:00–10:00",  "Sex 15:00–19:00"),
        ("Cody Gakpo",     "84", "Liverpool",       "Prem. League","750–900",  "1.700–2.200",  "+890",  "07:00–10:00",  "Sex 15:00–19:00"),
        ("Omar Marmoush",  "84", "Man. City",       "Prem. League","750–900",  "1.700–2.200",  "+890",  "07:00–10:00",  "Sex 15:00–19:00"),
        ("Bremer",         "85", "Juventus",        "Serie A",     "1.000–1.200","2.000–2.600","+990",  "07:00–10:00",  "Sex 15:00–20:00"),
        ("Bryan Mbeumo",   "85", "Brentford",       "Prem. League","1.500–1.700","2.800–3.500","+1.165","07:00–10:00",  "Sex 15:00–20:00"),
        ("Rúben Dias",     "86", "Man. City",       "Prem. League","1.300–1.500","2.800–3.600","+1.420","06:00–09:00",  "Sex 15:00–20:00"),
        ("H. Çalhanoğlu",  "86", "Inter Milan",     "Serie A",     "1.400–1.600","2.800–3.600","+1.350","06:00–09:00",  "Sáb 10:00–14:00"),
        ("Jonathan Tah",   "87", "Bayern Munich",   "Bundesliga",  "3.000–3.500","5.500–7.500","+2.350","06:00–09:00",  "Sáb 10:00–14:00"),
    ]

    data = [headers]
    for j in jogadores:
        row = [
            Paragraph(j[0], TL),
            Paragraph(j[1], TC),
            Paragraph(j[2], TC),
            Paragraph(j[3], TC),
            Paragraph(j[4], TC),
            Paragraph(j[5], TC),
            Paragraph(j[6], TC),
            Paragraph(j[7], TC),
            Paragraph(j[8], TC),
        ]
        data.append(row)

    col_widths = [3.1*cm, 0.9*cm, 2.6*cm, 2.5*cm, 1.8*cm, 2.0*cm, 1.5*cm, 2.2*cm, 2.4*cm]

    tabela = Table(data, colWidths=col_widths, repeatRows=1)
    estilo_tabela = TableStyle([
        # Cabeçalho
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        # Grid
        ("GRID",          (0, 0), (-1, -1), 0.5, VERDE_LINHA),
        ("BOX",           (0, 0), (-1, -1), 1.2, VERDE_MEDIO),
        # Linhas alternadas
        *[("BACKGROUND", (0, i), (-1, i), VERDE_FUNDO if i % 2 == 0 else BRANCO)
          for i in range(1, len(data))],
        # Alinhamento coluna jogador à esquerda
        ("ALIGN",         (0, 1), (0, -1), "LEFT"),
    ])
    tabela.setStyle(estilo_tabela)
    items.append(tabela)
    items.append(Spacer(1, 0.2 * cm))

    items.append(Paragraph(
        "* Margem líquida calculada sobre preço médio de venda após dedução de 5% de taxa EA. "
        "Preços baseados em dados de mercado coletados em 21/05/2026 (manhã BRT).",
        styles["Disclaimer"]
    ))
    items.append(Spacer(1, 0.3 * cm))

    # Legenda de alocação de budget
    items.append(Paragraph("<b>Sugestão de alocação do budget (40.000 coins):</b>", styles["CorpoNegrito"]))
    alocacao = [
        "• <b>16x cartas 84 OVR</b> (Grimaldo/De Paul/Gakpo/Marmoush): ~14.400 coins — maior volume, lucro por unidade menor",
        "• <b>6x cartas 85 OVR</b> (Bremer + Mbeumo): ~8.200 coins — balanço entre preço e margem",
        "• <b>6x cartas 86 OVR</b> (Ruben Dias + Çalhanoğlu): ~8.700 coins — alta demanda em SBCs premium",
        "• <b>2x Jonathan Tah 87 OVR</b>: ~7.000 coins — maior margem por carta, menor liquidez",
        "• <b>Reserva de caixa:</b> ~1.700 coins — para oportunidades de snipe intraday",
    ]
    for a in alocacao:
        items.append(Paragraph(a, styles["BulletItem"]))
    items.append(Spacer(1, 0.2 * cm))
    return items


def build_timing(styles):
    items = []
    items.append(secao_header("⏰  3. ESTRATÉGIA DE TIMING", styles))
    items.append(Spacer(1, 0.25 * cm))

    timing_data = [
        [Paragraph("<b>Fase</b>", styles["TableHeader"]),
         Paragraph("<b>Horário (BRT)</b>", styles["TableHeader"]),
         Paragraph("<b>Ação</b>", styles["TableHeader"]),
         Paragraph("<b>Motivo</b>", styles["TableHeader"])],
        [Paragraph("COMPRA — Janela Principal", styles["TableCell"]),
         Paragraph("Hoje 21/05 · 06:00–10:00", styles["TableCell"]),
         Paragraph("Comprar fodder 84-87 OVR", styles["TableCell"]),
         Paragraph("Mercado saturado com supply de WL/SB rewards. Preços no mínimo do dia.", styles["TableCell"])],
        [Paragraph("COMPRA — Janela Secundária", styles["TableCell"]),
         Paragraph("Hoje 21/05 · 13:00–15:00", styles["TableCell"]),
         Paragraph("Snipe cartas abaixo do BIN", styles["TableCell"]),
         Paragraph("Almoço na Europa reduz liquidez, criando outliers de preço baixo.", styles["TableCell"])],
        [Paragraph("VENDA — Pico TOTS Drop", styles["TableCell"]),
         Paragraph("Sex 22/05 · 14:00–18:00", styles["TableCell"]),
         Paragraph("Vender 60% do portfólio", styles["TableCell"]),
         Paragraph("TOTS lança às 14h00 BRT. SBCs abrem demanda explosiva em 1-2h. Vender no pico da onda.", styles["TableCell"])],
        [Paragraph("VENDA — Pico Weekend", styles["TableCell"]),
         Paragraph("Sáb 23/05 · 10:00–14:00", styles["TableCell"]),
         Paragraph("Vender 40% restante", styles["TableCell"]),
         Paragraph("Sábado de manhã é o horário de maior atividade do FUT. Demand de WL squads + SBCs.", styles["TableCell"])],
    ]
    col_w = [3.5*cm, 3.5*cm, 4.0*cm, 8.0*cm]
    t = Table(timing_data, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
        ("GRID",          (0, 0), (-1, -1), 0.5, VERDE_LINHA),
        ("BOX",           (0, 0), (-1, -1), 1.2, VERDE_MEDIO),
        ("BACKGROUND",    (0, 1), (-1, 1), VERDE_FUNDO),
        ("BACKGROUND",    (0, 2), (-1, 2), BRANCO),
        ("BACKGROUND",    (0, 3), (-1, 3), AMARELO_FUNDO),
        ("BACKGROUND",    (0, 4), (-1, 4), VERDE_FUNDO),
        ("ALIGN",         (3, 1), (3, -1), "LEFT"),
    ]))
    items.append(t)
    items.append(Spacer(1, 0.3 * cm))

    notas = [
        "⚡ <b>Dica crítica de timing:</b> Nos primeiros 30-60 minutos após abertura de SBC, os preços atingem "
        "o pico máximo pois players estão comprando urgentemente para completar. Após 2-3 horas o preço cai. "
        "Liste suas cartas <b>imediatamente</b> quando o SBC abrir.",
        "🔄 <b>Renovação de BIN:</b> Liste cartas com BIN ligeiramente abaixo da média do mercado para garantir "
        "venda rápida. Não seja ganancioso — um lucro travado é melhor que um lucro especulativo.",
    ]
    for n in notas:
        items.append(Paragraph(n, styles["Corpo"]))
    items.append(Spacer(1, 0.2 * cm))
    return items


def build_retorno(styles):
    items = []
    items.append(secao_header("💰  4. ESTIMATIVA DE RETORNO EM 48H", styles))
    items.append(Spacer(1, 0.25 * cm))

    retorno_data = [
        [Paragraph("Cenário", styles["TableHeader"]),
         Paragraph("Budget\nInvestido", styles["TableHeader"]),
         Paragraph("Retorno\nBruto", styles["TableHeader"]),
         Paragraph("Taxa EA\n(5%)", styles["TableHeader"]),
         Paragraph("Lucro\nLíquido", styles["TableHeader"]),
         Paragraph("Capital\nFinal", styles["TableHeader"]),
         Paragraph("ROI\n48h", styles["TableHeader"])],
        [Paragraph("🔵 Conservador\n(+40% spike médio)", styles["TableCell"]),
         Paragraph("40.000", styles["TableCell"]),
         Paragraph("56.000", styles["TableCell"]),
         Paragraph("−2.800", styles["TableCell"]),
         Paragraph("+13.200", styles["TableCell"]),
         Paragraph("53.200", styles["TableCell"]),
         Paragraph("+33%", styles["TableCell"])],
        [Paragraph("🟢 Otimista\n(+80% spike End of Era)", styles["TableCell"]),
         Paragraph("40.000", styles["TableCell"]),
         Paragraph("70.000", styles["TableCell"]),
         Paragraph("−3.500", styles["TableCell"]),
         Paragraph("+26.500", styles["TableCell"]),
         Paragraph("66.500", styles["TableCell"]),
         Paragraph("+66%", styles["TableCell"])],
    ]
    col_w = [3.8*cm, 2.4*cm, 2.4*cm, 2.2*cm, 2.2*cm, 2.4*cm, 1.6*cm]
    t = Table(retorno_data, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
        ("GRID",          (0, 0), (-1, -1), 0.5, VERDE_LINHA),
        ("BOX",           (0, 0), (-1, -1), 1.2, VERDE_MEDIO),
        ("BACKGROUND",    (0, 1), (-1, 1), VERDE_FUNDO),
        ("BACKGROUND",    (0, 2), (-1, 2), colors.HexColor("#DCEDC8")),
        ("TEXTCOLOR",     (4, 1), (4, 2), VERDE_ESCURO),
        ("FONTNAME",      (4, 1), (6, 2), "Helvetica-Bold"),
    ]))
    items.append(t)
    items.append(Spacer(1, 0.2 * cm))
    items.append(Paragraph(
        "* Cenário conservador assume spike de +40% nos 84-86 OVR e +55% nos 87 OVR durante o rush do Ultimate TOTS. "
        "Cenário otimista assume End of Era SBCs (Salah/Griezmann/B.Silva) exigindo squads de 86-88 OVR, "
        "gerando spike de +80-120% no valor dessas cartas. Calcule sempre com taxa EA de 5% sobre o valor bruto.",
        styles["Disclaimer"]
    ))
    items.append(Spacer(1, 0.2 * cm))
    return items


def build_regras(styles):
    items = []
    items.append(secao_header("📋  5. 8 REGRAS DE OURO DO TRADE", styles))
    items.append(Spacer(1, 0.25 * cm))

    regras = [
        ("1", "NUNCA compre cartas sem verificar o histórico de preço nos últimos 7 dias",
         "Preços podem estar artificialmente inflados por manipulação de mercado (snipers). Use FUTBIN/FUT.GG para verificar tendência."),
        ("2", "SEMPRE liste suas cartas durante horários de pico de uso",
         "Entre 19h-23h BRT (18h-22h UK) é quando o maior número de jogadores está online. Mais compradores = venda mais rápida e preço mais alto."),
        ("3", "A taxa de 5% da EA já comeu seus lucros — calcule ANTES de comprar",
         "Se comprar por 1.000 e vender por 1.100, você recebe 1.045 e lucra apenas 45 coins. Sempre calcule: (preço venda × 0.95) − preço compra."),
        ("4", "Diversifique entre ratings diferentes para diluir riscos",
         "Não coloque todo o budget em uma única carta ou rating. Se o spike não acontecer em 84 OVR, pode acontecer em 86 OVR."),
        ("5", "Nunca venda em pânico — aguarde o rebound",
         "Durante lançamentos de promo, o mercado cai e sobe rapidamente. Prices sempre recuperam ligeiramente. Venda no rebound, não na queda."),
        ("6", "Monitore leaks e anúncios da EA em tempo real",
         "Siga @EASPORTSFC no Twitter e r/fut no Reddit. SBCs são anunciados com poucas horas de antecedência — quem age primeiro, lucra mais."),
        ("7", "Use toda a capacidade de listings (30 slots ativos)",
         "Distribua suas cartas em lotes, use BIN competitivo e renove a cada hora se necessário. Volume × margem pequena = lucro consistente."),
        ("8", "Separe sempre uma reserva de 10-15% do capital para oportunidades de snipe",
         "Cartas aparecem abaixo do valor de mercado a qualquer hora. Sem caixa disponível, você perde essas oportunidades que podem dobrar seu capital."),
    ]

    for num, titulo, descricao in regras:
        row_data = [
            [Paragraph(f"<b>{num}</b>", ParagraphStyle("N", fontName="Helvetica-Bold", fontSize=14,
                                                         textColor=BRANCO, alignment=TA_CENTER)),
             Paragraph(f"<b>{titulo}</b><br/>{descricao}", styles["Regra"])]
        ]
        t = Table(row_data, colWidths=[0.8*cm, 18.2*cm])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (0, 0), VERDE_MEDIO),
            ("BACKGROUND",    (1, 0), (1, 0), CINZA_CLARO),
            ("TOPPADDING",    (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING",   (0, 0), (0, 0), 4),
            ("LEFTPADDING",   (1, 0), (1, 0), 8),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("BOX",           (0, 0), (-1, -1), 0.8, VERDE_LINHA),
        ]))
        items.append(t)
        items.append(Spacer(1, 0.15 * cm))
    items.append(Spacer(1, 0.1 * cm))
    return items


def build_disclaimer(styles):
    items = []
    items.append(HRFlowable(width="100%", thickness=0.5, color=VERDE_LINHA))
    items.append(Spacer(1, 0.2 * cm))
    items.append(Paragraph("<b>⚠️  DISCLAIMER</b>", styles["CorpoNegrito"]))
    disclaimer_text = (
        "Este relatório é gerado exclusivamente para fins informativos e educativos sobre estratégias de trading "
        "no modo Ultimate Team do jogo EA Sports FC 26. As análises e previsões apresentadas são baseadas em "
        "dados históricos de mercado, tendências de promo events e padrões de comportamento da comunidade FUT. "
        "O mercado do FUT é altamente volátil e imprevisível — os preços das cartas podem variar drasticamente "
        "em questão de minutos dependendo de anúncios da EA, novas SBCs, promos inesperadas e ações de outros traders. "
        "Não há garantia de lucro em qualquer operação de trading. O autor e os sistemas que geraram este relatório "
        "não se responsabilizam por perdas de coins decorrentes do uso das informações aqui contidas. "
        "Todas as moedas (coins) mencionadas são moeda virtual do jogo e não possuem valor monetário real. "
        "Trade com responsabilidade e nunca invista coins que você não pode perder."
    )
    items.append(Paragraph(disclaimer_text, styles["Disclaimer"]))
    items.append(Spacer(1, 0.2 * cm))
    items.append(Paragraph(
        f"Relatório gerado automaticamente em {DATA_RELATORIO} | EA FC 26 Trading Bot",
        ParagraphStyle("footer", fontName="Helvetica", fontSize=7, textColor=colors.grey, alignment=TA_CENTER)
    ))
    return items


def gerar_pdf():
    doc = SimpleDocTemplate(
        NOME_ARQUIVO,
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )

    styles = build_styles()
    story = []

    story.extend(build_cabecalho(styles))
    story.extend(build_contexto(styles))
    story.extend(build_tabela_recomendacoes(styles))
    story.extend(build_timing(styles))
    story.extend(build_retorno(styles))
    story.extend(build_regras(styles))
    story.extend(build_disclaimer(styles))

    doc.build(story)
    print(f"PDF gerado: {NOME_ARQUIVO}")


if __name__ == "__main__":
    gerar_pdf()
