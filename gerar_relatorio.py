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
from reportlab.lib.colors import HexColor
import os

# ── Configuração ──────────────────────────────────────────────────────────────
DATA_HORA = "22/05/2026 08:03"
FILENAME  = "relatorio-trading-2026-05-22-08h.pdf"
OUTPUT    = os.path.join(os.path.dirname(__file__), FILENAME)

# Paleta de cores EA FC / Ultimate Team
C_VERDE      = HexColor("#00D4AA")
C_VERDE_ESC  = HexColor("#007A62")
C_DOURADO    = HexColor("#FFD700")
C_LARANJA    = HexColor("#FF6B35")
C_CINZA_ESC  = HexColor("#1A1A2E")
C_CINZA_MED  = HexColor("#2D2D44")
C_CINZA_CLAR = HexColor("#4A4A6A")
C_TEXTO      = HexColor("#F0F0F0")
C_TEXTO_ESC  = HexColor("#1A1A2E")
C_BRANCO     = colors.white
C_VERMELHO   = HexColor("#FF4444")

PAGE_W, PAGE_H = A4

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=1.8*cm,
    leftMargin=1.8*cm,
    topMargin=2*cm,
    bottomMargin=2*cm,
)

styles = getSampleStyleSheet()

# ── Estilos customizados ──────────────────────────────────────────────────────
def s(name, **kw):
    base = kw.pop("parent", "Normal")
    st = ParagraphStyle(name=name, parent=styles[base], **kw)
    return st

sTitle   = s("sTitle",   fontSize=26, textColor=C_VERDE,   spaceAfter=4,
             alignment=TA_CENTER, fontName="Helvetica-Bold", leading=30)
sSubT    = s("sSubT",    fontSize=13, textColor=C_DOURADO, spaceAfter=2,
             alignment=TA_CENTER, fontName="Helvetica-Bold")
sDate    = s("sDate",    fontSize=10, textColor=C_CINZA_CLAR, spaceAfter=12,
             alignment=TA_CENTER, fontName="Helvetica")
sH1      = s("sH1",      fontSize=14, textColor=C_VERDE,   spaceBefore=14,
             spaceAfter=6, fontName="Helvetica-Bold")
sH2      = s("sH2",      fontSize=11, textColor=C_DOURADO, spaceBefore=10,
             spaceAfter=4, fontName="Helvetica-Bold")
sBody    = s("sBody",    fontSize=9,  textColor=C_TEXTO_ESC, spaceAfter=4,
             fontName="Helvetica", leading=14, alignment=TA_JUSTIFY)
sBullet  = s("sBullet",  fontSize=9,  textColor=C_TEXTO_ESC, spaceAfter=3,
             fontName="Helvetica", leading=13, leftIndent=14)
sSmall   = s("sSmall",   fontSize=7.5, textColor=HexColor("#666666"),
             fontName="Helvetica", leading=11, spaceAfter=3, alignment=TA_JUSTIFY)
sTag     = s("sTag",     fontSize=9,  textColor=C_VERDE_ESC,
             fontName="Helvetica-Bold", alignment=TA_CENTER)
sAlert   = s("sAlert",   fontSize=9,  textColor=C_LARANJA,
             fontName="Helvetica-Bold", spaceAfter=4)
sGold    = s("sGold",    fontSize=10, textColor=C_DOURADO,
             fontName="Helvetica-Bold", spaceBefore=6, spaceAfter=3)

# ── Helpers ───────────────────────────────────────────────────────────────────
def hr(color=C_VERDE, thickness=1):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceAfter=6, spaceBefore=4)

def section_title(text):
    return [Spacer(1, 6), Paragraph(text, sH1), hr()]

def spacer(h=0.3):
    return Spacer(1, h*cm)

# ── Conteúdo ──────────────────────────────────────────────────────────────────
story = []

# ── CABEÇALHO ─────────────────────────────────────────────────────────────────
story += [
    spacer(0.2),
    Paragraph("⚽ EA FC 26 ULTIMATE TEAM", sTitle),
    Paragraph("RELATÓRIO DE TRADING DIÁRIO", sSubT),
    Paragraph(f"Gerado em: {DATA_HORA} UTC", sDate),
    hr(C_VERDE, 2),
    spacer(0.3),
]

# ── EVENTO ATIVO ──────────────────────────────────────────────────────────────
story += section_title("📣 CONTEXTO DO MERCADO — EVENTO ATIVO")

