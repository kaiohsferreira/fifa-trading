#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Relatório de Trading - EA FC 26 Ultimate Team
Data: 25/05/2026 14:03 UTC
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import PageBreak
import os

# ─── Configurações ───────────────────────────────────────────────────────────
FILENAME = "relatorio-trading-2026-05-25-14h.pdf"
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAME)

# Paleta de cores EA FC 26
COR_PRINCIPAL   = colors.HexColor("#00D4AA")   # verde-azulado EA FC
COR_FUNDO_DARK  = colors.HexColor("#0A0E1A")   # fundo escuro
COR_FUNDO_CARD  = colors.HexColor("#1A2035")   # azul-escuro cards
COR_DOURADO     = colors.HexColor("#FFD700")   # dourado
COR_LARANJA     = colors.HexColor("#FF6B35")   # laranja alerta
COR_VERMELHO    = colors.HexColor("#E53935")   # vermelho venda
COR_VERDE       = colors.HexColor("#43A047")   # verde compra
COR_CINZA_CLARO = colors.HexColor("#B0BEC5")   # cinza texto secundário
COR_BRANCO      = colors.white
COR_PRETO       = colors.black

PAGE_W, PAGE_H = A4


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "TituloRelatorio",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=COR_PRINCIPAL,
        alignment=TA_CENTER,
        spaceAfter=4,
        leading=26,
    ))
    styles.add(ParagraphStyle(
        "Subtitulo",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=COR_DOURADO,
        alignment=TA_CENTER,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        "DataHora",
        fontName="Helvetica",
        fontSize=10,
        textColor=COR_CINZA_CLARO,
        alignment=TA_CENTER,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        "SecaoTitulo",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=COR_PRINCIPAL,
        spaceBefore=12,
        spaceAfter=4,
        leading=16,
    ))
    styles.add(ParagraphStyle(
        "Corpo",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=COR_PRETO,
        spaceAfter=5,
        leading=14,
        alignment=TA_JUSTIFY,
    ))
    styles.add(ParagraphStyle(
        "CorpoNegrito",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=COR_PRETO,
        spaceAfter=4,
        leading=14,
    ))
    styles.add(ParagraphStyle(
        "BulletItem",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=COR_PRETO,
        leftIndent=12,
        spaceAfter=3,
        leading=14,
    ))
    styles.add(ParagraphStyle(
        "Aviso",
        fontName="Helvetica-Oblique",
        fontSize=8,
        textColor=COR_CINZA_CLARO,
        alignment=TA_JUSTIFY,
        leading=12,
        spaceBefore=6,
    ))
    styles.add(ParagraphStyle(
        "Regra",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=COR_PRETO,
        leftIndent=14,
        spaceAfter=4,
        leading=14,
    ))
    styles.add(ParagraphStyle(
        "RegraNegrito",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=COR_FUNDO_DARK,
        spaceAfter=2,
        leading=14,
    ))
    return styles


