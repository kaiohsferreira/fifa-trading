#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# ── Configurações ──────────────────────────────────────────────────────────────
REPORT_DATE = "23/05/2026 20:04"
REPORT_DATE_UTC = "2026-05-23 20:04 UTC"
PDF_FILENAME = "relatorio-trading-2026-05-23-20h.pdf"
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), PDF_FILENAME)

# ── Paleta de cores ────────────────────────────────────────────────────────────
C_GOLD        = colors.HexColor("#FFD700")
C_DARK_GOLD   = colors.HexColor("#B8860B")
C_GREEN       = colors.HexColor("#00C851")
C_DARK_GREEN  = colors.HexColor("#007E33")
C_RED         = colors.HexColor("#FF4444")
C_DARK_BLUE   = colors.HexColor("#0D1B2A")
C_MID_BLUE    = colors.HexColor("#1A3A5C")
C_LIGHT_BLUE  = colors.HexColor("#E8F4FD")
C_WHITE       = colors.white
C_BLACK       = colors.black
C_GRAY        = colors.HexColor("#F5F5F5")
C_DARK_GRAY   = colors.HexColor("#555555")
C_ORANGE      = colors.HexColor("#FF8C00")

# ── Estilos ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def make_style(name, fontName="Helvetica", fontSize=10, textColor=C_BLACK,
               alignment=TA_LEFT, spaceBefore=4, spaceAfter=4,
               leading=None, bold=False):
    fn = fontName + ("-Bold" if bold and not fontName.endswith("-Bold") else "")
    return ParagraphStyle(
        name,
        fontName=fn,
        fontSize=fontSize,
        textColor=textColor,
        alignment=alignment,
        spaceBefore=spaceBefore,
        spaceAfter=spaceAfter,
        leading=leading or fontSize * 1.35,
    )

s_title       = make_style("Title",    fontSize=22, textColor=C_GOLD,        alignment=TA_CENTER, bold=True, spaceBefore=0, spaceAfter=6)
s_subtitle    = make_style("SubTitle", fontSize=13, textColor=C_WHITE,       alignment=TA_CENTER, spaceBefore=2, spaceAfter=2)
s_date        = make_style("Date",     fontSize=11, textColor=C_GOLD,        alignment=TA_CENTER, bold=True, spaceBefore=4, spaceAfter=6)
s_section     = make_style("Section",  fontSize=13, textColor=C_DARK_BLUE,   bold=True, spaceBefore=14, spaceAfter=4)
s_subsection  = make_style("SubSect",  fontSize=11, textColor=C_MID_BLUE,    bold=True, spaceBefore=8,  spaceAfter=3)
s_body        = make_style("Body",     fontSize=9,  textColor=C_BLACK,       alignment=TA_JUSTIFY, spaceBefore=2, spaceAfter=2, leading=13)
s_body_bold   = make_style("BodyBold", fontSize=9,  textColor=C_BLACK,       bold=True, spaceBefore=2, spaceAfter=2)
s_bullet      = make_style("Bullet",   fontSize=9,  textColor=C_BLACK,       spaceBefore=1, spaceAfter=1, leading=13)
s_table_hdr   = make_style("TblHdr",   fontSize=8,  textColor=C_WHITE,       alignment=TA_CENTER, bold=True, spaceBefore=1, spaceAfter=1)
s_table_cell  = make_style("TblCell",  fontSize=8,  textColor=C_BLACK,       alignment=TA_CENTER, spaceBefore=1, spaceAfter=1)
s_table_left  = make_style("TblLeft",  fontSize=8,  textColor=C_BLACK,       alignment=TA_LEFT,   spaceBefore=1, spaceAfter=1, bold=True)
s_highlight   = make_style("High",     fontSize=9,  textColor=C_DARK_BLUE,   spaceBefore=3, spaceAfter=3, leading=13)
s_green_val   = make_style("GreenV",   fontSize=9,  textColor=C_DARK_GREEN,  bold=True, alignment=TA_CENTER, spaceBefore=1, spaceAfter=1)
s_red_val     = make_style("RedV",     fontSize=9,  textColor=C_RED,         bold=True, alignment=TA_CENTER, spaceBefore=1, spaceAfter=1)
s_gold_val    = make_style("GoldV",    fontSize=9,  textColor=C_DARK_GOLD,   bold=True, alignment=TA_CENTER, spaceBefore=1, spaceAfter=1)
s_disclaimer  = make_style("Disc",     fontSize=7.5,textColor=C_DARK_GRAY,   alignment=TA_JUSTIFY, spaceBefore=2, spaceAfter=2, leading=11)
s_rule_num    = make_style("RuleNum",  fontSize=18, textColor=C_GOLD,        bold=True, alignment=TA_CENTER, spaceBefore=0, spaceAfter=0)
s_rule_title  = make_style("RuleT",    fontSize=10, textColor=C_DARK_BLUE,   bold=True, spaceBefore=0, spaceAfter=2)
s_rule_body   = make_style("RuleB",    fontSize=8.5,textColor=C_BLACK,       spaceBefore=1, spaceAfter=4, leading=12, alignment=TA_JUSTIFY)

# ── Funções auxiliares ─────────────────────────────────────────────────────────
def section_header(text):
    return [
        HRFlowable(width="100%", thickness=2, color=C_DARK_BLUE, spaceAfter=4),
        Paragraph(f"▸ {text}", s_section),
        HRFlowable(width="100%", thickness=0.5, color=C_MID_BLUE, spaceBefore=2, spaceAfter=6),
    ]

