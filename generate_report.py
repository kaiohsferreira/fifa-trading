from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.platypus import PageBreak
from reportlab.lib.colors import HexColor

OUTPUT = "relatorio-trading-2026-06-02-20h.pdf"

# Color palette
C_GREEN  = HexColor("#00C853")
C_GOLD   = HexColor("#FFD600")
C_DARK   = HexColor("#0D0D0D")
C_DARK2  = HexColor("#1A1A2E")
C_BLUE   = HexColor("#1565C0")
C_BLUE2  = HexColor("#0D47A1")
C_ACCENT = HexColor("#E65100")
C_GRAY   = HexColor("#424242")
C_LGRAY  = HexColor("#EEEEEE")
C_WHITE  = colors.white
C_RED    = HexColor("#C62828")
C_YELLOW = HexColor("#F9A825")

def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "ReportTitle",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=C_WHITE,
        alignment=TA_CENTER,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        "ReportSubtitle",
        fontName="Helvetica",
        fontSize=11,
        textColor=C_GOLD,
        alignment=TA_CENTER,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        "SectionHeader",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=C_DARK2,
        spaceBefore=14,
        spaceAfter=6,
        borderPad=4,
    ))
    styles.add(ParagraphStyle(
        "Body",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=C_DARK,
        leading=14,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
    ))
    styles.add(ParagraphStyle(
        "BulletItem",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=C_DARK,
        leading=14,
        leftIndent=12,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        "RuleTitle",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=C_BLUE2,
        leading=13,
        spaceAfter=1,
    ))
    styles.add(ParagraphStyle(
        "Disclaimer",
        fontName="Helvetica-Oblique",
        fontSize=8,
        textColor=C_GRAY,
        leading=11,
        alignment=TA_JUSTIFY,
    ))
    return styles

def header_band(styles):
    """Dark header block with title."""
    data = [[
        Paragraph("EA FC 26 — RELATÓRIO DE TRADING", styles["ReportTitle"]),
    ]]
    t = Table(data, colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_DARK2),
        ("TOPPADDING",    (0,0), (-1,-1), 14),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return t

def info_band(styles):
    data = [
        [
            Paragraph("<b>Data/Hora:</b>  02/06/2026  20:06 UTC", styles["ReportSubtitle"]),
            Paragraph("<b>Budget:</b>  40.000 coins", styles["ReportSubtitle"]),
        ]
    ]
    t = Table(data, colWidths=[9.5*cm, 7.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_DARK),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("RIGHTPADDING",  (0,0), (-1,-1), 12),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    return t

def section_header(text, styles, bar_color=C_BLUE2):
    data = [[Paragraph(text, styles["SectionHeader"])]]
    t = Table(data, colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_LGRAY),
        ("LINEBELOW", (0,0), (-1,-1), 2.5, bar_color),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
    ]))
    return t

def market_context_section(styles):
    items = [
        section_header("1. CONTEXTO DO MERCADO — JUNHO 2026", styles),
        Spacer(1, 4),
        Paragraph(
            "<b>Evento Ativo: Path to Glory (05/06 – 19/06/2026)</b> — Promo do Mundial FIFA 2026 (EUA, Canadá e México). "
            "Cartas dinâmicas que sobem de rating conforme as seleções avançam no torneio. "
            "Lançamento oficial: <b>sexta-feira, 5 de junho às 19h BRT</b>. "
            "Nomes confirmados: Vini Jr (Brasil), Musiala (Alemanha), Saka (Inglaterra), Pulisic (EUA), James Rodríguez (Colômbia).",
            styles["Body"]
        ),
        Paragraph(
            "<b>Festival of Football:</b> Campanha paralela que roda de 05/06 a 24/07/2026. Login diário garante "
            "Pelé 93 OVR ICON + 3 Evolutions 'Choose Your Journey'. Mais de 100 novos jogadores internacionais "
            "adicionados ao pool de pacotes.",
            styles["Body"]
        ),
        Paragraph(
            "<b>Tendência geral:</b> Mercado em estado de <b>alta volatilidade pré-promo</b>. "
            "Nas 48–72h antes do lançamento do Path to Glory, o fodder de rating 83–88 costuma se valorizar "
            "entre 15% e 40% por conta de SBCs novos. Após o lançamento, abertura massiva de pacotes gera "
            "flood de supply e queda de preços — ideal para acumulação.",
            styles["Body"]
        ),
        Paragraph(
            "<b>Momento atual (02/06, terça-feira):</b> Antevéspera do Path to Glory. Preços de fodder "
            "ainda baixos; janela ótima para comprar antes do spike de demanda.",
            styles["Body"]
        ),
    ]
    return items