def header_table(styles):
    """Bloco de cabeçalho com logo textual + data/hora."""
    data = [
        [Paragraph("⚽  EA FC 26 ULTIMATE TEAM", styles["TituloRelatorio"])],
        [Paragraph("RELATÓRIO DIÁRIO DE TRADING", styles["Subtitulo"])],
        [Paragraph("Data / Hora:  25/05/2026  14:03 UTC", styles["DataHora"])],
        [Paragraph("Budget: 40.000 coins  •  Estratégia: SBC Fodder Flipping + Evolutions + Thursday Flip", styles["DataHora"])],
    ]
    t = Table(data, colWidths=[PAGE_W - 28*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), COR_FUNDO_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return t


def secao_contexto(styles):
    elems = []
    elems.append(Paragraph("📊  CONTEXTO DO MERCADO — 25/05/2026", styles["SecaoTitulo"]))
    elems.append(HRFlowable(width="100%", thickness=1.5, color=COR_PRINCIPAL))
    elems.append(Spacer(1, 4))

    texto = (
        "Estamos na <b>Semana 6 (final) do TOTS 26 — Ultimate TOTS</b>, liberado em "
        "22/05/2026 e vigente até <b>29/05/2026</b>. São 60 cartas TOTS em pacotes "
        "simultaneamente, gerando o maior pico de oferta de cartas high-rated do ano. "
        "Paralelamente, os SBCs de <b>End of an Era</b> (Salah 96 OVR, Griezmann 94, "
        "Bernardo Silva 93, Robertson 93, Goretzka 93) consomem quantidades "
        "expressivas de <i>fodder</i> 83–88, criando pressão de compra sobre esse segmento "
        "de mercado — exatamente o nicho ideal para o nosso budget."
    )
    elems.append(Paragraph(texto, styles["Corpo"]))

    bullets = [
        "🔴  <b>Oferta alta:</b> pacotes TOTS flooding → preços de cartas meta em queda",
        "🟢  <b>Demanda de fodder alta:</b> SBCs End of Era + SBCs semanais → 83–88 em alta",
        "🟡  <b>Janela de oportunidade:</b> última semana de TOTS → últimas 96h de alto volume de SBCs",
        "🔵  <b>Thursday Flip (amanhã 26/05):</b> Rivals rewards → pico de oferta → preços caem → comprar",
        "⚪  <b>Pós-TOTS (a partir de 30/05):</b> abastecimento de pacotes cai → preços de cartas sobem",
    ]
    for b in bullets:
        elems.append(Paragraph(b, styles["BulletItem"]))

    return elems


def tabela_cartas(styles):
    elems = []
    elems.append(Spacer(1, 6))
    elems.append(Paragraph("💎  CARTAS RECOMENDADAS — COMPRA & VENDA", styles["SecaoTitulo"]))
    elems.append(HRFlowable(width="100%", thickness=1.5, color=COR_PRINCIPAL))
    elems.append(Spacer(1, 4))

    intro = (
        "Tabela com jogadores reais identificados via FUTBIN/FUT.GG/RealSport101 "
        "para flipping de <i>SBC fodder</i> dentro do budget de 40.000 coins. "
        "Margem líquida calculada após a taxa de <b>5% da EA</b>."
    )
    elems.append(Paragraph(intro, styles["Corpo"]))
    elems.append(Spacer(1, 6))

    # Cabeçalho
    headers = [
        Paragraph("<b>Jogador</b>",          styles["CorpoNegrito"]),
        Paragraph("<b>OVR</b>",              styles["CorpoNegrito"]),
        Paragraph("<b>Clube / Liga</b>",     styles["CorpoNegrito"]),
        Paragraph("<b>Compra\n(coins)</b>",  styles["CorpoNegrito"]),
        Paragraph("<b>Venda\n(coins)</b>",   styles["CorpoNegrito"]),
        Paragraph("<b>Margem\nLíquida</b>",  styles["CorpoNegrito"]),
        Paragraph("<b>Estratégia</b>",       styles["CorpoNegrito"]),
    ]

    # Dados — preços baseados em pesquisa (FUTBIN / RealSport101 / OperationSports)
    rows = [
        # [Jogador, OVR, Clube, Compra, Venda, Margem, Estratégia]
        ["Halhanoğlu (Calhanoglu)", "86", "Inter / Serie A",
         "1.300", "2.200", "+~790", "SBC Fodder 86"],
        ["Rüben Dias", "86", "Man City / PL",
         "1.300", "2.100", "+~695", "SBC Fodder 86"],
        ["Bruno Guimarães", "86", "Newcastle / PL",
         "1.400", "2.300", "+~785", "SBC Fodder 86"],
        ["Rüdiger", "86", "Real Madrid / LaLiga",
         "1.500", "2.500", "+~875", "SBC Fodder 86"],
        ["Ødegaard", "87", "Arsenal / PL",
         "1.800", "3.000", "+~1.050", "SBC Fodder 87"],
        ["Alessandro Bastoni", "87", "Inter / Serie A",
         "2.000", "3.400", "+~1.230", "SBC Fodder 87"],
        ["Sam Kerr", "87", "Chelsea / WSL",
         "1.900", "3.200", "+~1.140", "SBC Fodder 87 WWOTS"],
        ["Guro Reiten", "86", "Chelsea / WSL",
         "1.300", "2.200", "+~790", "SBC Fodder WWOTS"],
        ["Christiane Endler", "88", "Lyon / D1F",
         "7.000", "10.500", "+~2.975", "End of Era SBC demand"],
        ["Gabriel Magalhães", "88", "Arsenal / PL",
         "8.000", "12.500", "+~3.875", "End of Era SBC demand"],
        ["Robert Lewandowski", "88", "Barcelona / LaLiga",
         "7.500", "11.500", "+~3.425", "End of Era SBC demand"],
        ["Irene Paredes", "88", "Barcelona / LaLiga",
         "9.000", "13.500", "+~3.825", "End of Era SBC demand"],
    ]

    table_data = [headers]
    for r in rows:
        table_data.append([
            Paragraph(r[0], styles["Corpo"]),
            Paragraph(r[1], styles["Corpo"]),
            Paragraph(r[2], styles["Corpo"]),
            Paragraph(r[3], styles["Corpo"]),
            Paragraph(r[4], styles["Corpo"]),
            Paragraph(r[5], styles["Corpo"]),
            Paragraph(r[6], styles["Corpo"]),
        ])

    col_widths = [46*mm, 12*mm, 36*mm, 20*mm, 20*mm, 22*mm, 32*mm]
    t = Table(table_data, colWidths=col_widths, repeatRows=1)

    ts = TableStyle([
        # Cabeçalho
        ("BACKGROUND",    (0, 0), (-1, 0), COR_FUNDO_DARK),
        ("TEXTCOLOR",     (0, 0), (-1, 0), COR_PRINCIPAL),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 9),
        ("ALIGN",         (0, 0), (-1, 0), "CENTER"),
        ("VALIGN",        (0, 0), (-1, 0), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, 0), 6),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        # Linhas pares
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F0F4F8"), colors.white]),
        # Grade
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
        ("LINEBELOW",     (0, 0), (-1, 0),  1.5, COR_PRINCIPAL),
        # Alinhamentos
        ("ALIGN",  (1, 1), (1, -1), "CENTER"),
        ("ALIGN",  (3, 1), (5, -1), "CENTER"),
        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        # Coluna margem em verde
        ("TEXTCOLOR",     (5, 1), (5, -1), COR_VERDE),
        ("FONTNAME",      (5, 1), (5, -1), "Helvetica-Bold"),
        # Coluna compra em azul
        ("TEXTCOLOR",     (3, 1), (3, -1), colors.HexColor("#1565C0")),
        # Coluna venda em vermelho
        ("TEXTCOLOR",     (4, 1), (4, -1), COR_VERMELHO),
    ])
    t.setStyle(ts)
    elems.append(t)

    # Nota de budget
    elems.append(Spacer(1, 6))
    nota = (
        "<b>Gestão de Budget (40.000 coins):</b> Recomenda-se distribuir em lotes: "
        "70% em fodder 86–87 (alta rotatividade, risco baixo) e 30% em fodder 88 "
        "(maior margem, ciclo de 24–48h). Exemplo: 28.000 coins → ~18 cartas 86-rated "
        "e 12.000 coins → 1–2 cartas 88-rated."
    )
    elems.append(Paragraph(nota, styles["Corpo"]))
    return elems


