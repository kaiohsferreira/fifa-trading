#!/usr/bin/env python3
"""Gerador de relatório de trading EA FC 26 - 03/06/2026"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime

OUTPUT = "/home/user/fifa-trading/relatorio-trading-2026-06-03-08h.pdf"

# ──────────────────── CORES ────────────────────
VERDE        = colors.HexColor("#1DB954")
VERDE_ESCURO = colors.HexColor("#0D7A3B")
AMARELO      = colors.HexColor("#F5C518")
VERMELHO     = colors.HexColor("#C0392B")
AZUL_EA      = colors.HexColor("#0A2351")
CINZA_CLARO  = colors.HexColor("#F2F4F6")
CINZA_MEDIO  = colors.HexColor("#D5D8DC")
BRANCO       = colors.white
PRETO        = colors.black

def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles["titulo_doc"] = ParagraphStyle(
        "titulo_doc", parent=base["Title"],
        fontSize=22, textColor=BRANCO,
        alignment=TA_CENTER, leading=28, spaceAfter=4,
        fontName="Helvetica-Bold"
    )
    styles["subtitulo_doc"] = ParagraphStyle(
        "subtitulo_doc", parent=base["Normal"],
        fontSize=11, textColor=AMARELO,
        alignment=TA_CENTER, leading=16,
        fontName="Helvetica-Bold"
    )
    styles["data_doc"] = ParagraphStyle(
        "data_doc", parent=base["Normal"],
        fontSize=9, textColor=CINZA_CLARO,
        alignment=TA_CENTER, leading=14,
        fontName="Helvetica"
    )
    styles["secao"] = ParagraphStyle(
        "secao", parent=base["Heading1"],
        fontSize=13, textColor=BRANCO,
        leading=18, spaceAfter=6, spaceBefore=10,
        fontName="Helvetica-Bold"
    )
    styles["normal"] = ParagraphStyle(
        "normal", parent=base["Normal"],
        fontSize=9.5, textColor=PRETO,
        leading=14, spaceAfter=4, alignment=TA_JUSTIFY,
        fontName="Helvetica"
    )
    styles["normal_bold"] = ParagraphStyle(
        "normal_bold", parent=base["Normal"],
        fontSize=9.5, textColor=PRETO,
        leading=14, spaceAfter=4,
        fontName="Helvetica-Bold"
    )
    styles["bullet"] = ParagraphStyle(
        "bullet", parent=base["Normal"],
        fontSize=9.5, textColor=PRETO,
        leading=15, leftIndent=14, spaceAfter=3,
        fontName="Helvetica"
    )
    styles["aviso"] = ParagraphStyle(
        "aviso", parent=base["Normal"],
        fontSize=8, textColor=colors.HexColor("#555555"),
        leading=12, alignment=TA_JUSTIFY,
        fontName="Helvetica-Oblique"
    )
    styles["regra_num"] = ParagraphStyle(
        "regra_num", parent=base["Normal"],
        fontSize=9.5, textColor=AZUL_EA,
        leading=15, leftIndent=6, spaceAfter=5,
        fontName="Helvetica-Bold"
    )
    styles["regra_txt"] = ParagraphStyle(
        "regra_txt", parent=base["Normal"],
        fontSize=9, textColor=PRETO,
        leading=13, leftIndent=18, spaceAfter=6,
        fontName="Helvetica"
    )
    return styles


def header_banner(styles):
    """Retorna bloco de cabeçalho como tabela de largura total."""
    data = [
        [Paragraph("⚽  RELATÓRIO DE TRADING — EA FC 26 ULTIMATE TEAM", styles["titulo_doc"])],
        [Paragraph("Festival of Football | Path to Glory | Budget: 40.000 coins", styles["subtitulo_doc"])],
        [Paragraph("Data do relatório: 03/06/2026  08:06 UTC  •  Análise válida para as próximas 48 horas", styles["data_doc"])],
    ]
    t = Table(data, colWidths=[19.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), AZUL_EA),
        ("TOPPADDING",    (0, 0), (-1, 0), 14),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 12),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]))
    return t


def section_header(text, styles):
    data = [[Paragraph(text, styles["secao"])]]
    t = Table(data, colWidths=[19.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), AZUL_EA),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
    ]))
    return t


def make_player_table(styles):
    """Tabela principal de oportunidades de trading."""
    headers = [
        "Jogador", "OVR", "Clube / Liga", "Compra\n(coins)",
        "Venda\n(coins)", "Margem\nLíquida", "Janela"
    ]

    # Margem líquida = venda * 0.95 - compra
    rows = [
        # ── 85 OVR ──
        ("Youri Tielemans",      "85", "Aston Villa / PL",     "900",   "1.600",  "620",  "Jun 5–7"),
        ("Dani Carvajal",        "85", "Real Madrid / LaLiga",  "1.100", "1.850",  "658",  "Jun 5–7"),
        ("Scott McTominay",      "85", "Napoli / Serie A",      "3.700", "5.400", "1.430", "Jun 5–7"),
        # ── 86 OVR ──
        ("Claudia Pina",         "86", "FC Barcelona Fem.",     "800",   "1.400",  "530",  "Jun 5–8"),
        ("Michael Olise",        "86", "Bayern München",        "1.100", "1.900",  "705",  "Jun 5–8"),
        ("Bruno Guimarães",      "86", "Newcastle Utd",         "1.100", "1.900",  "705",  "Jun 5–8"),
        ("Hakan Çalhanoğlu",     "86", "Inter Milan",           "1.200", "2.000",  "700",  "Jun 5–8"),
        ("Rúben Dias",           "86", "Manchester City",       "1.200", "2.000",  "700",  "Jun 5–8"),
        ("Nico Williams",        "86", "Athletic Club",         "1.300", "2.100",  "695",  "Jun 5–8"),
        # ── 87 OVR ──
        ("Alessandro Bastoni",   "87", "Inter Milan",           "2.300", "3.500", "1.025", "Jun 5–9"),
        ("Alexis Mac Allister",  "87", "Liverpool",             "2.400", "3.600", "1.020", "Jun 5–9"),
        ("Bruno Fernandes",      "87", "Manchester United",     "2.500", "3.800", "1.110", "Jun 5–9"),
        ("Martin Ødegaard",      "87", "Arsenal",               "2.500", "3.800", "1.110", "Jun 5–9"),
        ("Declan Rice",          "87", "Arsenal",               "2.600", "3.900", "1.105", "Jun 5–9"),
    ]

    col_widths = [4.6*cm, 1.1*cm, 4.0*cm, 1.8*cm, 1.8*cm, 2.0*cm, 2.2*cm]

    table_data = [headers] + [list(r) for r in rows]

    style = TableStyle([
        # Cabeçalho
        ("BACKGROUND",   (0, 0), (-1, 0), AZUL_EA),
        ("TEXTCOLOR",    (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0), 8.5),
        ("ALIGN",        (0, 0), (-1, 0), "CENTER"),
        ("VALIGN",       (0, 0), (-1, 0), "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, 0), 6),
        ("BOTTOMPADDING",(0, 0), (-1, 0), 6),

        # Dados
        ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",     (0, 1), (-1, -1), 8),
        ("ALIGN",        (1, 1), (-1, -1), "CENTER"),
        ("ALIGN",        (0, 1), (0, -1), "LEFT"),
        ("VALIGN",       (0, 1), (-1, -1), "MIDDLE"),
        ("TOPPADDING",   (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 1), (-1, -1), 4),

        # Linhas alternadas
        *[("BACKGROUND", (0, i), (-1, i), CINZA_CLARO) for i in range(2, len(table_data), 2)],

        # Separadores entre grupos de OVR (linha 4 = início 86, linha 7 = início 87)
        ("LINEABOVE", (0, 4),  (-1, 4),  0.8, AZUL_EA),
        ("LINEABOVE", (0, 10), (-1, 10), 0.8, AZUL_EA),

        # Coluna margem em verde
        ("TEXTCOLOR",  (5, 1), (5, -1), VERDE_ESCURO),
        ("FONTNAME",   (5, 1), (5, -1), "Helvetica-Bold"),

        # Grid
        ("GRID",        (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
        ("ROWBACKGROUNDS", (0, 0), (-1, 0), [AZUL_EA]),
    ])

    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(style)
    return t


def make_budget_table(styles):
    """Tabela de alocação de budget."""
    headers = ["Estratégia", "Volume", "Investimento", "Retorno Cons.", "Retorno Otim."]
    rows = [
        ("85 OVR Fodder Flip",     "15 cartas", "~13.500c", "~19.000c (+41%)", "~23.000c (+70%)"),
        ("86 OVR Fodder Flip",     "15 cartas", "~16.500c", "~25.000c (+52%)", "~31.000c (+88%)"),
        ("87 OVR Fodder Flip",     "4 cartas",  "~ 9.600c", "~13.300c (+39%)", "~15.200c (+58%)"),
        ("Reserva / Oportunidade", "—",         "~  400c",  "—",               "—"),
        ("TOTAL",                  "34 cartas", "40.000c",  "~57.300c (+43%)", "~69.200c (+73%)"),
    ]
    col_widths = [4.8*cm, 2.0*cm, 2.8*cm, 3.4*cm, 3.4*cm]
    table_data = [headers] + [list(r) for r in rows]
    style = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 8.5),
        ("ALIGN",         (0, 0), (-1, 0), "CENTER"),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 8.5),
        ("ALIGN",         (1, 1), (-1, -1), "CENTER"),
        ("ALIGN",         (0, 1), (0, -1), "LEFT"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        *[("BACKGROUND",  (0, i), (-1, i), CINZA_CLARO) for i in range(2, len(table_data), 2)],
        # Linha de total em destaque
        ("BACKGROUND",    (0, -1), (-1, -1), AZUL_EA),
        ("TEXTCOLOR",     (0, -1), (-1, -1), BRANCO),
        ("FONTNAME",      (0, -1), (-1, -1), "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
    ])
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(style)
    return t


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=1.2*cm, leftMargin=1.2*cm,
        topMargin=1.2*cm,   bottomMargin=1.5*cm,
        title="Relatório Trading EA FC 26 — 03/06/2026",
        author="EA FC 26 Market Agent"
    )

    styles = build_styles()
    story  = []

    # ══════════════════════════════════════════
    # CABEÇALHO
    # ══════════════════════════════════════════
    story.append(header_banner(styles))
    story.append(Spacer(1, 0.4*cm))

    # ══════════════════════════════════════════
    # 1. CONTEXTO DO MERCADO
    # ══════════════════════════════════════════
    story.append(section_header("1.  CONTEXTO DO MERCADO — JUNHO 2026", styles))
    story.append(Spacer(1, 0.25*cm))

    ctx_items = [
        ("<b>Evento ativo agora:</b> The World's Game Update (lançado 28/05) — 53 seleções nacionais "
         "licenciadas, novo sistema de Tokens e conteúdo extra de FUT. As novidades de FUT do update "
         "entram ao vivo hoje, 04/06, preparando o terreno para o Festival of Football."),

        ("<b>Grande evento iminente:</b> <font color='#0A2351'><b>Festival of Football</b></font> — "
         "começa em 24 horas (04/06). Inclui: Path to Glory Team 1 (cartas live que evoluem com a "
         "Copa do Mundo 2026), ícones Mario Kempes e Rivelino, Token Store com packs e Evolutions, "
         "e SBCs temáticos novos até 24/07."),

        ("<b>Path to Glory Team 1 (05/06 — 19/06):</b> Cartas confirmadas/vazadas: Musiala 95 "
         "(Bayern / Alemanha), Vinicius Jr 94 (Real Madrid / Brasil), Bukayo Saka 94 (Arsenal / "
         "Inglaterra), De Bruyne 93 (Man City / Bélgica), Rúben Dias 93 (Man City / Portugal), "
         "Rodri 93 (Man City / Espanha), Pulisic 91 (AC Milan / EUA), Marmoush 90 (Man City / Egito), "
         "James Rodríguez 89 (Rayo Vallecano / Colômbia), Davies 88 (Bayern / Canadá)."),

        ("<b>Tendência de mercado hoje (03/06):</b> Mercado em baixa pré-evento — "
         "jogadores 85-87 OVR em fundo de preço. Quando os SBCs do Festival of Football forem "
         "ao ar na tarde de 04/06 (BRT), a demanda por fodder dispara em 40–90% em 2–6 horas."),

        ("<b>Tokens da Festival of Football:</b> Até 1.000 Tokens/semana via Rivals, Squad Battles, "
         "Rush, Objectives e SBCs. A Token Store abre com packs e Evolutions que exigem cartas 85-87 "
         "OVR como insumo, criando pico extra de demanda por fodder.")
    ]

    for item in ctx_items:
        story.append(Paragraph(f"• {item}", styles["bullet"]))
        story.append(Spacer(1, 0.08*cm))

    story.append(Spacer(1, 0.3*cm))

    # ══════════════════════════════════════════
    # 2. TABELA DE OPORTUNIDADES
    # ══════════════════════════════════════════
    story.append(section_header("2.  OPORTUNIDADES DE COMPRA — BUDGET 40.000 COINS", styles))
    story.append(Spacer(1, 0.25*cm))

    nota_tabela = ("Preços de compra baseados em mercado pré-evento (03/06 manhã). "
                   "Preços de venda estimados para o pico de SBC demand (05–09/06). "
                   "<b>Margem líquida</b> = venda × 0,95 − compra (já descontada taxa EA de 5%).")
    story.append(Paragraph(nota_tabela, styles["normal"]))
    story.append(Spacer(1, 0.2*cm))
    story.append(make_player_table(styles))
    story.append(Spacer(1, 0.3*cm))

    # ══════════════════════════════════════════
    # 3. ALOCAÇÃO DO BUDGET
    # ══════════════════════════════════════════
    story.append(section_header("3.  ALOCAÇÃO DO BUDGET — 40.000 COINS", styles))
    story.append(Spacer(1, 0.25*cm))
    story.append(make_budget_table(styles))
    story.append(Spacer(1, 0.3*cm))

    # ══════════════════════════════════════════
    # 4. ESTRATÉGIA DE TIMING
    # ══════════════════════════════════════════
    story.append(section_header("4.  ESTRATÉGIA DE TIMING", styles))
    story.append(Spacer(1, 0.25*cm))

    timing_data = [
        ["Fase", "Quando", "Ação", "Racional"],
        ["PRE-BUY",  "03/06  08h–14h BRT", "Comprar 85-87 OVR fodder\nnos preços listados",
         "Mercado pré-evento no fundo;\nmaior oferta, menor demanda"],
        ["HOLD",     "03/06  14h–04/06 18h BRT", "Manter cartas no clube.\nNão vender antes do evento",
         "SBCs e Token Store ainda\nnão exigem fodder"],
        ["VENDA 1",  "04/06  18h–22h BRT\n(lançamento FUT content)", "Vender 30% do estoque\nse preço subir 30%+",
         "Primeiros SBCs do Festival\nof Football ao vivo = 1ª spike"],
        ["VENDA 2",  "05/06  18h–23h BRT\n(Path to Glory live)", "Vender 50% do estoque\n(preço pico esperado)",
         "Path to Glory Team 1 gera\npico máximo de SBC demand"],
        ["VENDA 3",  "06–09/06 qualquer hora", "Vender restante se preço\nainda estiver alto",
         "Demanda sustentada por\nToken Store objectives"],
        ["SAÍDA",    "09/06 após recompensas\nde Rivals (quinta-feira)", "Liquidar posições restantes\ne avaliar reinvestimento",
         "Preços voltam a cair após\npico inicial do evento"],
    ]

    col_widths_t = [2.2*cm, 3.8*cm, 4.5*cm, 5.0*cm]
    ts = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_EA),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8),
        ("ALIGN",         (0, 0), (-1, -1), "LEFT"),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        *[("BACKGROUND",  (0, i), (-1, i), CINZA_CLARO) for i in range(2, len(timing_data), 2)],
        # Destaque fase VENDA 2 (linha 4) em verde claro
        ("BACKGROUND",    (0, 4), (-1, 4), colors.HexColor("#D5F5E3")),
        ("FONTNAME",      (0, 0), (0, -1), "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
    ])
    timing_table = Table(timing_data, colWidths=col_widths_t, repeatRows=1)
    timing_table.setStyle(ts)
    story.append(timing_table)
    story.append(Spacer(1, 0.3*cm))

    # ══════════════════════════════════════════
    # 5. ESTIMATIVA DE RETORNO EM 48H
    # ══════════════════════════════════════════
    story.append(section_header("5.  ESTIMATIVA DE RETORNO EM 48 HORAS", styles))
    story.append(Spacer(1, 0.25*cm))

    cenarios = [
        ["Cenário", "Premissa", "Capital Investido",
         "Capital Final", "Lucro Líquido", "ROI"],
        ["CONSERVADOR",
         "SBCs menores, demanda\n+30–40% sobre preço base",
         "40.000c", "~57.300c", "+17.300c", "+43%"],
        ["OTIMISTA",
         "SBCs grandes + Token Store\nObjectives; demanda +70–90%",
         "40.000c", "~69.200c", "+29.200c", "+73%"],
        ["PESSIMISTA\n(stop-loss)",
         "Evento adiado ou SBCs\ncom fodder genérico apenas",
         "40.000c", "~43.800c", "+3.800c", "+9.5%"],
    ]

    col_widths_c = [2.8*cm, 4.4*cm, 3.0*cm, 2.8*cm, 2.5*cm, 1.8*cm]
    cs = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), AZUL_EA),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8.5),
        ("ALIGN",         (0, 0), (-1, 0), "CENTER"),
        ("ALIGN",         (0, 1), (-1, -1), "CENTER"),
        ("ALIGN",         (1, 1), (1, -1), "LEFT"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        # Conservador
        ("BACKGROUND",    (0, 1), (-1, 1), colors.HexColor("#EBF5FB")),
        ("TEXTCOLOR",     (4, 1), (5, 1), colors.HexColor("#1A5276")),
        ("FONTNAME",      (4, 1), (5, 1), "Helvetica-Bold"),
        # Otimista
        ("BACKGROUND",    (0, 2), (-1, 2), colors.HexColor("#EAFAF1")),
        ("TEXTCOLOR",     (4, 2), (5, 2), VERDE_ESCURO),
        ("FONTNAME",      (4, 2), (5, 2), "Helvetica-Bold"),
        # Pessimista
        ("BACKGROUND",    (0, 3), (-1, 3), colors.HexColor("#FDEDEC")),
        ("TEXTCOLOR",     (4, 3), (5, 3), VERMELHO),
        ("FONTNAME",      (4, 3), (5, 3), "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.4, CINZA_MEDIO),
    ])
    cenario_table = Table(cenarios, colWidths=col_widths_c)
    cenario_table.setStyle(cs)
    story.append(cenario_table)
    story.append(Spacer(1, 0.3*cm))

    # ══════════════════════════════════════════
    # 6. 8 REGRAS DE OURO DO TRADE
    # ══════════════════════════════════════════
    story.append(section_header("6.  8 REGRAS DE OURO DO TRADE", styles))
    story.append(Spacer(1, 0.25*cm))

    regras = [
        ("1. COMPRE NO MEDO, VENDA NA EUFORIA",
         "Os melhores preços de compra aparecem quando o mercado está calmo, sem evento ativo. "
         "Venda sempre durante o pico de demanda — nunca antes."),
        ("2. CALCULE SEMPRE A MARGEM COM A TAXA DE 5%",
         "A EA cobra 5% em todo venda. Fórmula: Lucro = (Preço de Venda × 0,95) − Preço de Compra. "
         "Se a margem for negativa após o cálculo, não compre."),
        ("3. DIVERSIFIQUE O PORTFÓLIO",
         "Nunca coloque todo o budget em um único rating ou jogador. Distribua entre 85, 86 e 87 OVR "
         "para reduzir risco de oversupply em uma faixa específica."),
        ("4. DEFINA STOP-LOSS ANTES DE COMPRAR",
         "Decida o preço mínimo de saída antes de comprar. Se o mercado cair 15% abaixo do "
         "esperado, venda mesmo com prejuízo para preservar capital."),
        ("5. RESPEITE O TIMING DOS EVENTOS",
         "O pico de demanda por fodder ocorre nas primeiras 2–6 horas após o lançamento de um SBC "
         "grande. Após 24h, a oferta normaliza. Vender tarde é quase sempre vender barato."),
        ("6. MONITORE OS SBCs CONSTANTEMENTE",
         "Use FUTBIN ou FUT.GG para checar novos SBCs ao vivo. SBCs de ICON ou jogador especial "
         "com requerimento de 85+ OVR disparam o mercado instantaneamente."),
        ("7. NUNCA PERSIGA CARTAS EM ALTA",
         "Se um jogador já subiu 50%+, o pico provavelmente passou. Procure cartas que ainda estão "
         "flat e têm catalisador claro de alta nas próximas 24–48h."),
        ("8. GUARDE SEMPRE 10% DE RESERVA",
         "Mantenha ao menos 4.000c livres para aproveitar oportunidades relâmpago ou cobrir "
         "posições perdidas. Capital parado é custo de oportunidade, mas capital zero é risco total."),
    ]

    for num, (titulo, texto) in enumerate(regras, 1):
        data_r = [[Paragraph(f"🔑  {titulo}", styles["regra_num"])],
                  [Paragraph(texto, styles["regra_txt"])]]
        t_r = Table(data_r, colWidths=[19.0*cm])
        bg = CINZA_CLARO if num % 2 == 0 else BRANCO
        t_r.setStyle(TableStyle([
            ("BACKGROUND",   (0, 0), (-1, -1), bg),
            ("LEFTPADDING",  (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING",   (0, 0), (-1, 0),  4),
            ("BOTTOMPADDING",(0, -1),(-1, -1), 4),
            ("LINEBELOW",    (0, -1),(-1, -1), 0.4, CINZA_MEDIO),
        ]))
        story.append(KeepTogether([t_r]))

    story.append(Spacer(1, 0.4*cm))

    # ══════════════════════════════════════════
    # DISCLAIMER
    # ══════════════════════════════════════════
    story.append(HRFlowable(width="100%", thickness=0.8, color=CINZA_MEDIO))
    story.append(Spacer(1, 0.15*cm))
    disclaimer = (
        "⚠️  DISCLAIMER: Este relatório é gerado automaticamente com base em pesquisa de mercado "
        "realizada em 03/06/2026 às 08:06 UTC e tem caráter exclusivamente informativo. Preços do "
        "mercado de EA FC 26 Ultimate Team são voláteis e podem mudar em minutos. As estimativas "
        "de lucro não constituem garantia de retorno. O author e o repositório não se responsabilizam "
        "por perdas de coins resultantes das estratégias descritas. Jogue com responsabilidade. "
        "EA SPORTS FC™ e Ultimate Team™ são marcas registradas da Electronic Arts Inc."
    )
    story.append(Paragraph(disclaimer, styles["aviso"]))

    # ══════════════════════════════════════════
    # BUILD
    # ══════════════════════════════════════════
    doc.build(story)
    print(f"PDF gerado: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
