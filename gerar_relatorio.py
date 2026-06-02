#!/usr/bin/env python3
"""Gerador de relatório de trading EA FC 26 - 2026-06-02 14h"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak

REPORT_DATE = "02/06/2026 14:07"
FILENAME = "relatorio-trading-2026-06-02-14h.pdf"

# ── Cores ──────────────────────────────────────────────────────────────────
DARK_BG    = colors.HexColor("#0D0D1A")
GOLD       = colors.HexColor("#FFD700")
GREEN_NEON = colors.HexColor("#00FF88")
RED_SOFT   = colors.HexColor("#FF4C4C")
BLUE_SOFT  = colors.HexColor("#3A86FF")
WHITE      = colors.white
GREY_LIGHT = colors.HexColor("#F0F0F0")
GREY_MID   = colors.HexColor("#CCCCCC")
DARK_ROW   = colors.HexColor("#1A1A2E")
MID_ROW    = colors.HexColor("#16213E")
ACCENT     = colors.HexColor("#E94560")

def build_styles():
    base = getSampleStyleSheet()

    title = ParagraphStyle(
        "title", parent=base["Normal"],
        fontSize=26, textColor=GOLD, alignment=TA_CENTER,
        fontName="Helvetica-Bold", spaceAfter=4, leading=32
    )
    subtitle = ParagraphStyle(
        "subtitle", parent=base["Normal"],
        fontSize=13, textColor=GREY_LIGHT, alignment=TA_CENTER,
        fontName="Helvetica", spaceAfter=2
    )
    section_hdr = ParagraphStyle(
        "section_hdr", parent=base["Normal"],
        fontSize=14, textColor=GOLD, fontName="Helvetica-Bold",
        spaceBefore=14, spaceAfter=6, leading=18
    )
    body = ParagraphStyle(
        "body", parent=base["Normal"],
        fontSize=10, textColor=colors.HexColor("#222222"),
        fontName="Helvetica", leading=15, spaceAfter=4, alignment=TA_JUSTIFY
    )
    body_bold = ParagraphStyle(
        "body_bold", parent=body,
        fontName="Helvetica-Bold", textColor=colors.HexColor("#111111")
    )
    bullet = ParagraphStyle(
        "bullet", parent=body,
        leftIndent=14, bulletIndent=4, spaceAfter=3
    )
    disclaimer = ParagraphStyle(
        "disclaimer", parent=base["Normal"],
        fontSize=8, textColor=colors.HexColor("#888888"),
        fontName="Helvetica-Oblique", alignment=TA_CENTER,
        spaceBefore=10, leading=12
    )
    tag_green = ParagraphStyle(
        "tag_green", parent=base["Normal"],
        fontSize=9, textColor=colors.HexColor("#006600"),
        fontName="Helvetica-Bold", alignment=TA_CENTER
    )
    tag_yellow = ParagraphStyle(
        "tag_yellow", parent=base["Normal"],
        fontSize=9, textColor=colors.HexColor("#7A5C00"),
        fontName="Helvetica-Bold", alignment=TA_CENTER
    )
    return dict(
        title=title, subtitle=subtitle, section_hdr=section_hdr,
        body=body, body_bold=body_bold, bullet=bullet,
        disclaimer=disclaimer, tag_green=tag_green, tag_yellow=tag_yellow
    )


def header_table(s):
    data = [[
        Paragraph("⚽  EA FC 26 — RELATÓRIO DE TRADING", s["title"]),
    ]]
    tbl = Table(data, colWidths=[17*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_BG),
        ("ROUNDEDCORNERS", [8]),
        ("TOPPADDING", (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
    ]))
    return tbl


def info_band(s, date_str):
    data = [[
        Paragraph(f"<b>Data do Relatório:</b> {date_str}", s["body"]),
        Paragraph("<b>Budget:</b> 40.000 coins", s["body"]),
        Paragraph("<b>Plataforma:</b> Console / PC", s["body"]),
        Paragraph("<b>Taxa EA:</b> 5%", s["body"]),
    ]]
    tbl = Table(data, colWidths=[4.5*cm, 3.5*cm, 4*cm, 3*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREY_LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.5, GREY_MID),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return tbl


def market_context_section(s):
    items = []
    items.append(Paragraph("1. CONTEXTO DO MERCADO (02/06/2026)", s["section_hdr"]))
    items.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    items.append(Spacer(1, 6))

    items.append(Paragraph(
        "<b>Evento Ativo: Festival of Football — pré-lançamento</b>", s["body_bold"]
    ))
    items.append(Spacer(1, 4))

    ctx_text = (
        "O <b>Festival of Football</b> começa oficialmente em <b>5 de junho de 2026</b> e se "
        "estende até 24 de julho. A campanha é construída em torno da Copa do Mundo FIFA 2026 "
        "(EUA/Canadá/México) e traz o maior evento de verão do EA FC 26. Neste momento "
        "(2 de junho), o mercado está na janela de <b>pré-promo</b>: preços em geral "
        "deprimidos pois jogadores vendem cartas para acumular coins antes do evento."
    )
    items.append(Paragraph(ctx_text, s["body"]))
    items.append(Spacer(1, 6))

    bullets = [
        "🟢  <b>Path to Glory</b> (5–19 jun): Cartas dinâmicas com upgrades baseados em desempenho "
        "real das seleções na Copa. Criar demanda massiva por fodder 84–88.",
        "🟢  <b>10x 84+ Upgrade SBC</b> disponível até <b>12 de junho</b>: Demanda urgente por "
        "cartas 84-rated — preços tendem a subir nos próximos 10 dias.",
        "🟡  <b>EVO Undo</b> (ao vivo desde 4 jun): Permite resetar evoluções, liberando cartas "
        "tradable ao mercado. Pode criar leve baixa de preços em cartas evoluídas.",
        "🟡  <b>Greats of the Game</b> (19–26 jun): ICONs Mario Kempes e Rivellino — SBCs de "
        "alto rating gerarão pico de demanda por fodder 87–89 na próxima semana.",
        "🔵  <b>Thursday Flip Window</b>: Rivals Rewards chegam hoje (~17h–18h BRT). "
        "Preços de 85–86 rares deverão subir 30–50% entre 18h e 21h.",
        "🔵  <b>Weekend League começa sexta</b>: Demand por upgrades de squad sobe na "
        "noite de quinta/sexta — janela excelente para vender cartas compradas hoje.",
    ]
    for b in bullets:
        items.append(Paragraph(f"• {b}", s["bullet"]))
        items.append(Spacer(1, 2))

    items.append(Spacer(1, 8))
    items.append(Paragraph(
        "<b>Tendência Geral:</b> Mercado em acumulação pré-promo. Comprar agora e vender "
        "entre quinta 18h e domingo é a janela de maior probabilidade de lucro.",
        s["body_bold"]
    ))
    return items


def cards_table_section(s):
    items = []
    items.append(Paragraph("2. CARTAS RECOMENDADAS", s["section_hdr"]))
    items.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    items.append(Spacer(1, 6))

    intro = (
        "Tabela com jogadores específicos, preços-alvo e margem líquida após dedução da "
        "<b>taxa EA de 5%</b>. Preços baseados em FUTBIN/FUT.GG em 02/06/2026 ~14h UTC. "
        "Margem = (Venda × 0,95) − Compra."
    )
    items.append(Paragraph(intro, s["body"]))
    items.append(Spacer(1, 8))

    hdr_style = ParagraphStyle("th", fontSize=8, textColor=WHITE,
                                fontName="Helvetica-Bold", alignment=TA_CENTER, leading=11)
    cell_style = ParagraphStyle("td", fontSize=8, textColor=colors.HexColor("#111111"),
                                 fontName="Helvetica", alignment=TA_CENTER, leading=11)
    cell_bold = ParagraphStyle("td_b", fontSize=8, textColor=colors.HexColor("#111111"),
                                fontName="Helvetica-Bold", alignment=TA_CENTER, leading=11)
    green_cell = ParagraphStyle("td_g", fontSize=8, textColor=colors.HexColor("#006600"),
                                 fontName="Helvetica-Bold", alignment=TA_CENTER, leading=11)
    note_cell = ParagraphStyle("td_n", fontSize=7, textColor=colors.HexColor("#555555"),
                                fontName="Helvetica-Oblique", alignment=TA_LEFT, leading=10)

    def P(txt, st=cell_style): return Paragraph(str(txt), st)
    def PH(txt): return Paragraph(txt, hdr_style)
    def PB(txt): return Paragraph(str(txt), cell_bold)
    def PG(txt): return Paragraph(str(txt), green_cell)
    def PN(txt): return Paragraph(txt, note_cell)

    headers = [
        PH("Jogador"), PH("Rtg"), PH("Clube"), PH("Pos"),
        PH("Comprar\n(coins)"), PH("Vender\n(coins)"), PH("Margem\nLíquida"), PH("Estratégia")
    ]

    # Cálculo margem: (sell * 0.95) - buy
    rows_data = [
        # (nome, rating, clube, pos, compra, venda, estrategia)
        ("Marcus Thuram",    85, "Inter Milan",      "ST",  950,  1_450, "Flip Diário / 84+ SBC"),
        ("Dani Olmo",        85, "FC Barcelona",     "CAM", 950,  1_450, "Flip Diário / 84+ SBC"),
        ("Phil Foden",       85, "Manchester City",  "RW",  950,  1_450, "Flip Quinta / SBC fodder"),
        ("Scott McTominay",  85, "Napoli",           "CM",  900,  1_400, "Flip Diário / Evolução"),
        ("Upamecano",        85, "Bayern Munich",    "CB",  900,  1_400, "Flip Diário / 84+ SBC"),
        ("Michael Olise",    86, "Bayern Munich",    "RM",  950,  1_600, "SBC fodder / WL prep"),
        ("Bruno Guimarães",  86, "Newcastle",        "CM",  900,  1_550, "SBC fodder / WL prep"),
        ("Claudia Pina",     86, "FC Barcelona",     "LW",  800,  1_400, "Fodder Premium / Greats SBC"),
        ("Alessandro Bastoni",87,"Inter Milan",      "CB",  2_100,2_950, "Greats of the Game SBC"),
        ("Lucy Bronze",      87, "FC Barcelona",     "RB",  2_200,3_050, "Greats of the Game SBC"),
        ("Isco",             84, "Real Betis",       "CAM", 750,  1_200, "10x 84+ Upgrade SBC"),
        ("Rúben Neves",      84, "Al-Hilal",         "CDM", 750,  1_200, "10x 84+ Upgrade SBC"),
        ("Sandro Tonali",    84, "Newcastle",        "CM",  800,  1_250, "10x 84+ Upgrade SBC"),
        ("Orban",            84, "RB Leipzig",       "CB",  750,  1_200, "10x 84+ Upgrade SBC"),
    ]

    table_rows = [headers]
    for (nome, rat, clube, pos, buy, sell, strat) in rows_data:
        margin = int(sell * 0.95) - buy
        margin_pct = round((margin / buy) * 100, 1)
        margin_str = f"+{margin:,}  ({margin_pct}%)"
        table_rows.append([
            PB(nome),
            P(str(rat)),
            P(clube),
            P(pos),
            P(f"{buy:,}"),
            P(f"{sell:,}"),
            PG(margin_str),
            PN(strat),
        ])

    col_w = [3.8*cm, 1.0*cm, 3.2*cm, 0.9*cm, 1.7*cm, 1.7*cm, 2.1*cm, 3.1*cm]
    tbl = Table(table_rows, colWidths=col_w, repeatRows=1)

    ts = TableStyle([
        # header
        ("BACKGROUND", (0, 0), (-1, 0), DARK_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("TOPPADDING", (0, 0), (-1, 0), 7),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
        # alternating rows
        *[("BACKGROUND", (0, i), (-1, i),
           GREY_LIGHT if i % 2 == 1 else colors.HexColor("#E8F4FD"))
          for i in range(1, len(table_rows))],
        # lines
        ("GRID", (0, 0), (-1, -1), 0.4, GREY_MID),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, GOLD),
        # padding
        ("TOPPADDING", (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        # highlight margin col
        ("BACKGROUND", (6, 1), (6, -1), colors.HexColor("#D4EDDA")),
    ])
    tbl.setStyle(ts)
    items.append(tbl)
    return items


def timing_section(s):
    items = []
    items.append(Paragraph("3. ESTRATÉGIA DE TIMING", s["section_hdr"]))
    items.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    items.append(Spacer(1, 6))

    timing_data = [
        ["Período", "Ação", "Motivo"],
        ["Hoje 14h–17h BRT", "COMPRAR 84–86 rares",
         "Mercado calmo pré-rewards; preços no mínimo do dia"],
        ["Hoje 17h–19h BRT", "COMPRAR 87–88 fodder",
         "Rivals Rewards chegam: vendedores 'dumpam' packs"],
        ["Hoje 19h–22h BRT", "VENDER 85-86 rares",
         "Jogadores gastam coins → demanda por squad upgrades"],
        ["Qui–Sex 18h BRT", "VENDER fodder premium",
         "Content drop semanal: novo SBC ou Path to Glory = pico"],
        ["Qui 06h–10h BRT", "COMPRAR dip de madrugada",
         "Volume baixo = preços menores; restock para o dia"],
        ["Sex–Dom qualquer hora", "VENDER Path to Glory alvo",
         "WL players compram upgrades para o torneio"],
        ["Antes de 12/06", "LIQUIDAR 84-rated",
         "SBC 10x 84+ expira: demanda cai após vencimento"],
        ["19–20 jun", "COMPRAR 87-88 fodder",
         "Greats of the Game SBC vai exigir alta fodder rating"],
    ]

    hdr_s = ParagraphStyle("th2", fontSize=8, textColor=WHITE,
                            fontName="Helvetica-Bold", alignment=TA_CENTER, leading=11)
    cell_s = ParagraphStyle("td2", fontSize=8, textColor=colors.HexColor("#111111"),
                             fontName="Helvetica", alignment=TA_LEFT, leading=11)

    def PH(t): return Paragraph(t, hdr_s)
    def PC(t): return Paragraph(t, cell_s)

    tbl_rows = [[PH(h) for h in timing_data[0]]]
    for row in timing_data[1:]:
        tbl_rows.append([PC(c) for c in row])

    tbl = Table(tbl_rows, colWidths=[4*cm, 4.5*cm, 9*cm], repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), DARK_BG),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, GOLD),
        *[("BACKGROUND", (0, i), (-1, i),
           GREY_LIGHT if i % 2 == 1 else colors.HexColor("#E8F4FD"))
          for i in range(1, len(tbl_rows))],
        ("GRID", (0, 0), (-1, -1), 0.4, GREY_MID),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    items.append(tbl)
    return items


def roi_section(s):
    items = []
    items.append(Paragraph("4. ESTIMATIVA DE RETORNO EM 48H", s["section_hdr"]))
    items.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    items.append(Spacer(1, 6))

    scenarios = [
        ["Cenário", "Alocação", "Cartas / Vol.", "Profit Bruto", "Profit Líquido (–5%)", "ROI"],
        # CONSERVADOR
        ["🔵 CONSERVADOR",
         "20.000 c → 85-rares\n10.000 c → 84-rares\n10.000 c → 87 fodder",
         "~21 cartas 85\n~13 cartas 84\n~5 cartas 87",
         "+8.400 c\n+4.550 c\n+3.250 c",
         "+7.980 c\n+4.322 c\n+3.087 c",
         "+38,5%"],
        # OTIMISTA
        ["🟢 OTIMISTA",
         "20.000 c → 85-rares\n10.000 c → 84-rares\n10.000 c → 87 fodder",
         "~21 cartas 85\n~13 cartas 84\n~5 cartas 87",
         "+12.600 c\n+6.500 c\n+5.000 c",
         "+11.970 c\n+6.175 c\n+4.750 c",
         "+57,5%"],
    ]

    hdr_s = ParagraphStyle("th3", fontSize=8, textColor=WHITE,
                            fontName="Helvetica-Bold", alignment=TA_CENTER, leading=11)
    cell_s = ParagraphStyle("td3", fontSize=8, textColor=colors.HexColor("#111111"),
                             fontName="Helvetica", alignment=TA_LEFT, leading=11)
    cell_c = ParagraphStyle("td3c", fontSize=8, textColor=colors.HexColor("#111111"),
                             fontName="Helvetica", alignment=TA_CENTER, leading=11)
    green_s = ParagraphStyle("td3g", fontSize=9, textColor=colors.HexColor("#006600"),
                              fontName="Helvetica-Bold", alignment=TA_CENTER, leading=12)

    def PH(t): return Paragraph(t, hdr_s)
    def PC(t): return Paragraph(t.replace("\n", "<br/>"), cell_s)
    def PCC(t): return Paragraph(t.replace("\n", "<br/>"), cell_c)
    def PG(t): return Paragraph(t, green_s)

    tbl_rows = [[PH(h) for h in scenarios[0]]]
    for i, row in enumerate(scenarios[1:], 1):
        bg = colors.HexColor("#D6EAF8") if i == 1 else colors.HexColor("#D5F5E3")
        tbl_rows.append([
            PCC(row[0]), PC(row[1]), PCC(row[2]),
            PCC(row[3]), PCC(row[4]), PG(row[5])
        ])

    tbl = Table(tbl_rows, colWidths=[2.8*cm, 4.2*cm, 3*cm, 2.5*cm, 3.2*cm, 1.8*cm],
                repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), DARK_BG),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, GOLD),
        ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#D6EAF8")),
        ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#D5F5E3")),
        ("GRID", (0, 0), (-1, -1), 0.4, GREY_MID),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    items.append(tbl)

    items.append(Spacer(1, 8))
    note = (
        "<b>Nota metodológica:</b> Conservador assume 60% das cartas vendidas no preço-alvo; "
        "Otimista assume 90% vendidas. Profit Líquido já desconta a taxa de 5% da EA. "
        "Capital total alocado: 40.000 coins. Considere sempre reservar 10–15% como buffer "
        "para oportunidades emergenciais."
    )
    items.append(Paragraph(note, s["body"]))
    return items


def golden_rules_section(s):
    items = []
    items.append(Paragraph("5. 8 REGRAS DE OURO DO TRADE", s["section_hdr"]))
    items.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    items.append(Spacer(1, 6))

    rules = [
        ("01", "NUNCA compre no pânico nem venda no hype extremo.",
         "Espere a primeira onda de euforia passar (20–40 min após anúncio) para comprar mais barato."),
        ("02", "Sempre calcule a margem APÓS a taxa de 5%.",
         "Uma venda de 1.000 coins rende 950 coins. Nunca ignore esse corte na equação."),
        ("03", "Diversifique: máximo 40% do budget em um único tipo de carta.",
         "Concentração mata o capital. Se um SBC for removido, você perde tudo de uma vez."),
        ("04", "Defina stop-loss antes de comprar.",
         "Se o preço de uma carta cair 25% abaixo do seu preço de compra, venda imediatamente sem hesitar."),
        ("05", "Compre na madrugada / manhã cedo; venda no content drop.",
         "Volume baixo → preços baixos (madrugada BRT). Volume alto → preços altos (18h–22h BRT)."),
        ("06", "Monitore o calendário de SBCs ativamente.",
         "Um SBC novo pode dobrar o preço de uma carta em 15 minutos. Esteja pronto."),
        ("07", "Foque em volume, não em margens unitárias gigantes.",
         "30 cartas com +400 coins cada = 12.000 coins. Melhor que 2 cartas com esperança de 6.000."),
        ("08", "Venda ANTES do fim do evento, não depois.",
         "Quando o promo acaba, os preços despencam. Liquide 2–3 dias antes do encerramento."),
    ]

    rule_style_num = ParagraphStyle("rn", fontSize=14, textColor=GOLD,
                                     fontName="Helvetica-Bold", alignment=TA_CENTER, leading=16)
    rule_style_title = ParagraphStyle("rt", fontSize=10, textColor=DARK_BG,
                                       fontName="Helvetica-Bold", leading=13)
    rule_style_desc = ParagraphStyle("rd", fontSize=9, textColor=colors.HexColor("#333333"),
                                      fontName="Helvetica", leading=13, alignment=TA_JUSTIFY)

    rule_rows = []
    for i in range(0, len(rules), 2):
        row_cells = []
        for j in range(2):
            if i + j < len(rules):
                num, title, desc = rules[i + j]
                cell_content = [
                    Paragraph(num, rule_style_num),
                    Paragraph(title, rule_style_title),
                    Spacer(1, 3),
                    Paragraph(desc, rule_style_desc),
                ]
                row_cells.append(cell_content)
            else:
                row_cells.append("")
        rule_rows.append(row_cells)

    for row in rule_rows:
        tbl = Table([row], colWidths=[8.3*cm, 8.3*cm])
        bg_colors = [
            colors.HexColor("#FFF9E6"), colors.HexColor("#E6F7FF"),
            colors.HexColor("#E6FFE6"), colors.HexColor("#FFE6E6"),
        ]
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), bg_colors[rule_rows.index(row) % 4]),
            ("BACKGROUND", (1, 0), (1, 0), bg_colors[(rule_rows.index(row) + 1) % 4]),
            ("BOX", (0, 0), (0, 0), 1, GREY_MID),
            ("BOX", (1, 0), (1, 0), 1, GREY_MID),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        items.append(tbl)
        items.append(Spacer(1, 4))

    return items


def disclaimer_section(s):
    items = []
    items.append(HRFlowable(width="100%", thickness=0.5, color=GREY_MID))
    items.append(Spacer(1, 6))
    disc = (
        "DISCLAIMER: Este relatório é gerado automaticamente com fins educacionais e de entretenimento. "
        "Os preços apresentados são estimativas baseadas em dados públicos de FUTBIN, FUT.GG e outras "
        "fontes abertas no momento da geração. O mercado do EA FC 26 Ultimate Team é altamente volátil "
        "e pode mudar em questão de minutos após um novo anúncio da EA Sports. Não há garantia de lucro. "
        "Decisões de compra e venda são de responsabilidade exclusiva do trader. "
        "EA Sports FC 26 é marca registrada da Electronic Arts Inc."
    )
    items.append(Paragraph(disc, s["disclaimer"]))
    items.append(Spacer(1, 4))
    items.append(Paragraph(
        f"Relatório gerado em {REPORT_DATE} UTC  •  github.com/kaiohsferreira/fifa-trading",
        s["disclaimer"]
    ))
    return items


def build_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=1.8*cm,
        leftMargin=1.8*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm,
        title="Relatório Trading EA FC 26",
        author="fifa-trading bot",
        subject="EA FC 26 Ultimate Team Market Analysis",
    )

    s = build_styles()
    story = []

    # Header block
    story.append(header_table(s))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        f"Análise de Mercado  •  {REPORT_DATE} UTC  •  Budget: 40.000 coins",
        s["subtitle"]
    ))
    story.append(Spacer(1, 6))
    story.append(info_band(s, REPORT_DATE))
    story.append(Spacer(1, 14))

    # Sections
    for elem in market_context_section(s):
        story.append(elem)
    story.append(Spacer(1, 10))

    for elem in cards_table_section(s):
        story.append(elem)
    story.append(Spacer(1, 10))

    for elem in timing_section(s):
        story.append(elem)
    story.append(Spacer(1, 10))

    for elem in roi_section(s):
        story.append(elem)
    story.append(Spacer(1, 10))

    for elem in golden_rules_section(s):
        story.append(elem)

    for elem in disclaimer_section(s):
        story.append(elem)

    doc.build(story)
    print(f"PDF gerado: {output_path}")


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(__file__), FILENAME)
    build_pdf(out)