def cards_table_section(styles):
    header_style = ParagraphStyle(
        "TH", fontName="Helvetica-Bold", fontSize=8.5,
        textColor=C_WHITE, alignment=TA_CENTER, leading=11
    )
    cell_style = ParagraphStyle(
        "TC", fontName="Helvetica", fontSize=8.5,
        textColor=C_DARK, alignment=TA_CENTER, leading=11
    )
    cell_b = ParagraphStyle(
        "TCB", fontName="Helvetica-Bold", fontSize=8.5,
        textColor=C_DARK, alignment=TA_CENTER, leading=11
    )
    green_b = ParagraphStyle(
        "TCG", fontName="Helvetica-Bold", fontSize=8.5,
        textColor=HexColor("#1B5E20"), alignment=TA_CENTER, leading=11
    )

    headers = ["Jogador", "Rat.", "Clube / Seleção", "Comprar até", "Vender por", "Margem Líq.*", "Estratégia"]

    rows = [
        ["Vini Jr", "93", "Real Madrid / Brasil", "38.000", "52.000", "+11.600", "Path to Glory – sobe se Brasil avança"],
        ["James Rodríguez", "87", "Rayo Vallecano / Colômbia", "8.500", "13.000", "+3.850", "PTG estreia + hype Mundial"],
        ["Pulisic", "86", "AC Milan / EUA", "6.200", "9.500", "+2.825", "PTG EUA joga em casa – alta demanda"],
        ["Musiala", "90", "Bayern München / Alemanha", "22.000", "31.000", "+7.450", "PTG – Alemanha favorita ao título"],
        ["Saka", "88", "Arsenal / Inglaterra", "12.000", "18.500", "+5.575", "PTG – hype Premier League"],
        ["Rodrygo", "86", "Real Madrid / Brasil", "5.800", "9.000", "+2.750", "SBC fodder 86 + PTG Brasil"],
        ["Mkhitaryan", "83", "Inter / Armênia", "750", "1.400", "+580", "SBC fodder 83 – flip Thursday"],
        ["De Paul", "84", "Atlético Madrid / Argentina", "750", "1.350", "+533", "SBC fodder 84 – flip Thursday"],
        ["Mbeumo", "85", "Brentford / Camarões", "950", "1.650", "+618", "SBC fodder 85 – buy dip Sunday"],
        ["De Gea", "85", "Fiorentina / Espanha", "1.000", "1.700", "+615", "SBC fodder 85 – Thursday flip"],
        ["Schick", "85", "Leverkusen / República Checa", "1.100", "1.800", "+610", "SBC fodder 85 – demand PTG"],
        ["Kolo Muani", "86", "PSG / França", "3.200", "5.000", "+1.550", "SBC 86 + PTG França"],
    ]

    table_data = [[Paragraph(h, header_style) for h in headers]]
    row_colors = []
    for i, r in enumerate(rows):
        row = [Paragraph(r[0], cell_b if i < 6 else cell_style)]
        row += [Paragraph(r[j], cell_style) for j in range(1, 5)]
        row.append(Paragraph(r[5], green_b))
        row.append(Paragraph(r[6], cell_style))
        table_data.append(row)
        row_colors.append(i)

    col_widths = [3.0*cm, 1.1*cm, 3.2*cm, 2.0*cm, 2.0*cm, 2.0*cm, 3.7*cm]
    t = Table(table_data, colWidths=col_widths, repeatRows=1)

    style_cmds = [
        ("BACKGROUND", (0,0), (-1,0), C_BLUE2),
        ("TEXTCOLOR",  (0,0), (-1,0), C_WHITE),
        ("ALIGN",      (0,0), (-1,-1), "CENTER"),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), 8.5),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [C_WHITE, C_LGRAY]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#BDBDBD")),
        ("LINEBELOW", (0,0), (-1,0), 1.5, C_GOLD),
        ("LINEABOVE", (0,6), (-1,6), 1.2, C_ACCENT),
    ]
    t.setStyle(TableStyle(style_cmds))

    note = Paragraph(
        "* Margem líquida = receita de venda × 0,95 (taxa EA 5%) − custo de compra. "
        "Valores em coins estimados com base em dados de mercado de 02/06/2026.",
        styles["Disclaimer"]
    )

    return [
        section_header("2. CARTAS RECOMENDADAS (Budget: 40.000 coins)", styles, C_ACCENT),
        Spacer(1, 6),
        t,
        Spacer(1, 4),
        note,
    ]