evento_data = [
    ["PROMO ATIVA", "DETALHES", "IMPACTO NO MERCADO"],
    ["ULTIMATE TOTS\n(Team of the Season)",
     "Lançamento: 22/05 às 19h BRT\nDuração: até 29/05/2026\nMelhor promo do ano — cartas\ndas semanas anteriores reunidas",
     "📦 Abertura massiva de packs\n📉 Queda de preço em fodder 83–88\n📈 Alta demanda por SBC fodder\napós End of Era SBCs"],
    ["END OF ERA SBCs\n(Em breve)",
     "Jogadores: Salah (95), Griezmann (94),\nBernardo Silva (93), Goretzka (91),\nRobertson (91) — lançamento iminente",
     "🔥 Demanda explosiva por fodder\n85–88 rated quando os SBCs\ncaírem (janela de 24–48h)"],
    ["EVOLUTION CARDS\n(Ativo)",
     "TOTS Evolutions ativas: max 90 OVR\nJogadores 78–80 elegíveis para free\nou low-cost evolutions",
     "📊 Comprar Evo-eligible players\nbarato agora, vender pós-upgrade\ncomo fodder 86–88"],
]

evento_style = TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0),  C_CINZA_ESC),
    ("TEXTCOLOR",     (0, 0), (-1, 0),  C_VERDE),
    ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 0), (-1, 0),  9),
    ("ALIGN",         (0, 0), (-1, 0),  "CENTER"),
    ("BACKGROUND",    (0, 1), (-1, -1), HexColor("#F8F8F8")),
    ("FONTNAME",      (0, 1), (0, -1),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 1), (-1, -1), 8),
    ("TEXTCOLOR",     (0, 1), (0, -1),  C_CINZA_ESC),
    ("ALIGN",         (0, 0), (-1, -1), "LEFT"),
    ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS",(0, 1), (-1, -1), [colors.white, HexColor("#EEF8F5")]),
    ("GRID",          (0, 0), (-1, -1), 0.5, HexColor("#CCCCCC")),
    ("TOPPADDING",    (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING",   (0, 0), (-1, -1), 8),
])

evento_table = Table(
    evento_data,
    colWidths=[4.2*cm, 7.5*cm, 6.5*cm],
    style=evento_style,
)
story += [evento_table, spacer(0.4)]

# ── TENDÊNCIA GERAL ───────────────────────────────────────────────────────────
story += [
    Paragraph("📊 Tendência Geral do Mercado", sH2),
    Paragraph(
        "Com o lançamento do <b>Ultimate TOTS</b> hoje (22/05), o mercado entrou em modo de "
        "alta volatilidade. Há abertura massiva de packs, o que aumenta a oferta de cartas "
        "83–88 rated no mercado e derruba preços. Este é o <b>melhor momento do ciclo para "
        "comprar fodder barato</b>. A demanda irá subir quando os <b>End of Era SBCs</b> (Salah, "
        "Griezmann, Bernardo Silva) forem lançados nas próximas 24–48h — criando a janela de lucro.",
        sBody
    ),
    Paragraph(
        "⚡ <b>Janela crítica:</b> Comprar fodder 85–88 hoje (08h–16h BRT) enquanto packs ainda "
        "inundam o mercado, e vender quando o primeiro End of Era SBC cair.",
        sAlert
    ),
    spacer(0.3),
]

# ── TABELA DE OPORTUNIDADES ───────────────────────────────────────────────────
story += section_title("💰 CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA")

story += [
    Paragraph(
        "Todos os preços em coins. Margem líquida já descontando a taxa EA de 5% sobre a venda. "
        "Horizonte: lucro esperado nas próximas 24–48h.",
        sSmall
    ),
    spacer(0.2),
]

# Cabeçalho da tabela principal
header = [
    Paragraph("<b>#</b>", sTag),
    Paragraph("<b>JOGADOR</b>", sTag),
    Paragraph("<b>RAT</b>", sTag),
    Paragraph("<b>CLUBE</b>", sTag),
    Paragraph("<b>COMPRA\n(máx)</b>", sTag),
    Paragraph("<b>VENDA\n(alvo)</b>", sTag),
    Paragraph("<b>MARGEM\nLÍQ. (5%)</b>", sTag),
    Paragraph("<b>ESTRATÉGIA</b>", sTag),
]

def marg(buy, sell, qty=1):
    net = sell * 0.95 - buy
    pct = (net / buy) * 100
    return f"+{int(net):,}c\n({pct:.0f}%)"

