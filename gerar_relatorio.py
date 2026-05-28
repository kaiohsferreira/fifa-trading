#!/usr/bin/env python3
"""Gera o relatório de trading EA FC 26 em PDF."""

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
import sys
import os

# ─────────────────────────────────────────────
# Dados do relatório
# ─────────────────────────────────────────────
REPORT_DATETIME   = "28/05/2026 20:07"
REPORT_FILENAME   = "relatorio-trading-2026-05-28-20h.pdf"

# Cores institucionais
EA_DARK   = colors.HexColor("#0D0D0D")
EA_GOLD   = colors.HexColor("#F5C518")
EA_GREEN  = colors.HexColor("#00C853")
EA_RED    = colors.HexColor("#E53935")
EA_BLUE   = colors.HexColor("#1565C0")
EA_GREY   = colors.HexColor("#1E1E2E")
EA_LGREY  = colors.HexColor("#2C2C3E")
EA_WHITE  = colors.white
TEXT_LIGHT = colors.HexColor("#E0E0E0")

PAGE_W, PAGE_H = A4


def build_styles():
    base = getSampleStyleSheet()

    title = ParagraphStyle(
        "TitleStyle",
        parent=base["Title"],
        fontSize=22, textColor=EA_GOLD,
        alignment=TA_CENTER, spaceAfter=4,
        fontName="Helvetica-Bold",
    )
    subtitle = ParagraphStyle(
        "SubtitleStyle",
        parent=base["Normal"],
        fontSize=11, textColor=TEXT_LIGHT,
        alignment=TA_CENTER, spaceAfter=2,
        fontName="Helvetica",
    )
    section = ParagraphStyle(
        "SectionStyle",
        parent=base["Heading1"],
        fontSize=13, textColor=EA_GOLD,
        spaceBefore=14, spaceAfter=6,
        fontName="Helvetica-Bold",
        borderPad=0,
    )
    body = ParagraphStyle(
        "BodyStyle",
        parent=base["Normal"],
        fontSize=9.5, textColor=TEXT_LIGHT,
        spaceAfter=4, leading=14,
        fontName="Helvetica",
        alignment=TA_JUSTIFY,
    )
    body_bold = ParagraphStyle(
        "BodyBold",
        parent=body,
        fontName="Helvetica-Bold",
        textColor=EA_GOLD,
    )
    bullet = ParagraphStyle(
        "BulletStyle",
        parent=body,
        leftIndent=14, bulletIndent=4,
    )
    small = ParagraphStyle(
        "SmallStyle",
        parent=body,
        fontSize=7.5, textColor=colors.HexColor("#9E9E9E"),
        alignment=TA_CENTER,
    )
    th = ParagraphStyle(
        "TableHeader",
        parent=base["Normal"],
        fontSize=8, textColor=EA_DARK,
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
    )
    td = ParagraphStyle(
        "TableData",
        parent=base["Normal"],
        fontSize=8, textColor=EA_DARK,
        fontName="Helvetica",
        alignment=TA_CENTER,
    )
    return dict(title=title, subtitle=subtitle, section=section,
                body=body, body_bold=body_bold, bullet=bullet,
                small=small, th=th, td=td)


def divider(color=EA_GOLD, thickness=1):
    return HRFlowable(width="100%", thickness=thickness,
                      color=color, spaceAfter=6, spaceBefore=2)


def section_header(text, s):
    return [Spacer(1, 0.15 * cm), Paragraph(text, s["section"]), divider()]


def make_table(header, rows, s, col_widths=None):
    th, td = s["th"], s["td"]
    data = [[Paragraph(h, th) for h in header]]
    for row in rows:
        data.append([Paragraph(str(c), td) for c in row])

    if col_widths is None:
        col_widths = [(PAGE_W - 4 * cm) / len(header)] * len(header)

    style = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  EA_GOLD),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [colors.HexColor("#1A1A2E"),
                                              colors.HexColor("#16213E")]),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#333355")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(style)
    return t


