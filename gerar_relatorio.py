#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ── Cores da identidade EA FC / FUT ──────────────────────────────────────────
EA_GREEN   = colors.HexColor("#00FF87")
EA_DARK    = colors.HexColor("#0D0D0D")
EA_GOLD    = colors.HexColor("#F5C518")
EA_BLUE    = colors.HexColor("#1B4F72")
EA_CARD_BG = colors.HexColor("#1A1A2E")
EA_RED     = colors.HexColor("#E74C3C")
EA_GRAY    = colors.HexColor("#2C2C3E")
WHITE      = colors.white
LIGHT_GRAY = colors.HexColor("#F0F0F0")
EA_ACCENT  = colors.HexColor("#16213E")

DATA_HORA   = "31/05/2026 08:06"
ARQUIVO_PDF = "relatorio-trading-2026-05-31-08h.pdf"

# ── Documento ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    ARQUIVO_PDF,
    pagesize=A4,
    rightMargin=1.5*cm,
    leftMargin=1.5*cm,
    topMargin=1.8*cm,
    bottomMargin=1.8*cm,
    title="Relatório de Trading EA FC 26",
    author="Trading Bot - EA FC 26 Ultimate Team",
)

styles = getSampleStyleSheet()

# ── Estilos customizados ───────────────────────────────────────────────────────
def s(name, **kw):
    return ParagraphStyle(name, **kw)

style_title = s("Title",
    fontName="Helvetica-Bold", fontSize=22,
    textColor=EA_GREEN, alignment=TA_CENTER, spaceAfter=4)

style_subtitle = s("Subtitle",
    fontName="Helvetica-Bold", fontSize=13,
    textColor=EA_GOLD, alignment=TA_CENTER, spaceAfter=2)

style_datetime = s("DateTime",
    fontName="Helvetica", fontSize=10,
    textColor=WHITE, alignment=TA_CENTER, spaceAfter=10)

style_section = s("Section",
    fontName="Helvetica-Bold", fontSize=12,
    textColor=EA_GREEN, spaceBefore=14, spaceAfter=6,
    borderPad=4)

style_body = s("Body",
    fontName="Helvetica", fontSize=9.5,
    textColor=colors.HexColor("#DDDDDD"),
    leading=15, spaceAfter=4, alignment=TA_JUSTIFY)

style_body_dark = s("BodyDark",
    fontName="Helvetica", fontSize=9.5,
    textColor=EA_DARK,
    leading=15, spaceAfter=4, alignment=TA_JUSTIFY)

style_bullet = s("Bullet",
    fontName="Helvetica", fontSize=9.5,
    textColor=colors.HexColor("#CCCCCC"),
    leading=14, leftIndent=12, spaceAfter=3)

style_highlight = s("Highlight",
    fontName="Helvetica-Bold", fontSize=10,
    textColor=EA_GOLD, alignment=TA_LEFT, spaceAfter=3)

style_rule_num = s("RuleNum",
    fontName="Helvetica-Bold", fontSize=11,
    textColor=EA_GREEN, leading=14)

style_rule_body = s("RuleBody",
    fontName="Helvetica", fontSize=9.5,
    textColor=colors.HexColor("#DDDDDD"), leading=14, spaceAfter=6)

style_disclaimer = s("Disclaimer",
    fontName="Helvetica-Oblique", fontSize=8,
    textColor=colors.HexColor("#888888"), alignment=TA_JUSTIFY,
    leading=12, spaceBefore=8)

def header_row(text):
    return Paragraph(text, style_section)

def body(text, dark=False):
    st = style_body_dark if dark else style_body
    return Paragraph(text, st)

def bullet(text):
    return Paragraph(f"• &nbsp;{text}", style_bullet)

def hr(dark=False):
    c = colors.HexColor("#333355") if not dark else colors.HexColor("#BBBBBB")
    return HRFlowable(width="100%", thickness=0.8, color=c, spaceAfter=6, spaceBefore=2)

