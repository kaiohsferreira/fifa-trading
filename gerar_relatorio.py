#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import KeepTogether
import os

REPORT_DATE = "02/06/2026 08:06"
PDF_NAME = "relatorio-trading-2026-06-02-08h.pdf"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), PDF_NAME)

# ── Cores ────────────────────────────────────────────────────────────────────
DARK_BG    = colors.HexColor("#0D1117")
GREEN_EA   = colors.HexColor("#00D26A")
GOLD       = colors.HexColor("#FFD700")
SILVER     = colors.HexColor("#C0C0C0")
RED_SELL   = colors.HexColor("#FF4D4D")
BLUE_INFO  = colors.HexColor("#4DA6FF")
DARK_CARD  = colors.HexColor("#161B22")
MID_GREY   = colors.HexColor("#30363D")
LIGHT_TEXT = colors.HexColor("#E6EDF3")
GREEN_ROW  = colors.HexColor("#0D2818")
ALT_ROW    = colors.HexColor("#1C2128")

def build_styles():
    base = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=22,
        textColor=GREEN_EA, alignment=TA_CENTER,
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        "Subtitle", parent=base["Normal"],
        fontName="Helvetica", fontSize=11,
        textColor=SILVER, alignment=TA_CENTER,
        spaceAfter=2
    )
    section_header = ParagraphStyle(
        "SectionHeader", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=13,
        textColor=GOLD, spaceBefore=14, spaceAfter=6,
        borderPad=4
    )
    body_style = ParagraphStyle(
        "Body", parent=base["Normal"],
        fontName="Helvetica", fontSize=9,
        textColor=LIGHT_TEXT, leading=14,
        alignment=TA_JUSTIFY, spaceAfter=4
    )
    bullet_style = ParagraphStyle(
        "Bullet", parent=base["Normal"],
        fontName="Helvetica", fontSize=9,
        textColor=LIGHT_TEXT, leading=13,
        leftIndent=14, bulletIndent=4, spaceAfter=3
    )
    bold_bullet = ParagraphStyle(
        "BoldBullet", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=9,
        textColor=GREEN_EA, leading=13,
        leftIndent=14, bulletIndent=4, spaceAfter=3
    )
    disclaimer = ParagraphStyle(
        "Disclaimer", parent=base["Normal"],
        fontName="Helvetica-Oblique", fontSize=7.5,
        textColor=colors.HexColor("#8B949E"),
        alignment=TA_JUSTIFY, leading=11
    )
    label_style = ParagraphStyle(
        "Label", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=8,
        textColor=GOLD
    )
    value_style = ParagraphStyle(
        "Value", parent=base["Normal"],
        fontName="Helvetica", fontSize=8,
        textColor=LIGHT_TEXT
    )
    rule_number = ParagraphStyle(
        "RuleNumber", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=10,
        textColor=GREEN_EA
    )
    rule_text = ParagraphStyle(
        "RuleText", parent=base["Normal"],
        fontName="Helvetica", fontSize=9,
        textColor=LIGHT_TEXT, leading=13,
        leftIndent=22, spaceAfter=5
    )
    return {
        "title": title_style, "subtitle": subtitle_style,
        "section": section_header, "body": body_style,
        "bullet": bullet_style, "bold_bullet": bold_bullet,
        "disclaimer": disclaimer, "label": label_style,
        "value": value_style, "rule_number": rule_number,
        "rule_text": rule_text
    }


def dark_page_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # top accent bar
    canvas.setFillColor(GREEN_EA)
    canvas.rect(0, A4[1] - 4, A4[0], 4, fill=1, stroke=0)
    # bottom bar
    canvas.setFillColor(MID_GREY)
    canvas.rect(0, 0, A4[0], 22, fill=1, stroke=0)
    canvas.setFillColor(SILVER)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(2 * cm, 7, f"EA FC 26 — Relatório de Trading  |  {REPORT_DATE} UTC")
    canvas.drawRightString(A4[0] - 2 * cm, 7, f"Página {doc.page}")
    canvas.restoreState()