def colored_box(content_paragraphs, bg_color=C_LIGHT_BLUE, border_color=C_MID_BLUE):
    data = [[p] for p in content_paragraphs]
    tbl = Table(data, colWidths=[16.5*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg_color),
        ("BOX",        (0,0), (-1,-1), 1, border_color),
        ("LEFTPADDING",(0,0), (-1,-1), 10),
        ("RIGHTPADDING",(0,0),(-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
    ]))
    return tbl

def opportunity_marker(text, color):
    tbl = Table([[Paragraph(text, make_style("Tag", fontSize=8, textColor=C_WHITE,
                                             bold=True, alignment=TA_CENTER))]],
                colWidths=[2.5*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color),
        ("BOX",        (0,0), (-1,-1), 0.5, color),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING",(0,0),(-1,-1), 3),
    ]))
    return tbl

# ── Construção do documento ────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm,  bottomMargin=2*cm,
    title="Relatório de Trading EA FC 26",
    author="Agente de Análise FUT",
)

story = []

# ══════════════════════════════════════════════════════════════════════════════
# CABEÇALHO
# ══════════════════════════════════════════════════════════════════════════════
header_data = [[
    Paragraph("⚽ EA FC 26 ULTIMATE TEAM", s_title),
    Paragraph("RELATÓRIO DE TRADING & ANÁLISE DE MERCADO", s_subtitle),
    Paragraph(f"📅  {REPORT_DATE}  UTC", s_date),
    Paragraph("Budget Disponível: 40.000 coins  |  Meta: SBC Fodder Flipping + Evolution Investing + Thursday Flip",
              make_style("Budget", fontSize=9, textColor=C_GOLD, alignment=TA_CENTER, spaceBefore=0, spaceAfter=0)),
]]
header_tbl = Table(header_data, colWidths=[16.5*cm])
header_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), C_DARK_BLUE),
    ("BOX",           (0,0), (-1,-1), 2, C_GOLD),
    ("TOPPADDING",    (0,0), (-1,-1), 14),
    ("BOTTOMPADDING", (0,0), (-1,-1), 14),
    ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ("RIGHTPADDING",  (0,0), (-1,-1), 12),
]))
story.append(header_tbl)
story.append(Spacer(1, 0.5*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 1: CONTEXTO DO MERCADO
# ══════════════════════════════════════════════════════════════════════════════
story.extend(section_header("1. CONTEXTO DO MERCADO — 23 MAI 2026"))

story.append(Paragraph(
    "O mercado de EA FC 26 encontra-se em um dos momentos mais críticos e lucrativos do ano: "
    "a semana do <b>Ultimate TOTS (Team of the Season)</b>, lançado em 22 de maio de 2026 às 18h BST. "
    "Esta é a promoção final e mais prestigiosa da temporada, reunindo os melhores jogadores de todas "
    "as ligas em uma única equipa de élite.",
    s_body
))
story.append(Spacer(1, 0.2*cm))

# Box de eventos ativos
eventos_data = [
    [Paragraph("🔴 EVENTO ATIVO", make_style("EvHdr", fontSize=10, textColor=C_WHITE, bold=True, alignment=TA_CENTER))],
    [Paragraph(
        "<b>Ultimate TOTS</b> — Lançado 22/05/2026 | Inclui: Messi (96 OVR), Mbappé (95 OVR), "
        "Cristiano Ronaldo, Lamine Yamal, Erling Haaland e outros craques com 93-96 rated.",
        make_style("EvBody", fontSize=9, textColor=C_WHITE, spaceBefore=2, spaceAfter=2)
    )],
    [Paragraph(
        "<b>End of an Era SBCs</b> — Ativas durante o Ultimate TOTS | Salah 95 OVR (Liverpool), "
        "Griezmann 94 OVR (Atlético de Madrid), Bernardo Silva 93 OVR (Man. City), "
        "Robertson ~91 OVR, Goretzka ~91 OVR, John Stones 91 OVR.",
        make_style("EvBody2", fontSize=9, textColor=C_WHITE, spaceBefore=2, spaceAfter=2)
    )],
    [Paragraph(
        "<b>La Liga TOTS Upgrade SBC</b> — Expira 26/05/2026 | Requer squads 86 + 87 rated. "
        "<b>Festival of Football: Answer the Call</b> — Cartas dinâmicas ligadas à convocação Copa do Mundo. "
        "<b>Live-Upgrading Cards</b> — Ligadas a ligas e copas domésticas (até 29/05/2026).",
        make_style("EvBody3", fontSize=9, textColor=C_GOLD, spaceBefore=2, spaceAfter=2)
    )],
]
eventos_tbl = Table(eventos_data, colWidths=[16.5*cm])
eventos_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (0,0),  C_RED),
    ("BACKGROUND",    (0,1), (0,3),  C_DARK_BLUE),
    ("BOX",           (0,0), (-1,-1), 1.5, C_GOLD),
    ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ("RIGHTPADDING",  (0,0), (-1,-1), 10),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(eventos_tbl)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Tendência Geral do Mercado:</b>", s_body_bold))
tendencias = [
    "📉 <b>Fase de queda inicial (dias 1-2 do TOTS):</b> A abertura massiva de pacotes durante recompensas "
    "inunda o mercado com cartas 88-94 rated, pressionando os preços de fodder para baixo. "
    "<b>Este é o momento ideal de compra.</b>",
    "📈 <b>Recuperação (dia 3-5):</b> À medida que os jogadores completam SBCs de End of an Era e Upgrade, "
    "a demanda por fodder 85-88 rated dispara, os preços sobem 20-45% em relação ao fundo.",
    "⏰ <b>Quinta-feira (29/05) — Pico de demanda:</b> Dia de recompensas de Division Rivals e FUT Champions, "
    "jogadores abrem pacotes e completam SBCs em massa. Fodder de 86-87 tende a atingir pico de preço.",
    "🎯 <b>La Liga TOTS Upgrade SBC expira 26/05:</b> Criação de janela de oportunidade para vender "
    "fodder 86-87 rated antes da expiração.",
]
for t in tendencias:
    story.append(Paragraph(f"• {t}", s_bullet))
story.append(Spacer(1, 0.2*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2: TABELA DE CARTAS RECOMENDADAS
# ══════════════════════════════════════════════════════════════════════════════
story.extend(section_header("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE TRADING"))

story.append(Paragraph(
    "Jogadores específicos identificados com base em dados de mercado de FUTBIN, FUT.GG, "
    "análise de SBCs ativos e padrões históricos de TOTS. Margem líquida calculada após taxa EA de 5%.",
    s_body
))
story.append(Spacer(1, 0.2*cm))

# Cabeçalho da tabela
hdr_style = s_table_hdr
cell_style = s_table_cell
left_style = s_table_left

def p(text, style=cell_style): return Paragraph(text, style)
def ph(text): return Paragraph(text, hdr_style)
def pl(text): return Paragraph(text, left_style)
def pg(text): return Paragraph(text, s_green_val)
def pr(text): return Paragraph(text, s_red_val)
def po(text): return Paragraph(text, s_gold_val)

table_data = [
    # Cabeçalho
    [ph("JOGADOR"), ph("OVR"), ph("CLUBE"), ph("TIPO"), ph("COMPRA\n(coins)"), ph("VENDA\n(coins)"), ph("MARGEM\nLÍQ."), ph("JANELA")],

    # ── FODDER SBC 83-84 rated ───────────────────────────────────────────────
    [pl("Iago Aspas"),         p("83"), p("Celta de Vigo"),     p("Fodder SBC"), p("700"),   p("1.100"),  pg("+346"),   po("Agora → 26/05")],
    [pl("Luka Modrić"),        p("83"), p("Real Madrid"),       p("Fodder SBC"), p("750"),   p("1.200"),  pg("+390"),   po("Agora → 26/05")],
    [pl("Anthony Gordon"),     p("83"), p("Newcastle Utd"),     p("Fodder SBC"), p("750"),   p("1.150"),  pg("+343"),   po("Agora → 26/05")],
    [pl("Benjamin White"),     p("83"), p("Arsenal"),           p("Fodder SBC"), p("750"),   p("1.100"),  pg("+295"),   po("Agora → 26/05")],
    [pl("Romelu Lukaku"),      p("84"), p("Napoli"),            p("Fodder SBC"), p("900"),   p("1.500"),  pg("+525"),   po("Agora → 26/05")],
    [pl("Hakan Çalhanoğlu"),   p("86"), p("Internazionale"),   p("Fodder SBC"), p("1.100"), p("2.000"),  pg("+800"),   po("Agora → 25/05")],
    [pl("Rubén Días"),         p("86"), p("Man. City"),         p("Fodder SBC"), p("1.200"), p("2.100"),  pg("+795"),   po("Agora → 26/05")],
    [pl("Jonathan Tah"),       p("87"), p("Bayern Munich"),     p("Fodder SBC"), p("1.400"), p("2.600"),  pg("+1.070"), po("Agora → 26/05")],
    [pl("Keira Walsh"),        p("85"), p("FC Barcelona"),      p("Fodder SBC"), p("800"),   p("1.400"),  pg("+530"),   po("Agora → 26/05")],
    [pl("Lucy Bronze"),        p("87"), p("FC Barcelona"),      p("Fodder SBC"), p("1.300"), p("2.400"),  pg("+980"),   po("Agora → 26/05")],

    # ── FODDER 88 rated para End of Era SBCs ────────────────────────────────
    [pl("Ann-Katrin Berger"),  p("88"), p("Chelsea"),           p("Fodder EoE"), p("1.800"), p("3.500"),  pg("+1.525"), po("Agora → 27/05")],
    [pl("Ada Hegerberg"),      p("87"), p("Lyon"),              p("Fodder SBC"), p("1.400"), p("2.700"),  pg("+1.165"), po("Agora → 27/05")],
    [pl("Patrik Schick"),      p("85"), p("Bayer Leverkusen"),  p("Fodder SBC"), p("850"),   p("1.600"),  pg("+670"),   po("Agora → 26/05")],
    [pl("S. Milinković-Savić"),p("85"), p("Al-Hilal"),          p("Fodder SBC"), p("800"),   p("1.500"),  pg("+625"),   po("Agora → 26/05")],

    # ── FLIPPING THURSDAY ────────────────────────────────────────────────────
    [pl("Casemiro TOTS"),      p("91"), p("Man. United"),       p("Thursday Flip"), p("14.000"), p("18.500"), pg("+3.575"), po("Compra 22h\nVende 5h")],
    [pl("Vinicius Jr TOTS"),   p("95"), p("Real Madrid"),       p("Thursday Flip"), p("38.000"), p("* Hold"), pr("* Alto risco"), po("Ver notas")],

    # ── EVOLUTION INVESTING ──────────────────────────────────────────────────
    [pl("Dele Alli"),          p("78"), p("Everton"),           p("Evolution"),  p("500"),   p("12.000"), pg("+10.900"), po("Curto prazo")],
    [pl("Kalvin Phillips"),    p("80"), p("Leeds Utd"),         p("Evolution"),  p("600"),   p("9.500"),  pg("+8.425"),  po("Curto prazo")],
]

col_widths = [4.0*cm, 1.1*cm, 3.2*cm, 2.3*cm, 1.7*cm, 1.7*cm, 1.6*cm, 2.2*cm]

main_table = Table(table_data, colWidths=col_widths, repeatRows=1)
main_table.setStyle(TableStyle([
    # Cabeçalho
    ("BACKGROUND",    (0,0),  (-1,0),  C_DARK_BLUE),
    ("TEXTCOLOR",     (0,0),  (-1,0),  C_WHITE),
    ("FONTNAME",      (0,0),  (-1,0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0,0),  (-1,0),  8),
    ("ALIGN",         (0,0),  (-1,0),  "CENTER"),
    ("VALIGN",        (0,0),  (-1,-1), "MIDDLE"),
    # Linhas alternadas
    *[("BACKGROUND", (0,i), (-1,i), C_GRAY if i % 2 == 0 else C_WHITE)
      for i in range(1, len(table_data))],
    # Separadores de grupo
    ("BACKGROUND", (0,1),  (-1,10),  colors.HexColor("#EFF8FF")),  # Fodder 83-87
    ("BACKGROUND", (0,11), (-1,14),  colors.HexColor("#FFF8E7")),  # Fodder 88
    ("BACKGROUND", (0,15), (-1,16),  colors.HexColor("#FFF0F0")),  # Thursday
    ("BACKGROUND", (0,17), (-1,18),  colors.HexColor("#F0FFF0")),  # Evolution
    # Bordas
    ("BOX",           (0,0),  (-1,-1), 1.5, C_DARK_BLUE),
    ("INNERGRID",     (0,0),  (-1,-1), 0.3, colors.HexColor("#CCCCCC")),
    ("LINEBELOW",     (0,0),  (-1,0),  1.5, C_GOLD),
    ("LINEBELOW",     (0,10), (-1,10), 1,   C_MID_BLUE),
    ("LINEBELOW",     (0,14), (-1,14), 1,   C_MID_BLUE),
    ("LINEBELOW",     (0,16), (-1,16), 1,   C_MID_BLUE),
    # Padding
    ("LEFTPADDING",   (0,0),  (-1,-1), 4),
    ("RIGHTPADDING",  (0,0),  (-1,-1), 4),
    ("TOPPADDING",    (0,0),  (-1,-1), 4),
    ("BOTTOMPADDING", (0,0),  (-1,-1), 4),
]))
story.append(main_table)
story.append(Spacer(1, 0.2*cm))

# Legenda
legend_items = [
    ("📘 Fodder SBC 83-87", C_LIGHT_BLUE),
    ("📙 Fodder EoE 87-88", colors.HexColor("#FFF8E7")),
    ("📕 Thursday Flip",    colors.HexColor("#FFF0F0")),
    ("📗 Evolution Invest", colors.HexColor("#F0FFF0")),
]
leg_data = [[Paragraph(f"<b>{txt}</b>", make_style(f"Leg{idx}", fontSize=7.5,
             textColor=C_DARK_BLUE, bold=True, alignment=TA_CENTER))
             for idx, (txt, _) in enumerate(legend_items)]]
leg_tbl = Table(leg_data, colWidths=[4.1*cm]*4)
leg_tbl.setStyle(TableStyle([
    *[("BACKGROUND", (i,0), (i,0), legend_items[i][1]) for i in range(4)],
    ("BOX",          (0,0), (-1,-1), 0.5, C_DARK_BLUE),
    ("INNERGRID",    (0,0), (-1,-1), 0.3, C_DARK_BLUE),
    ("TOPPADDING",   (0,0), (-1,-1), 3),
    ("BOTTOMPADDING",(0,0), (-1,-1), 3),
]))
story.append(leg_tbl)

story.append(Spacer(1, 0.15*cm))
story.append(Paragraph(
    "⚠ * <b>Vinicius Jr TOTS</b>: Preço alvo de compra de 38.000 coins representa 95% do budget. "
    "Recomendado apenas como posição especulativa se houver queda adicional. "
    "Margem líquida estimada: +3.600 coins se vendido a 42.000. Alto risco. Não recomendado para iniciantes.",
    s_disclaimer
))
story.append(Spacer(1, 0.3*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 3: ESTRATÉGIA DE TIMING
# ══════════════════════════════════════════════════════════════════════════════
story.extend(section_header("3. ESTRATÉGIA DE TIMING — QUANDO COMPRAR E QUANDO VENDER"))

timing_data = [
    [ph("ESTRATÉGIA"), ph("JANELA DE COMPRA"), ph("JANELA DE VENDA"), ph("RACIONAL")],
    [p("Fodder 83-84\n(Aspas, Modrić, Gordon...)"),
     p("23/05 20h-23h\n(mercado baixo)"),
     p("25-26/05 12h-18h\n(pico La Liga SBC)"),
     p("La Liga Upgrade expira 26/05\nDemanda alta antes do prazo")],
    [p("Fodder 85-86\n(Schick, Milinković, Çalha...)"),
     p("24/05 00h-08h\n(madrugada BR)"),
     p("25-26/05 15h-20h\n(EU peak hours)"),
     p("SBCs End of Era exigem\n85-87 rated. Pico de demanda")],
    [p("Fodder 86-87\n(Tah, Bronze, Hegerberg...)"),
     p("23/05 20h-23h\n(agora - mercado deprimido)"),
     p("25-27/05 17h-22h\n(recompensas + SBCs)"),
     p("87-rated escasso pós\nPremier League TOTS Upgrade")],
    [p("Fodder 88\n(Berger End of Era)"),
     p("23-24/05 qualquer hora\n(preço ainda baixo)"),
     p("25-27/05 18h-22h\n(SBCs End of Era ativos)"),
     p("End of Era Salah/Griezmann\nexige 88+ rated squads")],
    [p("Thursday Flip\n(TOTS 91 rated)"),
     p("28/05 (Quarta) 22h-02h\n(madrugada antes rewards)"),
     p("29/05 (Quinta) 10h-14h\n(pós-rewards EU)"),
     p("Rewards Day: demanda máxima\nJogadores pagam premium")],
    [p("Evolution Investing\n(Delle Alli, Phillips...)"),
     p("Agora (qualquer horário)\nPreços próximos a discard"),
     p("Quando nova Evolution\nfor anunciada (48-72h)"),
     p("Evoluções frequentes em\nfim de temporada valorizam\ncartas base baratas")],
]

timing_table = Table(timing_data, colWidths=[3.8*cm, 3.2*cm, 3.2*cm, 6.3*cm], repeatRows=1)
timing_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),  (-1,0),  C_MID_BLUE),
    ("TEXTCOLOR",     (0,0),  (-1,0),  C_WHITE),
    ("FONTNAME",      (0,0),  (-1,0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0,0),  (-1,-1), 8),
    ("ALIGN",         (0,0),  (-1,-1), "CENTER"),
    ("VALIGN",        (0,0),  (-1,-1), "MIDDLE"),
    *[("BACKGROUND", (0,i), (-1,i), C_GRAY if i % 2 == 0 else C_WHITE)
      for i in range(1, len(timing_data))],
    ("BOX",           (0,0),  (-1,-1), 1.5, C_MID_BLUE),
    ("INNERGRID",     (0,0),  (-1,-1), 0.3, colors.HexColor("#AAAAAA")),
    ("LINEBELOW",     (0,0),  (-1,0),  1.5, C_GOLD),
    ("LEFTPADDING",   (0,0),  (-1,-1), 5),
    ("RIGHTPADDING",  (0,0),  (-1,-1), 5),
    ("TOPPADDING",    (0,0),  (-1,-1), 5),
    ("BOTTOMPADDING", (0,0),  (-1,-1), 5),
]))
story.append(timing_table)
story.append(Spacer(1, 0.3*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 4: ALOCAÇÃO DO BUDGET
# ══════════════════════════════════════════════════════════════════════════════
story.extend(section_header("4. ALOCAÇÃO DO BUDGET — 40.000 COINS"))

budget_data = [
    [ph("ESTRATÉGIA"), ph("COINS ALOCADOS"), ph("% DO BUDGET"), ph("POSIÇÕES"), ph("RISCO")],
    [p("Fodder SBC 83-87\n(bulk buy 30-50 cartas)"),
     p("16.000"),
     p("40%"),
     p("~25 cartas\n83-84 rated"),
     p("BAIXO")],
    [p("Fodder 86-88\n(End of Era demand)"),
     p("12.000"),
     p("30%"),
     p("~8 cartas\n86-88 rated"),
     p("BAIXO-MÉDIO")],
    [p("Evolution Investing\n(Delle Alli, Phillips)"),
     p("6.000"),
     p("15%"),
     p("~8-10 cartas\n78-80 rated"),
     p("MÉDIO")],
    [p("Thursday Flip\n(TOTS 91 rated, 1 carta)"),
     p("4.000"),
     p("10%"),
     p("1 carta\n91 rated"),
     p("MÉDIO")],
    [p("Reserva Emergência\n(oportunidades snipe)"),
     p("2.000"),
     p("5%"),
     p("Flexível"),
     p("—")],
    [p("TOTAL"), p("40.000"), p("100%"), p(""), p("")],
]

budget_table = Table(budget_data, colWidths=[4.5*cm, 2.8*cm, 2.3*cm, 3.0*cm, 3.9*cm], repeatRows=1)
budget_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),  (-1,0),  C_DARK_BLUE),
    ("TEXTCOLOR",     (0,0),  (-1,0),  C_WHITE),
    ("FONTNAME",      (0,0),  (-1,0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0,0),  (-1,-1), 8),
    ("ALIGN",         (0,0),  (-1,-1), "CENTER"),
    ("VALIGN",        (0,0),  (-1,-1), "MIDDLE"),
    ("BACKGROUND",    (0,1),  (-1,1),  colors.HexColor("#EFF8FF")),
    ("BACKGROUND",    (0,2),  (-1,2),  colors.HexColor("#FFF8E7")),
    ("BACKGROUND",    (0,3),  (-1,3),  colors.HexColor("#F0FFF0")),
    ("BACKGROUND",    (0,4),  (-1,4),  colors.HexColor("#FFF0F0")),
    ("BACKGROUND",    (0,5),  (-1,5),  colors.HexColor("#F8F8F8")),
    ("BACKGROUND",    (0,6),  (-1,6),  C_DARK_BLUE),
    ("TEXTCOLOR",     (0,6),  (-1,6),  C_GOLD),
    ("FONTNAME",      (0,6),  (-1,6),  "Helvetica-Bold"),
    ("BOX",           (0,0),  (-1,-1), 1.5, C_DARK_BLUE),
    ("INNERGRID",     (0,0),  (-1,-1), 0.3, colors.HexColor("#AAAAAA")),
    ("LINEBELOW",     (0,0),  (-1,0),  1.5, C_GOLD),
    ("LINEABOVE",     (0,6),  (-1,6),  1.5, C_GOLD),
    ("LEFTPADDING",   (0,0),  (-1,-1), 5),
    ("RIGHTPADDING",  (0,0),  (-1,-1), 5),
    ("TOPPADDING",    (0,0),  (-1,-1), 5),
    ("BOTTOMPADDING", (0,0),  (-1,-1), 5),
]))
story.append(budget_table)
story.append(Spacer(1, 0.3*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 5: ESTIMATIVA DE RETORNO EM 48H
# ══════════════════════════════════════════════════════════════════════════════
story.extend(section_header("5. ESTIMATIVA DE RETORNO EM 48H"))

return_data = [
    [ph("ESTRATÉGIA"), ph("INVEST.\nINICIAL"), ph("RETORNO\nCONSERVADOR"), ph("LUCRO\nLÍQ. CONS."), ph("RETORNO\nOTIMISTA"), ph("LUCRO\nLÍQ. OTI.")],
    [p("Fodder SBC\n83-84 rated (25 cartas)"),
     p("16.000"),
     pg("20.000\n(+25%)"),
     pg("+3.200"),
     pg("24.000\n(+50%)"),
     pg("+6.800")],
    [p("Fodder 86-88\n(8 cartas)"),
     p("12.000"),
     pg("15.000\n(+25%)"),
     pg("+2.325"),
     pg("18.500\n(+54%)"),
     pg("+5.575")],
    [p("Evolution Investing\n(10 cartas baixo custo)"),
     p("6.000"),
     pg("9.000\n(+50%)"),
     pg("+2.550"),
     pg("14.000\n(+133%)"),
     pg("+7.300")],
    [p("Thursday Flip\n(1 carta TOTS 91)"),
     p("4.000"),
     pg("5.200\n(+30%)"),
     pg("+940"),
     pg("6.500\n(+63%)"),
     pg("+2.175")],
    [p("Reserva / Snipe"),
     p("2.000"),
     pg("2.400\n(+20%)"),
     pg("+380"),
     pg("3.200\n(+60%)"),
     pg("+1.040")],
    [p("TOTAL"),
     p("40.000"),
     pg("51.600"),
     pg("+9.195"),
     pg("66.200"),
     pg("+22.890")],
    [p("ROI Total"),
     p(""),
     pg("+23% em 48h"),
     p(""),
     pg("+57% em 48h"),
     p("")],
]

return_table = Table(return_data, colWidths=[3.8*cm, 2.0*cm, 2.4*cm, 2.0*cm, 2.4*cm, 2.0*cm], repeatRows=1)
return_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),  (-1,0),  C_DARK_BLUE),
    ("TEXTCOLOR",     (0,0),  (-1,0),  C_WHITE),
    ("FONTNAME",      (0,0),  (-1,0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0,0),  (-1,-1), 8),
    ("ALIGN",         (0,0),  (-1,-1), "CENTER"),
    ("VALIGN",        (0,0),  (-1,-1), "MIDDLE"),
    *[("BACKGROUND", (0,i), (-1,i), C_GRAY if i % 2 == 0 else C_WHITE)
      for i in range(1, len(return_data)-2)],
    ("BACKGROUND",    (0,6),  (-1,6),  C_DARK_BLUE),
    ("BACKGROUND",    (0,7),  (-1,7),  C_MID_BLUE),
    ("TEXTCOLOR",     (0,6),  (-1,6),  C_GOLD),
    ("TEXTCOLOR",     (0,7),  (-1,7),  C_GOLD),
    ("FONTNAME",      (0,6),  (-1,6),  "Helvetica-Bold"),
    ("FONTNAME",      (0,7),  (-1,7),  "Helvetica-Bold"),
    ("FONTSIZE",      (0,6),  (-1,-1), 9),
    ("BOX",           (0,0),  (-1,-1), 1.5, C_DARK_BLUE),
    ("INNERGRID",     (0,0),  (-1,-1), 0.3, colors.HexColor("#AAAAAA")),
    ("LINEBELOW",     (0,0),  (-1,0),  1.5, C_GOLD),
    ("LINEABOVE",     (0,6),  (-1,6),  1.5, C_GOLD),
    ("LEFTPADDING",   (0,0),  (-1,-1), 4),
    ("RIGHTPADDING",  (0,0),  (-1,-1), 4),
    ("TOPPADDING",    (0,0),  (-1,-1), 4),
    ("BOTTOMPADDING", (0,0),  (-1,-1), 4),
]))
story.append(return_table)
story.append(Spacer(1, 0.2*cm))