# ── Tabela de cartas ─────────────────────────────────────────────────────────
def card_table():
    header = ["Jogador", "Rat.", "Clube / Liga", "Compra\n(coins)", "Venda\n(coins)", "Margem\nLíq. (-5%)", "Janela"]

    rows = [
        # SBC Fodder 85-rated (cheap leagues)
        ["Popp (ST)", "85", "Chelsea / WSL", "750", "1.600", "770", "Agora → Qui"],
        ["Mbeumo (RW)", "85", "Brentford / PL", "800", "1.700", "815", "Agora → Qui"],
        ["Giugliano (CM)", "85", "Roma / Serie A", "750", "1.600", "770", "Agora → Qui"],
        ["Renard (CB)", "85", "Lyon / D1F", "750", "1.600", "770", "Agora → Sex"],
        # SBC Fodder 86-rated
        ["Ona Batlle (RB)", "86", "Barcelona / LF", "900", "2.000", "1.000", "Agora → Qui"],
        ["Tonali (CDM)", "86", "AC Milan / SA", "1.000", "2.200", "1.090", "Agora → Qui"],
        ["R. Dias (CB)", "86", "Man City / PL", "1.100", "2.400", "1.180", "Agora → Sex"],
        # SBC Fodder 87-rated
        ["Hemp (LW)", "87", "Man City / PL", "1.800", "3.800", "1.810", "Agora → Qui"],
        ["Sommer (GK)", "87", "Inter / Serie A", "1.800", "4.000", "2.000", "Agora → Qui"],
        ["Osimhen (ST)", "87", "Napoli / Serie A", "1.900", "4.200", "2.090", "Agora → Sex"],
        # Evolutions eligible / meta crash buy
        ["Szoboszlai (CAM)", "88", "Liverpool / PL", "3.500", "6.500", "2.675", "Dom → Qui"],
        ["Kulusevski (RM)", "88", "Spurs / PL", "3.200", "6.000", "2.500", "Dom → Qui"],
        # End of an Era SBC prep
        ["Salah (RW) - Gold", "88", "Liverpool / PL", "4.000", "7.500", "3.125", "Hoje → Seg"],
        ["Robertson (LB)", "87", "Liverpool / PL", "2.200", "4.800", "2.360", "Hoje → Seg"],
    ]

    col_widths = [4.6*cm, 1.3*cm, 4.2*cm, 2.1*cm, 2.1*cm, 2.3*cm, 2.5*cm]

    table_data = [header] + rows

    tbl = Table(table_data, colWidths=col_widths, repeatRows=1)

    tbl_style = TableStyle([
        # Header
        ("BACKGROUND",   (0,0), (-1,0), EA_BLUE),
        ("TEXTCOLOR",    (0,0), (-1,0), EA_GOLD),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,0), 8.5),
        ("ALIGN",        (0,0), (-1,0), "CENTER"),
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",   (0,0), (-1,0), 6),
        ("BOTTOMPADDING",(0,0), (-1,0), 6),
        # Alternating rows
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [EA_DARK, EA_GRAY]),
        ("TEXTCOLOR",    (0,1), (-1,-1), WHITE),
        ("FONTNAME",     (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",     (0,1), (-1,-1), 8.5),
        ("ALIGN",        (1,1), (-1,-1), "CENTER"),
        ("ALIGN",        (0,1), (0,-1), "LEFT"),
        ("TOPPADDING",   (0,1), (-1,-1), 4),
        ("BOTTOMPADDING",(0,1), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        # Highlight margin column
        ("TEXTCOLOR",    (5,1), (5,-1), EA_GREEN),
        ("FONTNAME",     (5,1), (5,-1), "Helvetica-Bold"),
        # Borders
        ("GRID",         (0,0), (-1,-1), 0.4, colors.HexColor("#3A3A5C")),
        ("LINEBELOW",    (0,0), (-1,0), 1.2, EA_GOLD),
        ("BOX",          (0,0), (-1,-1), 1.0, EA_BLUE),
    ])
    tbl.setStyle(tbl_style)
    return tbl

# ── Caixa colorida para seção de destaque ────────────────────────────────────
def info_box(lines, bg=EA_CARD_BG, text_color=WHITE):
    inner = []
    for line in lines:
        inner.append([Paragraph(line, ParagraphStyle(
            "BoxLine", fontName="Helvetica", fontSize=9.5,
            textColor=text_color, leading=15))])
    t = Table(inner, colWidths=[17.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (0,-1), 6),
        ("BOX", (0,0), (-1,-1), 0.8, EA_BLUE),
    ]))
    return t