def make_table(data_rows, col_widths):
    header = [
        Paragraph("<b>Jogador</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8, textColor=DARK_BG, alignment=TA_CENTER)),
        Paragraph("<b>Rating</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8, textColor=DARK_BG, alignment=TA_CENTER)),
        Paragraph("<b>Clube / Liga</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8, textColor=DARK_BG, alignment=TA_CENTER)),
        Paragraph("<b>Compra (coins)</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8, textColor=DARK_BG, alignment=TA_CENTER)),
        Paragraph("<b>Venda alvo</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8, textColor=DARK_BG, alignment=TA_CENTER)),
        Paragraph("<b>Margem líq. (-5%)</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8, textColor=DARK_BG, alignment=TA_CENTER)),
        Paragraph("<b>Tipo</b>", ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8, textColor=DARK_BG, alignment=TA_CENTER)),
    ]

    table_data = [header]
    for i, row in enumerate(data_rows):
        bg = GREEN_ROW if i % 2 == 0 else ALT_ROW
        table_data.append(row)

    t = Table(table_data, colWidths=col_widths, repeatRows=1)

    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), GREEN_EA),
        ("TEXTCOLOR", (0, 0), (-1, 0), DARK_BG),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.4, MID_GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8),
        ("TEXTCOLOR", (0, 1), (-1, -1), LIGHT_TEXT),
    ]
    for i in range(1, len(data_rows) + 1):
        bg = GREEN_ROW if i % 2 == 1 else ALT_ROW
        style_cmds.append(("BACKGROUND", (0, i), (-1, i), bg))
    t.setStyle(TableStyle(style_cmds))
    return t


def cell(text, color=LIGHT_TEXT, bold=False, align=TA_CENTER):
    fn = "Helvetica-Bold" if bold else "Helvetica"
    return Paragraph(
        text,
        ParagraphStyle("c", fontName=fn, fontSize=8, textColor=color, alignment=align)
    )


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        rightMargin=1.8 * cm, leftMargin=1.8 * cm,
        topMargin=1.5 * cm, bottomMargin=1.5 * cm
    )
    s = build_styles()
    story = []

    # ── CABEÇALHO ────────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph("EA FC 26 — RELATÓRIO DE TRADING", s["title"]))
    story.append(Paragraph(f"Gerado em: {REPORT_DATE} UTC", s["subtitle"]))
    story.append(Paragraph("Budget: 40.000 coins  |  Meta: SBC Fodder Flip + Evo Investing + Thursday Flip", s["subtitle"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=GREEN_EA, spaceAfter=10))

    # ── CONTEXTO DE MERCADO ───────────────────────────────────────────────────
    story.append(Paragraph("1. CONTEXTO DO MERCADO — 02/06/2026", s["section"]))
    story.append(Paragraph(
        "O mercado do EA FC 26 está em pré-lançamento do maior evento do ano: o <b>Festival of Football</b>, "
        "celebrando a Copa do Mundo de 2026 (EUA, Canadá e México — 11 jun a 19 jul). "
        "O servidor receberá atualização em <b>04/06/2026</b> com a funcionalidade de <b>EVO Reset/Undo</b> — "
        "primeira vez que cartas tradables evoluídas poderão ser revendidas no mercado. "
        "No dia <b>05/06/2026</b>, o promo <b>Path to Glory</b> será lançado com cartas dinâmicas de jogadores da Copa do Mundo. "
        "O janela atual (02-04/06) é uma das melhores oportunidades de compra do ano, antes do boom de demanda.",
        s["body"]
    ))

    # sub-box: eventos
    events_data = [
        [cell("EVENTO", bold=True, color=GOLD), cell("PERÍODO", bold=True, color=GOLD), cell("IMPACTO NO MERCADO", bold=True, color=GOLD)],
        [cell("World's Game Update + EVO Reset"), cell("04/06/2026"), cell("Cartas evoluídas voltam ao mercado — queda pontual de preços", color=SILVER)],
        [cell("Festival of Football Tokens"), cell("04/06 em diante"), cell("Novo sistema de tokens — demanda alta por SBC fodder", color=SILVER)],
        [cell("Path to Glory (WC Cards)"), cell("05/06 – 19/06"), cell("Alta demanda por fodder 83-88 rated; preços sobem 20-40%", color=GREEN_EA)],
        [cell("Shapeshifters"), cell("12/06 – 10/07"), cell("SBCs massivos — pico de demanda por fodder premium", color=SILVER)],
        [cell("Greats of the Game (ICONs)"), cell("19/06 – 26/06"), cell("SBCs de ícones — forte consumo de 87-88 rated", color=SILVER)],
        [cell("Thursday Flip (semanal)"), cell("Toda quinta-feira"), cell("Preços caem de manhã (rewards) e sobem à tarde", color=BLUE_INFO)],
    ]
    et = Table(events_data, colWidths=[5.2*cm, 3.0*cm, 9.5*cm])
    et_style = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1A2332")),
        ("GRID", (0, 0), (-1, -1), 0.4, MID_GREY),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(events_data)):
        bg = ALT_ROW if i % 2 == 1 else GREEN_ROW
        et_style.append(("BACKGROUND", (0, i), (-1, i), bg))
    et.setStyle(TableStyle(et_style))
    story.append(et)
    story.append(Spacer(1, 0.3 * cm))

    # ── TABELA DE OPORTUNIDADES ───────────────────────────────────────────────
    story.append(Paragraph("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA AGORA", s["section"]))
    story.append(Paragraph(
        "Foco em cartas <b>83-88 rated</b> com preço de compra abaixo de 8.000 coins e margem líquida positiva "
        "após a taxa de 5% da EA. Previsão de valorização com o início do Path to Glory (05/06) e SBCs do Festival of Football.",
        s["body"]
    ))

    # Dados: [Jogador, Rating, Clube/Liga, Compra, Venda, Margem, Tipo]
    cards = [
        # SBC Fodder 84-rated
        ("Bernardo Silva",    "84", "Man City / Premier League", "1.800", "2.800", "+760",   "SBC Fodder 84"),
        ("Maddison",          "84", "Man City / Premier League", "1.600", "2.600", "+870",   "SBC Fodder 84"),
        ("Grimaldo",          "84", "Bayer Leverkusen / Bundesliga", "1.500", "2.400", "+780", "SBC Fodder 84"),
        ("De Paul",           "84", "Atlético Madrid / La Liga", "1.600", "2.500", "+775",   "SBC Fodder 84"),
        ("Dumfries",          "84", "Inter Milan / Serie A",    "1.700", "2.700", "+865",   "SBC Fodder 84"),
        ("Sørloth",           "84", "Atlético Madrid / La Liga", "1.500", "2.400", "+780",  "SBC Fodder 84"),
        # SBC Fodder 85-rated
        ("Mbeumo",            "85", "Brentford / Premier League", "2.000", "3.200", "+1.040", "SBC Fodder 85"),
        ("Schick",            "85", "Bayer Leverkusen / Bundesliga", "1.800", "2.900", "+955", "SBC Fodder 85"),
        ("Rodrygo",           "85", "Real Madrid / La Liga",    "2.200", "3.500", "+1.125",  "SBC Fodder 85"),
        ("Griezmann",         "85", "Atlético Madrid / La Liga", "2.100", "3.300", "+1.035", "SBC Fodder 85"),
        ("Tielemans",         "85", "Aston Villa / Premier League", "1.900", "3.000", "+950", "SBC Fodder 85"),
        ("Carvajal",          "85", "Real Madrid / La Liga",    "1.800", "2.900", "+955",   "SBC Fodder 85"),
        # SBC Fodder 86-rated (premium)
        ("Olise",             "86", "Bayern Munich / Bundesliga", "3.500", "5.500", "+1.725", "SBC Fodder 86"),
        ("Bruno Guimarães",   "86", "Newcastle / Premier League", "3.200", "5.000", "+1.550", "SBC Fodder 86"),
        ("Çalhanoğlu",        "86", "Inter Milan / Serie A",    "3.000", "4.800", "+1.560",  "SBC Fodder 86"),
        ("Nico Williams",     "86", "Athletic Club / La Liga",  "2.800", "4.500", "+1.475",  "SBC Fodder 86"),
        ("Ona Batlle",        "86", "Real Madrid F / Liga F",   "5.500", "8.500", "+2.575",  "SBC Fodder 86"),
        # Evolução / Thursday Flip
        ("Rúben Dias",        "86", "Man City / Premier League", "3.000", "5.000", "+1.750", "Evo + Fodder"),
        ("Iñigo Martínez",    "85", "Barcelona / La Liga",      "2.000", "3.200", "+1.040",  "Thursday Flip"),
        ("De Gea",            "85", "Fiorentina / Serie A",     "1.800", "2.900", "+955",    "Thursday Flip"),
    ]

    def coins(v):
        return cell(v + " c", color=LIGHT_TEXT)

    def margin_cell(v):
        c = GREEN_EA if "+" in v else RED_SELL
        return cell(v + " c", color=c, bold=True)

    def type_cell(t):
        if "86" in t:
            return cell(t, color=GOLD)
        elif "85" in t:
            return cell(t, color=BLUE_INFO)
        elif "Evo" in t:
            return cell(t, color=colors.HexColor("#FF9500"))
        elif "Thursday" in t:
            return cell(t, color=SILVER)
        else:
            return cell(t, color=GREEN_EA)

    rows = []
    for c_ in cards:
        rows.append([
            cell(c_[0], align=TA_LEFT),
            cell(c_[1], bold=True, color=GOLD),
            cell(c_[2], align=TA_LEFT, color=SILVER),
            coins(c_[3]),
            coins(c_[4]),
            margin_cell(c_[5]),
            type_cell(c_[6]),
        ])

    col_w = [3.8*cm, 1.5*cm, 4.5*cm, 2.4*cm, 2.2*cm, 2.4*cm, 2.5*cm]
    story.append(make_table(rows, col_w))

    story.append(Spacer(1, 0.25*cm))
    story.append(Paragraph(
        "<b>Nota:</b> Margem líquida calculada como: (Preço Venda × 0.95) − Preço Compra. "
        "Valores estimados com base em dados de mercado de 02/06/2026 — oscilações normais de ±15% são esperadas.",
        ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=7.5, textColor=SILVER, leading=10)
    ))

    # ── ESTRATÉGIA DE TIMING ─────────────────────────────────────────────────
    story.append(Paragraph("3. ESTRATÉGIA DE TIMING", s["section"]))

    timing_blocks = [
        ("HOJE — 02/06 (Terça)", GREEN_EA, [
            "Compre o máximo de cartas 84-86 rated abaixo de 2.500 coins enquanto o mercado está calmo.",
            "Priorize jogadores de ligas populares (PL, La Liga, Bundesliga) — maior demanda em SBCs.",
            "Evite gastar mais de 8.000 coins por carta individualmente.",
            "Acumule 15-20 cartas de fodder para estar pronto quando os SBCs do Festival chegarem.",
        ]),
        ("04/06 — EVO Reset Live", GOLD, [
            "Observe o mercado ao vivo: cartas evoluídas de jogadores tradables retornam ao mercado.",
            "Pode haver queda pontual de preços em cartas específicas (oportunidade de compra rápida).",
            "Fique atento ao Token Store — revelação de jogadores disponíveis define quais SBCs priorizar.",
            "NÃO venda fodder ainda — guarde para os SBCs que serão anunciados.",
        ]),
        ("05/06 — Path to Glory Launch (Quinta)", BLUE_INFO, [
            "THURSDAY FLIP: Compre de manhã (6h-12h BRT) quando os preços caem com abertura de packs.",
            "Venda à tarde (16h-22h BRT) quando jogadores constroem squads para o Weekend League.",
            "SBCs do Path to Glory serão anunciados — USE o fodder acumulado para completá-los.",
            "Cartas de jogadores da Copa do Mundo que atuam bem sobem de preço instantaneamente.",
        ]),
        ("06-07/06 — Fim de Semana Pós-Launch", SILVER, [
            "Weekend League começa — demanda por bons jogadores no pico máximo.",
            "Venda qualquer fodder restante que não usou nos SBCs (preços ainda altos).",
            "Monitore os primeiros jogos da Copa (11/06) — cartas de jogadores que marcam gols sobem.",
            "Reinvista lucros em cartas de jogadores participantes do Mundial antes do próximo upgrade.",
        ]),
    ]

    for title, tcolor, bullets in timing_blocks:
        story.append(Paragraph(f"▶ {title}", ParagraphStyle(
            "tb", fontName="Helvetica-Bold", fontSize=10, textColor=tcolor,
            spaceBefore=8, spaceAfter=3
        )))
        for b in bullets:
            story.append(Paragraph(f"• {b}", s["bullet"]))

    # ── ESTIMATIVA DE RETORNO ─────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("4. ESTIMATIVA DE RETORNO EM 48H", s["section"]))
    story.append(Paragraph(
        "Baseado em budget de <b>40.000 coins</b>, comprando ~20 cartas de fodder 84-86 rated a preço médio de 2.200 coins "
        "e vendendo após o lançamento do Path to Glory.",
        s["body"]
    ))

    ret_data = [
        [cell("CENÁRIO", bold=True, color=GOLD),
         cell("ESTRATÉGIA", bold=True, color=GOLD),
         cell("CARTAS COMPRADAS", bold=True, color=GOLD),
         cell("RECEITA BRUTA", bold=True, color=GOLD),
         cell("CUSTO TOTAL", bold=True, color=GOLD),
         cell("LUCRO LÍQUIDO", bold=True, color=GOLD),
         cell("ROI", bold=True, color=GOLD)],
        [cell("Conservador", color=SILVER),
         cell("SBC Fodder 84-85", color=SILVER),
         cell("18 cartas × 2.000c", color=SILVER),
         cell("54.720c", color=SILVER),
         cell("36.000c", color=SILVER),
         cell("+18.720c", color=GREEN_EA, bold=True),
         cell("+52%", color=GREEN_EA, bold=True)],
        [cell("Moderado", color=LIGHT_TEXT),
         cell("Fodder 84-86 + EVO reset", color=LIGHT_TEXT),
         cell("16 cartas × 2.400c", color=LIGHT_TEXT),
         cell("60.800c", color=LIGHT_TEXT),
         cell("38.400c", color=LIGHT_TEXT),
         cell("+22.400c", color=GREEN_EA, bold=True),
         cell("+58%", color=GREEN_EA, bold=True)],
        [cell("Otimista", color=GOLD),
         cell("Fodder 85-86 + Path to Glory rush", color=GOLD),
         cell("12 cartas × 3.500c", color=GOLD),
         cell("79.800c", color=GOLD),
         cell("42.000c", color=GOLD),
         cell("+37.800c", color=GREEN_EA, bold=True),
         cell("+90%", color=GREEN_EA, bold=True)],
    ]
    rt = Table(ret_data, colWidths=[2.5*cm, 3.8*cm, 3.5*cm, 2.5*cm, 2.5*cm, 2.5*cm, 1.4*cm])
    rt_style = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1A2332")),
        ("BACKGROUND", (0, 1), (-1, 1), ALT_ROW),
        ("BACKGROUND", (0, 2), (-1, 2), GREEN_ROW),
        ("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#1A2800")),
        ("GRID", (0, 0), (-1, -1), 0.4, MID_GREY),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    rt.setStyle(TableStyle(rt_style))
    story.append(rt)

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>Obs:</b> Receita bruta já descontada a taxa de 5% da EA. "
        "Cenário otimista assume que pelo menos 2-3 cartas se valorizaram 80%+ com o início do Path to Glory. "
        "Nunca invista 100% do budget em uma única carta ou estratégia.",
        ParagraphStyle("note2", fontName="Helvetica-Oblique", fontSize=7.5, textColor=SILVER, leading=10)
    ))

    # ── 8 REGRAS DE OURO ─────────────────────────────────────────────────────
    story.append(Paragraph("5. 8 REGRAS DE OURO DO TRADE", s["section"]))

    rules = [
        ("01", "NUNCA invista mais de 30% do budget em uma única carta",
         "Diversifique sempre. Uma carta que não vende pode prender seu capital por dias."),
        ("02", "Compre na QUEDA, venda na ALTA do ciclo semanal",
         "Quinta de manhã (rewards abertos) = comprar. Quinta à tarde / sábado = vender."),
        ("03", "Sempre calcule a MARGEM LÍQUIDA antes de comprar",
         "Venda alvo × 0,95 − preço de compra = lucro real. Se for negativo, não compre."),
        ("04", "Respeite os PRICE RANGES da EA",
         "Cartas com range muito estreito têm menos potencial de valorização. Prefira cartas com range amplo."),
        ("05", "Monitore os SBCs ATIVOS em tempo real",
         "Quando um SBC novo aparece, os jogadores requeridos sobem em segundos. Seja o primeiro a comprar."),
        ("06", "Não segure cartas por mais de 72h sem revisar",
         "O mercado do EA FC muda rapidamente. Um novo promo pode desvalorizar sua posição da noite para o dia."),
        ("07", "Use o THURSDAY FLIP como renda semanal garantida",
         "É o ciclo mais previsível e seguro. Discipline-se: compre às 6h-12h BRT, venda às 16h-22h BRT."),
        ("08", "REINVISTA os lucros — não gaste em packs",
         "Packs têm retorno esperado negativo. Cada lucro reinvestido aumenta seu poder de compra exponencialmente."),
    ]

    for num, title, desc in rules:
        story.append(KeepTogether([
            Paragraph(f"{num}. {title}", ParagraphStyle(
                "rh", fontName="Helvetica-Bold", fontSize=9.5, textColor=GREEN_EA,
                spaceBefore=6, spaceAfter=1
            )),
            Paragraph(desc, ParagraphStyle(
                "rd", fontName="Helvetica", fontSize=8.5, textColor=LIGHT_TEXT,
                leftIndent=18, spaceAfter=4, leading=12
            )),
        ]))

    story.append(HRFlowable(width="100%", thickness=0.8, color=MID_GREY, spaceBefore=10, spaceAfter=10))

    # ── DISCLAIMER ───────────────────────────────────────────────────────────
    story.append(Paragraph("DISCLAIMER", ParagraphStyle(
        "disc_h", fontName="Helvetica-Bold", fontSize=9, textColor=RED_SELL, spaceAfter=4
    )))
    story.append(Paragraph(
        "Este relatório é gerado por um agente de inteligência artificial com base em dados públicos de mercado e "
        "tendências observadas em comunidades do EA FC 26 Ultimate Team. Os preços e margens apresentados são "
        "<b>estimativas baseadas em dados históricos e tendências de promo anteriores</b>, e não constituem garantia "
        "de lucro. O mercado de FUT pode variar significativamente com base em decisões da EA Sports (mudanças de "
        "price range, ban de métodos de trading, bugs), desempenho de jogadores em partidas reais e comportamento "
        "imprevisível da comunidade. <b>Nunca invista mais do que está disposto a perder.</b> "
        "O trading em EA FC 26 não é uma atividade financeira regulamentada.",
        s["disclaimer"]
    ))

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        f"Relatório gerado automaticamente em {REPORT_DATE} UTC  •  EA FC 26 Trading Agent  •  Budget: 40.000 coins",
        ParagraphStyle("footer", fontName="Helvetica", fontSize=7, textColor=colors.HexColor("#484F58"), alignment=TA_CENTER)
    ))

    doc.build(story, onFirstPage=dark_page_bg, onLaterPages=dark_page_bg)
    print(f"PDF gerado: {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    build_pdf()