def secao_timing(styles):
    elems = []
    elems.append(Spacer(1, 6))
    elems.append(Paragraph("⏱️  ESTRATÉGIA DE TIMING", styles["SecaoTitulo"]))
    elems.append(HRFlowable(width="100%", thickness=1.5, color=COR_PRINCIPAL))
    elems.append(Spacer(1, 4))

    timing_data = [
        [Paragraph("<b>Período</b>", styles["CorpoNegrito"]),
         Paragraph("<b>Ação</b>", styles["CorpoNegrito"]),
         Paragraph("<b>Racional</b>", styles["CorpoNegrito"])],

        [Paragraph("Hoje 25/05\n14h–20h UTC", styles["Corpo"]),
         Paragraph("🟢 COMPRAR\n86–87 rated fodder", styles["Corpo"]),
         Paragraph("Mercado ainda ativo pós-lançamento Ultimate TOTS. "
                   "SBCs End of Era consumindo estoque. "
                   "Preço de fodder levemente elevado → comprar agora antes de nova onda.",
                   styles["Corpo"])],

        [Paragraph("Amanhã 26/05\n08h–12h UTC\n(Thursday Flip)", styles["Corpo"]),
         Paragraph("🔵 COMPRAR MAIS\n+ barato possível", styles["Corpo"]),
         Paragraph("Rivals Rewards caem → oferta explode → fodder 86–87 pode cair "
                   "10–25%. Janela de compra mais barata da semana. "
                   "Meta: encher estoque para flipar no fim de semana.",
                   styles["Corpo"])],

        [Paragraph("26/05–27/05\n(Sex–Sáb) Noite", styles["Corpo"]),
         Paragraph("🔴 VENDER\nfodder 86–87", styles["Corpo"]),
         Paragraph("WL (Weekend League) começa → demanda por SBCs e upgrades sobe. "
                   "Players buscam fodder para terminar SBCs semanais "
                   "→ preços sobem 20–40%.",
                   styles["Corpo"])],

        [Paragraph("27/05–28/05\n(Sáb–Dom)", styles["Corpo"]),
         Paragraph("🟢 COMPRAR\n88 rated fodder", styles["Corpo"]),
         Paragraph("Fim de WL → SBC runners buscam 88-rated para End of Era. "
                   "Comprar 88s em baixa (domingo noite = mínimo da semana).",
                   styles["Corpo"])],

        [Paragraph("28/05–29/05\n(Dom–Seg)", styles["Corpo"]),
         Paragraph("🔴 VENDER\n88 rated", styles["Corpo"]),
         Paragraph("Último dia de TOTS (29/05) → rush final de SBCs. "
                   "Jogadores tentam completar End of Era → pico de demanda de 88s "
                   "nas últimas 48h do evento.",
                   styles["Corpo"])],
    ]

    col_widths = [35*mm, 35*mm, 112*mm]
    t = Table(timing_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), COR_FUNDO_DARK),
        ("TEXTCOLOR",     (0, 0), (-1, 0), COR_PRINCIPAL),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
        ("LINEBELOW",     (0, 0), (-1, 0),  1.5, COR_PRINCIPAL),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [colors.HexColor("#F0F4F8"), colors.white]),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    elems.append(t)
    return elems


