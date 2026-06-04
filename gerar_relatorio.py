#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak

FILENAME = "relatorio-trading-2026-06-04-20h.pdf"
DATA_HORA = "04/06/2026 20:06"

# ── Cores
VERDE_ESCURO  = colors.HexColor("#1a6b3c")
VERDE_MEDIO   = colors.HexColor("#2d9c5e")
VERDE_CLARO   = colors.HexColor("#d4edda")
AMARELO       = colors.HexColor("#ffc107")
AMARELO_CLARO = colors.HexColor("#fff8e1")
CINZA_ESCURO  = colors.HexColor("#343a40")
CINZA_CLARO   = colors.HexColor("#f8f9fa")
BRANCO        = colors.white
VERMELHO      = colors.HexColor("#dc3545")
AZUL          = colors.HexColor("#0d6efd")
LARANJA       = colors.HexColor("#fd7e14")

doc = SimpleDocTemplate(
    FILENAME,
    pagesize=A4,
    rightMargin=1.8*cm, leftMargin=1.8*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

W = A4[0] - 3.6*cm

styles = getSampleStyleSheet()

titulo_style = ParagraphStyle(
    "Titulo", parent=styles["Title"],
    fontSize=22, textColor=BRANCO, alignment=TA_CENTER,
    spaceAfter=4, fontName="Helvetica-Bold"
)
subtitulo_style = ParagraphStyle(
    "Subtitulo", parent=styles["Normal"],
    fontSize=11, textColor=AMARELO, alignment=TA_CENTER,
    spaceAfter=2, fontName="Helvetica-Bold"
)
data_style = ParagraphStyle(
    "Data", parent=styles["Normal"],
    fontSize=10, textColor=BRANCO, alignment=TA_CENTER,
    fontName="Helvetica"
)
secao_style = ParagraphStyle(
    "Secao", parent=styles["Heading1"],
    fontSize=13, textColor=BRANCO, alignment=TA_LEFT,
    spaceAfter=6, spaceBefore=14, fontName="Helvetica-Bold",
    backColor=VERDE_ESCURO, leftIndent=-4, rightIndent=-4,
    borderPad=6
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"],
    fontSize=9.5, textColor=CINZA_ESCURO, alignment=TA_JUSTIFY,
    spaceAfter=5, leading=14, fontName="Helvetica"
)
bullet_style = ParagraphStyle(
    "Bullet", parent=styles["Normal"],
    fontSize=9.5, textColor=CINZA_ESCURO, alignment=TA_LEFT,
    spaceAfter=3, leading=13, leftIndent=14, fontName="Helvetica",
    bulletIndent=4
)
aviso_style = ParagraphStyle(
    "Aviso", parent=styles["Normal"],
    fontSize=8.5, textColor=colors.HexColor("#6c757d"),
    alignment=TA_JUSTIFY, leading=12, fontName="Helvetica-Oblique"
)
regra_titulo_style = ParagraphStyle(
    "RegraTitulo", parent=styles["Normal"],
    fontSize=10, textColor=VERDE_ESCURO, alignment=TA_LEFT,
    spaceAfter=1, fontName="Helvetica-Bold"
)
regra_body_style = ParagraphStyle(
    "RegraBody", parent=styles["Normal"],
    fontSize=9, textColor=CINZA_ESCURO, alignment=TA_JUSTIFY,
    spaceAfter=6, leading=12, fontName="Helvetica"
)

elements = []

# ══════════════════════════════════════════════════════════
# CABEÇALHO
# ══════════════════════════════════════════════════════════
header_data = [[
    Paragraph("EA FC 26 ULTIMATE TEAM", titulo_style),
]]
header_table = Table([[
    Paragraph("EA FC 26 ULTIMATE TEAM", titulo_style),
]], colWidths=[W])
header_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), VERDE_ESCURO),
    ("TOPPADDING",    (0,0), (-1,-1), 18),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ("RIGHTPADDING",  (0,0), (-1,-1), 10),
    ("ROUNDEDCORNERS",(0,0), (-1,-1), [8,8,0,0]),
]))
elements.append(header_table)

