#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.colors import HexColor
import os

# ── Paleta ──────────────────────────────────────────────────────────────────
VERDE_EA    = HexColor("#00C48C")
VERDE_ESCURO= HexColor("#007A5C")
CINZA_FUNDO = HexColor("#F4F6F8")
CINZA_BORDA = HexColor("#D0D5DD")
AZUL_TITULO = HexColor("#1A1F36")
LARANJA     = HexColor("#F59E0B")
VERMELHO    = HexColor("#EF4444")
BRANCO      = colors.white

DATA_HORA    = "29/05/2026 14:06"
NOME_ARQUIVO = "relatorio-trading-2026-05-29-14h.pdf"

# ── Helpers de estilo ────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    def add(name, **kw):
        base.add(ParagraphStyle(name=name, **kw))

    add("Titulo",
        fontName="Helvetica-Bold", fontSize=22, textColor=BRANCO,
        alignment=TA_CENTER, spaceAfter=4)
    add("Subtitulo",
        fontName="Helvetica", fontSize=11, textColor=HexColor("#C9FFE8"),
        alignment=TA_CENTER, spaceAfter=2)
    add("DataHora",
        fontName="Helvetica-Bold", fontSize=10, textColor=HexColor("#A3FDD8"),
        alignment=TA_CENTER, spaceAfter=0)
    add("SecHead",
        fontName="Helvetica-Bold", fontSize=13, textColor=AZUL_TITULO,
        spaceBefore=14, spaceAfter=6, borderPad=0)
    add("Body",
        fontName="Helvetica", fontSize=9.5, textColor=HexColor("#374151"),
        leading=15, alignment=TA_JUSTIFY, spaceAfter=4)
    add("BulletItem",
        fontName="Helvetica", fontSize=9.5, textColor=HexColor("#374151"),
        leading=15, leftIndent=14, spaceAfter=3)
    add("BulletBold",
        fontName="Helvetica-Bold", fontSize=9.5, textColor=AZUL_TITULO,
        leading=15, leftIndent=14, spaceAfter=3)
    add("Disclaimer",
        fontName="Helvetica-Oblique", fontSize=8, textColor=HexColor("#6B7280"),
        leading=12, alignment=TA_JUSTIFY)
    add("CellHeader",
        fontName="Helvetica-Bold", fontSize=8.5, textColor=BRANCO,
        alignment=TA_CENTER)
    add("CellBody",
        fontName="Helvetica", fontSize=8.5, textColor=HexColor("#1F2937"),
        alignment=TA_CENTER)
    add("CellGreen",
        fontName="Helvetica-Bold", fontSize=8.5, textColor=VERDE_ESCURO,
        alignment=TA_CENTER)
    add("Tag",
        fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO,
        alignment=TA_CENTER)
    return base


def header_block(styles):
    """Banner verde no topo."""
    data = [[Paragraph("EA FC 26 ULTIMATE TEAM", styles["Titulo"]),
             Paragraph("Relatório Diário de Trading", styles["Subtitulo"]),
             Paragraph(f"Gerado em: {DATA_HORA} UTC", styles["DataHora"])]]
    t = Table(data, colWidths=[17.2*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), VERDE_EA),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [VERDE_EA]),
        ("TOPPADDING",    (0,0), (-1,-1), 18),
        ("BOTTOMPADDING", (0,0), (-1,-1), 18),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("RIGHTPADDING",  (0,0), (-1,-1), 12),
        ("ROUNDEDCORNERS", [8]),
    ]))
    return t