def gold_box(lines):
    return info_box(lines, bg=colors.HexColor("#1A1200"), text_color=EA_GOLD)

def green_box(lines):
    return info_box(lines, bg=colors.HexColor("#001A0D"), text_color=EA_GREEN)

# ── Construção do documento ───────────────────────────────────────────────────
story = []

# ── HEADER ────────────────────────────────────────────────────────────────────
hdr_data = [[
    Paragraph(
        '<font size="20"><b>EA FC 26</b></font><br/>'
        '<font size="14" color="#F5C518">RELATÓRIO DE TRADING · ULTIMATE TEAM</font>',
        ParagraphStyle("H", fontName="Helvetica-Bold", fontSize=20,
                       textColor=EA_GREEN, alignment=TA_CENTER)),
    Paragraph(
        f'<font size="10" color="#AAAAAA">Emitido em</font><br/>'
        f'<font size="14" color="#F5C518"><b>{DATA_HORA} UTC</b></font><br/>'
        f'<font size="9" color="#888888">Budget: 40.000 coins</font>',
        ParagraphStyle("H2", fontName="Helvetica", fontSize=10,
                       textColor=WHITE, alignment=TA_CENTER))
]]
hdr_tbl = Table(hdr_data, colWidths=[10*cm, 8.5*cm])
hdr_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), EA_CARD_BG),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 14),
    ("BOTTOMPADDING", (0,0), (-1,-1), 14),
    ("LEFTPADDING", (0,0), (-1,-1), 14),
    ("BOX", (0,0), (-1,-1), 1.5, EA_GREEN),
    ("LINEAFTER", (0,0), (0,-1), 0.8, EA_BLUE),
]))
story.append(hdr_tbl)
story.append(Spacer(1, 0.4*cm))

# ── 1. CONTEXTO DE MERCADO ────────────────────────────────────────────────────
story.append(header_row("1. CONTEXTO DO MERCADO — 31/05/2026"))
story.append(hr())

story.append(info_box([
    "<b>EVENTO ATIVO:</b> Ultimate TOTS (Team of the Season) — Iniciado em 22 de maio de 2026. "
    "Estamos no <b>Dia 9</b> do Ultimate TOTS, fase final da maior promo do ano.",

    "<b>THE WORLD'S GAME UPDATE:</b> Lançado em 28/05/2026 — 53 seleções nacionais licenciadas "
    "adicionadas ao jogo (incluindo Brasil), criando novo interesse por jogadores internacionais.",

    "<b>SOCCER AID SHOWDOWN:</b> SBC do Berbatov ativo HOJE (31/05) — demanda por fodder "
    "aumentada temporariamente, especialmente cartas 85–87 rated.",

    "<b>END OF AN ERA SBCs ESPERADOS:</b> Salah, Robertson, Griezmann, Bernardo Silva, "
    "Goretzka, Brandt e Süle — cards Icon Chemistry previstos para os próximos dias.",

    "<b>TENDÊNCIA GERAL:</b> Crash de mercado profundo. Cartas 85–88 rated estão nos "
    "menores preços do ano. Momento ideal para acumulação de fodder e posicionamento.",
]))

story.append(Spacer(1, 0.3*cm))

# Status rápido de preços de referência
price_status = [
    ["Rating", "Preço Mín.", "Preço Médio", "Tendência"],
    ["83-rated", "~400 coins", "~600 coins", "QUEDA (crash TOTS)"],
    ["84-rated", "~550 coins", "~750 coins", "QUEDA (crash TOTS)"],
    ["85-rated", "~700 coins", "~900 coins", "ESTÁVEL / QUEDA"],
    ["86-rated", "~850 coins", "~1.100 coins", "ESTÁVEL"],
    ["87-rated", "~1.800 coins", "~2.500 coins", "LEVE ALTA (procura SBC)"],
    ["88-rated", "~3.000 coins", "~4.500 coins", "VOLATIL / OPORTUNIDADE"],
]
ps_tbl = Table(price_status, colWidths=[2.8*cm, 3.5*cm, 3.5*cm, 8.6*cm])
ps_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), EA_BLUE),
    ("TEXTCOLOR", (0,0), (-1,0), EA_GOLD),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 9),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [EA_DARK, EA_GRAY]),
    ("TEXTCOLOR", (0,1), (-1,-1), WHITE),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#3A3A5C")),
    ("TEXTCOLOR", (3,1), (3,4), EA_RED),
    ("TEXTCOLOR", (3,5), (3,5), EA_GREEN),
    ("TEXTCOLOR", (3,6), (3,6), EA_GOLD),
    ("FONTNAME", (3,1), (3,-1), "Helvetica-Bold"),
]))
story.append(ps_tbl)
story.append(Spacer(1, 0.3*cm))