players = [
    # (#, nome, rating, clube, buy_max, sell_target, estrategia)
    (1, "Hakan Çalhanoğlu", 86, "Inter Milan",      1_500, 2_900, "SBC Fodder — End of Era"),
    (2, "Romelu Lukaku",    84, "Napoli",             800, 1_700, "SBC Fodder 84 genérico"),
    (3, "Rúben Dias",       86, "Manchester City",  1_400, 2_700, "SBC Fodder PL demand"),
    (4, "Brian Mbeumo",     85, "Brentford",         1_600, 2_900, "SBC Fodder — alta liga"),
    (5, "Keira Walsh",      85, "Man City (fem.)",  1_500, 2_700, "SBC Fodder TOTS liga F"),
    (6, "Lautaro Martínez", 87, "Inter Milan",      3_200, 5_800, "Fodder 87 para End of Era"),
    (7, "João Cancelo",     86, "Barcelona",        1_600, 3_000, "Fodder Liga — demanda alta"),
    (8, "Théo Hernández",   86, "AC Milan",         1_700, 3_100, "Alta liquidez Série A/WC"),
    (9, "Rodri",            87, "Manchester City",  3_500, 6_200, "Fodder 87 Premier League"),
   (10, "Alexia Putellas",  87, "Barcelona (fem.)", 2_800, 5_200, "Evo candidate + SBC fodder"),
]

rows = [header]
for p in players:
    idx, nome, rating, clube, buy, sell, strat = p
    net = sell * 0.95 - buy
    pct = (net / buy) * 100
    sign = "▲" if net > 0 else "▼"
    marg_str = f"{sign} +{int(net):,}c\n({pct:.0f}%)"
    rows.append([
        Paragraph(str(idx), sTag),
        Paragraph(f"<b>{nome}</b>", ParagraphStyle("pb", fontSize=8, fontName="Helvetica-Bold",
                  textColor=C_CINZA_ESC, leading=11)),
        Paragraph(str(rating), ParagraphStyle("pr", fontSize=9, fontName="Helvetica-Bold",
                  textColor=C_VERDE_ESC, alignment=TA_CENTER, leading=12)),
        Paragraph(clube, ParagraphStyle("pc", fontSize=7.5, fontName="Helvetica",
                  textColor=C_CINZA_CLAR, leading=11)),
        Paragraph(f"{buy:,}", ParagraphStyle("pp", fontSize=8.5, fontName="Helvetica-Bold",
                  textColor=C_VERMELHO, alignment=TA_CENTER, leading=11)),
        Paragraph(f"{sell:,}", ParagraphStyle("ps", fontSize=8.5, fontName="Helvetica-Bold",
                  textColor=C_VERDE_ESC, alignment=TA_CENTER, leading=11)),
        Paragraph(marg_str, ParagraphStyle("pm", fontSize=8, fontName="Helvetica-Bold",
                  textColor=C_VERDE_ESC, alignment=TA_CENTER, leading=12)),
        Paragraph(strat, ParagraphStyle("pst", fontSize=7.5, fontName="Helvetica",
                  textColor=C_CINZA_ESC, leading=11)),
    ])

col_w = [0.7*cm, 3.5*cm, 1*cm, 3.2*cm, 1.8*cm, 1.8*cm, 2*cm, 3.5*cm]
tbl_style = TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0),  C_CINZA_ESC),
    ("TEXTCOLOR",     (0, 0), (-1, 0),  C_VERDE),
    ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 0), (-1, 0),  8),
    ("ALIGN",         (0, 0), (-1, 0),  "CENTER"),
    ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS",(0, 1), (-1, -1), [colors.white, HexColor("#EEF8F5")]),
    ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
    ("TOPPADDING",    (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING",   (0, 0), (-1, -1), 5),
])

main_table = Table(rows, colWidths=col_w, style=tbl_style, repeatRows=1)
story += [main_table, spacer(0.3)]

# ── NOTA DE QUANTIDADE ────────────────────────────────────────────────────────
story += [
    Paragraph(
        "💡 <b>Alocação sugerida com budget de 40.000 coins:</b> Distribuir em 3–4 tipos de "
        "fodder diferentes (ex: 15 cartas 86-rated × 1.500 = 22.500c | 5 cartas 87-rated × "
        "3.500 = 17.500c). Nunca concentrar 100% em um único jogador.",
        sBody
    ),
    spacer(0.3),
]

# ── ESTRATÉGIA DE TIMING ──────────────────────────────────────────────────────
story += section_title("⏰ ESTRATÉGIA DE TIMING — QUANDO COMPRAR E VENDER")