def secao_retorno(styles):
    elems = []
    elems.append(Spacer(1, 8))
    elems.append(Paragraph("📈  ESTIMATIVA DE RETORNO EM 48 HORAS", styles["SecaoTitulo"]))
    elems.append(HRFlowable(width="100%", thickness=1.5, color=COR_PRINCIPAL))
    elems.append(Spacer(1, 4))

    # Premissas
    premissas = (
        "<b>Premissas do cálculo:</b> Budget de 40.000 coins | Lote A: 28.000 coins em "
        "fodder 86–87 (≈16 cartas × 1.750 avg) | Lote B: 12.000 coins em fodder 88 "
        "(≈1,5 cartas × 8.000 avg) | Taxa EA: 5% sobre venda | Giro completo em 48h."
    )
    elems.append(Paragraph(premissas, styles["Corpo"]))
    elems.append(Spacer(1, 6))

    retorno_data = [
        [Paragraph("<b>Cenário</b>", styles["CorpoNegrito"]),
         Paragraph("<b>Preço\nCompra</b>", styles["CorpoNegrito"]),
         Paragraph("<b>Preço\nVenda</b>", styles["CorpoNegrito"]),
         Paragraph("<b>Receita\nBruta</b>", styles["CorpoNegrito"]),
         Paragraph("<b>Taxa\nEA (5%)</b>", styles["CorpoNegrito"]),
         Paragraph("<b>Lucro\nLíquido</b>", styles["CorpoNegrito"]),
         Paragraph("<b>ROI</b>", styles["CorpoNegrito"])],

        [Paragraph("🟡 Conservador\n(+20% valorização)", styles["Corpo"]),
         Paragraph("40.000", styles["Corpo"]),
         Paragraph("48.000", styles["Corpo"]),
         Paragraph("48.000", styles["Corpo"]),
         Paragraph("2.400", styles["Corpo"]),
         Paragraph("5.600", styles["Corpo"]),
         Paragraph("+14%", styles["Corpo"])],

        [Paragraph("🟢 Base\n(+35% valorização)", styles["Corpo"]),
         Paragraph("40.000", styles["Corpo"]),
         Paragraph("54.000", styles["Corpo"]),
         Paragraph("54.000", styles["Corpo"]),
         Paragraph("2.700", styles["Corpo"]),
         Paragraph("11.300", styles["Corpo"]),
         Paragraph("+28,3%", styles["Corpo"])],

        [Paragraph("🚀 Otimista\n(+50% valorização)", styles["Corpo"]),
         Paragraph("40.000", styles["Corpo"]),
         Paragraph("60.000", styles["Corpo"]),
         Paragraph("60.000", styles["Corpo"]),
         Paragraph("3.000", styles["Corpo"]),
         Paragraph("17.000", styles["Corpo"]),
         Paragraph("+42,5%", styles["Corpo"])],
    ]

    col_widths = [42*mm, 22*mm, 22*mm, 22*mm, 22*mm, 22*mm, 16*mm]
    t = Table(retorno_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), COR_FUNDO_DARK),
        ("TEXTCOLOR",     (0, 0), (-1, 0), COR_PRINCIPAL),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
        ("LINEBELOW",     (0, 0), (-1, 0),  1.5, COR_PRINCIPAL),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [colors.HexColor("#FFF9C4"), colors.HexColor("#E8F5E9"), colors.HexColor("#E3F2FD")]),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",         (1, 0), (-1, -1), "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        # Coluna lucro em verde
        ("TEXTCOLOR",     (5, 1), (5, -1), COR_VERDE),
        ("FONTNAME",      (5, 1), (5, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (6, 1), (6, -1), COR_VERDE),
        ("FONTNAME",      (6, 1), (6, -1), "Helvetica-Bold"),
    ]))
    elems.append(t)

    obs = (
        "<b>Nota:</b> Cenário Conservador assume low-demand Thursday com venda no sábado. "
        "Cenário Base assume Thursday flip + venda pico WL. "
        "Cenário Otimista inclui rush final TOTS (28–29/05) com 88-rated a +50%. "
        "Todos os cálculos consideram taxa de 5% EA e não incluem tempo de listagem."
    )
    elems.append(Spacer(1, 6))
    elems.append(Paragraph(obs, styles["Corpo"]))
    return elems