sub_data = [
    [Paragraph("RELATÓRIO DE TRADING — ANÁLISE DE MERCADO", subtitulo_style)],
    [Paragraph(f"Gerado em: {DATA_HORA} UTC", data_style)],
    [Paragraph("Budget: 40.000 coins | Plataforma: Console (PS/Xbox)", data_style)],
]
sub_table = Table(sub_data, colWidths=[W])
sub_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), VERDE_MEDIO),
    ("TOPPADDING",    (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ("RIGHTPADDING",  (0,0), (-1,-1), 10),
    ("ROUNDEDCORNERS",(0,0), (-1,-1), [0,0,8,8]),
]))
elements.append(sub_table)
elements.append(Spacer(1, 12))

# ══════════════════════════════════════════════════════════
# 1. CONTEXTO DE MERCADO
# ══════════════════════════════════════════════════════════
elements.append(Paragraph(" 1.  CONTEXTO DO MERCADO — MOMENTO ATUAL", secao_style))
elements.append(Spacer(1, 4))

ctx_box_data = [[
    Paragraph(
        "<b>EVENTO ATIVO: Festival of Football — Season 8</b><br/>"
        "O maior evento do calendário EA FC 26 está prestes a começar. "
        "A promo <b>Path to Glory (PTG) — Team 1</b> entra em packs em "
        "<b>05/06/2026 às 19h00 BST (15h00 BRT)</b>, marcando o início "
        "do Festival of Football temático da Copa do Mundo 2026 "
        "(EUA / Canadá / México, início: 11 de junho).",
        body_style
    )
]]
ctx_box = Table(ctx_box_data, colWidths=[W - 16])
ctx_box.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), AMARELO_CLARO),
    ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ("RIGHTPADDING",  (0,0), (-1,-1), 10),
    ("TOPPADDING",    (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("BOX",           (0,0), (-1,-1), 1.5, AMARELO),
    ("ROUNDEDCORNERS",(0,0), (-1,-1), [6,6,6,6]),
]))
elements.append(ctx_box)
elements.append(Spacer(1, 8))

ctx_items = [
    ("<b>Cartas PTG dinâmicas:</b>", "Recebem upgrades de overall e PlayStyles conforme o selecionado do jogador avança na Copa do Mundo 2026."),
    ("<b>Novos ICONs:</b>", "Mario Kempes e Rivelino chegam na segunda fase da promo (Greats of the Game, a partir de 19/06)."),
    ("<b>Token Store:</b>", "Novo sistema de tokens — colete via objetivos, SBCs e gameplay para resgatar cartas promo específicas."),
    ("<b>10x 84+ Upgrade SBC:</b>", "Disponível até 12/06/2026 às 18h UTC. Custo médio: ~15.750 coins (console). Boa relação custo-benefício com fodder barato."),
    ("<b>83+ Player Pick SBC:</b>", "Disponível até 08/06/2026. Custo ~2.200 coins por conclusão. Repetível — ideal para grindar com fodder 83-rated."),
    ("<b>Tendência geral:</b>", "Abertura massiva de packs amanhã → aumento de supply → queda nos preços de 83-86 rated. HOJE à noite é o momento de comprar fodder ANTES da queda de amanhã."),
]

for bold_part, normal_part in ctx_items:
    elements.append(Paragraph(
        f"• {bold_part} {normal_part}", bullet_style
    ))
elements.append(Spacer(1, 4))

# ══════════════════════════════════════════════════════════
# 2. OPORTUNIDADES — TABELA DE CARTAS
# ══════════════════════════════════════════════════════════
elements.append(Paragraph(" 2.  OPORTUNIDADES DE COMPRA — CARTAS RECOMENDADAS", secao_style))
elements.append(Spacer(1, 4))