timing_data = [
    ["HORÁRIO / JANELA", "AÇÃO", "MOTIVO"],
    ["08h–14h BRT\n(Hoje — 22/05)",
     "🛒 COMPRAR fodder 85–87\nPreços mínimos no mercado",
     "Pack openings inundando o\nmercado após TOTS launch"],
    ["14h–18h BRT\n(Hoje — 22/05)",
     "✅ Finalizar compras\nMonitorar anúncios de SBCs",
     "EA anuncia novos SBCs no\nmid-afternoon (hora UK)"],
    ["19h–22h BRT\n(Hoje — 22/05)",
     "📣 Acompanhar lançamento\nUltimate TOTS + End of Era",
     "Confirmação dos SBCs\ndispara demanda por fodder"],
    ["22h–02h BRT\n(22→23/05)",
     "📤 VENDER fodder comprado\nse End of Era SBC lançado",
     "Demanda máxima: traders\nbuscam fodder às pressas"],
    ["Quinta-feira\n(28/05 — refresh)",
     "🔄 Novo ciclo: comprar\nfodder novo na baixa",
     "Refresh de recompensas\nWL inunda mercado novamente"],
]

timing_style = TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0),  C_CINZA_ESC),
    ("TEXTCOLOR",     (0, 0), (-1, 0),  C_DOURADO),
    ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 0), (-1, 0),  9),
    ("ALIGN",         (0, 0), (-1, 0),  "CENTER"),
    ("ROWBACKGROUNDS",(0, 1), (-1, -1), [colors.white, HexColor("#FFFBEE")]),
    ("FONTNAME",      (0, 1), (0, -1),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 1), (-1, -1), 8.5),
    ("TEXTCOLOR",     (0, 1), (0, -1),  C_CINZA_ESC),
    ("ALIGN",         (0, 0), (-1, -1), "LEFT"),
    ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ("GRID",          (0, 0), (-1, -1), 0.5, HexColor("#CCCCCC")),
    ("TOPPADDING",    (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING",   (0, 0), (-1, -1), 8),
])

timing_table = Table(
    timing_data,
    colWidths=[3.5*cm, 6*cm, 8.7*cm],
    style=timing_style,
)
story += [timing_table, spacer(0.3)]

# ── ESTIMATIVA DE RETORNO 48H ─────────────────────────────────────────────────
story += section_title("📈 ESTIMATIVA DE RETORNO EM 48H")

story += [
    Paragraph("Cenário base: budget de 40.000 coins — SBC Fodder Flipping (85–87 rated)", sH2),
    spacer(0.2),
]

retorno_data = [
    ["CENÁRIO", "ESTRATÉGIA", "BUDGET\nINVESTIDO", "RETORNO\nBRUTO", "TAXA\nEA (5%)", "LUCRO\nLÍQUIDO", "ROI"],
    ["🐢 CONSERVADOR",
     "10x cartas 86 (@1.500) + 5x cartas 87 (@3.500)\nVenda com +60% de markup médio",
     "32.500", "52.000", "2.600", "+16.900", "+52%"],
    ["⚡ OTIMISTA",
     "20x cartas 86 (@1.500) + 5x cartas 87 (@3.000)\nEnd of Era SBC lança + preços sobem 120%",
     "45.000*", "85.500", "4.275", "+36.225", "+80%"],
    ["💎 MOONSHOT",
     "Comprar 5x cartas 87 (@3.000) + hold até SBC\npremium (Salah-level) — venda em pico",
     "15.000", "39.000", "1.950", "+22.050", "+147%"],
]

ret_style = TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0),  C_CINZA_ESC),
    ("TEXTCOLOR",     (0, 0), (-1, 0),  C_VERDE),
    ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 0), (-1, 0),  8),
    ("ALIGN",         (0, 0), (-1, 0),  "CENTER"),
    ("ROWBACKGROUNDS",(0, 1), (-1, -1), [HexColor("#F0FFF8"), HexColor("#FFF8E8"), HexColor("#F8F0FF")]),
    ("FONTNAME",      (0, 1), (0, -1),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 1), (-1, -1), 8),
    ("ALIGN",         (1, 0), (-1, -1), "CENTER"),
    ("ALIGN",         (1, 1), (1, -1),  "LEFT"),
    ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
    ("TOPPADDING",    (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    # Highlight ROI column
    ("BACKGROUND",    (-1, 1), (-1, 1),  HexColor("#D4EDDA")),
    ("BACKGROUND",    (-1, 2), (-1, 2),  HexColor("#FFF3CD")),
    ("BACKGROUND",    (-1, 3), (-1, 3),  HexColor("#E8D5FF")),
    ("FONTNAME",      (-1, 1), (-1, -1), "Helvetica-Bold"),
    ("TEXTCOLOR",     (-1, 1), (-1, 1),  C_VERDE_ESC),
    ("TEXTCOLOR",     (-1, 2), (-1, 2),  HexColor("#856404")),
    ("TEXTCOLOR",     (-1, 3), (-1, 3),  HexColor("#6F42C1")),
])

