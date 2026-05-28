#!/usr/bin/env python3
"""Gerador de relatório de trading EA FC 26 Ultimate Team."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.frames import Frame
import datetime

# ── Constantes ──────────────────────────────────────────────────────────────
REPORT_DATE = datetime.datetime(2026, 5, 28, 8, 7)
FILENAME = f"relatorio-trading-{REPORT_DATE.strftime('%Y-%m-%d')}-%02dh.pdf" % REPORT_DATE.hour
FILEPATH = f"/home/user/fifa-trading/{FILENAME}"

VERDE_ESCURO  = colors.HexColor("#1a6b2e")
VERDE_MEDIO   = colors.HexColor("#27ae60")
VERDE_CLARO   = colors.HexColor("#d5f5e3")
AMARELO       = colors.HexColor("#f39c12")
AMARELO_CLARO = colors.HexColor("#fef9e7")
VERMELHO      = colors.HexColor("#c0392b")
CINZA_ESCURO  = colors.HexColor("#2c3e50")
CINZA_MEDIO   = colors.HexColor("#7f8c8d")
CINZA_CLARO   = colors.HexColor("#ecf0f1")
BRANCO        = colors.white
PRETO         = colors.black

PAGE_W, PAGE_H = A4
MARGIN = 1.8 * cm


# ── Numeração de páginas ─────────────────────────────────────────────────────
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_page_number(total)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def _draw_page_number(self, total):
        self.setFont("Helvetica", 8)
        self.setFillColor(CINZA_MEDIO)
        text = f"Página {self._pageNumber} de {total}"
        self.drawRightString(PAGE_W - MARGIN, 0.7 * cm, text)
        self.drawString(MARGIN, 0.7 * cm, "EA FC 26 Ultimate Team — Relatório de Trading Diário")
        self.setStrokeColor(CINZA_CLARO)
        self.line(MARGIN, 1.0 * cm, PAGE_W - MARGIN, 1.0 * cm)


# ── Estilos ──────────────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    titulo = ParagraphStyle(
        "Titulo",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=BRANCO,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    subtitulo = ParagraphStyle(
        "Subtitulo",
        fontName="Helvetica",
        fontSize=11,
        textColor=BRANCO,
        alignment=TA_CENTER,
        spaceAfter=2,
    )
    secao = ParagraphStyle(
        "Secao",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=VERDE_ESCURO,
        spaceBefore=14,
        spaceAfter=6,
        borderPad=4,
    )
    corpo = ParagraphStyle(
        "Corpo",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=CINZA_ESCURO,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
    )
    bullet = ParagraphStyle(
        "Bullet",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=CINZA_ESCURO,
        leading=14,
        leftIndent=14,
        spaceAfter=3,
    )
    negrito = ParagraphStyle(
        "Negrito",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=CINZA_ESCURO,
        leading=14,
        spaceAfter=4,
    )
    aviso = ParagraphStyle(
        "Aviso",
        fontName="Helvetica-Oblique",
        fontSize=8,
        textColor=CINZA_MEDIO,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    regra_titulo = ParagraphStyle(
        "RegraTitulo",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=VERDE_ESCURO,
        leading=14,
        spaceAfter=2,
    )
    return {
        "titulo": titulo, "subtitulo": subtitulo, "secao": secao,
        "corpo": corpo, "bullet": bullet, "negrito": negrito,
        "aviso": aviso, "regra_titulo": regra_titulo,
    }


# ── Cabeçalho com faixa verde ─────────────────────────────────────────────────
def header_block(styles):
    dt_str = REPORT_DATE.strftime("%d/%m/%Y %H:%M")
    elements = []

    # Faixa de cabeçalho via Table com fundo verde
    header_data = [
        [Paragraph("⚽ EA FC 26 Ultimate Team", styles["titulo"])],
        [Paragraph("Relatório Diário de Trading", styles["titulo"])],
        [Paragraph(f"Gerado em: {dt_str} UTC", styles["subtitulo"])],
        [Paragraph("Budget: 40.000 coins  |  Estratégia: SBC Fodder + Evolution + Flipping", styles["subtitulo"])],
    ]
    t = Table(header_data, colWidths=[PAGE_W - 2 * MARGIN])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), VERDE_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, 0), 14),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 14),
        ("LEFTPADDING",  (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [VERDE_ESCURO]),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.4 * cm))
    return elements


# ── Seção: Contexto de Mercado ────────────────────────────────────────────────
def market_context(styles):
    elems = []
    elems.append(Paragraph("1. Contexto de Mercado — 28/05/2026", styles["secao"]))
    elems.append(HRFlowable(width="100%", thickness=1, color=VERDE_MEDIO, spaceAfter=6))

    ctx_data = [
        ["Evento Ativo", "Ultimate Team of the Season (Ultimate TOTS)"],
        ["Período do Evento", "22/05/2026 → 29/05/2026 (amanhã termina!)"],
        ["Tendência Geral", "MERCADO EM QUEDA — Massa de packs abertos flooda oferta"],
        ["TOTW", "Sem TOTW regular em Maio — encerrado em Abril/2026"],
        ["Preço Fodder 85-rated", "900 – 1.500 coins (mínimo histórico / near discard)"],
        ["Preço Fodder 86-rated", "1.300 – 1.700 coins (oportunidade rara)"],
        ["Preço Fodder 87-rated", "2.200 – 2.500 coins (levemente abaixo da média)"],
        ["Oportunidade-Chave", "Comprar fodder AGORA antes do fim do TOTS (29/05)"],
    ]
    t = Table(ctx_data, colWidths=[5.5 * cm, PAGE_W - 2 * MARGIN - 5.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, -1), VERDE_CLARO),
        ("BACKGROUND",    (1, 0), (1, -1), BRANCO),
        ("ROWBACKGROUNDS",(0, 2), (-1, 2), [colors.HexColor("#fef9e7")]),
        ("ROWBACKGROUNDS",(0, 7), (-1, 7), [colors.HexColor("#d5f5e3")]),
        ("FONTNAME",      (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME",      (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("TEXTCOLOR",     (0, 0), (0, -1), VERDE_ESCURO),
        ("TEXTCOLOR",     (1, 2), (1, 2), VERMELHO),
        ("TEXTCOLOR",     (1, 7), (1, 7), VERDE_ESCURO),
        ("FONTNAME",      (1, 2), (1, 2), "Helvetica-Bold"),
        ("FONTNAME",      (1, 7), (1, 7), "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.5, CINZA_CLARO),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
    ]))
    elems.append(t)

    elems.append(Spacer(1, 0.3 * cm))
    elems.append(Paragraph(
        "<b>Análise:</b> O Ultimate TOTS trouxe 38 jogadores de alto nível ao mercado (preços entre 14.250 e "
        "4.910.000 coins), causando um flood de supply que derrubou preços de fodder a mínimos históricos. "
        "Com o evento encerrando em <b>29/05 (amanhã)</b>, a janela ideal de compra de fodder barato é "
        "<b>agora</b> — as próximas SBCs pós-TOTS vão sugar essa oferta e puxar preços para cima.",
        styles["corpo"]
    ))
    return elems


# ── Seção: Tabela de Cartas Recomendadas ─────────────────────────────────────
def cards_table(styles):
    elems = []
    elems.append(Paragraph("2. Cartas Recomendadas — Oportunidades de Compra", styles["secao"]))
    elems.append(HRFlowable(width="100%", thickness=1, color=VERDE_MEDIO, spaceAfter=6))

    elems.append(Paragraph(
        "Margem líquida calculada após dedução da taxa EA de 5% sobre o preço de venda. "
        "Preços em coins (PS5/Xbox). Data de referência: 28/05/2026 08:07 UTC.",
        styles["aviso"]
    ))
    elems.append(Spacer(1, 0.2 * cm))

    headers = [
        "Jogador", "Rat.", "Clube / Liga", "Compra\n(coins)",
        "Venda\n(coins)", "Venda c/\n-5% EA", "Margem\nLíquida", "Horizonte"
    ]

    # (nome, rating, clube/liga, compra, venda, horizonte, categoria)
    players = [
        # SBC FODDER 85-rated
        ("Little (CDM)", "85", "Man City / Premier League",   1100, 2200, "24-48h",  "fodder"),
        ("Keira Walsh (CDM)", "85", "Barcelona / La Liga",     1200, 2300, "24-48h",  "fodder"),
        ("Thuram (ST)", "85", "Inter Milan / Serie A",         1300, 2400, "24-48h",  "fodder"),
        ("Mbeumo (RW)", "85", "Brentford / Premier League",   1200, 2200, "24-48h",  "fodder"),
        ("Schlotterbeck (CB)", "85", "Dortmund / Bundesliga", 1300, 2300, "24-48h",  "fodder"),
        # SBC FODDER 86-rated
        ("Dybala (CAM)", "86", "Roma / Serie A",               1300, 2800, "24-48h",  "fodder"),
        ("Bruno Guimarães (CM)", "86", "Newcastle / Premier",  1300, 2700, "24-48h",  "fodder"),
        ("Rúben Dias (CB)", "86", "Man City / Premier League", 1400, 2800, "24-48h",  "fodder"),
        ("Çalhanoğlu (CDM)", "86", "Inter Milan / Serie A",   1500, 2900, "24-48h",  "fodder"),
        # SBC FODDER 87-rated
        ("Tah (CB)", "87", "Bayern München / Bundesliga",      2200, 4000, "48h",     "fodder"),
        ("Guirassy (ST)", "87", "Dortmund / Bundesliga",       2300, 4100, "48h",     "fodder"),
        ("Swanson (LM)", "87", "Man City / Premier League",   2200, 3900, "48h",     "fodder"),
        # EVOLUTION TARGETS 84-rated
        ("Emily Fox (RB)", "84", "Arsenal / Premier League",  1500, 3500, "3-5 dias", "evo"),
        ("Milinkovic-Savic (CM)", "84", "Al-Hilal / Saudi",   1800, 4000, "3-5 dias", "evo"),
        ("Alex Greenwood (CB)", "84", "Man City / Premier",   1500, 3200, "3-5 dias", "evo"),
    ]

    col_w = [3.8*cm, 0.9*cm, 4.0*cm, 1.4*cm, 1.4*cm, 1.6*cm, 1.6*cm, 1.7*cm]

    table_data = [headers]
    for (nome, rat, clube, compra, venda, horizonte, cat) in players:
        venda_taxa = int(venda * 0.95)
        margem = venda_taxa - compra
        table_data.append([
            nome, rat, clube,
            f"{compra:,}".replace(",", "."),
            f"{venda:,}".replace(",", "."),
            f"{venda_taxa:,}".replace(",", "."),
            f"+{margem:,}".replace(",", "."),
            horizonte
        ])

    t = Table(table_data, colWidths=col_w, repeatRows=1)

    style_cmds = [
        # Cabeçalho
        ("BACKGROUND",   (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",    (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0), 8),
        ("ALIGN",        (0, 0), (-1, 0), "CENTER"),
        ("VALIGN",       (0, 0), (-1, 0), "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, 0), 6),
        ("BOTTOMPADDING",(0, 0), (-1, 0), 6),
        # Corpo
        ("FONTSIZE",     (0, 1), (-1, -1), 8),
        ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
        ("ALIGN",        (1, 1), (-1, -1), "CENTER"),
        ("ALIGN",        (0, 1), (0, -1),  "LEFT"),
        ("ALIGN",        (2, 1), (2, -1),  "LEFT"),
        ("VALIGN",       (0, 1), (-1, -1), "MIDDLE"),
        ("TOPPADDING",   (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 1), (-1, -1), 4),
        ("LEFTPADDING",  (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("GRID",         (0, 0), (-1, -1), 0.3, CINZA_CLARO),
        # Margem em verde
        ("TEXTCOLOR",    (6, 1), (6, -1), VERDE_ESCURO),
        ("FONTNAME",     (6, 1), (6, -1), "Helvetica-Bold"),
        # Separador entre grupos de rating
        ("LINEBELOW",    (0, 5),  (-1, 5),  1.0, VERDE_MEDIO),
        ("LINEBELOW",    (0, 9),  (-1, 9),  1.0, AMARELO),
        ("LINEBELOW",    (0, 12), (-1, 12), 1.0, AMARELO),
    ]
    # Zebra rows
    for i in range(1, len(table_data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), CINZA_CLARO))
        else:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), BRANCO))

    # Highlight linhas de Evolution
    for i in range(13, 16):
        style_cmds.append(("BACKGROUND", (0, i), (-1, i), AMARELO_CLARO))

    t.setStyle(TableStyle(style_cmds))
    elems.append(t)

    # Legenda
    elems.append(Spacer(1, 0.2 * cm))
    legenda_data = [
        [Paragraph("■ Fundo branco/cinza: SBC Fodder Flipping (83-87 rated)", styles["aviso"]),
         Paragraph("■ Fundo amarelo: Evolution Investing (84 rated)", styles["aviso"])]
    ]
    lt = Table(legenda_data, colWidths=[(PAGE_W - 2 * MARGIN) / 2] * 2)
    lt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), CINZA_CLARO),
        ("BACKGROUND", (1, 0), (1, 0), AMARELO_CLARO),
        ("GRID", (0, 0), (-1, -1), 0.3, CINZA_CLARO),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    elems.append(lt)
    return elems


# ── Seção: Alocação de Budget ─────────────────────────────────────────────────
def budget_allocation(styles):
    elems = []
    elems.append(Paragraph("3. Alocação de Budget — 40.000 Coins", styles["secao"]))
    elems.append(HRFlowable(width="100%", thickness=1, color=VERDE_MEDIO, spaceAfter=6))

    alloc_data = [
        ["Estratégia", "Budget", "Qtd. Cartas", "Custo Médio", "Retorno Esperado"],
        ["Fodder 85-rated (bulk)", "15.000 coins", "12 cartas", "~1.250 coins", "22.800 (líq.)"],
        ["Fodder 86-rated (bulk)", "14.000 coins", "9 cartas",  "~1.550 coins", "23.940 (líq.)"],
        ["Fodder 87-rated (bulk)", "7.000 coins",  "3 cartas",  "~2.333 coins", "11.400 (líq.)"],
        ["Evolution 84-rated",     "4.000 coins",  "2 cartas",  "~2.000 coins", "6.650 (líq.)"],
        ["TOTAL",                  "40.000 coins", "26 cartas", "—",            "64.790 (líq.)"],
    ]

    col_w2 = [5.0*cm, 3.2*cm, 2.5*cm, 2.8*cm, 3.5*cm]
    t = Table(alloc_data, colWidths=col_w2)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("ALIGN",         (1, 0), (-1, -1), "CENTER"),
        ("ALIGN",         (0, 0), (0, -1), "LEFT"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("GRID",          (0, 0), (-1, -1), 0.3, CINZA_CLARO),
        ("ROWBACKGROUNDS",(0, 1), (-1, -2), [BRANCO, CINZA_CLARO]),
        ("BACKGROUND",    (0, -1), (-1, -1), VERDE_CLARO),
        ("FONTNAME",      (0, -1), (-1, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0, -1), (-1, -1), VERDE_ESCURO),
    ]))
    elems.append(t)
    return elems


# ── Seção: Timing ─────────────────────────────────────────────────────────────
def timing_section(styles):
    elems = []
    elems.append(Paragraph("4. Estratégia de Timing", styles["secao"]))
    elems.append(HRFlowable(width="100%", thickness=1, color=VERDE_MEDIO, spaceAfter=6))

    timing_data = [
        ["Momento", "Ação", "Razão"],
        ["28/05 — AGORA\n08h–14h UTC", "COMPRAR fodder 85/86/87 rated\ne Evolution 84-rated",
         "Preços no fundo: packs do TOTS flooded\no mercado, oferta > demanda"],
        ["28/05 — Tarde\n16h–22h UTC", "Monitorar: recompor posições\nse preços caírem mais",
         "Horário pico PS/Xbox (Europa+BR) pode\naumentar venda e baixar preços"],
        ["29/05 — Manhã\n10h UTC", "TOTS encerra — SEGURAR posições",
         "Fim do evento = queda do supply de\nnovas cartas no mercado"],
        ["29/05 – 30/05\nTarde/Noite", "VENDER fodder 85/86 rated",
         "Novas SBCs pós-TOTS chegam e\npuxam demanda de fodder para cima"],
        ["30/05 – 31/05", "VENDER fodder 87-rated +\nEvolution 84-rated",
         "Pico de demanda para SBCs premium\ne novos eventos do Outono"],
    ]

    col_w3 = [3.5*cm, 5.5*cm, PAGE_W - 2*MARGIN - 9.0*cm]
    t = Table(timing_data, colWidths=col_w3)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8.5),
        ("ALIGN",         (0, 0), (-1, -1), "LEFT"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("GRID",          (0, 0), (-1, -1), 0.3, CINZA_CLARO),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("FONTNAME",      (0, 1), (0, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0, 1), (0, -1), VERDE_ESCURO),
        ("BACKGROUND",    (0, 3), (-1, 3), colors.HexColor("#fff3cd")),
    ]))
    elems.append(t)
    return elems


# ── Seção: Estimativa de Retorno ──────────────────────────────────────────────
def return_estimate(styles):
    elems = []
    elems.append(Paragraph("5. Estimativa de Retorno em 48h", styles["secao"]))
    elems.append(HRFlowable(width="100%", thickness=1, color=VERDE_MEDIO, spaceAfter=6))

    ret_data = [
        ["Cenário", "Capital Inicial", "Capital Final", "Lucro Líquido", "ROI"],
        ["Conservador\n(venda parcial, preços baixos)",
         "40.000 coins", "53.000 coins", "+13.000 coins", "+32,5%"],
        ["Base\n(venda total, preços médios)",
         "40.000 coins", "64.790 coins", "+24.790 coins", "+62,0%"],
        ["Otimista\n(nova SBC grande + demanda alta)",
         "40.000 coins", "78.000 coins", "+38.000 coins", "+95,0%"],
    ]

    col_w4 = [4.5*cm, 3.0*cm, 3.0*cm, 3.0*cm, 2.5*cm]
    t = Table(ret_data, colWidths=col_w4)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("ALIGN",         (1, 0), (-1, -1), "CENTER"),
        ("ALIGN",         (0, 0), (0, -1), "LEFT"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("GRID",          (0, 0), (-1, -1), 0.3, CINZA_CLARO),
        ("BACKGROUND",    (0, 1), (-1, 1), CINZA_CLARO),
        ("BACKGROUND",    (0, 2), (-1, 2), BRANCO),
        ("BACKGROUND",    (0, 3), (-1, 3), VERDE_CLARO),
        ("FONTNAME",      (4, 1), (4, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (4, 1), (4, -1), VERDE_ESCURO),
        ("TEXTCOLOR",     (3, 1), (3, -1), VERDE_ESCURO),
        ("FONTNAME",      (3, 1), (3, -1), "Helvetica-Bold"),
    ]))
    elems.append(t)

    elems.append(Spacer(1, 0.3 * cm))
    elems.append(Paragraph(
        "<b>Nota:</b> O cenário conservador assume que apenas 60% das cartas são vendidas dentro de 48h "
        "e a 80% do preço-alvo. O cenário otimista considera uma nova SBC grande anunciada no fim do "
        "evento TOTS, gerando pico de demanda de fodder 86-87. O ROI é calculado sobre o investimento "
        "total de 40.000 coins antes da taxa EA.",
        styles["corpo"]
    ))
    return elems


# ── Seção: 8 Regras de Ouro ───────────────────────────────────────────────────
def golden_rules(styles):
    elems = []
    elems.append(Paragraph("6. As 8 Regras de Ouro do Trade", styles["secao"]))
    elems.append(HRFlowable(width="100%", thickness=1, color=VERDE_MEDIO, spaceAfter=6))

    rules = [
        ("Regra 01 — Nunca invista 100% do budget de uma vez",
         "Reserve ao menos 20% do capital como reserva líquida para oportunidades "
         "inesperadas. Flexibilidade é um ativo."),
        ("Regra 02 — Compre no pânico, venda no hype",
         "Os melhores preços aparecem quando todos estão vendendo (packs abertos, "
         "eventos novos). Aja contra o movimento da massa."),
        ("Regra 03 — Sempre calcule a taxa EA de 5%",
         "Todo preço de venda deve ser multiplicado por 0,95 para obter o valor real "
         "recebido. Nunca esqueça essa dedução nos seus cálculos de margem."),
        ("Regra 04 — Distribua entre múltiplos jogadores",
         "Nunca coloque todo o capital em uma única carta. Diversifique entre diferentes "
         "ratings e ligas para reduzir risco de travamento de preço."),
        ("Regra 05 — Conheça o preço mínimo (discard) de cada rating",
         "85-rated: ~750 coins | 86-rated: ~900 coins | 87-rated: ~1.500 coins. "
         "Se o preço de venda está próximo do discard, não há margem viável."),
        ("Regra 06 — Monitore os horários de pico",
         "Os preços costumam subir entre 18h–23h UTC (horário pico europeu e "
         "brasileiro). Venda nesse janela para maximizar o retorno."),
        ("Regra 07 — Acompanhe os anúncios de SBC",
         "Uma nova SBC exigindo 87-rated pode triplicar a demanda em minutos. "
         "Tenha posição antes do anúncio, não depois."),
        ("Regra 08 — Defina stop-loss antes de comprar",
         "Se o preço cair 30% abaixo do seu custo e não houver catalisador visível "
         "nas próximas 24h, venda e preserve capital para a próxima oportunidade."),
    ]

    for i, (titulo, descricao) in enumerate(rules):
        cor_fundo = VERDE_CLARO if i % 2 == 0 else AMARELO_CLARO
        rule_data = [[
            Paragraph(f"<b>{titulo}</b><br/>{descricao}", ParagraphStyle(
                f"rule{i}", fontName="Helvetica", fontSize=9,
                textColor=CINZA_ESCURO, leading=13,
                leftIndent=0, spaceAfter=0,
            ))
        ]]
        rt = Table(rule_data, colWidths=[PAGE_W - 2 * MARGIN])
        rt.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), cor_fundo),
            ("LEFTPADDING",   (0, 0), (-1, -1), 10),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
            ("TOPPADDING",    (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("BOX",           (0, 0), (-1, -1), 0.5, VERDE_MEDIO),
        ]))
        elems.append(rt)
        elems.append(Spacer(1, 0.15 * cm))
    return elems


# ── Seção: Disclaimer ─────────────────────────────────────────────────────────
def disclaimer(styles):
    elems = []
    elems.append(Spacer(1, 0.5 * cm))
    elems.append(HRFlowable(width="100%", thickness=1, color=CINZA_MEDIO, spaceAfter=6))

    disc_data = [[Paragraph(
        "<b>⚠ DISCLAIMER</b><br/>"
        "Este relatório foi gerado automaticamente com base em dados públicos de mercado disponíveis em "
        "28/05/2026. Os preços de cartas no EA FC 26 Ultimate Team são altamente voláteis e podem mudar "
        "significativamente em minutos após eventos, anúncios ou atualizações do jogo. As estimativas de "
        "retorno são projeções baseadas em padrões históricos de mercado e NÃO garantem lucro. "
        "Sempre verifique os preços em tempo real no FUTBIN (futbin.com) ou FUT.GG (fut.gg) antes de "
        "executar qualquer trade. O autor não se responsabiliza por perdas decorrentes do uso deste "
        "relatório. Trade responsável: nunca invista coins que não possa perder.",
        ParagraphStyle("disc", fontName="Helvetica", fontSize=7.5, textColor=CINZA_MEDIO,
                      leading=11, alignment=TA_JUSTIFY)
    )]]
    dt = Table(disc_data, colWidths=[PAGE_W - 2 * MARGIN])
    dt.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), CINZA_CLARO),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("BOX",           (0, 0), (-1, -1), 0.5, CINZA_MEDIO),
    ]))
    elems.append(dt)
    return elems


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    doc = SimpleDocTemplate(
        FILEPATH,
        pagesize=A4,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=1.5 * cm,
        title="Relatório de Trading EA FC 26",
        author="EA FC 26 Trading Agent",
        subject=f"Trading Report {REPORT_DATE.strftime('%d/%m/%Y')}",
    )

    styles = build_styles()
    story = []

    story += header_block(styles)
    story += market_context(styles)
    story.append(Spacer(1, 0.3 * cm))
    story += cards_table(styles)
    story.append(Spacer(1, 0.3 * cm))
    story += budget_allocation(styles)
    story.append(Spacer(1, 0.3 * cm))
    story += timing_section(styles)
    story.append(Spacer(1, 0.3 * cm))
    story += return_estimate(styles)
    story.append(Spacer(1, 0.3 * cm))
    story += golden_rules(styles)
    story += disclaimer(styles)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF gerado: {FILEPATH}")
    return FILEPATH


if __name__ == "__main__":
    main()