# ── 2. OPORTUNIDADES RECOMENDADAS ─────────────────────────────────────────────
story.append(header_row("2. OPORTUNIDADES DE COMPRA — TABELA DE CARTAS"))
story.append(hr())

story.append(body(
    "Cartas selecionadas com base no contexto de crash do Ultimate TOTS, SBCs ativos e "
    "expectativa de End of an Era. <b>Margem líquida calculada após desconto de 5% da EA.</b> "
    "Priorize ligas menos usadas (WSL, Serie A, Liga F) — mesmo rating, menor custo de fodder."
))
story.append(Spacer(1, 0.2*cm))
story.append(card_table())
story.append(Spacer(1, 0.15*cm))

story.append(gold_box([
    "NOTA IMPORTANTE: Preços são estimativas baseadas em padrões históricos do TOTS + dados de "
    "maio/2026. Verifique sempre no FUTBIN / FUT.GG antes de executar qualquer operação. "
    "Cartas de ligas menores tendem a ser 20–40% mais baratas que equivalentes da PL/La Liga."
]))
story.append(Spacer(1, 0.3*cm))

# ── 3. ESTRATÉGIA DE TIMING ───────────────────────────────────────────────────
story.append(header_row("3. ESTRATÉGIA DE TIMING"))
story.append(hr())

timing_data = [
    ["Período", "Ação", "Motivo"],
    ["Dom 31/05\n07h–12h UTC", "COMPRAR fodder 85–87\nCOMPRAR Salah/Robertson gold",
     "Domingo cedo = menor liquidez, preços no fundo. "
     "Soccer Aid SBC ativo aumenta demanda por fodder em breve."],
    ["Dom 31/05\n14h–22h UTC", "SEGURAR / aguardar\nnovo SBC anunciado",
     "EA costuma anunciar novos SBCs domingo à tarde. "
     "Não venda antes do anúncio — espere o spike de demanda."],
    ["Seg 01/06\n08h–18h UTC", "VENDER fodder acumulado\n(se SBC novo ativo)",
     "Pico de demanda nas primeiras 6–12h após novo SBC. "
     "Venda escalonada em lotes de 5 cartas a cada 30 min."],
    ["Qui 04/06\n15h–18h UTC", "COMPRAR meta players\npré-weekend league",
     "Novo conteúdo de quinta-feira (SBCs/Evos) cria demanda. "
     "Players meta sobem 15–30% na sexta antes do WL."],
    ["Sex 05/06\n17h–20h UTC", "VENDER meta players\ncomprados na quinta",
     "Pico de preços na sexta à tarde — jogadores montam times "
     "para o Weekend League. Melhor janela de venda da semana."],
]

t_col = [3*cm, 5*cm, 10.4*cm]
tim_tbl = Table(timing_data, colWidths=t_col, repeatRows=1)
tim_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), EA_BLUE),
    ("TEXTCOLOR", (0,0), (-1,0), EA_GOLD),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 8.5),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [EA_DARK, EA_GRAY]),
    ("TEXTCOLOR", (0,1), (-1,-1), WHITE),
    ("FONTNAME", (0,1), (1,-1), "Helvetica-Bold"),
    ("FONTNAME", (2,1), (2,-1), "Helvetica"),
    ("TEXTCOLOR", (0,1), (0,-1), EA_GOLD),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#3A3A5C")),
    ("BOX", (0,0), (-1,-1), 1.0, EA_BLUE),
    ("LINEBELOW", (0,0), (-1,0), 1.2, EA_GOLD),
]))
story.append(tim_tbl)
story.append(Spacer(1, 0.3*cm))

# ── 4. ESTIMATIVA DE RETORNO 48H ──────────────────────────────────────────────
story.append(header_row("4. ESTIMATIVA DE RETORNO EM 48 HORAS"))
story.append(hr())