def secao_regras(styles):
    elems = []
    elems.append(Spacer(1, 8))
    elems.append(Paragraph("🏆  8 REGRAS DE OURO DO TRADE", styles["SecaoTitulo"]))
    elems.append(HRFlowable(width="100%", thickness=1.5, color=COR_DOURADO))
    elems.append(Spacer(1, 6))

    regras = [
        ("1", "Nunca invista 100% do budget em uma única carta.",
         "Diversifique em lotes de no máximo 25% por jogador/tipo. "
         "Perda de um lote não compromete o capital total."),

        ("2", "Compre na janela de oversupply, venda na de demand.",
         "Thursday (Rivals rewards) e domingos (WL ending) = janelas de compra. "
         "Sexta à noite e sábado à tarde = janelas de venda."),

        ("3", "Sempre calcule a margem líquida ANTES de comprar.",
         "Fórmula: (Preço de venda × 0,95) - Preço de compra = Lucro líquido. "
         "Só execute se margem ≥ 15% (absorve variação de mercado)."),

        ("4", "Fique de olho nos SBCs novos — eles criam demanda instantânea.",
         "Um SBC novo que exige 85-rated pode triplicar o preço de fodder em horas. "
         "Compre antes do rush, venda no pico."),

        ("5", "Nunca segure cards por mais de 48h sem motivo claro.",
         "Cartas paradas = capital parado. Se o preço não subiu em 24h, "
         "reavalie e, se necessário, venda com margem menor para liberar budget."),

        ("6", "Defina stop-loss: se o preço cair 20%, venda e proteja o capital.",
         "Mercados de TOTS são voláteis. Um pacote especial pode crashar preços em minutos. "
         "Ter disciplina de stop evita prejuízos maiores."),

        ("7", "Mantenha 20% de reserva para oportunidades relâmpago.",
         "Lightning rounds, SBC surpresas e crashes repentinos criam janelas de "
         "segundos. Budget reservado = agilidade para agir rápido."),

        ("8", "Registre todos os trades: compra, venda, lucro, data e hora.",
         "Dados históricos são a base para melhorar sua estratégia. "
         "Sem registro não há aprendizado nem controle de risco real."),
    ]

    for num, titulo, desc in regras:
        # Fundo colorido para o número
        row_data = [
            [Paragraph(f"<b>{num}</b>", ParagraphStyle(
                "NumRegra", fontName="Helvetica-Bold", fontSize=14,
                textColor=COR_BRANCO, alignment=TA_CENTER)),
             Paragraph(f"<b>{titulo}</b><br/><font size=9>{desc}</font>",
                       styles["Regra"])],
        ]
        rt = Table(row_data, colWidths=[12*mm, 165*mm])
        rt.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (0, 0), COR_PRINCIPAL),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING",   (1, 0), (1, 0), 8),
            ("BOX",           (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ]))
        elems.append(rt)
        elems.append(Spacer(1, 3))

    return elems