def info_strip(styles):
    """Faixa de resumo rápido."""
    cells = [
        [Paragraph("💰 Budget", styles["Tag"]),
         Paragraph("40.000 coins", styles["Tag"])],
        [Paragraph("📅 Evento", styles["Tag"]),
         Paragraph("TOTS Final → Festival of Football", styles["Tag"])],
        [Paragraph("🎯 Meta", styles["Tag"]),
         Paragraph("SBC Fodder + Evo Invest", styles["Tag"])],
        [Paragraph("⏱ Horizonte", styles["Tag"]),
         Paragraph("2–7 dias", styles["Tag"])],
    ]
    flat = [[c for pair in cells for c in pair]]
    t = Table(flat, colWidths=[2.15*cm]*8)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (1,0), VERDE_ESCURO),
        ("BACKGROUND", (2,0), (3,0), HexColor("#1D4ED8")),
        ("BACKGROUND", (4,0), (5,0), HexColor("#7C3AED")),
        ("BACKGROUND", (6,0), (7,0), HexColor("#D97706")),
        ("TEXTCOLOR", (0,0), (-1,-1), BRANCO),
        ("FONTNAME",  (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE",  (0,0), (-1,-1), 8),
        ("ALIGN",     (0,0), (-1,-1), "CENTER"),
        ("VALIGN",    (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    return t


def section_head(text, styles):
    bar = HRFlowable(width="100%", thickness=2, color=VERDE_EA, spaceAfter=4)
    head = Paragraph(text, styles["SecHead"])
    return [bar, head]


def cards_table(styles):
    """Tabela principal de cartas recomendadas."""
    headers = [
        "Jogador", "OVR", "Clube / Liga", "Tipo",
        "Compra\n(coins)", "Venda\n(coins)", "Margem\n(líq. 5%)", "ROI %"
    ]

    # Colunas: nome | rating | clube | tipo | compra | venda | margem | roi
    rows = [
        # ── SBC Fodder ──
        ["Rubén Díaz",       "86", "Man. City / PL",     "Fodder 86",  "750",   "1.400",  "+580",  "77%"],
        ["H. Çalhanoğlu",    "86", "Inter / Serie A",    "Fodder 86",  "1.000", "1.800",  "+710",  "71%"],
        ["Romelu Lukaku",    "84", "AS Roma / Serie A",  "Fodder 84",  "750",   "1.250",  "+438",  "58%"],
        ["Jonathan Tah",     "84", "B. Leverkusen / BL", "Fodder 84",  "700",   "1.200",  "+440",  "63%"],
        ["Bernardo Silva",   "87", "Man. City / PL",     "Fodder 87",  "1.500", "2.800",  "+1.160","77%"],
        ["Theo Hernández",   "87", "AC Milan / Serie A", "Fodder 87",  "1.800", "3.200",  "+1.240","69%"],
        # ── Evolution ──
        ["Pedri",            "88", "FC Barcelona / LL",  "Evo Cand.",  "3.000", "6.500",  "+3.175","106%"],
        ["Phil Foden",       "88", "Man. City / PL",     "Evo Cand.",  "2.800", "6.000",  "+2.900","104%"],
        # ── Festival of Football Prep ──
        ["Lamine Yamal",     "88", "FC Barcelona / LL",  "FoF Prep",   "5.000", "10.000", "+4.500","90%"],
        ["Jude Bellingham",  "91", "Real Madrid / LL",   "FoF Prep",   "12.000","22.000", "+8.900","74%"],
    ]

    col_w = [3.6*cm, 1.1*cm, 3.4*cm, 2.0*cm, 1.6*cm, 1.6*cm, 1.7*cm, 1.2*cm]

    head_row = [Paragraph(h, styles["CellHeader"]) for h in headers]
    data_rows = []
    for r in rows:
        row = []
        for i, cell in enumerate(r):
            if i == 6:
                row.append(Paragraph(cell, styles["CellGreen"]))
            else:
                row.append(Paragraph(cell, styles["CellBody"]))
        data_rows.append(row)

    all_rows = [head_row] + data_rows

    t = Table(all_rows, colWidths=col_w, repeatRows=1)

    # Estilo base
    style = [
        ("BACKGROUND",    (0,0), (-1,0), AZUL_TITULO),
        ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("ALIGN",         (0,0), (-1,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("FONTSIZE",      (0,1), (-1,-1), 8.5),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("GRID",          (0,0), (-1,-1), 0.4, CINZA_BORDA),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [BRANCO, CINZA_FUNDO]),
    ]

    # Destaque por tipo
    fodder_rows  = [1,2,3,4,5,6]
    evo_rows     = [7,8]
    fof_rows     = [9,10]

    for r in fodder_rows:
        style.append(("BACKGROUND", (3,r), (3,r), HexColor("#ECFDF5")))
        style.append(("TEXTCOLOR",  (3,r), (3,r), VERDE_ESCURO))
        style.append(("FONTNAME",   (3,r), (3,r), "Helvetica-Bold"))
    for r in evo_rows:
        style.append(("BACKGROUND", (3,r), (3,r), HexColor("#EDE9FE")))
        style.append(("TEXTCOLOR",  (3,r), (3,r), HexColor("#6D28D9")))
        style.append(("FONTNAME",   (3,r), (3,r), "Helvetica-Bold"))
    for r in fof_rows:
        style.append(("BACKGROUND", (3,r), (3,r), HexColor("#FFF7ED")))
        style.append(("TEXTCOLOR",  (3,r), (3,r), HexColor("#C2410C")))
        style.append(("FONTNAME",   (3,r), (3,r), "Helvetica-Bold"))

    t.setStyle(TableStyle(style))
    return t


def timing_table(styles):
    headers = ["Estratégia", "Quando Comprar", "Quando Vender", "Duração Est."]
    rows = [
        ["SBC Fodder Flip",       "Agora (29/05) — mercado em baixa\nFim de TOTS = supply máximo",
         "Qui 04/06 — antes do\nFestival of Football",        "4–6 dias"],
        ["Evolution Candidates",  "Hoje e amanhã (30/05)\nBase gold em mínimos anuais",
         "Após lançamento de\nnova Evo (05–07/06)",           "5–9 dias"],
        ["Festival of Football\nPath to Glory Prep", "Hoje–01/06\nJogadores internacionais baratos",
         "06–08/06 (pico de hype\nno lançamento)",            "7–10 dias"],
        ["Thursday Flip",         "Qua 03/06 à noite (recompensas\nRivals/Squad Battles abertas)",
         "Qui 04/06 manhã\n(pico de demanda)",                "< 24h"],
    ]

    col_w = [3.5*cm, 5.0*cm, 4.5*cm, 2.2*cm]

    head_row = [Paragraph(h, styles["CellHeader"]) for h in headers]
    data_rows = []
    for r in rows:
        data_rows.append([Paragraph(c, styles["CellBody"]) for c in r])

    all_rows = [head_row] + data_rows
    t = Table(all_rows, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), AZUL_TITULO),
        ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("ALIGN",         (0,0), (-1,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("FONTSIZE",      (0,1), (-1,-1), 8.5),
        ("TOPPADDING",    (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("GRID",          (0,0), (-1,-1), 0.4, CINZA_BORDA),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [BRANCO, CINZA_FUNDO]),
    ]))
    return t


def returns_table(styles):
    headers = ["Cenário", "Capital Inicial", "Retorno Esperado", "Capital Final", "Lucro Líquido", "ROI 48h"]
    rows = [
        ["Conservador",  "40.000",  "+15%",  "46.000",  "+6.000",   "15%"],
        ["Moderado",     "40.000",  "+28%",  "51.200",  "+11.200",  "28%"],
        ["Otimista",     "40.000",  "+48%",  "59.200",  "+19.200",  "48%"],
    ]

    col_w = [2.6*cm, 2.6*cm, 2.6*cm, 2.6*cm, 2.6*cm, 2.6*cm]

    head_row = [Paragraph(h, styles["CellHeader"]) for h in headers]
    data_rows = []
    for r in rows:
        data_rows.append([Paragraph(c, styles["CellBody"]) for c in r])
        # Colorir lucro coluna 4
    data_rows[0][4] = Paragraph("+6.000",  styles["CellGreen"])
    data_rows[1][4] = Paragraph("+11.200", styles["CellGreen"])
    data_rows[2][4] = Paragraph("+19.200", ParagraphStyle("GreenBig",
        parent=styles["CellGreen"], textColor=VERDE_ESCURO, fontName="Helvetica-Bold"))

    all_rows = [head_row] + data_rows
    t = Table(all_rows, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), AZUL_TITULO),
        ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("ALIGN",         (0,0), (-1,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("FONTSIZE",      (0,1), (-1,-1), 9),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("GRID",          (0,0), (-1,-1), 0.4, CINZA_BORDA),
        ("BACKGROUND",    (0,1), (-1,1), HexColor("#F0FDF4")),
        ("BACKGROUND",    (0,2), (-1,2), HexColor("#ECFDF5")),
        ("BACKGROUND",    (0,3), (-1,3), HexColor("#DCFCE7")),
    ]))
    return t


def golden_rules_table(styles):
    rules = [
        ("1", "Compre no desespero, venda na empolgação.",
              "Preços caem quando packs são abertos em massa. Aproveite o panic-sell."),
        ("2", "Respeite a taxa EA de 5%.",
              "Sempre calcule o preço de venda real: venda × 0.95. Nunca esqueça isso ao definir margem."),
        ("3", "Diversifique o portfólio.",
              "Distribua o budget em pelo menos 3 tipos de carta (fodder, evo, promo). Não ponha tudo em 1 card."),
        ("4", "Conheça o calendário de eventos.",
              "Quinta-feira = novos SBCs/TOTW. Sexta = pacotes de recompensa. Monitore datas de promos."),
        ("5", "Defina stop-loss.",
              "Se uma carta cair >20% do preço de compra e o evento já passou, venda e realoque. Não espere recuperação."),
        ("6", "Compre em volume nos mínimos.",
              "Com budget de 40k, prefira 20–30 cartas de fodder a 1 carta cara. Volume gera lucro mais seguro."),
        ("7", "Monitore oferta × demanda.",
              "Muitos packs abertos = preços caem. Novos SBCs = demanda sobe. Antecipe o ciclo."),
        ("8", "Venda antes do pico, não no pico.",
              "Poucos vendem no pico exato. Saia com 70–80% do lucro máximo para garantir a operação."),
    ]

    col_w = [0.7*cm, 5.0*cm, 10.5*cm]
    data = []
    for num, titulo, desc in rules:
        data.append([
            Paragraph(num, ParagraphStyle("RuleNum", fontName="Helvetica-Bold",
                fontSize=11, textColor=BRANCO, alignment=TA_CENTER)),
            Paragraph(titulo, ParagraphStyle("RuleTitle", fontName="Helvetica-Bold",
                fontSize=9, textColor=AZUL_TITULO, leading=13)),
            Paragraph(desc, ParagraphStyle("RuleDesc", fontName="Helvetica",
                fontSize=8.5, textColor=HexColor("#374151"), leading=13)),
        ])

    t = Table(data, colWidths=col_w)
    style = [
        ("ALIGN",         (0,0), (0,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (1,0), (-1,-1), 8),
        ("GRID",          (0,0), (-1,-1), 0.4, CINZA_BORDA),
        ("ROWBACKGROUNDS",(0,0), (-1,-1), [BRANCO, CINZA_FUNDO]),
    ]
    # Numeração verde
    for i in range(len(rules)):
        style.append(("BACKGROUND", (0,i), (0,i), VERDE_EA))
    t.setStyle(TableStyle(style))
    return t


# ── Main ─────────────────────────────────────────────────────────────────────
def build_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=1.8*cm,
        leftMargin=1.8*cm,
        topMargin=1.8*cm,
        bottomMargin=1.8*cm,
        title="Relatório Trading EA FC 26",
        author="Trading Bot EA FC 26",
    )

    styles = build_styles()
    story  = []

    # ── 1. HEADER ─────────────────────────────────────────────────────────
    story.append(header_block(styles))
    story.append(Spacer(1, 0.3*cm))
    story.append(info_strip(styles))
    story.append(Spacer(1, 0.4*cm))

    # ── 2. CONTEXTO DO MERCADO ────────────────────────────────────────────
    story += section_head("📊 Contexto do Mercado — 29/05/2026", styles)
    story.append(Paragraph(
        "<b>Evento Ativo:</b> TOTS Ultimate (Team of the Season Ultimate Edition) encerra <b>hoje, 29/05/2026</b>. "
        "Este é o último TOTS da temporada, reunindo as maiores estrelas de todas as ligas. Com o fim do ciclo, "
        "o mercado está inundado de cartas especiais e a demanda por ouro-base cai ao mínimo anual — criando a "
        "<b>melhor janela de compra do ano</b> para fodder e Evolutions.",
        styles["Body"]))
    story.append(Spacer(1, 0.2*cm))

    ctx_data = [
        ["Evento em Vigor",   "TOTS Ultimate — encerra hoje (29/05)"],
        ["Próximo Evento",    "Festival of Football — início 05/06/2026 (Path to Glory)"],
        ["Tendência Geral",   "Mercado em queda (TOTS supply alto) → virada esperada em 03–05/06"],
        ["Cartas em Alta",    "TOTS especiais (demanda alta), Evolutions (procura constante)"],
        ["Cartas em Baixa",   "Gold base 83–88 OVR — supply máximo = preços nos mínimos"],
        ["Oportunidade-Chave","Comprar fodder e base gold agora, vender no lançamento Festival of Football"],
        ["Impacto do Update", "World's Game Update: novo sistema de Evos, Pelé grátis, tokens renovados"],
    ]
    ctx_t = Table(ctx_data, colWidths=[4.5*cm, 12.7*cm])
    ctx_t.setStyle(TableStyle([
        ("FONTNAME",      (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME",      (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE",      (0,0), (-1,-1), 9),
        ("TEXTCOLOR",     (0,0), (0,-1), AZUL_TITULO),
        ("TEXTCOLOR",     (1,0), (1,-1), HexColor("#374151")),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("GRID",          (0,0), (-1,-1), 0.4, CINZA_BORDA),
        ("ROWBACKGROUNDS",(0,0), (-1,-1), [BRANCO, CINZA_FUNDO]),
        ("BACKGROUND",    (0,0), (0,-1), HexColor("#F0FDF4")),
    ]))
    story.append(ctx_t)
    story.append(Spacer(1, 0.5*cm))

    # ── 3. TABELA DE CARTAS ───────────────────────────────────────────────
    story += section_head("🃏 Cartas Recomendadas — Budget: 40.000 Coins", styles)
    story.append(Paragraph(
        "Margem líquida calculada após <b>taxa EA de 5%</b> sobre o preço de venda. "
        "Preços baseados em dados de mercado de 29/05/2026 (fim de TOTS = supply máximo = mínimos de preço).",
        styles["Body"]))
    story.append(Spacer(1, 0.2*cm))

    # Legenda
    legend_data = [[
        Paragraph("● Fodder 83-87", ParagraphStyle("L1", fontName="Helvetica-Bold",
            fontSize=8, textColor=VERDE_ESCURO)),
        Paragraph("● Evo Candidate", ParagraphStyle("L2", fontName="Helvetica-Bold",
            fontSize=8, textColor=HexColor("#6D28D9"))),
        Paragraph("● FoF Prep", ParagraphStyle("L3", fontName="Helvetica-Bold",
            fontSize=8, textColor=HexColor("#C2410C"))),
        Paragraph("* 5% tax já descontado da margem", ParagraphStyle("L4", fontName="Helvetica-Oblique",
            fontSize=7.5, textColor=HexColor("#6B7280"))),
    ]]
    leg_t = Table(legend_data, colWidths=[3.5*cm, 3.5*cm, 3.0*cm, 7.2*cm])
    leg_t.setStyle(TableStyle([
        ("ALIGN",  (0,0), (-1,-1), "LEFT"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    story.append(leg_t)
    story.append(Spacer(1, 0.15*cm))
    story.append(cards_table(styles))
    story.append(Spacer(1, 0.3*cm))

    # Sugestão de distribuição de budget
    story.append(Paragraph(
        "<b>Distribuição Sugerida do Budget (40.000 coins):</b>",
        styles["BulletBold"]))
    budget_items = [
        "• <b>50% (20.000 coins)</b> → SBC Fodder 84–87 OVR: Rubén Díaz, Çalhanoğlu, Lukaku, Tah, Bernardo Silva (~18–24 cartas)",
        "• <b>25% (10.000 coins)</b> → Evolution Candidates: Pedri, Foden (~3–4 cartas base gold)",
        "• <b>20% (8.000 coins)</b>  → Festival of Football Prep: Lamine Yamal (1–2 cartas)",
        "• <b>5%  (2.000 coins)</b>  → Reserva de liquidez para oportunidades de curto prazo",
    ]
    for item in budget_items:
        story.append(Paragraph(item, styles["BulletItem"]))
    story.append(Spacer(1, 0.5*cm))

    # ── 4. ESTRATÉGIA DE TIMING ───────────────────────────────────────────
    story += section_head("⏰ Estratégia de Timing", styles)
    story.append(timing_table(styles))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "<b>Calendário crítico da semana:</b>",
        styles["BulletBold"]))
    calendar_items = [
        "• <b>29/05 (Sexta) — HOJE:</b> Comprar fodder e base gold. Packs de recompensas do Squad Battles "
        "inundam o mercado → preços no chão. Janela de compra ideal.",
        "• <b>30–31/05 (Sáb–Dom):</b> Monitorar preços. Se algum card subiu >20%, considerar venda parcial.",
        "• <b>02–03/06 (Seg–Ter):</b> Mercado estabilizando. Preparar lista de venda.",
        "• <b>04/06 (Qua) à noite:</b> Pré-lançamento Festival of Football — demanda começa a subir. "
        "Bom momento para vender fodder de forma escalonada.",
        "• <b>05/06 (Qui):</b> Festival of Football ao vivo! Novos SBCs no ar = demanda por fodder dispara. "
        "Vender restante do estoque de fodder. Momento de maior liquidez.",
    ]
    for item in calendar_items:
        story.append(Paragraph(item, styles["BulletItem"]))
    story.append(Spacer(1, 0.5*cm))

    # ── 5. ESTIMATIVA DE RETORNO 48H ──────────────────────────────────────
    story += section_head("📈 Estimativa de Retorno em 48h–7 dias", styles)
    story.append(Paragraph(
        "Estimativas baseadas em padrões históricos de transição TOTS → novo promo. "
        "O cenário <b>conservador</b> considera apenas flips de fodder sem eventos extraordinários. "
        "O cenário <b>otimista</b> inclui valorização de Evolutions e cartas de Festival of Football.",
        styles["Body"]))
    story.append(Spacer(1, 0.2*cm))
    story.append(returns_table(styles))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "<b>Premissas do cálculo:</b>",
        styles["BulletBold"]))
    premissas = [
        "• Fodder 84–87: compra em mínimos de TOTS, venda +70–80% no lançamento do Festival of Football",
        "• Evolutions: +100–120% após lançamento de nova Evo compatível (histórico de promos similares)",
        "• Festival of Football Prep: +80–100% no pico de hype do evento (primeiros 2 dias)",
        "• Taxa EA de 5% descontada em todos os cálculos de margem",
        "• Cenário adverso considera vender apenas 60% do estoque no pico (liquidez parcial)",
    ]
    for p in premissas:
        story.append(Paragraph(p, styles["BulletItem"]))
    story.append(Spacer(1, 0.5*cm))

    # ── 6. 8 REGRAS DE OURO ──────────────────────────────────────────────
    story += section_head("🏆 8 Regras de Ouro do Trade", styles)
    story.append(KeepTogether([golden_rules_table(styles)]))
    story.append(Spacer(1, 0.5*cm))

    # ── 7. DISCLAIMER ────────────────────────────────────────────────────
    story += section_head("⚠️ Disclaimer", styles)
    story.append(Paragraph(
        "Este relatório é gerado por um agente de análise automatizada com base em dados de mercado "
        "coletados em fontes públicas (FUT.GG, FUTBIN, Reddit, notícias de jogos) em 29/05/2026. "
        "Preços de cartas em Ultimate Team são <b>extremamente voláteis</b> e podem variar em minutos "
        "dependendo de eventos do jogo, decisões da EA Sports e comportamento da comunidade. "
        "As estimativas de retorno são <b>projeções educacionais</b> baseadas em padrões históricos e "
        "<b>não constituem garantia de lucro</b>. O usuário é inteiramente responsável por suas decisões "
        "de trading. Sempre reserve uma margem de segurança e nunca invista mais do que pode perder. "
        "EA FC 26 é um produto da EA Sports — todas as marcas e nomes de jogadores pertencem aos seus "
        "respectivos proprietários.",
        styles["Disclaimer"]))

    # Rodapé
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width="100%", thickness=1, color=CINZA_BORDA))
    story.append(Spacer(1, 0.15*cm))
    footer_data = [[
        Paragraph("EA FC 26 Trading Bot", ParagraphStyle("FLeft", fontName="Helvetica",
            fontSize=7.5, textColor=HexColor("#9CA3AF"))),
        Paragraph(f"Relatório gerado em {DATA_HORA} UTC", ParagraphStyle("FCenter",
            fontName="Helvetica", fontSize=7.5, textColor=HexColor("#9CA3AF"),
            alignment=TA_CENTER)),
        Paragraph("kaiohsferreira/fifa-trading", ParagraphStyle("FRight",
            fontName="Helvetica", fontSize=7.5, textColor=HexColor("#9CA3AF"),
            alignment=TA_CENTER)),
    ]]
    ft = Table(footer_data, colWidths=[5.7*cm, 5.7*cm, 5.7*cm])
    ft.setStyle(TableStyle([
        ("ALIGN",  (0,0), (-1,-1), "LEFT"),
        ("ALIGN",  (1,0), (1,-1), "CENTER"),
        ("ALIGN",  (2,0), (2,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    story.append(ft)

    doc.build(story)
    print(f"PDF gerado: {output_path}")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)
    build_pdf(out)