# Boxes conservador e otimista
cenarios_data = [[
    colored_box([
        Paragraph("🐢 CENÁRIO CONSERVADOR", make_style("CC", fontSize=10, textColor=C_MID_BLUE, bold=True, alignment=TA_CENTER)),
        Paragraph("Capital final: <b>49.195 coins</b>", make_style("CCv", fontSize=9, textColor=C_DARK_BLUE, alignment=TA_CENTER)),
        Paragraph("Lucro líquido: <b>+9.195 coins (+23%)</b>", make_style("CCl", fontSize=9, textColor=C_DARK_GREEN, bold=True, alignment=TA_CENTER)),
        Paragraph("Estimativa em 48h com mercado neutro, SBCs\ncom demanda moderada e vendas sem snipe.",
                  make_style("CCd", fontSize=8, textColor=C_DARK_GRAY, alignment=TA_CENTER)),
    ], bg_color=C_LIGHT_BLUE, border_color=C_MID_BLUE),
    colored_box([
        Paragraph("🚀 CENÁRIO OTIMISTA", make_style("CO", fontSize=10, textColor=C_DARK_GREEN, bold=True, alignment=TA_CENTER)),
        Paragraph("Capital final: <b>62.890 coins</b>", make_style("COv", fontSize=9, textColor=C_DARK_BLUE, alignment=TA_CENTER)),
        Paragraph("Lucro líquido: <b>+22.890 coins (+57%)</b>", make_style("COl", fontSize=9, textColor=C_DARK_GREEN, bold=True, alignment=TA_CENTER)),
        Paragraph("Com pico de demanda End of Era SBCs,\nnova Evolution anunciada e Thursday Flip\nperfeito em horário de pico.",
                  make_style("COd", fontSize=8, textColor=C_DARK_GRAY, alignment=TA_CENTER)),
    ], bg_color=colors.HexColor("#F0FFF0"), border_color=C_DARK_GREEN),
]]
cenarios_tbl = Table(cenarios_data, colWidths=[8.1*cm, 8.4*cm])
cenarios_tbl.setStyle(TableStyle([
    ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING",   (0,0), (-1,-1), 3),
    ("RIGHTPADDING",  (0,0), (-1,-1), 3),
    ("TOPPADDING",    (0,0), (-1,-1), 0),
    ("BOTTOMPADDING", (0,0), (-1,-1), 0),
]))
story.append(cenarios_tbl)
story.append(Spacer(1, 0.3*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 6: 8 REGRAS DE OURO DO TRADE
# ══════════════════════════════════════════════════════════════════════════════
story.extend(section_header("6. AS 8 REGRAS DE OURO DO TRADE"))

regras = [
    ("1", "NUNCA COMPRE NO PICO",
     "O hype de lançamento infla os preços em 30-80%. Espere 1-3 horas após qualquer anúncio "
     "para a euforia inicial cair e compre quando o mercado estabilizar. Paciência é lucro."),
    ("2", "DIVERSIFIQUE SEMPRE",
     "Não coloque mais de 30% do budget em uma única carta ou estratégia. "
     "Distribua entre fodder, flipping e evolution. Uma posição ruim não arruína o todo."),
    ("3", "CALCULE A TAXA DE 5%",
     "A EA cobra 5% em cada venda. Se comprou por 1.000, precisará vender por 1.053 só para empatar. "
     "Sempre calcule: Preço de Venda × 0,95 — Preço de Compra = Lucro Real."),
    ("4", "RESPEITE OS HORÁRIOS DE PICO",
     "Quinta (rewards), Sexta (18h-22h BST), Sábado e Domingo têm maior volume de compradores. "
     "Venda sempre nestes períodos. Compre de madrugada (menor concorrência = preços menores)."),
    ("5", "MONITORE DATAS DE EXPIRAÇÃO",
     "SBCs com prazo curto criam demanda artificial. A La Liga Upgrade expira em 26/05. "
     "Venda fodder 86-87 pelo menos 4 horas antes do prazo final para não perder o pico."),
    ("6", "USE LISTAS DE 1 HORA",
     "Ao vender, use duração de 1 hora nos horários de pico. Cartas visíveis por menos tempo "
     "tendem a ser compradas mais rápido por quem tem urgência de completar SBCs."),
    ("7", "NUNCA INVISTA EM CARTA QUE VOCÊ NÃO SABE VENDER",
     "Só compre um jogador se você tem certeza de quem quer esse item e por quê. "
     "'Essa carta vai subir' sem fundamento é especulação pura, não trading."),
    ("8", "GUARDE SEMPRE 10% DE RESERVA",
     "Mantenha ao menos 4.000 coins livres para oportunidades de snipe ou para cobrir "
     "quedas inesperadas. O mercado surpreende, e quem tem liquidez aproveita o caos."),
]

# Layout das regras em 2 colunas
for i in range(0, len(regras), 2):
    row_items = []
    for j in range(2):
        if i + j < len(regras):
            num, title, body = regras[i + j]
            inner = Table([
                [Paragraph(num, s_rule_num), Paragraph(title, s_rule_title)],
                ["", Paragraph(body, s_rule_body)],
            ], colWidths=[1.0*cm, 6.8*cm])
            inner.setStyle(TableStyle([
                ("VALIGN",        (0,0), (-1,-1), "TOP"),
                ("LEFTPADDING",   (0,0), (-1,-1), 4),
                ("RIGHTPADDING",  (0,0), (-1,-1), 4),
                ("TOPPADDING",    (0,0), (-1,-1), 4),
                ("BOTTOMPADDING", (0,0), (-1,-1), 2),
                ("SPAN",          (1,1), (1,1)),
                ("BACKGROUND",    (0,0), (-1,-1), C_GRAY),
                ("BOX",           (0,0), (-1,-1), 1, C_DARK_BLUE),
                ("LINEBELOW",     (0,0), (-1,0),  0.5, C_GOLD),
            ]))
            row_items.append(inner)
        else:
            row_items.append(Paragraph("", s_body))

    row_tbl = Table([row_items], colWidths=[8.1*cm, 8.4*cm])
    row_tbl.setStyle(TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",   (0,0), (-1,-1), 2),
        ("RIGHTPADDING",  (0,0), (-1,-1), 2),
        ("TOPPADDING",    (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ]))
    story.append(row_tbl)

story.append(Spacer(1, 0.3*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 7: ANÁLISE DE RISCOS
# ══════════════════════════════════════════════════════════════════════════════
story.extend(section_header("7. ANÁLISE DE RISCOS E MITIGAÇÕES"))

risks = [
    ("🟡 MÉDIO", "Queda de preços por excesso de oferta",
     "TOTS packs liberam muitas cartas 88-94 rated, podendo deprimir preços de fodder intermediário.",
     "Compre cartas 83-84 que nunca são obtidas em packs premium. Evite 88+ se os packs TOTS estiverem muito ativos."),
    ("🟡 MÉDIO", "SBCs cancelados ou alterados",
     "EA pode cancelar ou modificar SBCs, reduzindo a demanda por fodder específico.",
     "Diversifique em 3+ faixas de rating. Nunca dependa de uma única SBC para toda a posição."),
    ("🟢 BAIXO", "Variação de preço intra-dia",
     "Preços podem cair 10-15% entre o horário de compra e venda esperado.",
     "Venda em múltiplas listas, não tudo de uma vez. Use o horário de pico para liquidez."),
    ("🔴 ALTO", "Atualização de preço limite (price range)",
     "EA pode ajustar price ranges, bloqueando a venda acima de certo valor.",
     "Monitore FUTBIN antes de comprar. Prefira cartas sem histórico recente de price cap."),
    ("🟡 MÉDIO", "Snipe falho / cartas travadas no transfer",
     "Cartas compradas por engano acima do preço alvo ou que não vendem no prazo.",
     "Defina um preço máximo de compra e nunca exceda. Se não vender em 3 listagens, baixe o preço."),
]

risk_data = [[ph("NÍVEL"), ph("RISCO"), ph("DESCRIÇÃO"), ph("MITIGAÇÃO")]]
for level, risk, desc, mitigation in risks:
    risk_data.append([p(level), p(risk), Paragraph(desc, s_table_cell), Paragraph(mitigation, s_table_cell)])

risk_table = Table(risk_data, colWidths=[1.8*cm, 3.8*cm, 5.4*cm, 5.5*cm], repeatRows=1)
risk_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),  (-1,0),  C_DARK_BLUE),
    ("TEXTCOLOR",     (0,0),  (-1,0),  C_WHITE),
    ("FONTNAME",      (0,0),  (-1,0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0,0),  (-1,-1), 7.5),
    ("ALIGN",         (0,0),  (-1,-1), "CENTER"),
    ("VALIGN",        (0,0),  (-1,-1), "MIDDLE"),
    *[("BACKGROUND", (0,i), (-1,i), C_GRAY if i % 2 == 0 else C_WHITE)
      for i in range(1, len(risk_data))],
    ("BOX",           (0,0),  (-1,-1), 1.5, C_DARK_BLUE),
    ("INNERGRID",     (0,0),  (-1,-1), 0.3, colors.HexColor("#AAAAAA")),
    ("LINEBELOW",     (0,0),  (-1,0),  1.5, C_GOLD),
    ("LEFTPADDING",   (0,0),  (-1,-1), 4),
    ("RIGHTPADDING",  (0,0),  (-1,-1), 4),
    ("TOPPADDING",    (0,0),  (-1,-1), 4),
    ("BOTTOMPADDING", (0,0),  (-1,-1), 4),
]))
story.append(risk_table)
story.append(Spacer(1, 0.3*cm))

