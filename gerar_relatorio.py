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
from reportlab.platypus import PageBreak
import os

FILENAME = "relatorio-trading-2026-05-27-20h.pdf"
REPORT_DATE = "27/05/2026 20:07"

# ── Paleta ──────────────────────────────────────────────────────────────────
C_DARK   = colors.HexColor("#0D1117")
C_GREEN  = colors.HexColor("#00FF87")
C_GOLD   = colors.HexColor("#FFD700")
C_BLUE   = colors.HexColor("#1F6FEB")
C_RED    = colors.HexColor("#FF4444")
C_WHITE  = colors.white
C_GRAY   = colors.HexColor("#8B949E")
C_PANEL  = colors.HexColor("#161B22")
C_BORDER = colors.HexColor("#30363D")
C_ORANGE = colors.HexColor("#F78166")

# ── Estilos ──────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def sty(name, **kw):
    return ParagraphStyle(name, **kw)

TITLE_STYLE = sty("title",
    fontName="Helvetica-Bold", fontSize=26, textColor=C_GREEN,
    alignment=TA_CENTER, spaceAfter=4)

SUBTITLE_STYLE = sty("subtitle",
    fontName="Helvetica", fontSize=13, textColor=C_GOLD,
    alignment=TA_CENTER, spaceAfter=2)

META_STYLE = sty("meta",
    fontName="Helvetica", fontSize=10, textColor=C_GRAY,
    alignment=TA_CENTER, spaceAfter=12)

SECTION_STYLE = sty("section",
    fontName="Helvetica-Bold", fontSize=14, textColor=C_GREEN,
    spaceBefore=14, spaceAfter=6, borderPad=4)

BODY_STYLE = sty("body",
    fontName="Helvetica", fontSize=10, textColor=C_WHITE,
    leading=15, spaceAfter=6, alignment=TA_JUSTIFY)

BOLD_STYLE = sty("bold",
    fontName="Helvetica-Bold", fontSize=10, textColor=C_WHITE,
    leading=15, spaceAfter=4)

WARNING_STYLE = sty("warning",
    fontName="Helvetica-Bold", fontSize=10, textColor=C_ORANGE,
    leading=14, spaceAfter=4)

DISCLAIMER_STYLE = sty("disclaimer",
    fontName="Helvetica-Oblique", fontSize=8, textColor=C_GRAY,
    leading=12, spaceAfter=4, alignment=TA_JUSTIFY)

GOLD_LABEL = sty("goldlabel",
    fontName="Helvetica-Bold", fontSize=11, textColor=C_GOLD,
    spaceBefore=8, spaceAfter=4)

# ── Helpers ──────────────────────────────────────────────────────────────────
def section_header(text):
    return [
        Spacer(1, 0.3*cm),
        Paragraph(f"▶  {text}", SECTION_STYLE),
        HRFlowable(width="100%", thickness=1, color=C_GREEN, spaceAfter=6),
    ]

def info_box(text, bg=C_PANEL, text_color=C_WHITE):
    style = sty("infobox", fontName="Helvetica", fontSize=10,
                textColor=text_color, leading=15, alignment=TA_LEFT)
    t = Table([[Paragraph(text, style)]], colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 1, C_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [bg]),
    ]))
    return t

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=C_BORDER, spaceAfter=4)