def timing_section(styles):
    return [
        section_header("3. ESTRATÉGIA DE TIMING", styles),
        Spacer(1, 4),
        Paragraph("<b>AGORA (02/06 – 04/06)  |  Janela de Acumulação</b>", styles["Body"]),
        Paragraph("• Comprar fodder 83–86 no piso do mercado (mercado quieto, pré-evento).", styles["BulletItem"]),
        Paragraph("• Acumular jogadores PTG de menor custo (Pulisic, James Rodríguez, Schick, Rodrygo).", styles["BulletItem"]),
        Paragraph("• Evitar comprar cartas >20k antes de conhecer o valor exato de lançamento.", styles["BulletItem"]),
        Spacer(1, 6),
        Paragraph("<b>05/06 (Sex) – 30 min após lançamento do Path to Glory  |  Venda de Fodder</b>", styles["Body"]),
        Paragraph("• SBCs novos geram demanda imediata por fodder 83–86 → vender nessa janela.", styles["BulletItem"]),
        Paragraph("• Preços sobem 20–40% em 1–2h. Colocar BIN ligeiramente abaixo do pico para vender rápido.", styles["BulletItem"]),
        Spacer(1, 6),
        Paragraph("<b>05/06 (Sex) – 2–4h após lançamento  |  Compra de PTG Descartados</b>", styles["Body"]),
        Paragraph("• Após spike inicial, quem abre pacotes inunda o mercado → preços caem.", styles["BulletItem"]),
        Paragraph("• Comprar Vini Jr e Musiala PTG nessa queda para segurar até próximo jogo do Brasil/Alemanha.", styles["BulletItem"]),
        Spacer(1, 6),
        Paragraph("<b>Quinta-feira (04/06 – manhã)  |  Thursday Flip</b>", styles["Body"]),
        Paragraph("• Recompensas de Rivals chegam → supply alto → comprar fodder no piso.", styles["BulletItem"]),
        Paragraph("• Recolocar à venda 3–6h depois quando o supply se estabiliza.", styles["BulletItem"]),
        Spacer(1, 6),
        Paragraph("<b>Domingo (07/06 – fim do Weekend League)  |  Buy Dip</b>", styles["Body"]),
        Paragraph("• Queda de preços após WL → segundo momento de acumulação para semana seguinte.", styles["BulletItem"]),
    ]