# ══════════════════════════════════════════════════════════════════════════════
# DISCLAIMER
# ══════════════════════════════════════════════════════════════════════════════
story.append(HRFlowable(width="100%", thickness=1, color=C_DARK_GRAY, spaceBefore=4, spaceAfter=6))

disclaimer_box = colored_box([
    Paragraph("⚠ DISCLAIMER", make_style("DiscHdr", fontSize=9, textColor=C_DARK_GRAY, bold=True)),
    Paragraph(
        "Este relatório é produzido por um agente de análise de mercado automatizado com base em dados "
        "públicos coletados de FUTBIN, FUT.GG, TeamGullit, Football Gaming Zone, Sportskeeda, e outras fontes "
        "especializadas em EA FC 26 Ultimate Team. Os preços indicados são estimativas baseadas em tendências "
        "históricas e eventos ativos no momento da análise — não constituem garantia de lucro.",
        s_disclaimer
    ),
    Paragraph(
        "O mercado de EA FC 26 é altamente volátil e sujeito a mudanças imediatas decorrentes de decisões "
        "da Electronic Arts, como lançamento inesperado de promoções, alteração de price ranges, ou "
        "cancelamento de SBCs. Invista apenas o que pode perder sem comprometer sua experiência de jogo. "
        "Toda a responsabilidade pelas decisões de trading é exclusivamente do usuário final.",
        s_disclaimer
    ),
    Paragraph(
        f"Gerado em: {REPORT_DATE_UTC}  |  Fonte: Análise automatizada de mercado FUT  |  "
        "Dados: FUTBIN · FUT.GG · TeamGullit · FootballGamingZone · Sportskeeda",
        make_style("DiscFt", fontSize=7, textColor=C_DARK_GRAY, alignment=TA_CENTER)
    ),
], bg_color=colors.HexColor("#F9F9F9"), border_color=C_DARK_GRAY)
story.append(disclaimer_box)

# ── Gerar PDF ──────────────────────────────────────────────────────────────────
doc.build(story)
print(f"✅ PDF gerado com sucesso: {OUTPUT_PATH}")