def build_doc(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="Relatório de Trading EA FC 26",
        author="FIFA Trading Bot",
    )

    s = build_styles()
    story = []

    # ── CAPA / CABEÇALHO ──────────────────────────────────────────────
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("⚽ EA FC 26 — RELATÓRIO DE TRADING", s["title"]))
    story.append(Paragraph(f"Ultimate Team · Análise de Mercado", s["subtitle"]))
    story.append(Paragraph(f"Gerado em: {REPORT_DATETIME} UTC", s["subtitle"]))
    story.append(divider(EA_GOLD, 2))
    story.append(Spacer(1, 0.3 * cm))

    # ── 1. CONTEXTO DO MERCADO ────────────────────────────────────────
    story += section_header("1. CONTEXTO DO MERCADO — 28/05/2026", s)

    contexto = [
        ("<b>Evento Ativo:</b> <b>Ultimate TOTS</b> (Team of the Season) — "
         "última semana da promoção, com encerramento previsto para "
         "<b>29/05/2026 às 18h UTC</b>."),
        ("<b>Fantasy FC</b> também ativo, com boost nas cartas de jogadores "
         "bloqueados pelas finais das ligas domésticas — encerra igualmente "
         "em 29/05/2026."),
        ("O <b>Ultimate TOTS</b> traz de volta os maiores craques de todas "
         "as ligas ao mesmo tempo (Mbappé, Vini Jr., Haaland, Bellingham), "
         "criando enorme pressão de pack opening e um ciclo clássico de "
         "<b>crash → recuperação</b>."),
        ("<b>Tendência atual:</b> Com o evento se encerrando amanhã, "
         "espera-se uma <b>queda acentuada de preços nas próximas 12-24h</b> "
         "enquanto os últimos packs são abertos, seguida de uma "
         "<b>recuperação gradual nos 3-5 dias após o fim do TOTS</b>, "
         "pois a oferta seca e a demanda por SBCs cresce."),
        ("<b>Fator Thursday (29/05):</b> Amanhã é dia de recompensas do "
         "Division Rivals — novo influxo de cartas no mercado, especialmente "
         "nas faixas 83-86, gerando janelas de compra barata nas primeiras "
         "2-3 horas após a distribuição (~18h UTC)."),
        ("<b>Próxima promo:</b> Aguarda-se anúncio nos próximos dias — "
         "cartas fora de packs costumam valorizar 15-30% na transição "
         "entre promos."),
    ]
    for p in contexto:
        story.append(Paragraph(f"• {p}", s["bullet"]))
    story.append(Spacer(1, 0.2 * cm))

    # ── 2. OPORTUNIDADES DE COMPRA ────────────────────────────────────
    story += section_header("2. OPORTUNIDADES DE COMPRA — Budget: 40.000 coins", s)

    story.append(Paragraph(
        "Tabela com cartas recomendadas, preço-alvo de compra, preço-alvo de venda "
        "e margem líquida após taxa EA de 5%:",
        s["body"]
    ))
    story.append(Spacer(1, 0.2 * cm))

    hdr = ["Jogador", "Rat.", "Clube", "Tipo", "Compra (c)", "Venda (c)", "Margem líq."]
    # margem = venda * 0.95 - compra
    rows_fodder = [
        # SBC Fodder Flipping (83-88)
        ["Unai Simón",      "85", "Athletic Club",    "Gold Fodder", "1.300",  "1.900",  "+505"],
        ["De Gea",          "85", "sem clube",        "Gold Fodder", "1.500",  "2.100",  "+495"],
        ["Weir",            "85", "Chelsea FC W",     "Gold Fodder", "1.200",  "1.800",  "+510"],
        ["Isco",            "84", "Real Betis",       "Gold Fodder", "750",    "1.200",  "+390"],
        ["Mahrez",          "84", "Al-Ahli",          "Gold Fodder", "750",    "1.150",  "+343"],
        ["Acerbi",          "84", "Inter de Milão",   "Gold Fodder", "750",    "1.100",  "+295"],
        ["Tonali",          "86", "Newcastle",        "Gold Fodder", "1.500",  "2.300",  "+685"],
        ["Bruno Guimarães", "86", "Newcastle",        "Gold Fodder", "1.600",  "2.400",  "+680"],
        ["Nico Williams",   "86", "Athletic Club",    "Gold Fodder", "1.800",  "2.700",  "+765"],
        # Evolutions
        ["Nwaneri",         "91", "Arsenal",          "Fantasy FC",  "3.000",  "5.000", "+1.750"],
        ["Chawinga",        "90", "Man City W",       "Fantasy FC",  "2.800",  "4.500", "+1.475"],
        # Sell spike pós-TOTS
        ["Courtois",        "92", "Real Madrid",      "TOTS GK",    "18.000", "28.000", "+8.600"],
        ["Kiwior",          "94", "Arsenal",          "TOTS CB",    "14.250", "22.000", "+6.650"],
    ]

    col_w = [3.8*cm, 1.0*cm, 3.0*cm, 2.2*cm, 1.8*cm, 1.8*cm, 1.8*cm]
    story.append(make_table(hdr, rows_fodder, s, col_widths=col_w))
    story.append(Spacer(1, 0.15*cm))
    story.append(Paragraph(
        "* Margem líquida = Preço de venda × 0,95 − Preço de compra. "
        "Preços em coins (console PS/Xbox), baseados em médias de mercado às 20h UTC.",
        s["small"]
    ))

    # ── 3. ESTRATÉGIA DE TIMING ───────────────────────────────────────
    story += section_header("3. ESTRATÉGIA DE TIMING", s)

    timing = [
        ("<b>AGORA (20h–23h UTC, 28/05):</b> Comprar fodder 84-86 "
         "aproveitar pack openings que derrubam preços. Meta: estocar "
         "20-25 cartas abaixo do preço médio. Investir ~15.000 coins."),
        ("<b>QUINTA-FEIRA (29/05, 18h UTC) — Rivals Rewards:</b> "
         "Mercado sobe 15-25 min após recompensas, depois cai durante "
         "1-2h. Janela de COMPRA agressiva entre 18h30 e 20h UTC. "
         "Usar ~15.000 coins restantes."),
        ("<b>APÓS FIM DO TOTS (29/05, 18h UTC):</b> "
         "Evento encerra — cartas saem de packs. "
         "VENDER fodder comprado nos próximos 12-24h "
         "enquanto demanda de SBC sobe."),
        ("<b>SÁBADO–DOMINGO (30-31/05):</b> "
         "Weekend League libera jogadores; mercado fica instável. "
         "Ideal para vender as últimas cartas em estoque e realizar lucros."),
        ("<b>Atenção Evolution:</b> Monitorar anúncios de nova Evolution "
         "após TOTS. Comprar base cards de jogadores elegíveis ANTES do "
         "anúncio oficial (vazamentos aparecem 2-6h antes no Twitter/Reddit)."),
    ]
    for p in timing:
        story.append(Paragraph(f"• {p}", s["bullet"]))

    # ── 4. ESTIMATIVA DE RETORNO EM 48H ──────────────────────────────
    story += section_header("4. ESTIMATIVA DE RETORNO EM 48H", s)

    hdr_ret = ["Cenário", "Investimento", "Retorno Bruto", "Taxa EA (5%)", "Lucro Líquido", "ROI"]
    rows_ret = [
        ["Conservador", "40.000",  "49.000",  "2.450",  "+6.550",  "16,4%"],
        ["Moderado",    "40.000",  "55.000",  "2.750",  "+12.250", "30,6%"],
        ["Otimista",    "40.000",  "64.000",  "3.200",  "+20.800", "52,0%"],
    ]
    col_w2 = [2.8*cm, 2.4*cm, 2.4*cm, 2.4*cm, 2.4*cm, 2.0*cm]
    story.append(Paragraph(
        "Projeção baseada no flip fodder 84-86 + posição em TOTS baratos "
        "no encerramento do evento:",
        s["body"]
    ))
    story.append(Spacer(1, 0.15*cm))
    story.append(make_table(hdr_ret, rows_ret, s, col_widths=col_w2))

    story.append(Spacer(1, 0.25*cm))
    # Tabela de alocação
    story.append(Paragraph("<b>Alocação sugerida dos 40.000 coins:</b>", s["body_bold"]))
    story.append(Spacer(1, 0.1*cm))
    hdr_alloc = ["Estratégia", "Coins", "% Budget", "Horizonte"]
    rows_alloc = [
        ["SBC Fodder Flip (84-86)",         "15.000", "37,5%", "12-24h"],
        ["Thursday Flip Rivals Rewards",    "15.000", "37,5%", "24-48h"],
        ["TOTS Baratos (pós-crash)",        "7.000",  "17,5%", "48-96h"],
        ["Reserva de liquidez",             "3.000",  "7,5%",  "—"],
    ]
    col_w3 = [5.5*cm, 2.2*cm, 2.2*cm, 2.2*cm]
    story.append(make_table(hdr_alloc, rows_alloc, s, col_widths=col_w3))

    # ── 5. 8 REGRAS DE OURO DO TRADE ─────────────────────────────────
    story += section_header("5. 8 REGRAS DE OURO DO TRADE", s)

    regras = [
        ("1", "Nunca invista mais de 50% do capital em um único ativo — "
              "diversificação protege de quedas inesperadas."),
        ("2", "Compre sempre na mínima do dia; venda na máxima. "
              "Patience > FOMO."),
        ("3", "Considere SEMPRE a taxa de 5% da EA no cálculo do lucro. "
              "Venda por X; recebe 0,95X."),
        ("4", "Thursday é dia de compra, não de venda — aproveite o dump "
              "de Rivals Rewards para estocar fodder."),
        ("5", "Monitore vazamentos de novos SBCs e Evolutions no Twitter/Reddit "
              "antes do anúncio oficial — o preço sobe minutos após a release."),
        ("6", "Mantenha sempre 7-10% do budget em coins líquidos para "
              "oportunidades de snipe rápido."),
        ("7", "Acompanhe o fim de eventos: cartas fora de packs se valorizam "
              "15-30% em 24-72h após o encerramento da promo."),
        ("8", "Documente cada trade: preço de compra, data, preço de venda. "
              "Sem histórico, não há aprendizado."),
    ]
    hdr_regras = ["#", "Regra"]
    col_w4 = [0.6*cm, (PAGE_W - 4*cm - 0.6*cm)]
    story.append(make_table(hdr_regras, regras, s, col_widths=col_w4))

    # ── 6. DISCLAIMER ────────────────────────────────────────────────
    story += section_header("6. DISCLAIMER", s)
    story.append(Paragraph(
        "Este relatório é gerado por um agente de análise automatizado com base "
        "em dados públicos de mercado (FUTBIN, FUT.GG, TeamGullit, Reddit) e "
        "tendências históricas do Ultimate Team. "
        "Os preços indicados são estimativas e podem variar significativamente "
        "conforme a plataforma (PS/Xbox/PC), o horário e eventos imprevistos "
        "publicados pela EA Sports. "
        "Nenhuma operação de trading é garantida — o mercado do FUT é volátil "
        "e influenciado por fatores externos. "
        "Use este relatório como guia complementar à sua própria análise. "
        "O autor não se responsabiliza por perdas decorrentes de decisões "
        "baseadas neste documento.",
        s["body"]
    ))

    story.append(Spacer(1, 0.4 * cm))
    story.append(divider(EA_GOLD, 1))
    story.append(Paragraph(
        f"FIFA Trading · EA FC 26 Ultimate Team · {REPORT_DATETIME} UTC · "
        "github.com/kaiohsferreira/fifa-trading",
        s["small"]
    ))

    doc.build(story)
    print(f"PDF gerado: {output_path}")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), REPORT_FILENAME)
    build_doc(out)