def secao_disclaimer(styles):
    elems = []
    elems.append(Spacer(1, 10))
    elems.append(HRFlowable(width="100%", thickness=0.8, color=COR_CINZA_CLARO))
    elems.append(Spacer(1, 4))
    disc = (
        "<b>DISCLAIMER:</b> Este relatório é gerado automaticamente com fins educacionais e de "
        "suporte à tomada de decisão em EA FC 26 Ultimate Team. Os preços indicados são "
        "estimativas baseadas em dados de mercado coletados via FUTBIN, FUT.GG, RealSport101 "
        "e OperationSports em 25/05/2026 e podem variar significativamente por fatores como "
        "novos pacotes, SBCs surpresa, eventos especiais ou mudanças de meta. "
        "Trading em FUT envolve risco de perda de coins. Nunca invista coins que não possa "
        "perder. Este documento não constitui aconselhamento financeiro. "
        "EA Sports, EA FC 26 e Ultimate Team são marcas registradas da Electronic Arts Inc."
    )
    elems.append(Paragraph(disc, styles["Aviso"]))
    return elems


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=14*mm,
        rightMargin=14*mm,
        topMargin=14*mm,
        bottomMargin=14*mm,
        title="Relatório Trading EA FC 26 - 25/05/2026",
        author="EA FC 26 Trading Bot",
    )

    styles = build_styles()
    story = []

    # ── Cabeçalho ──────────────────────────────────────────────────────────
    story.append(header_table(styles))
    story.append(Spacer(1, 8))

    # ── Contexto do mercado ────────────────────────────────────────────────
    story.extend(secao_contexto(styles))

    # ── Tabela de cartas ──────────────────────────────────────────────────
    story.extend(tabela_cartas(styles))

    # ── Timing ───────────────────────────────────────────────────────────
    story.extend(secao_timing(styles))

    # ── Retorno estimado ─────────────────────────────────────────────────
    story.extend(secao_retorno(styles))

    # ── Regras de ouro ───────────────────────────────────────────────────
    story.extend(secao_regras(styles))

    # ── Disclaimer ───────────────────────────────────────────────────────
    story.extend(secao_disclaimer(styles))

    doc.build(story)
    print(f"✅  PDF gerado: {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    build_pdf()