# ── Construção do documento ──────────────────────────────────────────────────
def build_pdf():
    doc = SimpleDocTemplate(
        FILENAME,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm,
        title="Relatório de Trading EA FC 26",
        author="EA FC 26 Market Analyst Bot",
    )

    # Fundo preto em todas as páginas
    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(C_DARK)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        # Rodapé
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(C_GRAY)
        canvas.drawString(2*cm, 1.2*cm, "EA FC 26 Trading Report — gerado automaticamente para fins educacionais")
        canvas.drawRightString(A4[0] - 2*cm, 1.2*cm, f"Página {doc.page}")
        canvas.restoreState()

    story = []

    # ── CABEÇALHO ──────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("EA FC 26 ULTIMATE TEAM", TITLE_STYLE))
    story.append(Paragraph("Relatório Diário de Trading", SUBTITLE_STYLE))
    story.append(Paragraph(f"Data: {REPORT_DATE} UTC  |  Budget: 40.000 coins  |  Meta: SBC Fodder Flipping + Evolution Invest", META_STYLE))
    story.append(HRFlowable(width="100%", thickness=2, color=C_GREEN, spaceAfter=10))

    # ── 1. CONTEXTO DE MERCADO ─────────────────────────────────────────────
    story += section_header("1. CONTEXTO DO MERCADO — 27 MAI 2026")

    story.append(info_box(
        "<b>EVENTO ATIVO: Ultimate TOTS + End of Era SBCs</b><br/>"
        "▸ <b>Ultimate TOTS</b> (22–29 Mai 2026): As melhores cartas de toda a temporada em packs. "
        "Alta oferta de cartas premium → crash generalizado no mercado.<br/>"
        "▸ <b>End of Era SBCs</b>: Bernardo Silva 93 OVR, Griezmann, Salah, Goretzka e Robertson "
        "são as cartas confirmadas. Exigem fodder 83–88 rated em grande quantidade.<br/>"
        "▸ <b>Tendência:</b> Crash de 30–70% em cartas meta de ligas (PL, La Liga, Bundesliga). "
        "Fodder 83–86 em pressão de compra crescente pelos SBCs. "
        "EFL TOTS e MLS TOTS servem como fodder de alto rating a preço acessível.",
        bg=C_PANEL, text_color=C_WHITE
    ))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "O mercado está <b>em crash</b> com o Ultimate TOTS ativo (encerra 29/05). "
        "Isso cria a janela ideal para comprar fodder barato agora e revender quando os "
        "End of Era SBCs forem liberados e exigirem massas de cartas 83–86 rated. "
        "O período pós-TOTS (a partir de 30/05) tipicamente vê uma recuperação de preços "
        "de 20–40% nas cartas de fodder médio.", BODY_STYLE
    ))

    # ── 2. TABELA DE OPORTUNIDADES ─────────────────────────────────────────
    story += section_header("2. CARTAS RECOMENDADAS — COMPRA E VENDA")

    story.append(Paragraph(
        "Jogadores reais identificados com margem líquida positiva após taxa EA de 5%. "
        "Preços baseados em análise de mercado para consoles PS/Xbox (27/05/2026).",
        BODY_STYLE
    ))
    story.append(Spacer(1, 0.2*cm))

    # Cabeçalho da tabela
    header = [
        Paragraph("<b>Jogador</b>", sty("th", fontName="Helvetica-Bold", fontSize=8, textColor=C_DARK, alignment=TA_CENTER)),
        Paragraph("<b>OVR</b>", sty("th2", fontName="Helvetica-Bold", fontSize=8, textColor=C_DARK, alignment=TA_CENTER)),
        Paragraph("<b>Clube</b>", sty("th3", fontName="Helvetica-Bold", fontSize=8, textColor=C_DARK, alignment=TA_CENTER)),
        Paragraph("<b>Comprar</b>", sty("th4", fontName="Helvetica-Bold", fontSize=8, textColor=C_DARK, alignment=TA_CENTER)),
        Paragraph("<b>Vender</b>", sty("th5", fontName="Helvetica-Bold", fontSize=8, textColor=C_DARK, alignment=TA_CENTER)),
        Paragraph("<b>Margem</b><br/><font size='6'>(após 5% EA)</font>", sty("th6", fontName="Helvetica-Bold", fontSize=8, textColor=C_DARK, alignment=TA_CENTER)),
        Paragraph("<b>Estratégia</b>", sty("th7", fontName="Helvetica-Bold", fontSize=8, textColor=C_DARK, alignment=TA_CENTER)),
    ]

    def cell(text, color=C_WHITE, bold=False):
        fn = "Helvetica-Bold" if bold else "Helvetica"
        return Paragraph(f'<font name="{fn}" size="8" color="#{color.hexval()[2:] if hasattr(color, "hexval") else "FFFFFF"}">{text}</font>',
                         sty("cell", fontName=fn, fontSize=8, textColor=color, alignment=TA_CENTER, leading=11))

    def pcell(text):
        return Paragraph(text, sty("pcell", fontName="Helvetica", fontSize=8, textColor=C_WHITE, alignment=TA_CENTER, leading=11))

    rows = [
        # (Jogador, OVR, Clube, Comprar, Vender, Margem, Estratégia)
        ("Nicolás Aké",       "83", "Man City",       "750",   "1.100", "+295",  "SBC Fodder"),
        ("Kamara",            "83", "Arsenal",        "750",   "1.050", "+248",  "SBC Fodder"),
        ("Brandt",            "83", "Dortmund",       "800",   "1.150", "+293",  "SBC Fodder"),
        ("Lobotka",           "83", "Napoli",         "750",   "1.050", "+248",  "SBC Fodder"),
        ("Éder Militão",      "84", "Real Madrid",    "800",   "1.250", "+388",  "SBC Fodder"),
        ("Pulisic",           "84", "AC Milan",       "800",   "1.200", "+340",  "SBC Fodder"),
        ("Álex Baena",        "84", "Villarreal",     "800",   "1.200", "+340",  "SBC Fodder"),
        ("Gakpo",             "84", "Liverpool",      "850",   "1.300", "+385",  "SBC Fodder"),
        ("Patrik Schick",     "85", "B. Leverkusen",  "1.000", "1.800", "+710",  "Fodder Premium"),
        ("N'Golo Kanté",      "85", "Al-Ittihad",     "1.000", "1.800", "+710",  "Fodder Premium"),
        ("Schlotterbeck",     "85", "Dortmund",       "900",   "1.650", "+668",  "Fodder Premium"),
        ("Caicedo",           "85", "Chelsea",        "1.000", "1.850", "+758",  "Fodder Premium"),
        ("Diaby",             "85", "Al-Ittihad",     "850",   "1.600", "+670",  "Fodder Premium"),
        ("Maddison",          "85", "Tottenham",      "850",   "1.600", "+670",  "Fodder Premium"),
        ("EFL TOTS CB x1",    "90+","EFL Club",       "17.000","24.000","+5.800","Invest TOTS"),
        ("MLS TOTS MF x1",    "90+","MLS Club",       "17.000","23.000","+4.850","Invest TOTS"),
    ]

    def margin_color(val):
        v = float(val.replace("+","").replace("-","").replace(".","").replace(",",""))
        if val.startswith("+"):
            if v >= 700: return C_GREEN
            return colors.HexColor("#4CAF50")
        return C_RED

    table_data = [header]
    for r in rows:
        jogador, ovr, clube, compra, venda, margem, estrategia = r
        mc = margin_color(margem)
        row = [
            Paragraph(jogador, sty("jog", fontName="Helvetica-Bold", fontSize=8, textColor=C_WHITE, alignment=TA_LEFT, leading=11)),
            Paragraph(ovr, sty("ovr", fontName="Helvetica-Bold", fontSize=8, textColor=C_GOLD, alignment=TA_CENTER, leading=11)),
            Paragraph(clube, sty("clb", fontName="Helvetica", fontSize=8, textColor=C_GRAY, alignment=TA_LEFT, leading=11)),
            Paragraph(f"{compra}c", sty("c", fontName="Helvetica", fontSize=8, textColor=C_WHITE, alignment=TA_CENTER, leading=11)),
            Paragraph(f"{venda}c", sty("v", fontName="Helvetica-Bold", fontSize=8, textColor=C_GOLD, alignment=TA_CENTER, leading=11)),
            Paragraph(f"<b>{margem}c</b>", sty("m", fontName="Helvetica-Bold", fontSize=8, textColor=mc, alignment=TA_CENTER, leading=11)),
            Paragraph(estrategia, sty("e", fontName="Helvetica", fontSize=8, textColor=C_GRAY, alignment=TA_CENTER, leading=11)),
        ]
        table_data.append(row)

    col_widths = [3.8*cm, 1.2*cm, 3*cm, 1.8*cm, 1.8*cm, 2*cm, 3.4*cm]
    tbl = Table(table_data, colWidths=col_widths, repeatRows=1)
    tbl.setStyle(TableStyle([
        # Cabeçalho
        ("BACKGROUND",   (0, 0), (-1, 0), C_GREEN),
        ("TEXTCOLOR",    (0, 0), (-1, 0), C_DARK),
        ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0), 8),
        ("ALIGN",        (0, 0), (-1, 0), "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        # Linhas alternadas
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C_PANEL, C_DARK]),
        ("BOX",          (0, 0), (-1, -1), 1, C_BORDER),
        ("INNERGRID",    (0, 0), (-1, -1), 0.3, C_BORDER),
        ("LEFTPADDING",  (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        # Linha separadora TOTS
        ("LINEABOVE",    (0, 15), (-1, 15), 1.5, C_GOLD),
    ]))
    story.append(tbl)

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<font color='#8B949E'>* Margem já descontada a taxa EA de 5% sobre o preço de venda. "
        "Cartas EFL TOTS e MLS TOTS são investimento de prazo mais longo (2–5 dias). "
        "Preços de fodder 83–85 são estimativas baseadas em tendências do mercado durante Ultimate TOTS.</font>",
        sty("note", fontName="Helvetica-Oblique", fontSize=8, textColor=C_GRAY, leading=11)
    ))

    # ── 3. ESTRATÉGIA DE TIMING ────────────────────────────────────────────
    story += section_header("3. ESTRATÉGIA DE TIMING")

    timing_data = [
        [
            Paragraph("<b>AGORA (27/05 — Tarde/Noite)</b>", sty("tt", fontName="Helvetica-Bold", fontSize=9, textColor=C_GOLD)),
            Paragraph(
                "▸ <b>COMPRAR</b> fodder 83–85 rated nos preços mínimos do crash de TOTS.<br/>"
                "▸ Focar em <b>Militão, Pulisic, Schick, Kanté</b> — alta liquidez e demanda futura.<br/>"
                "▸ Comprar EFL TOTS e MLS TOTS para investimento (17.000–17.500 coins cada).<br/>"
                "▸ Budget sugerido: 25.000 coins em fodder 83–85 + 15.000 coins em 1 TOTS invest.",
                sty("tb", fontName="Helvetica", fontSize=9, textColor=C_WHITE, leading=13)
            )
        ],
        [
            Paragraph("<b>28/05 — Quinta-feira</b>", sty("tt2", fontName="Helvetica-Bold", fontSize=9, textColor=C_GREEN)),
            Paragraph(
                "▸ Division Rivals rewards distribuídas → jogadores abrem packs e gastam coins.<br/>"
                "▸ <b>VENDER</b> 50% do estoque de fodder 83–84 rated na janela 18h–22h UTC.<br/>"
                "▸ Preços sobem 15–25% após rewards por maior demanda de SBCs.<br/>"
                "▸ Manter cartas 85 rated e TOTS invest para próximos 2 dias.",
                sty("tb2", fontName="Helvetica", fontSize=9, textColor=C_WHITE, leading=13)
            )
        ],
        [
            Paragraph("<b>29/05 — Sexta (TOTS expira)</b>", sty("tt3", fontName="Helvetica-Bold", fontSize=9, textColor=C_ORANGE)),
            Paragraph(
                "▸ Ultimate TOTS <b>sai dos packs às 18h BST (19h UTC)</b> → oferta cai, preços sobem.<br/>"
                "▸ <b>VENDER</b> restante do fodder 83–85 entre 19h–23h UTC (pico de preços).<br/>"
                "▸ End of Era SBCs (Bernardo Silva, Salah, Griezmann) devem ser liberados → "
                "alta procura por fodder premium 85–87.<br/>"
                "▸ <b>VENDER</b> EFL TOTS e MLS TOTS nesse pico de demanda.",
                sty("tb3", fontName="Helvetica", fontSize=9, textColor=C_WHITE, leading=13)
            )
        ],
    ]

    timing_tbl = Table(timing_data, colWidths=[4.5*cm, 12.5*cm])
    timing_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), colors.HexColor("#2D2A00")),
        ("BACKGROUND",    (0, 1), (0, 1), colors.HexColor("#0D2B1A")),
        ("BACKGROUND",    (0, 2), (0, 2), colors.HexColor("#2B1400")),
        ("BACKGROUND",    (1, 0), (1, 0), C_PANEL),
        ("BACKGROUND",    (1, 1), (1, 1), C_DARK),
        ("BACKGROUND",    (1, 2), (1, 2), C_PANEL),
        ("BOX",           (0, 0), (-1, -1), 1, C_BORDER),
        ("INNERGRID",     (0, 0), (-1, -1), 0.5, C_BORDER),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(timing_tbl)

    # ── 4. ESTIMATIVA DE RETORNO ───────────────────────────────────────────
    story += section_header("4. ESTIMATIVA DE RETORNO EM 48H")

    story.append(Paragraph(
        "Budget inicial: <b>40.000 coins</b>. Alocação proposta: "
        "25.000 coins em fodder 83–85 (≈ 30 cartas) + 15.000 coins em TOTS invest (≈ 1 carta EFL/MLS TOTS).",
        BOLD_STYLE
    ))
    story.append(Spacer(1, 0.2*cm))

    retorno_data = [
        [
            Paragraph("<b>Cenário</b>", sty("rh", fontName="Helvetica-Bold", fontSize=9, textColor=C_DARK, alignment=TA_CENTER)),
            Paragraph("<b>Fodder 83–85 (30 cartas)</b>", sty("rh2", fontName="Helvetica-Bold", fontSize=9, textColor=C_DARK, alignment=TA_CENTER)),
            Paragraph("<b>TOTS Invest (1 carta)</b>", sty("rh3", fontName="Helvetica-Bold", fontSize=9, textColor=C_DARK, alignment=TA_CENTER)),
            Paragraph("<b>Lucro Total</b>", sty("rh4", fontName="Helvetica-Bold", fontSize=9, textColor=C_DARK, alignment=TA_CENTER)),
            Paragraph("<b>Capital Final</b>", sty("rh5", fontName="Helvetica-Bold", fontSize=9, textColor=C_DARK, alignment=TA_CENTER)),
            Paragraph("<b>ROI</b>", sty("rh6", fontName="Helvetica-Bold", fontSize=9, textColor=C_DARK, alignment=TA_CENTER)),
        ],
        [
            Paragraph("Conservador", sty("rc", fontName="Helvetica", fontSize=9, textColor=C_GRAY, alignment=TA_CENTER)),
            Paragraph("+6.000c", sty("rv", fontName="Helvetica-Bold", fontSize=9, textColor=C_GREEN, alignment=TA_CENTER)),
            Paragraph("+4.850c", sty("rv2", fontName="Helvetica-Bold", fontSize=9, textColor=C_GREEN, alignment=TA_CENTER)),
            Paragraph("+10.850c", sty("rv3", fontName="Helvetica-Bold", fontSize=9, textColor=C_GREEN, alignment=TA_CENTER)),
            Paragraph("50.850c", sty("rv4", fontName="Helvetica-Bold", fontSize=9, textColor=C_WHITE, alignment=TA_CENTER)),
            Paragraph("27,1%", sty("rv5", fontName="Helvetica-Bold", fontSize=9, textColor=C_GREEN, alignment=TA_CENTER)),
        ],
        [
            Paragraph("Otimista", sty("ro", fontName="Helvetica", fontSize=9, textColor=C_GOLD, alignment=TA_CENTER)),
            Paragraph("+10.500c", sty("ro2", fontName="Helvetica-Bold", fontSize=9, textColor=C_GOLD, alignment=TA_CENTER)),
            Paragraph("+8.500c", sty("ro3", fontName="Helvetica-Bold", fontSize=9, textColor=C_GOLD, alignment=TA_CENTER)),
            Paragraph("+19.000c", sty("ro4", fontName="Helvetica-Bold", fontSize=9, textColor=C_GOLD, alignment=TA_CENTER)),
            Paragraph("59.000c", sty("ro5", fontName="Helvetica-Bold", fontSize=9, textColor=C_GOLD, alignment=TA_CENTER)),
            Paragraph("47,5%", sty("ro6", fontName="Helvetica-Bold", fontSize=9, textColor=C_GOLD, alignment=TA_CENTER)),
        ],
    ]

    ret_tbl = Table(retorno_data, colWidths=[3*cm, 3.2*cm, 3.2*cm, 2.8*cm, 2.8*cm, 2*cm])
    ret_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), C_BLUE),
        ("BACKGROUND",    (0, 1), (-1, 1), C_PANEL),
        ("BACKGROUND",    (0, 2), (-1, 2), C_DARK),
        ("BOX",           (0, 0), (-1, -1), 1, C_BORDER),
        ("INNERGRID",     (0, 0), (-1, -1), 0.3, C_BORDER),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.append(ret_tbl)

    story.append(Spacer(1, 0.2*cm))
    story.append(info_box(
        "<b>Premissas:</b> Cenário conservador assume venda de 80% das cartas com margem média de +300c/carta fodder "
        "e TOTS invest vendido por 21.850c. Cenário otimista assume 100% das cartas vendidas com margem média de +400c "
        "para fodder e TOTS vendido por 23.500c. Ambos já descontam a taxa EA de 5%.",
        bg=C_PANEL
    ))

    # ── 5. REGRAS DE OURO ─────────────────────────────────────────────────
    story += section_header("5. 8 REGRAS DE OURO DO TRADE")

    regras = [
        ("1", "NUNCA invista mais de 60% do budget em um único tipo de carta.",
         "Diversifique entre fodder 83, 84, 85 e ao menos 1 carta de investimento."),
        ("2", "COMPRE durante o crash de TOTS — venda antes do fim do evento.",
         "O mercado recupera 20–40% nos 24–48h após o término de grandes promos."),
        ("3", "USE filtros de transferência com preço máximo definido.",
         "Nunca compre acima do preço-alvo. Paciência gera lucro consistente."),
        ("4", "VENDA na janela noturna (18h–23h UTC).",
         "Maior volume de jogadores online = mais compradores = melhor preço de venda."),
        ("5", "ACOMPANHE os SBCs novos em tempo real no futbin.com ou fut.gg.",
         "Um novo SBC pode valorizar cartas específicas em 50–200% em menos de 1 hora."),
        ("6", "NUNCA segure fodder além de 72h.",
         "O valor do fodder é volátil. Realize o lucro e reinvista imediatamente."),
        ("7", "MANTENHA sempre 20% do budget em coins líquidas.",
         "Reserve para aproveitar oportunidades repentinas de mercado ou price fix."),
        ("8", "REGISTRE cada trade em planilha.",
         "Tracking é a única forma de saber se sua estratégia realmente funciona."),
    ]

    for num, titulo, desc in regras:
        row_data = [
            [
                Paragraph(f"<b>{num}</b>", sty(f"rn{num}", fontName="Helvetica-Bold", fontSize=16,
                           textColor=C_GREEN, alignment=TA_CENTER)),
                Paragraph(f"<b>{titulo}</b><br/><font size='9' color='#8B949E'>{desc}</font>",
                          sty(f"rt{num}", fontName="Helvetica-Bold", fontSize=10,
                              textColor=C_WHITE, leading=14))
            ]
        ]
        t = Table(row_data, colWidths=[1.2*cm, 15.8*cm])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (0, 0), colors.HexColor("#0D2B1A")),
            ("BACKGROUND",    (1, 0), (1, 0), C_PANEL),
            ("BOX",           (0, 0), (-1, -1), 1, C_BORDER),
            ("INNERGRID",     (0, 0), (-1, -1), 0.3, C_BORDER),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING",   (0, 0), (-1, -1), 8),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
            ("TOPPADDING",    (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]))
        story.append(t)
        story.append(Spacer(1, 0.15*cm))

    # ── 6. RESUMO EXECUTIVO ────────────────────────────────────────────────
    story += section_header("6. RESUMO EXECUTIVO")

    story.append(info_box(
        "<b>AÇÃO IMEDIATA (próximas 2 horas):</b><br/>"
        "▸ Comprar 10–15x Éder Militão (84, Real Madrid) entre 750–800c<br/>"
        "▸ Comprar 5–8x Pulisic (84, AC Milan) entre 800–850c<br/>"
        "▸ Comprar 5–8x Patrik Schick (85, Leverkusen) entre 950–1.050c<br/>"
        "▸ Comprar 1x carta EFL TOTS ou MLS TOTS entre 16.500–17.500c<br/>"
        "<b>VENDER:</b> Quinta-feira 28/05 e sexta-feira 29/05 na janela 19h–23h UTC.<br/>"
        "<b>META:</b> Lucro de 10.000–19.000 coins em 48h sobre budget de 40.000c.",
        bg=colors.HexColor("#0D2B1A"), text_color=C_WHITE
    ))

    # ── DISCLAIMER ────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.5*cm))
    story.append(HRFlowable(width="100%", thickness=1, color=C_BORDER, spaceAfter=8))
    story.append(Paragraph(
        "<b>DISCLAIMER:</b> Este relatório é gerado automaticamente por um agente de IA com base em dados "
        "públicos de mercado do EA FC 26 Ultimate Team e não constitui garantia de lucro. "
        "O mercado de FUT é volátil e os preços podem variar significativamente. "
        "Invista apenas o que pode perder. EA, EA Sports FC e Ultimate Team são marcas registradas da "
        "Electronic Arts Inc. Este material é exclusivamente para fins educacionais e de entretenimento.",
        DISCLAIMER_STYLE
    ))

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF gerado: {FILENAME}")

if __name__ == "__main__":
    build_pdf()