elements.append(Paragraph(
    "Todas as margens líquidas já consideram a taxa EA de <b>5%</b> sobre o valor de venda. "
    "Preços estimados com base no mercado de console (PS5/Xbox) em 04/06/2026 20:00 UTC. "
    "Verifique FUTBIN/FUT.GG antes de executar cada compra.",
    body_style
))
elements.append(Spacer(1, 6))

# Cabeçalho da tabela
col_headers = [
    Paragraph("<b>Jogador</b>", ParagraphStyle("th", parent=styles["Normal"],
        fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER, fontName="Helvetica-Bold")),
    Paragraph("<b>OVR</b>", ParagraphStyle("th", parent=styles["Normal"],
        fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER, fontName="Helvetica-Bold")),
    Paragraph("<b>Clube / Tipo</b>", ParagraphStyle("th", parent=styles["Normal"],
        fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER, fontName="Helvetica-Bold")),
    Paragraph("<b>Comprar</b>", ParagraphStyle("th", parent=styles["Normal"],
        fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER, fontName="Helvetica-Bold")),
    Paragraph("<b>Vender</b>", ParagraphStyle("th", parent=styles["Normal"],
        fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER, fontName="Helvetica-Bold")),
    Paragraph("<b>Margem Liq.</b>", ParagraphStyle("th", parent=styles["Normal"],
        fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER, fontName="Helvetica-Bold")),
    Paragraph("<b>Horizonte</b>", ParagraphStyle("th", parent=styles["Normal"],
        fontSize=8.5, textColor=BRANCO, alignment=TA_CENTER, fontName="Helvetica-Bold")),
]

def cell(txt, color=CINZA_ESCURO, bold=False, align=TA_CENTER):
    fn = "Helvetica-Bold" if bold else "Helvetica"
    return Paragraph(txt, ParagraphStyle("td", parent=styles["Normal"],
        fontSize=8.5, textColor=color, alignment=align, fontName=fn, leading=11))

def margem(compra, venda):
    liq = round(venda * 0.95 - compra)
    return liq

rows_data = [
    # ( Jogador, OVR, Clube/Tipo, Compra, Venda, Horizonte )
    ("Luka Modrić",       "83", "Real Madrid / Gold Fodder",   750,  1_350, "2-6h pós-SBC"),
    ("Kasper Schmeichel", "83", "Anderlecht / Gold Fodder",    750,  1_300, "2-6h pós-SBC"),
    ("Manuel Neuer",      "84", "Bayern München / Gold Fodder",800,  1_500, "2-6h pós-SBC"),
    ("Szczesny",          "84", "FC Barcelona / Gold Fodder",  750,  1_400, "2-6h pós-SBC"),
    ("Romelu Lukaku",     "84", "Napoli / Gold Fodder",        800,  1_450, "2-6h pós-SBC"),
    ("Patrik Schick",     "85", "Bayer Leverkusen / Gold Fod.",900,  1_700, "2-6h pós-SBC"),
    ("Keira Walsh",       "85", "FC Barcelona W / Gold Fod.",  800,  1_600, "2-6h pós-SBC"),
    ("Amad Diallo (PTG)", "94", "Man. United / Path to Glory", 32_000, 41_000, "3-5 dias (WC)"),
    ("Bukayo Saka (PTG)", "93", "Arsenal / Path to Glory",     28_000, 37_000, "3-5 dias (WC)"),
    ("Jamal Musiala(PTG)","93", "Bayern / Path to Glory",      27_000, 35_000, "3-5 dias (WC)"),
]

table_rows = [col_headers]
for i, (nome, ovr, clube, compra, venda, horizonte) in enumerate(rows_data):
    liq = margem(compra, venda)
    liq_str = f"+{liq:,}".replace(",", ".") + " c"
    c_str   = f"{compra:,}".replace(",", ".") + " c"
    v_str   = f"{venda:,}".replace(",", ".") + " c"
    liq_color = VERDE_ESCURO if liq > 0 else VERMELHO
    row = [
        cell(nome, align=TA_LEFT),
        cell(ovr, bold=True),
        cell(clube, align=TA_LEFT),
        cell(c_str),
        cell(v_str),
        cell(liq_str, color=liq_color, bold=True),
        cell(horizonte),
    ]
    table_rows.append(row)