ret_data = [
    ["Estratégia", "Capital\nAlocado", "Retorno\nConservador", "Retorno\nOtimista", "Cenário"],
    ["SBC Fodder 85-rated\n(20 cartas × 800)", "16.000", "+8.000\n(+50%)", "+14.400\n(+90%)",
     "SBC novo ativo — demanda sobe\npara fodder de qualquer liga"],
    ["SBC Fodder 86/87-rated\n(8 cartas mistas)", "12.000", "+7.200\n(+60%)", "+12.000\n(+100%)",
     "87-rated com maior margem por\nSBC End of an Era exige fodder"],
    ["Meta Players (Szoboszlai\nKulusevski × 2 cada)", "6.800", "+2.040\n(+30%)", "+4.760\n(+70%)",
     "Pre-WL spike sexta — alta\nde 30–70% é histórica"],
    ["EOAE Prep (Salah/Robertson\ngold × 2 cada)", "5.200", "+1.040\n(+20%)", "+6.240\n(+120%)",
     "Depende do SBC EOAE ser\nanunciado antes de sex"],
    ["TOTAL", "40.000", "+18.280\n(+46%)", "+37.400\n(+93.5%)", "Budget total alocado"],
]

r_col = [5*cm, 2.2*cm, 2.5*cm, 2.5*cm, 6.2*cm]
ret_tbl = Table(ret_data, colWidths=r_col, repeatRows=1)
ret_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), EA_BLUE),
    ("TEXTCOLOR", (0,0), (-1,0), EA_GOLD),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 8.5),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("ALIGN", (0,1), (0,-1), "LEFT"),
    ("ALIGN", (4,1), (4,-1), "LEFT"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0,1), (-1,-2), [EA_DARK, EA_GRAY]),
    ("BACKGROUND", (0,-1), (-1,-1), EA_CARD_BG),
    ("TEXTCOLOR", (0,1), (-1,-1), WHITE),
    ("TEXTCOLOR", (2,1), (2,-1), colors.HexColor("#90EE90")),
    ("TEXTCOLOR", (3,1), (3,-1), EA_GREEN),
    ("FONTNAME", (2,1), (3,-1), "Helvetica-Bold"),
    ("FONTNAME", (0,-1), (-1,-1), "Helvetica-Bold"),
    ("TEXTCOLOR", (0,-1), (-1,-1), EA_GOLD),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#3A3A5C")),
    ("BOX", (0,0), (-1,-1), 1.0, EA_BLUE),
    ("LINEBELOW", (0,0), (-1,0), 1.2, EA_GOLD),
    ("LINEABOVE", (0,-1), (-1,-1), 1.2, EA_GOLD),
]))
story.append(ret_tbl)
story.append(Spacer(1, 0.2*cm))

story.append(green_box([
    "CENÁRIO CONSERVADOR: +18.280 coins → Capital final ~58.280 coins (+46%)",
    "CENÁRIO OTIMISTA: +37.400 coins → Capital final ~77.400 coins (+93.5%)",
    "Premissa: pelo menos 1 novo SBC de upgrade lançado entre dom-sex e SBC EOAE anunciado.",
]))
story.append(Spacer(1, 0.3*cm))

# ── 5. 8 REGRAS DE OURO ───────────────────────────────────────────────────────
story.append(header_row("5. AS 8 REGRAS DE OURO DO TRADE"))
story.append(hr())