ret_table = Table(
    retorno_data,
    colWidths=[2.8*cm, 6.2*cm, 2.2*cm, 2.2*cm, 2.0*cm, 2.2*cm, 1.6*cm],
    style=ret_style,
)
story += [
    ret_table,
    Paragraph("* Cenário otimista usa ligeiramente mais coins (até 45k); possível se o budget for reforçado.", sSmall),
    spacer(0.4),
]

# ── 8 REGRAS DE OURO ─────────────────────────────────────────────────────────
story += section_title("🏆 8 REGRAS DE OURO DO TRADE")

regras = [
    ("1", "Compre na baixa — venda na alta",
     "Compre fodder nas primeiras horas após pack openings massivos (lançamentos de promo). "
     "Venda quando um SBC popular for anunciado e a demanda disparar. Nunca inverta a ordem."),
    ("2", "Nunca concentre 100% do budget",
     "Diversifique em pelo menos 3 tipos de cartas diferentes. Uma falha de SBC (EA cancela) "
     "não pode secar todo seu capital. Máximo 40% por tipo de carta."),
    ("3", "Respeite a taxa de 5% da EA",
     "Toda venda perde 5%. Se você compra a 2.000 e vende a 2.100, você perde 105 coins. "
     "Calcule sempre margem mínima de 15% bruto para ter lucro real."),
    ("4", "Defina preço de saída antes de comprar",
     "Antes de comprar qualquer carta, anote: preço de compra, preço alvo de venda, e preço "
     "de stop-loss (quanto você aceita perder). Disciplina > emoção."),
    ("5", "Monitore o mercado nos horários certos",
     "Mercado mais barato: madrugada BRT (03h–08h). Mercado mais caro / maior liquidez: "
     "19h–23h BRT. Compre quando todos dormem, venda quando todos jogam."),
    ("6", "Fuja de hype sem fundamento",
     "Se um jogador 'vai explodir' sem SBC confirmado, é armadilha. Só invista quando há "
     "catalisador real: SBC lançado, promo confirmada, ou evento de upgrade anunciado."),
    ("7", "Use o Thursday Flip",
     "Toda quinta-feira, recompensas do Weekend League são distribuídas, inundando o mercado. "
     "Compre fodder na quinta de tarde/noite, venda na sexta ou no próximo ciclo de SBC."),
    ("8", "Registre todas as operações",
     "Anote cada compra e venda: jogador, preço de entrada, preço de saída, lucro/prejuízo. "
     "Em 7 dias você vai identificar quais cartas rendem mais e ajustar sua estratégia."),
]

for r in regras:
    num, titulo, desc = r
    story += [
        KeepTogether([
            Paragraph(
                f'<font color="#00D4AA"><b>Regra {num}:</b></font> <b>{titulo}</b>',
                ParagraphStyle("rh", fontSize=10, fontName="Helvetica-Bold",
                               textColor=C_CINZA_ESC, spaceBefore=8, spaceAfter=2, leading=14)
            ),
            Paragraph(desc, sBody),
        ])
    ]

story += [spacer(0.4)]

# ── DISCLAIMER ────────────────────────────────────────────────────────────────
story += [
    hr(C_CINZA_CLAR, 0.5),
    spacer(0.2),
    Paragraph("⚠️ DISCLAIMER", sH2),
    Paragraph(
        "Este relatório é gerado para fins informativos e educacionais sobre trading no EA FC 26 "
        "Ultimate Team. Os preços indicados são estimativas baseadas em dados de mercado públicos "
        "(futbin.com, fut.gg, fontes da comunidade) no momento da geração do relatório e podem "
        "variar significativamente. Nenhuma operação de trading garante lucro. O mercado do FUT é "
        "altamente volátil e influenciado por decisões da EA Sports que podem não ser antecipáveis. "
        "Opere apenas com coins que você pode se dar ao luxo de perder. Este documento não tem "
        "qualquer afiliação com a EA Sports ou a Electronic Arts Inc.",
        sSmall
    ),
    spacer(0.1),
    Paragraph(
        f"Relatório gerado automaticamente | {DATA_HORA} UTC | EA FC 26 Trading Bot v2.6",
        ParagraphStyle("footer", fontSize=7, textColor=HexColor("#AAAAAA"),
                       alignment=TA_CENTER, fontName="Helvetica")
    ),
]

# ── BUILD PDF ─────────────────────────────────────────────────────────────────
doc.build(story)
print(f"✅ PDF gerado: {OUTPUT}")
