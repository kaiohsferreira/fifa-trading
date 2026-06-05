#!/usr/bin/env python3
"""Gerador de relatório diário de trading EA FC 26 Ultimate Team."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak
import os

# ─── Configuração ──────────────────────────────────────────────────────────────
DATA_HORA = "05/06/2026 14:04"
NOME_ARQUIVO = "relatorio-trading-2026-06-05-14h.pdf"
CAMINHO = os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)

W, H = A4

# ─── Paleta de cores ───────────────────────────────────────────────────────────
VERDE_ESCURO   = colors.HexColor("#0d4a2e")
VERDE_MEDIO    = colors.HexColor("#1a7a4e")
VERDE_CLARO    = colors.HexColor("#27ae60")
VERDE_FUNDO    = colors.HexColor("#eafaf1")
AMARELO_OURO   = colors.HexColor("#f1c40f")
AMARELO_CLARO  = colors.HexColor("#fef9e7")
CINZA_ESCURO   = colors.HexColor("#2c3e50")
CINZA_MEDIO    = colors.HexColor("#7f8c8d")
CINZA_CLARO    = colors.HexColor("#ecf0f1")
VERMELHO       = colors.HexColor("#c0392b")
BRANCO         = colors.white
PRETO          = colors.black

# ─── Estilos ───────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def estilo(nome, parent="Normal", **kwargs):
    return ParagraphStyle(nome, parent=styles[parent], **kwargs)

s_titulo = estilo(
    "sTitulo",
    fontSize=22, textColor=BRANCO, alignment=TA_CENTER,
    fontName="Helvetica-Bold", spaceAfter=4,
)
s_subtitulo = estilo(
    "sSubtitulo",
    fontSize=11, textColor=AMARELO_OURO, alignment=TA_CENTER,
    fontName="Helvetica-Bold", spaceAfter=2,
)
s_datahora = estilo(
    "sDatahora",
    fontSize=9, textColor=VERDE_CLARO, alignment=TA_CENTER,
    fontName="Helvetica",
)
s_section = estilo(
    "sSection",
    fontSize=12, textColor=BRANCO, fontName="Helvetica-Bold",
    spaceAfter=6, spaceBefore=10,
    backColor=VERDE_MEDIO, borderPadding=(4, 8, 4, 8),
    leftIndent=-10,
)
s_body = estilo(
    "sBody",
    fontSize=9, textColor=CINZA_ESCURO, fontName="Helvetica",
    spaceAfter=4, leading=13, alignment=TA_JUSTIFY,
)
s_bullet = estilo(
    "sBullet",
    fontSize=9, textColor=CINZA_ESCURO, fontName="Helvetica",
    spaceAfter=3, leading=13, leftIndent=12,
    bulletIndent=0,
)
s_aviso = estilo(
    "sAviso",
    fontSize=8, textColor=CINZA_MEDIO, fontName="Helvetica-Oblique",
    alignment=TA_JUSTIFY, spaceAfter=4, leading=12,
)
s_th = estilo(
    "sTH",
    fontSize=8, textColor=BRANCO, fontName="Helvetica-Bold",
    alignment=TA_CENTER,
)
s_td = estilo(
    "sTD",
    fontSize=8, textColor=CINZA_ESCURO, fontName="Helvetica",
    alignment=TA_CENTER,
)
s_td_left = estilo(
    "sTDLeft",
    fontSize=8, textColor=CINZA_ESCURO, fontName="Helvetica",
    alignment=TA_LEFT,
)
s_regra_num = estilo(
    "sRegraNum",
    fontSize=11, textColor=VERDE_CLARO, fontName="Helvetica-Bold",
    alignment=TA_CENTER,
)
s_regra_titulo = estilo(
    "sRegraTitulo",
    fontSize=10, textColor=CINZA_ESCURO, fontName="Helvetica-Bold",
    spaceAfter=1,
)
s_regra_desc = estilo(
    "sRegraDesc",
    fontSize=8.5, textColor=CINZA_ESCURO, fontName="Helvetica",
    leading=12,
)


def cabecalho():
    """Bloco de cabeçalho com fundo verde escuro."""
    dados = [
        [Paragraph("EA FC 26 ULTIMATE TEAM", s_titulo)],
        [Paragraph("RELATÓRIO DIÁRIO DE TRADING", s_subtitulo)],
        [Paragraph(f"Gerado em: {DATA_HORA} UTC", s_datahora)],
    ]
    t = Table(dados, colWidths=[W - 4 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), VERDE_ESCURO),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return t


def secao(texto):
    dados = [[Paragraph(f"▌  {texto}", s_section)]]
    t = Table(dados, colWidths=[W - 4 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), VERDE_MEDIO),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return t


def p(texto, estilo_=None):
    return Paragraph(texto, estilo_ or s_body)


def bullet(texto):
    return Paragraph(f"• {texto}", s_bullet)


def sp(altura=0.3):
    return Spacer(1, altura * cm)


def hr():
    return HRFlowable(width="100%", thickness=0.5,
                      color=VERDE_CLARO, spaceAfter=6, spaceBefore=2)


# ─── Tabela de Oportunidades ───────────────────────────────────────────────────
def tabela_oportunidades():
    """Retorna a tabela principal de cartas recomendadas."""
    cabecalhos = [
        Paragraph("Jogador", s_th),
        Paragraph("Rat.", s_th),
        Paragraph("Clube", s_th),
        Paragraph("Compra\n(coins)", s_th),
        Paragraph("Venda\n(coins)", s_th),
        Paragraph("Margem\nLíquida", s_th),
        Paragraph("ROI%", s_th),
        Paragraph("Estratégia", s_th),
    ]

    # (jogador, rating, clube, compra, venda, estrategia)
    jogadores = [
        ("Çalhanoğlu",    86, "Inter Milan",      950,  1_350, "SBC Fodder / Festival of Football"),
        ("Konaté",        86, "Liverpool",         950,  1_320, "SBC Fodder – alta demanda CB"),
        ("Olise",         86, "Bayern München",    950,  1_350, "SBC Fodder – liga top"),
        ("Reijnders",     86, "AC Milan",          950,  1_300, "SBC Fodder – MF Serie A"),
        ("Weir",          85, "Chelsea FC W",      750,  1_050, "SBC Fodder – mais barato 85"),
        ("Stanway",       85, "Bayern München W",  750,  1_050, "SBC Fodder – CDM demandado"),
        ("Bruno Fernandes",87,"Manchester United",1_400, 2_000, "SBC Premium / TOTW spike"),
        ("Rice",          87, "Arsenal",          1_400, 1_950, "SBC Premium – CDM chave"),
        ("Lavelle",       87, "NJ/NY Gotham",     1_400, 1_900, "SBC Premium – fora de packs"),
        ("Osimhen",       87, "Galatasaray",      1_450, 2_100, "SBC + Evolução alt-nac"),
        ("Amad Diallo",   84, "Manchester United",  800,  1_050, "Fodder – PTG hype Man Utd"),
        ("Schick",        83, "Bayer Leverkusen",   750,  1_000, "Fodder – PTG Bundesliga"),
    ]

    def margem(compra, venda):
        liquido = int(venda * 0.95)
        return liquido - compra

    def roi(compra, venda):
        m = margem(compra, venda)
        return round(m / compra * 100, 1)

    linhas = [cabecalhos]
    for i, (nome, rat, clube, compra, venda, strat) in enumerate(jogadores):
        m = margem(compra, venda)
        r = roi(compra, venda)
        cor_roi = VERDE_CLARO if r >= 20 else (AMARELO_OURO if r >= 10 else VERMELHO)
        linha = [
            Paragraph(nome, s_td_left),
            Paragraph(str(rat), s_td),
            Paragraph(clube, s_td_left),
            Paragraph(f"{compra:,}".replace(",", "."), s_td),
            Paragraph(f"{venda:,}".replace(",", "."), s_td),
            Paragraph(f"{m:,}".replace(",", "."), s_td),
            Paragraph(f"{r}%", s_td),
            Paragraph(strat, s_td_left),
        ]
        linhas.append(linha)

    col_w = [2.5*cm, 0.8*cm, 2.8*cm, 1.5*cm, 1.5*cm, 1.5*cm, 0.9*cm, 4.5*cm]
    t = Table(linhas, colWidths=col_w, repeatRows=1)

    ts = TableStyle([
        # Cabeçalho
        ("BACKGROUND",    (0, 0), (-1, 0),  VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0),  8),
        ("ALIGN",         (0, 0), (-1, 0),  "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, 0),  5),
        ("BOTTOMPADDING", (0, 0), (-1, 0),  5),
        # Linhas
        ("FONTSIZE",      (0, 1), (-1, -1), 7.5),
        ("TOPPADDING",    (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#bdc3c7")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, VERDE_FUNDO]),
        # Colunas numéricas centralizadas
        ("ALIGN", (1, 1), (6, -1), "CENTER"),
    ])

    # Colorir margem negativa em vermelho
    for i, (_, _, _, compra, venda, _strat) in enumerate(jogadores, start=1):
        m = margem(compra, venda)
        if m < 0:
            ts.add("TEXTCOLOR", (5, i), (5, i), VERMELHO)

    t.setStyle(ts)
    return t


# ─── Tabela de Timing ──────────────────────────────────────────────────────────
def tabela_timing():
    dados = [
        [Paragraph("Janela", s_th),
         Paragraph("Ação", s_th),
         Paragraph("Motivo", s_th)],
        [Paragraph("Sex 14h–18h UTC\n(AGORA)", s_td),
         Paragraph("COMPRAR SBC Fodder 85–87", s_td_left),
         Paragraph("Início do Festival of Football → demanda por fodder explode", s_td_left)],
        [Paragraph("Sex 19h–23h UTC", s_td),
         Paragraph("MANTER / observar mercado", s_td_left),
         Paragraph("Players completando novos SBCs → preços sobem organicamente", s_td_left)],
        [Paragraph("Sáb 10h–20h UTC", s_td),
         Paragraph("VENDER Fodder 85–87", s_td_left),
         Paragraph("Pico de jogadores online no fim de semana = maior liquidez", s_td_left)],
        [Paragraph("Dom 12h–16h UTC", s_td),
         Paragraph("COMPRAR PTG (Path to Glory)", s_td_left),
         Paragraph("Após 48h do lançamento, preços baixam; escolher nações favoritas", s_td_left)],
        [Paragraph("Qua 17h–20h UTC\n(TOTW drop)", s_td),
         Paragraph("COMPRAR TOTW a partir 10k", s_td_left),
         Paragraph("TOTW novo → antigos caem; comprar para SBC que requer TOTW", s_td_left)],
        [Paragraph("Qui 18h–22h UTC\n(Rivals rewards)", s_td),
         Paragraph("VENDER TOTW / COMPRAR dips", s_td_left),
         Paragraph("Jogadores recebem coins de rivals e compram → alta de preços", s_td_left)],
    ]
    col_w = [2.8*cm, 4.2*cm, 9.0*cm]
    t = Table(dados, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#bdc3c7")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, VERDE_FUNDO]),
        ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#d5f5e3")),  # destaque agora
    ]))
    return t


# ─── Tabela de Retorno ─────────────────────────────────────────────────────────
def tabela_retorno():
    dados = [
        [Paragraph("Cenário", s_th),
         Paragraph("Estratégia Principal", s_th),
         Paragraph("Capital Inicial", s_th),
         Paragraph("Retorno Esperado 48h", s_th),
         Paragraph("Capital Final", s_th),
         Paragraph("Lucro Líquido", s_th)],
        [Paragraph("🟡 Conservador", s_td),
         Paragraph("SBC Fodder 85–86 ×25 cartas", s_td_left),
         Paragraph("25.000", s_td),
         Paragraph("+12–15%", s_td),
         Paragraph("28.000–28.750", s_td),
         Paragraph("3.000–3.750", s_td)],
        [Paragraph("🟢 Otimista", s_td),
         Paragraph("Fodder 85–87 + TOTW flip + PTG", s_td_left),
         Paragraph("38.000", s_td),
         Paragraph("+20–28%", s_td),
         Paragraph("45.600–48.640", s_td),
         Paragraph("7.600–10.640", s_td)],
    ]
    col_w = [2.2*cm, 4.2*cm, 2.5*cm, 2.8*cm, 3.3*cm, 2.5*cm]
    t = Table(dados, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",         (0, 0), (-1, 0), "CENTER"),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#bdc3c7")),
        ("BACKGROUND",    (0, 1), (-1, 1), AMARELO_CLARO),
        ("BACKGROUND",    (0, 2), (-1, 2), VERDE_FUNDO),
        ("FONTNAME",      (3, 1), (5, 2),  "Helvetica-Bold"),
    ]))
    return t


# ─── 8 Regras de Ouro ─────────────────────────────────────────────────────────
REGRAS = [
    ("1", "Nunca Compre no Pico",
     "Cards recém-lançados de promos têm preço inflado. Aguarde 48–72h para o mercado se estabilizar antes de comprar para especulação."),
    ("2", "Taxa EA de 5% é Real",
     "Calcule SEMPRE o preço de venda × 0,95 para saber seu lucro real. Uma carta vendida a 2.000 rende apenas 1.900 coins."),
    ("3", "Venda no Pico de Demanda",
     "Sábado/domingo entre 12h–20h UTC é o horário de maior número de jogadores ativos. Venda nesse horário para ter melhor liquidez e preços mais altos."),
    ("4", "Diversifique o Portfolio",
     "Não concentre todo o budget em um único jogador. Use pelo menos 4–5 cartas diferentes para diluir o risco de trava de preço."),
    ("5", "Acompanhe SBCs Novos",
     "Quando novos SBCs chegam, cartas específicas sobem em minutos. Fique alerta no site futbin.com/sbc às sextas e segundas-feiras."),
    ("6", "Respeite o Stop Loss",
     "Se uma carta cair 20% abaixo do preço de compra e não houver SBC em vista, venda e preserve o capital. Não case com a carta."),
    ("7", "Quinta é o Dia de Ouro",
     "Na quinta-feira, jogadores recebem recompensas de Division Rivals e compram cartas. Tenha cartas prontas para vender na janela 18h–22h UTC."),
    ("8", "Confira o Path to Glory Tracker",
     "Durante o FIFA World Cup 2026, cartas PTG sobem automaticamente quando a seleção avança. Compre cartas de seleções favoritas (Brasil, Argentina, França, Portugal) com 48h de antecedência dos jogos decisivos."),
]


def tabela_regras():
    linhas = []
    for num, titulo, desc in REGRAS:
        linhas.append([
            Paragraph(num, s_regra_num),
            [Paragraph(titulo, s_regra_titulo), Paragraph(desc, s_regra_desc)],
        ])

    col_w = [1.0*cm, W - 4*cm - 1.2*cm]
    t = Table(linhas, colWidths=col_w)
    ts = TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("GRID",          (0, 0), (-1, -1), 0.3, colors.HexColor("#d5dbdb")),
        ("BACKGROUND",    (0, 0), (0, -1), VERDE_ESCURO),
    ])
    for i in range(0, len(REGRAS), 2):
        ts.add("BACKGROUND", (1, i), (1, i), BRANCO)
    for i in range(1, len(REGRAS), 2):
        ts.add("BACKGROUND", (1, i), (1, i), VERDE_FUNDO)
    t.setStyle(ts)
    return t


# ─── Construção do Documento ───────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(
        CAMINHO,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.5*cm, bottomMargin=1.8*cm,
        title="Relatório Trading EA FC 26",
        author="EA FC 26 Trading Agent",
    )

    story = []

    # ── Cabeçalho ──────────────────────────────────────────────────────────────
    story.append(cabecalho())
    story.append(sp(0.5))

    # ── 1. Contexto de Mercado ─────────────────────────────────────────────────
    story.append(secao("1. CONTEXTO DO MERCADO — 05/06/2026"))
    story.append(sp(0.2))

    story.append(p(
        "<b>Evento Ativo: Festival of Football</b> (5 de junho – 24 de julho de 2026) — "
        "o maior evento de verão do EA FC 26, atrelado à <b>Copa do Mundo FIFA 2026</b>. "
        "O promo de abertura é o <b>Path to Glory (PTG)</b>, ativo de 5 a 19 de junho, "
        "com cartas dinâmicas que recebem upgrades automáticos conforme a seleção do "
        "jogador avança na Copa. Cada vitória em fase mata-mata ativa um upgrade — "
        "até 5 upgrades por carta."
    ))
    story.append(sp(0.2))

    story.append(p("<b>Tendências de Mercado Hoje (Sexta-feira, Dia 1 do Promo):</b>"))
    story.append(bullet("🔴 Cartas PTG recém-lançadas estão SOBREVALORIZADAS — <b>evite comprar Path to Glory no Dia 1</b>."))
    story.append(bullet("🟢 Demanda por SBC Fodder (83–88) está em alta máxima com novos SBCs sendo lançados."))
    story.append(bullet("🟡 SBC <b>10× 84+ Upgrade</b> disponível até 12/06 (pode ser feito 3×) — consome fodder 84+."))
    story.append(bullet("🟢 SBC <b>3× 85+ Upgrade</b> diário (3× por dia) — alta rotatividade de 85/86/87."))
    story.append(bullet("📈 Jogadores 86–87 rated de ligas top (Premier League, Serie A, Bundesliga) estão subindo."))
    story.append(bullet("⚡ Quinta-feira será crucial: Rivals Rewards + possível novo TOTW criarão spike de preços."))
    story.append(sp(0.4))

    # ── 2. Oportunidades de Compra ─────────────────────────────────────────────
    story.append(secao("2. OPORTUNIDADES DE COMPRA — Budget: 40.000 coins"))
    story.append(sp(0.2))
    story.append(p(
        "Cartas selecionadas com base na demanda ativa de SBCs, ligas de alta procura e "
        "potencial de valorização no período do Festival of Football. "
        "<b>Margem líquida já descontada a taxa de 5% da EA.</b>"
    ))
    story.append(sp(0.25))
    story.append(tabela_oportunidades())
    story.append(sp(0.3))
    story.append(p(
        "<i>* Preços baseados em FUTBIN/FUT.GG em 05/06/2026. Recomenda-se sempre verificar "
        "o preço mínimo atual antes de comprar. Filtrar por BIN (Buy It Now).</i>",
        s_aviso
    ))
    story.append(sp(0.4))

    # ── 3. Alocação do Budget ──────────────────────────────────────────────────
    story.append(secao("3. ALOCAÇÃO SUGERIDA DO BUDGET (40.000 coins)"))
    story.append(sp(0.2))

    alloc = [
        [Paragraph("Bloco", s_th),
         Paragraph("Estratégia", s_th),
         Paragraph("Coins Alocados", s_th),
         Paragraph("Cartas Estimadas", s_th)],
        [Paragraph("A", s_td),
         Paragraph("SBC Fodder 86-rated (Çalhanoğlu, Konaté, Olise, Reijnders)", s_td_left),
         Paragraph("16.000", s_td),
         Paragraph("~16 cartas @ 1.000", s_td)],
        [Paragraph("B", s_td),
         Paragraph("SBC Fodder 87-rated (Bruno Fernandes, Rice, Lavelle, Osimhen)", s_td_left),
         Paragraph("14.000", s_td),
         Paragraph("~10 cartas @ 1.400", s_td)],
        [Paragraph("C", s_td),
         Paragraph("SBC Fodder 85-rated (Weir, Stanway) — maior volume, menor risco", s_td_left),
         Paragraph("6.000", s_td),
         Paragraph("~8 cartas @ 750", s_td)],
        [Paragraph("D", s_td),
         Paragraph("Reserva: PTG Especulação / TOTW flip (Domingo–Quarta)", s_td_left),
         Paragraph("4.000", s_td),
         Paragraph("Oportunístico"),],
    ]
    ta = Table(alloc, colWidths=[1.2*cm, 8.0*cm, 3.0*cm, 3.8*cm], repeatRows=1)
    ta.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), BRANCO),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 8),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#bdc3c7")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, VERDE_FUNDO]),
        ("FONTNAME", (2, 1), (2, -1), "Helvetica-Bold"),
        ("TEXTCOLOR", (2, 1), (2, -1), VERDE_ESCURO),
    ]))
    story.append(ta)
    story.append(sp(0.4))

    # ── 4. Estratégia de Timing ────────────────────────────────────────────────
    story.append(secao("4. ESTRATÉGIA DE TIMING"))
    story.append(sp(0.2))
    story.append(tabela_timing())
    story.append(sp(0.4))

    # ── 5. Estimativa de Retorno 48h ───────────────────────────────────────────
    story.append(secao("5. ESTIMATIVA DE RETORNO EM 48H"))
    story.append(sp(0.2))
    story.append(tabela_retorno())
    story.append(sp(0.3))
    story.append(p(
        "⚠️  <b>Cenário Conservador</b>: Foco exclusivo em SBC Fodder 85–86, "
        "venda no fim de semana. Sem especulação em PTG. "
        "Retorno estimado de +3.000 a +3.750 coins líquidos."
    ))
    story.append(p(
        "🚀  <b>Cenário Otimista</b>: Fodder 85–87 vendido no sábado + flip de TOTW na quinta + "
        "uma aposta pontual em PTG de seleção favorita. "
        "Retorno estimado de +7.600 a +10.640 coins líquidos."
    ))
    story.append(sp(0.4))

    # ── 6. 8 Regras de Ouro ────────────────────────────────────────────────────
    story.append(secao("6. AS 8 REGRAS DE OURO DO TRADE"))
    story.append(sp(0.2))
    story.append(tabela_regras())
    story.append(sp(0.4))

    # ── 7. Disclaimer ──────────────────────────────────────────────────────────
    story.append(hr())
    story.append(secao("7. DISCLAIMER"))
    story.append(sp(0.2))
    story.append(p(
        "Este relatório é gerado automaticamente com base em dados públicos de mercado do "
        "EA FC 26 Ultimate Team (fontes: FUTBIN, FUT.GG, FUTMind, RealSport101, Dexerto). "
        "Os preços indicados são estimativas baseadas em médias de mercado e podem variar "
        "significativamente em função de eventos do jogo, novos SBCs, promos inesperadas ou "
        "flutuações orgânicas do mercado. <b>Não há garantia de lucro.</b> "
        "Trading em FUT envolve risco de perda de coins. "
        "Nunca invista mais do que você pode se dar ao luxo de perder. "
        "Este documento não constitui aconselhamento financeiro de qualquer natureza.",
        s_aviso
    ))
    story.append(sp(0.2))
    story.append(p(
        f"<b>Relatório gerado em:</b> {DATA_HORA} UTC  |  "
        "<b>Budget:</b> 40.000 coins  |  "
        "<b>Jogo:</b> EA FC 26 Ultimate Team  |  "
        "<b>Meta:</b> SBC Fodder Flipping + Evolution Investing + Thursday Flipping",
        s_aviso
    ))

    doc.build(story)
    print(f"PDF gerado: {CAMINHO}")


if __name__ == "__main__":
    build()