def returns_section(styles):
    header_s = ParagraphStyle("RH", fontName="Helvetica-Bold", fontSize=9,
                               textColor=C_WHITE, alignment=TA_CENTER)
    cell_s  = ParagraphStyle("RC", fontName="Helvetica", fontSize=9,
                               textColor=C_DARK, alignment=TA_CENTER)
    cell_b  = ParagraphStyle("RCB", fontName="Helvetica-Bold", fontSize=9,
                               textColor=C_DARK, alignment=TA_CENTER)
    green_s = ParagraphStyle("RCG", fontName="Helvetica-Bold", fontSize=9,
                               textColor=HexColor("#1B5E20"), alignment=TA_CENTER)
    red_s   = ParagraphStyle("RCR", fontName="Helvetica-Bold", fontSize=9,
                               textColor=C_RED, alignment=TA_CENTER)

    data = [
        [Paragraph(h, header_s) for h in
         ["Estratégia", "Capital Inicial", "Retorno Conservador", "Retorno Otimista", "Capital Final (Otimista)"]],
        [Paragraph("SBC Fodder Flip (83–86)", cell_b),
         Paragraph("15.000", cell_s), Paragraph("+12%  (+1.800)", green_s),
         Paragraph("+30%  (+4.500)", green_s), Paragraph("19.500", cell_b)],
        [Paragraph("PTG Invest (Pulisic, James, Schick)", cell_b),
         Paragraph("12.000", cell_s), Paragraph("+18%  (+2.160)", green_s),
         Paragraph("+55%  (+6.600)", green_s), Paragraph("18.600", cell_b)],
        [Paragraph("PTG Premium (Vini Jr + Musiala)", cell_b),
         Paragraph("10.000", cell_s), Paragraph("+10%  (+1.000)", green_s),
         Paragraph("+45%  (+4.500)", green_s), Paragraph("14.500", cell_b)],
        [Paragraph("Thursday Flip (reserva)", cell_b),
         Paragraph("3.000", cell_s), Paragraph("+8%  (+240)", green_s),
         Paragraph("+20%  (+600)", green_s), Paragraph("3.600", cell_b)],
        [Paragraph("TOTAL", cell_b),
         Paragraph("40.000", cell_b), Paragraph("+5.200 coins", green_s),
         Paragraph("+16.200 coins", green_s), Paragraph("56.200", cell_b)],
    ]
    col_widths = [5.5*cm, 3*cm, 3.2*cm, 3.2*cm, 3.1*cm]
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), C_DARK2),
        ("BACKGROUND", (0,5), (-1,5), HexColor("#E3F2FD")),
        ("LINEBELOW", (0,5), (-1,5), 2, C_BLUE2),
        ("LINEABOVE", (0,5), (-1,5), 1.5, C_BLUE2),
        ("ROWBACKGROUNDS", (0,1), (-1,4), [C_WHITE, C_LGRAY]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#BDBDBD")),
        ("LINEBELOW", (0,0), (-1,0), 1.5, C_GOLD),
        ("ALIGN",   (0,0), (-1,-1), "CENTER"),
        ("VALIGN",  (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))

    return [
        section_header("4. ESTIMATIVA DE RETORNO EM 48H", styles, C_GREEN),
        Spacer(1, 6),
        t,
        Spacer(1, 4),
        Paragraph(
            "Cenário conservador: SBCs normais, Path to Glory moderado. "
            "Cenário otimista: Brasil e Alemanha vencem na fase de grupos, SBCs de alto requisito ativados.",
            styles["Disclaimer"]
        ),
    ]

def golden_rules_section(styles):
    rules = [
        ("Regra 1 — Taxa sempre em mente",
         "Toda venda perde 5% para a EA. Só feche a compra se o lucro líquido após a taxa justificar."),
        ("Regra 2 — Compre no dip, venda no hype",
         "Quinta-feira (Rivals rewards) e domingo (pós-WL) são os melhores momentos de compra. "
         "Sexta-feira pós-SBC e sábado pré-WL são os melhores momentos de venda."),
        ("Regra 3 — Nunca aposte tudo em uma carta",
         "Diversifique: no máximo 30% do budget em um único jogador. Liquidez é sobrevivência."),
        ("Regra 4 — Path to Glory = risco de não-upgrade",
         "Cartas PTG só sobem se a seleção avançar. Venda antes do jogo para garantir lucro."),
        ("Regra 5 — Fodder é rei no início de promo",
         "Nos primeiros 60 minutos após SBC novo, fodder 83–86 valoriza. Tenha estoque pronto."),
        ("Regra 6 — Sniping filter com margem mínima 15%",
         "Só compre no mercado se houver margem mínima de 15% após taxa. Menos que isso, o risco supera o ganho."),
        ("Regra 7 — Monitore futbin/fut.gg antes de vender",
         "Cheque o preço médio de mercado antes de colocar à venda. BIN 2–3% abaixo do menor listado garante venda rápida."),
        ("Regra 8 — Mantenha reserva de 20%",
         "Nunca invista 100% do budget. Guarde 20% (≈8.000 coins) para oportunidades inesperadas ou recovery de perda."),
    ]

    items = [section_header("5. AS 8 REGRAS DE OURO DO TRADE", styles, C_GOLD), Spacer(1, 6)]
    for title, desc in rules:
        block = KeepTogether([
            Paragraph(f"▶ {title}", styles["RuleTitle"]),
            Paragraph(desc, styles["BulletItem"]),
            Spacer(1, 4),
        ])
        items.append(block)
    return items

def disclaimer_section(styles):
    return [
        HRFlowable(width="100%", thickness=0.5, color=C_GRAY),
        Spacer(1, 4),
        Paragraph(
            "AVISO LEGAL: Este relatório é gerado automaticamente para fins educativos e de entretenimento. "
            "Os preços de mercado são estimativas baseadas em dados históricos e tendências observadas — "
            "valores reais podem diferir. O trading em Ultimate Team envolve risco de perda de coins. "
            "A EA pode alterar dinâmicas de mercado, preços de pacotes ou regras de SBC sem aviso prévio. "
            "Este documento não constitui aconselhamento financeiro.",
            styles["Disclaimer"]
        ),
        Spacer(1, 2),
        Paragraph(
            "Fontes consultadas: FUTBIN, FUT.GG, TeamGullit, fifauteam.com, mmopixel.com, football-talk.co.uk, "
            "operationsports.com, soccergaming.com — dados coletados em 02/06/2026.",
            styles["Disclaimer"]
        ),
    ]

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=2*cm,
        rightMargin=2*cm,
        topMargin=1.8*cm,
        bottomMargin=1.8*cm,
        title="Relatório de Trading EA FC 26",
        author="FIFA Trading Bot",
    )

    styles = build_styles()
    story = []

    # Header
    story.append(header_band(styles))
    story.append(Spacer(1, 2))
    story.append(info_band(styles))
    story.append(Spacer(1, 10))

    # Sections
    story.extend(market_context_section(styles))
    story.append(Spacer(1, 8))
    story.extend(cards_table_section(styles))
    story.append(Spacer(1, 8))
    story.extend(timing_section(styles))
    story.append(Spacer(1, 8))
    story.extend(returns_section(styles))
    story.append(Spacer(1, 8))
    story.extend(golden_rules_section(styles))
    story.append(Spacer(1, 8))
    story.extend(disclaimer_section(styles))

    doc.build(story)
    print(f"PDF gerado: {OUTPUT}")

if __name__ == "__main__":
    build_pdf()