col_widths = [3.5*cm, 1.1*cm, 4.0*cm, 1.9*cm, 1.9*cm, 2.0*cm, 3.0*cm]
card_table = Table(table_rows, colWidths=col_widths, repeatRows=1)

ts = TableStyle([
    # Cabeçalho
    ("BACKGROUND",    (0,0), (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 4),
    ("RIGHTPADDING",  (0,0), (-1,-1), 4),
    ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#ced4da")),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [BRANCO, CINZA_CLARO]),
    # Destaque cartas PTG (linhas 8,9,10 = índice 8-10)
    ("BACKGROUND",    (0,8), (-1,10), colors.HexColor("#fff3cd")),
    ("FONTNAME",      (0,8), (-1,10), "Helvetica-Bold"),
])
card_table.setStyle(ts)
elements.append(card_table)

elements.append(Spacer(1, 6))
elements.append(Paragraph(
    "<b>Legenda:</b> Linhas amarelas = cartas Path to Glory (investimento maior, horizonte de 3-5 dias). "
    "Linhas brancas/cinzas = fodder para SBC flipping (curto prazo, 2-6h pós-lançamento de SBC). "
    "Margem líquida já descontada taxa EA de 5%.",
    aviso_style
))

# ══════════════════════════════════════════════════════════
# 3. ESTRATÉGIA DE TIMING
# ══════════════════════════════════════════════════════════
elements.append(Spacer(1, 8))
elements.append(Paragraph(" 3.  ESTRATÉGIA DE TIMING", secao_style))
elements.append(Spacer(1, 4))

timing_data = [
    [
        Paragraph("<b>AGORA (04/06 — noite)</b>", ParagraphStyle("tt", parent=styles["Normal"],
            fontSize=9, textColor=VERDE_ESCURO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>05/06 — manhã (8-12h BRT)</b>", ParagraphStyle("tt", parent=styles["Normal"],
            fontSize=9, textColor=AZUL, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>05/06 — tarde/noite (15-22h BRT)</b>", ParagraphStyle("tt", parent=styles["Normal"],
            fontSize=9, textColor=LARANJA, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>06-07/06 (48h+)</b>", ParagraphStyle("tt", parent=styles["Normal"],
            fontSize=9, textColor=VERMELHO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ],
    [
        Paragraph(
            "• Compre fodder 83-85 rated antes da queda de amanhã\n"
            "• Preços ainda estáveis (sem promo ativa)\n"
            "• Reserve ~8.000c para PTG oportunidades",
            ParagraphStyle("tb", parent=styles["Normal"], fontSize=8.5, leading=12, fontName="Helvetica")
        ),
        Paragraph(
            "• Division Rivals rewards às 8h BRT → flood de packs\n"
            "• Preços de fodder caem: COMPRE mais 83-85\n"
            "• Monitore o mercado no FUTBIN app",
            ParagraphStyle("tb", parent=styles["Normal"], fontSize=8.5, leading=12, fontName="Helvetica")
        ),
        Paragraph(
            "• PTG Team 1 lança às 15h BRT → SBC rush\n"
            "• VENDA fodder 83-85 no pico de demanda\n"
            "• Avalie Saka/Musiala/Amad se < preço-alvo",
            ParagraphStyle("tb", parent=styles["Normal"], fontSize=8.5, leading=12, fontName="Helvetica")
        ),
        Paragraph(
            "• Monitor PTG cards — busque queda pós-hype\n"
            "• Recompre fodder barato após normalização\n"
            "• Cartas de seleções vencedoras valorizam",
            ParagraphStyle("tb", parent=styles["Normal"], fontSize=8.5, leading=12, fontName="Helvetica")
        ),
    ]
]

timing_table = Table(timing_data, colWidths=[W/4]*4)
timing_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (0,0), colors.HexColor("#d4edda")),
    ("BACKGROUND",    (1,0), (1,0), colors.HexColor("#cce5ff")),
    ("BACKGROUND",    (2,0), (2,0), colors.HexColor("#fff3cd")),
    ("BACKGROUND",    (3,0), (3,0), colors.HexColor("#f8d7da")),
    ("BACKGROUND",    (0,1), (0,1), colors.HexColor("#f0fff4")),
    ("BACKGROUND",    (1,1), (1,1), colors.HexColor("#f0f8ff")),
    ("BACKGROUND",    (2,1), (2,1), colors.HexColor("#fffdf0")),
    ("BACKGROUND",    (3,1), (3,1), colors.HexColor("#fff5f5")),
    ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#ced4da")),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING",   (0,0), (-1,-1), 5),
    ("RIGHTPADDING",  (0,0), (-1,-1), 5),
    ("FONTSIZE",      (0,0), (-1,-1), 8.5),
]))
elements.append(timing_table)