rules = [
    ("1", "NUNCA COMPRE NO PICO",
     "Após um SBC ou promo ser anunciado, aguarde 30–60 minutos. O pico inicial cai "
     "quando a oferta sobe. Entrar cedo é pagar premium por impaciência."),
    ("2", "VENDA ANTES DO FIM DO SBC",
     "Cartas de fodder perdem valor conforme o SBC se aproxima do prazo. Venda "
     "com 24–48h de antecedência para garantir liquidez e preço."),
    ("3", "DIVERSIFIQUE EM RATINGS",
     "Combine 85-rated (volume, margem menor) com 87-rated (volume menor, margem maior). "
     "Nunca concentre 100% do budget em um único rating ou jogador."),
    ("4", "USE HORÁRIOS DE BAIXA LIQUIDEZ",
     "Madrugadas (01h–06h UTC) e manhãs de domingo têm os menores preços do mercado. "
     "Compre nessa janela; venda nos horários de pico (18h–22h)."),
    ("5", "RESPEITE A TAXA DE 5% DA EA",
     "Toda venda tem custo de 5%. Sempre calcule: Preço de venda × 0,95 > Preço de compra. "
     "Margem bruta de 5% = breakeven. Mínimo recomendado: 20%."),
    ("6", "NUNCA INVISTA 100% DO BUDGET",
     "Mantenha 20–30% em coins líquidos. Flash SBCs, Evolutions e promos aparecem sem aviso. "
     "Quem tem coins disponíveis pega as melhores oportunidades."),
    ("7", "LIGUE/SIGA ANÚNCIOS DA EA",
     "Twitter/X @EASPORTSFC, Reddit r/EAFC e canais do YouTube avisam SBCs minutos antes. "
     "Reaja rápido — a janela de lucro nas primeiras 2h é a maior do ciclo."),
    ("8", "DOCUMENTE CADA OPERAÇÃO",
     "Registre: jogador, rating, preço de compra, preço de venda, lucro líquido. "
     "Sem histórico não há aprendizado. Dados salvam o budget a longo prazo."),
]

for num, title, desc in rules:
    rule_row = [
        [Paragraph(num, ParagraphStyle("RN", fontName="Helvetica-Bold", fontSize=14,
                                        textColor=EA_GREEN, alignment=TA_CENTER))],
        [Paragraph(f"<b>{title}</b>", ParagraphStyle("RT", fontName="Helvetica-Bold", fontSize=10,
                                                       textColor=EA_GOLD)),
         Paragraph(desc, ParagraphStyle("RD", fontName="Helvetica", fontSize=9,
                                          textColor=colors.HexColor("#CCCCCC"), leading=13))]
    ]
    inner = Table([[
        Paragraph(num, ParagraphStyle("N", fontName="Helvetica-Bold", fontSize=16,
                                       textColor=EA_GREEN, alignment=TA_CENTER)),
        Table([[Paragraph(f"<b>{title}</b>",
                           ParagraphStyle("T", fontName="Helvetica-Bold", fontSize=10,
                                          textColor=EA_GOLD))],
               [Paragraph(desc, ParagraphStyle("D", fontName="Helvetica", fontSize=9,
                                                textColor=colors.HexColor("#CCCCCC"),
                                                leading=13))]],
              colWidths=[15.8*cm]),
    ]], colWidths=[1.2*cm, 15.8*cm])
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), EA_CARD_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LINEAFTER", (0,0), (0,-1), 0.8, EA_BLUE),
        ("BOX", (0,0), (-1,-1), 0.6, EA_BLUE),
    ]))
    story.append(inner)
    story.append(Spacer(1, 0.15*cm))

story.append(Spacer(1, 0.2*cm))

# ── 6. DISCLAIMER ─────────────────────────────────────────────────────────────
story.append(hr())
story.append(Paragraph(
    "<b>DISCLAIMER:</b> Este relatório é gerado automaticamente com fins informativos e educacionais. "
    "Os preços apresentados são estimativas baseadas em dados históricos, padrões sazonais do "
    "Ultimate Team e informações públicas disponíveis até a data de emissão. O mercado do FUT é "
    "altamente volátil e os valores reais podem diferir significativamente. Verifique sempre os "
    "preços em tempo real no FUTBIN (futbin.com) e FUT.GG antes de executar operações. "
    "O autor não assume responsabilidade por perdas decorrentes das decisões de trading. "
    "Trade consciente — nunca invista mais do que está disposto a perder.",
    style_disclaimer
))

# ── BUILD PDF ─────────────────────────────────────────────────────────────────
def add_page_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(EA_ACCENT)
    canvas.rect(0, 0, A4[0], A4[1], fill=True, stroke=False)
    # Rodapé
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.HexColor("#555577"))
    page_num = canvas.getPageNumber()
    canvas.drawCentredString(A4[0]/2, 0.8*cm,
        f"EA FC 26 Ultimate Team · Relatório de Trading · {DATA_HORA} UTC · Página {page_num}")
    canvas.restoreState()

doc.build(story, onFirstPage=add_page_background, onLaterPages=add_page_background)
print(f"PDF gerado: {ARQUIVO_PDF}")