# ══════════════════════════════════════════════════════════
# 4. ESTIMATIVA DE RETORNO EM 48H
# ══════════════════════════════════════════════════════════
elements.append(Spacer(1, 10))
elements.append(Paragraph(" 4.  ESTIMATIVA DE RETORNO EM 48H", secao_style))
elements.append(Spacer(1, 4))

ret_data = [
    [
        Paragraph("<b>Cenário</b>", ParagraphStyle("rh", parent=styles["Normal"],
            fontSize=9, textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Estratégia</b>", ParagraphStyle("rh", parent=styles["Normal"],
            fontSize=9, textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Budget Alocado</b>", ParagraphStyle("rh", parent=styles["Normal"],
            fontSize=9, textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Retorno Estimado</b>", ParagraphStyle("rh", parent=styles["Normal"],
            fontSize=9, textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Lucro Líquido</b>", ParagraphStyle("rh", parent=styles["Normal"],
            fontSize=9, textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>ROI</b>", ParagraphStyle("rh", parent=styles["Normal"],
            fontSize=9, textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ],
    [
        Paragraph("Conservador", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica-Bold", alignment=TA_CENTER, textColor=AZUL)),
        Paragraph("Fodder Flipping 83-85 apenas\n(20 cartas @800c avg)", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=8.5, fontName="Helvetica", alignment=TA_LEFT, leading=11)),
        Paragraph("16.000 coins", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica", alignment=TA_CENTER)),
        Paragraph("~20.000 coins", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica", alignment=TA_CENTER)),
        Paragraph("+4.000 coins", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica-Bold", alignment=TA_CENTER, textColor=VERDE_ESCURO)),
        Paragraph("+25%", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica-Bold", alignment=TA_CENTER, textColor=VERDE_ESCURO)),
    ],
    [
        Paragraph("Moderado", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica-Bold", alignment=TA_CENTER, textColor=LARANJA)),
        Paragraph("Fodder (50%) + 1 carta PTG Musiala/Saka", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=8.5, fontName="Helvetica", alignment=TA_LEFT, leading=11)),
        Paragraph("40.000 coins", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica", alignment=TA_CENTER)),
        Paragraph("~52.000 coins", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica", alignment=TA_CENTER)),
        Paragraph("+12.000 coins", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica-Bold", alignment=TA_CENTER, textColor=VERDE_ESCURO)),
        Paragraph("+30%", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica-Bold", alignment=TA_CENTER, textColor=VERDE_ESCURO)),
    ],
    [
        Paragraph("Otimista", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica-Bold", alignment=TA_CENTER, textColor=VERMELHO)),
        Paragraph("Fodder (30%) + PTG (seleção campeã) + Evo invest.", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=8.5, fontName="Helvetica", alignment=TA_LEFT, leading=11)),
        Paragraph("40.000 coins", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica", alignment=TA_CENTER)),
        Paragraph("~65.000 coins", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica", alignment=TA_CENTER)),
        Paragraph("+25.000 coins", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica-Bold", alignment=TA_CENTER, textColor=VERDE_ESCURO)),
        Paragraph("+62%", ParagraphStyle("rb", parent=styles["Normal"],
            fontSize=9, fontName="Helvetica-Bold", alignment=TA_CENTER, textColor=VERDE_ESCURO)),
    ],
]

ret_col_widths = [2.5*cm, 5.2*cm, 2.5*cm, 2.5*cm, 2.8*cm, 1.8*cm]
ret_table = Table(ret_data, colWidths=ret_col_widths, repeatRows=1)
ret_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 4),
    ("RIGHTPADDING",  (0,0), (-1,-1), 4),
    ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#ced4da")),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.HexColor("#e8f4fc"), colors.HexColor("#fff8e8"), colors.HexColor("#fdecea")]),
]))
elements.append(ret_table)

elements.append(Spacer(1, 6))
elements.append(Paragraph(
    "<b>Nota:</b> O cenário otimista depende da seleção do jogador PTG investido avançar às semifinais da Copa do Mundo 2026 "
    "(início 11/06). Cartas de jogadores de Brasil, França, Argentina e Espanha tendem a ter maior valorização por volume de fãs.",
    aviso_style
))

# ══════════════════════════════════════════════════════════
# 5. 8 REGRAS DE OURO DO TRADE
# ══════════════════════════════════════════════════════════
elements.append(Spacer(1, 10))
elements.append(Paragraph(" 5.  AS 8 REGRAS DE OURO DO TRADE", secao_style))
elements.append(Spacer(1, 6))

regras = [
    ("1. Compre no valley, venda no pico",
     "O fodder cai nas manhãs de quinta-feira (rewards de Rivals) e quando promos começam. "
     "O pico ocorre 30-60 minutos após o lançamento de um novo SBC. Respeite esse ciclo."),
    ("2. Nunca coloque todos os ovos numa cesta",
     "Distribua o budget: máximo 60% numa única estratégia. Reserve sempre 20-25% de coins líquidos "
     "para aproveitar oportunidades inesperadas no mercado."),
    ("3. Cheque FUTBIN antes de qualquer compra",
     "Preços no mercado podem estar inflacionados por hype. Confirme o histórico de preços "
     "das últimas 24h no FUTBIN ou FUT.GG antes de executar qualquer compra acima de 5.000c."),
    ("4. A taxa EA de 5% é implacável",
     "Toda venda perde 5%. Nunca calcule seu lucro sem descontar essa taxa. "
     "Uma margem bruta de 600c vira apenas 550c após a taxa — ou até prejuízo com spread de listing."),
    ("5. PTG: espere 48-72h antes de comprar",
     "Cartas de Path to Glory chegam superinflacionadas no dia 1 por hype de streamers. "
     "Aguarde a estabilização. Compre somente após identificar qual seleção está performando bem."),
    ("6. Evite comprar durante Weekend League (sex-dom)",
     "A demanda por fodder cai no fim de semana — jogadores estão focados em jogar, não em SBCs. "
     "O mercado volta a aquecer na segunda-feira quando players completam objetivos."),
    ("7. Listing time = 1 hora para snipes, 12h para trades planejados",
     "Para sniping rápido, liste por 1h e monitore. Para investimentos de médio prazo, "
     "liste por 12h ou 24h para capturar diferentes horários de pico de compradores."),
    ("8. Lucro realizado é lucro real",
     "Um investimento com potencial de +50% que você não vendeu não vale nada. "
     "Defina seu target price, execute a venda quando atingir, e reinvista. "
     "Ganância é o maior inimigo do trader de FUT."),
]

regras_table_data = []
for i, (titulo, descricao) in enumerate(regras):
    num_style = ParagraphStyle("num", parent=styles["Normal"],
        fontSize=18, textColor=VERDE_CLARO if i % 2 == 0 else AMARELO_CLARO,
        fontName="Helvetica-Bold", alignment=TA_CENTER)
    left_cell = Paragraph(titulo.split(". ", 1)[0] + ".", num_style)
    right_cell_title = Paragraph(f"<b>{titulo.split('. ', 1)[1]}</b>", regra_titulo_style)
    right_cell_body = Paragraph(descricao, regra_body_style)
    # Combine title and body
    from reportlab.platypus import KeepTogether
    right_content = Table([[right_cell_title], [right_cell_body]], colWidths=[W - 2.5*cm - 8])
    right_content.setStyle(TableStyle([
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("TOPPADDING",    (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    regras_table_data.append([left_cell, right_content])

bg_colors = []
for i in range(len(regras)):
    if i % 2 == 0:
        bg_colors.append(("BACKGROUND", (0,i), (0,i), VERDE_ESCURO))
        bg_colors.append(("BACKGROUND", (1,i), (1,i), CINZA_CLARO))
    else:
        bg_colors.append(("BACKGROUND", (0,i), (0,i), VERDE_MEDIO))
        bg_colors.append(("BACKGROUND", (1,i), (1,i), BRANCO))

regras_table = Table(regras_table_data, colWidths=[2.2*cm, W - 2.2*cm])
ts_regras = TableStyle([
    ("ALIGN",         (0,0), (0,-1), "CENTER"),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ("RIGHTPADDING",  (0,0), (-1,-1), 6),
    ("LINEBELOW",     (0,0), (-1,-2), 0.5, colors.HexColor("#dee2e6")),
    ("BOX",           (0,0), (-1,-1), 1, VERDE_ESCURO),
] + bg_colors)
regras_table.setStyle(ts_regras)
elements.append(regras_table)

# ══════════════════════════════════════════════════════════
# 6. DISCLAIMER
# ══════════════════════════════════════════════════════════
elements.append(Spacer(1, 12))
disclaimer_data = [[
    Paragraph(
        "<b>DISCLAIMER — AVISO LEGAL</b><br/><br/>"
        "Este relatório foi gerado automaticamente para fins educacionais e de entretenimento. "
        "As previsões de preços, margens e retornos são baseadas em dados históricos de mercado, "
        "tendências de eventos e padrões observados no EA FC 26 Ultimate Team, <b>não constituindo "
        "garantia de lucro</b>. O mercado de FUT é altamente volátil e imprevisível — preços podem "
        "variar significativamente em minutos. <b>Nunca invista mais do que está disposto a perder.</b> "
        "Este documento não tem afiliação com a Electronic Arts Inc. EA FC, FIFA e Ultimate Team são "
        "marcas registradas de seus respectivos proprietários. Sempre verifique preços em tempo real "
        "no FUTBIN (futbin.com) ou FUT.GG (fut.gg) antes de qualquer operação.",
        aviso_style
    )
]]
disclaimer_table = Table(disclaimer_data, colWidths=[W])
disclaimer_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#f8f9fa")),
    ("BOX",           (0,0), (-1,-1), 1, colors.HexColor("#6c757d")),
    ("TOPPADDING",    (0,0), (-1,-1), 10),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ("RIGHTPADDING",  (0,0), (-1,-1), 12),
    ("ROUNDEDCORNERS",(0,0), (-1,-1), [6,6,6,6]),
]))
elements.append(disclaimer_table)

# Rodapé
elements.append(Spacer(1, 8))
elements.append(HRFlowable(width="100%", thickness=1, color=VERDE_ESCURO))
elements.append(Spacer(1, 4))
elements.append(Paragraph(
    f"EA FC 26 Ultimate Team — Relatório de Trading | {DATA_HORA} UTC | "
    "Gerado automaticamente | github.com/kaiohsferreira/fifa-trading",
    ParagraphStyle("footer", parent=styles["Normal"],
        fontSize=7.5, textColor=colors.HexColor("#6c757d"),
        alignment=TA_CENTER, fontName="Helvetica-Oblique")
))

# ── Build
doc.build(elements)
print(f"PDF gerado: {FILENAME}")
