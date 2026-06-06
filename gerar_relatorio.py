#!/usr/bin/env python3
"""Gerador de relatório de trading EA FC 26 Ultimate Team."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import (
    HexColor, white, black, Color
)
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os

# ─────────────────────────── PALETTE ────────────────────────────
C_DARK    = HexColor("#0D1B2A")   # azul marinho escuro
C_ACCENT  = HexColor("#F5A623")   # laranja dourado EA
C_GREEN   = HexColor("#27AE60")
C_RED     = HexColor("#E74C3C")
C_LIGHT   = HexColor("#F0F4F8")
C_BORDER  = HexColor("#2C3E50")
C_HEADER_BG = HexColor("#1A2B3C")
C_ROW1    = HexColor("#FFFFFF")
C_ROW2    = HexColor("#EBF2FB")

# ────────────────────────── ESTILOS ─────────────────────────────
styles = getSampleStyleSheet()

def style(name, parent="Normal", **kw):
    s = ParagraphStyle(name, parent=styles[parent], **kw)
    return s

TITLE_STYLE = style("titulo",
    fontSize=26, leading=32, alignment=TA_CENTER,
    textColor=C_ACCENT, fontName="Helvetica-Bold",
    spaceAfter=4)

SUBTITLE_STYLE = style("subtitulo",
    fontSize=11, leading=14, alignment=TA_CENTER,
    textColor=white, fontName="Helvetica")

DATE_STYLE = style("data",
    fontSize=13, leading=16, alignment=TA_CENTER,
    textColor=C_ACCENT, fontName="Helvetica-Bold", spaceAfter=2)

SECTION_STYLE = style("secao",
    fontSize=14, leading=18, alignment=TA_LEFT,
    textColor=C_ACCENT, fontName="Helvetica-Bold",
    spaceBefore=14, spaceAfter=4)

BODY_STYLE = style("corpo",
    fontSize=9.5, leading=14, alignment=TA_JUSTIFY,
    textColor=C_DARK, fontName="Helvetica")

BULLET_STYLE = style("bullet",
    fontSize=9.5, leading=14, alignment=TA_LEFT,
    textColor=C_DARK, fontName="Helvetica",
    leftIndent=12, firstLineIndent=-12)

SMALL_STYLE = style("pequeno",
    fontSize=8.5, leading=12, alignment=TA_LEFT,
    textColor=HexColor("#555555"), fontName="Helvetica")

DISCLAIMER_STYLE = style("disclaimer",
    fontSize=8, leading=11, alignment=TA_JUSTIFY,
    textColor=HexColor("#888888"), fontName="Helvetica-Oblique")

WARNING_STYLE = style("aviso",
    fontSize=9, leading=13, alignment=TA_LEFT,
    textColor=HexColor("#C0392B"), fontName="Helvetica-Bold")


def header_table(doc_date: str) -> Table:
    data = [
        [Paragraph(
            "⚽  EA FC 26 ULTIMATE TEAM", style(
                "h1t", fontSize=22, leading=26, alignment=TA_CENTER,
                textColor=C_ACCENT, fontName="Helvetica-Bold")),
        ],
        [Paragraph(
            "RELATÓRIO DIÁRIO DE TRADING · FUT MARKET ANALYSIS",
            SUBTITLE_STYLE)],
        [Paragraph(doc_date, DATE_STYLE)],
    ]
    t = Table(data, colWidths=[17 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return t


def section_title(text: str):
    return Paragraph(text, SECTION_STYLE)


def hr():
    return HRFlowable(width="100%", thickness=1, color=C_ACCENT,
                      spaceAfter=6, spaceBefore=2)


def body(text: str):
    return Paragraph(text, BODY_STYLE)


def bullet(text: str):
    return Paragraph(f"▸  {text}", BULLET_STYLE)


def context_box(lines: list) -> Table:
    content = "<br/>".join(f"<b>•</b> {l}" for l in lines)
    p = Paragraph(content, style("ctx", parent="Normal",
                                 fontSize=9.5, leading=14,
                                 textColor=C_DARK, fontName="Helvetica"))
    t = Table([[p]], colWidths=[17 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), HexColor("#FFF8E7")),
        ("BOX",           (0, 0), (-1, -1), 1, C_ACCENT),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
    ]))
    return t


def cards_table(rows: list) -> Table:
    headers = [
        Paragraph("<b>Jogador</b>", style("th", fontSize=8.5, textColor=white,
                                          fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Rating</b>", style("th", fontSize=8.5, textColor=white,
                                         fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Clube / Nação</b>", style("th", fontSize=8.5, textColor=white,
                                                fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Tipo</b>", style("th", fontSize=8.5, textColor=white,
                                       fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Compra (k)</b>", style("th", fontSize=8.5, textColor=white,
                                             fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Venda (k)</b>", style("th", fontSize=8.5, textColor=white,
                                            fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Margem Líq.</b>", style("th", fontSize=8.5, textColor=white,
                                              fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Risco</b>", style("th", fontSize=8.5, textColor=white,
                                        fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ]

    cell_style = style("td", fontSize=8.5, textColor=C_DARK,
                       fontName="Helvetica", alignment=TA_CENTER)
    green_style = style("tdg", fontSize=8.5, textColor=C_GREEN,
                        fontName="Helvetica-Bold", alignment=TA_CENTER)

    data = [headers]
    for i, r in enumerate(rows):
        row = [
            Paragraph(r["nome"], cell_style),
            Paragraph(str(r["rating"]), cell_style),
            Paragraph(r["clube"], cell_style),
            Paragraph(r["tipo"], cell_style),
            Paragraph(r["compra"], cell_style),
            Paragraph(r["venda"], cell_style),
            Paragraph(r["margem"], green_style),
            Paragraph(r["risco"], cell_style),
        ]
        data.append(row)

    col_w = [3.2*cm, 1.3*cm, 3.2*cm, 2.2*cm, 1.8*cm, 1.8*cm, 2.0*cm, 1.5*cm]
    t = Table(data, colWidths=col_w, repeatRows=1)

    ts = [
        ("BACKGROUND",    (0, 0), (-1, 0), C_HEADER_BG),
        ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C_ROW1, C_ROW2]),
        ("BOX",           (0, 0), (-1, -1), 1, C_BORDER),
    ]
    t.setStyle(TableStyle(ts))
    return t


def timing_table(rows: list) -> Table:
    headers = [
        Paragraph("<b>Estratégia</b>", style("th2", fontSize=8.5, textColor=white,
                                             fontName="Helvetica-Bold")),
        Paragraph("<b>Quando Comprar</b>", style("th2", fontSize=8.5, textColor=white,
                                                  fontName="Helvetica-Bold")),
        Paragraph("<b>Quando Vender</b>", style("th2", fontSize=8.5, textColor=white,
                                                 fontName="Helvetica-Bold")),
        Paragraph("<b>Janela</b>", style("th2", fontSize=8.5, textColor=white,
                                         fontName="Helvetica-Bold")),
    ]
    cell = style("tdc", fontSize=8.5, textColor=C_DARK, fontName="Helvetica")
    data = [headers]
    for i, r in enumerate(rows):
        data.append([
            Paragraph(r[0], cell),
            Paragraph(r[1], cell),
            Paragraph(r[2], cell),
            Paragraph(r[3], cell),
        ])
    t = Table(data, colWidths=[4.5*cm, 4.5*cm, 5.0*cm, 3.0*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), C_HEADER_BG),
        ("GRID",       (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C_ROW1, C_ROW2]),
        ("BOX",        (0, 0), (-1, -1), 1, C_BORDER),
    ]))
    return t


def return_table(conservative: dict, optimistic: dict) -> Table:
    headers = [
        Paragraph("<b>Cenário</b>", style("th3", fontSize=9, textColor=white,
                                          fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Capital Inicial</b>", style("th3", fontSize=9, textColor=white,
                                                   fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Capital Final</b>", style("th3", fontSize=9, textColor=white,
                                                 fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Lucro Bruto</b>", style("th3", fontSize=9, textColor=white,
                                               fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Retorno %</b>", style("th3", fontSize=9, textColor=white,
                                             fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ]
    cons_style = style("tdc2", fontSize=9, textColor=HexColor("#1A5276"),
                       fontName="Helvetica", alignment=TA_CENTER)
    opt_style  = style("tdo2", fontSize=9, textColor=C_GREEN,
                       fontName="Helvetica-Bold", alignment=TA_CENTER)

    data = [headers,
            [Paragraph("Conservador", cons_style)] +
            [Paragraph(str(v), cons_style) for v in list(conservative.values())],
            [Paragraph("Otimista", opt_style)] +
            [Paragraph(str(v), opt_style) for v in list(optimistic.values())],
           ]
    t = Table(data, colWidths=[3.5*cm, 3.5*cm, 3.5*cm, 3.5*cm, 3.0*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), C_HEADER_BG),
        ("GRID",          (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C_ROW1, C_ROW2]),
        ("BOX",           (0, 0), (-1, -1), 1, C_BORDER),
    ]))
    return t


def golden_rules_table(rules: list) -> Table:
    cell = style("rule_cell", fontSize=9.5, textColor=C_DARK,
                 fontName="Helvetica", leading=13)
    num_style = style("rule_num", fontSize=11, textColor=C_ACCENT,
                      fontName="Helvetica-Bold", alignment=TA_CENTER)

    data = []
    for i, rule in enumerate(rules, 1):
        row = [
            Paragraph(str(i), num_style),
            Paragraph(f"<b>{rule[0]}</b><br/>{rule[1]}", cell),
        ]
        data.append(row)

    t = Table(data, colWidths=[1.2*cm, 15.8*cm])
    t.setStyle(TableStyle([
        ("GRID",           (0, 0), (-1, -1), 0.3, HexColor("#DDDDDD")),
        ("TOPPADDING",     (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 7),
        ("LEFTPADDING",    (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",   (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [C_ROW1, C_ROW2]),
        ("BOX",            (0, 0), (-1, -1), 1, C_BORDER),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t


# ═══════════════════════════ MAIN ═══════════════════════════════
def generate_pdf(output_path: str, report_datetime: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.5*cm, bottomMargin=1.5*cm,
        title="Relatório de Trading EA FC 26",
        author="FIFA Trading Bot",
    )

    story = []

    # ── CABEÇALHO ──────────────────────────────────────────────
    story.append(header_table(f"Gerado em: {report_datetime}  ·  Budget: 40.000 coins"))
    story.append(Spacer(1, 14))

    # ── CONTEXTO DO MERCADO ────────────────────────────────────
    story.append(section_title("📊  Contexto do Mercado"))
    story.append(hr())

    context_lines = [
        "EVENTO ATIVO: Festival of Football — início 05/06/2026 (6PM BST). "
        "Mega-evento temático Copa do Mundo com 6 semanas de promos consecutivas.",
        "PROMO EM DESTAQUE: Path to Glory (PTG) — Fase 1 ativa (05/06 a 19/06). "
        "Cartas dinâmicas de jogadores da seleção que sobem de rating conforme o país avança na Copa.",
        "BÔNUS: Free Pelé 93 OVR distribuído em 04/06. "
        "100+ jogadores de seleção nacionais entraram nos packs — oferta alta, preços em queda.",
        "SBC ATIVO: 'Grind Upgrade SBC' disponível até 12/06/2026 — repete até 3x. "
        "Exige fodder 83-88 rated, gerando demanda constante nessa faixa.",
        "TENDÊNCIA GERAL: Preços de golds e fodder 83-88 em pressão de baixa pelo "
        "alto pack weight do evento. Janela de compra favorável nas próximas 24-48h.",
        "ATENÇÃO: Upgrades de PTG processados toda quarta-feira após resultados — "
        "comprar PTG de nações fortes antes das partidas pode render 30-80% de retorno.",
    ]
    story.append(context_box(context_lines))
    story.append(Spacer(1, 14))

    # ── TABELA DE CARTAS RECOMENDADAS ──────────────────────────
    story.append(section_title("🎯  Cartas Recomendadas — Budget 40.000 coins"))
    story.append(hr())

    story.append(body(
        "Margem líquida calculada após desconto de 5% de taxa EA sobre o valor de venda. "
        "Preços referentes à plataforma PS/Xbox. Verifique sempre no FUTBIN/FUT.GG antes de comprar."
    ))
    story.append(Spacer(1, 6))

    cards = [
        # SBC Fodder 86-rated bulk
        {
            "nome": "Çalhanoğlu",
            "rating": 86,
            "clube": "Inter / Turquia",
            "tipo": "SBC Fodder",
            "compra": "~950",
            "venda": "~1.800",
            "margem": "+760",
            "risco": "🟢 Baixo",
        },
        {
            "nome": "Bruno Guimarães",
            "rating": 86,
            "clube": "Newcastle / Brasil",
            "tipo": "SBC Fodder",
            "compra": "~900",
            "venda": "~1.700",
            "margem": "+715",
            "risco": "🟢 Baixo",
        },
        {
            "nome": "Claudia Pina",
            "rating": 86,
            "clube": "Barcelona F. / Esp.",
            "tipo": "SBC Fodder",
            "compra": "~850",
            "venda": "~1.600",
            "margem": "+670",
            "risco": "🟢 Baixo",
        },
        # SBC Fodder 87-rated
        {
            "nome": "Lauren Hemp",
            "rating": 87,
            "clube": "Man City F. / Ing.",
            "tipo": "SBC Fodder",
            "compra": "~900",
            "venda": "~2.000",
            "margem": "+1.000",
            "risco": "🟢 Baixo",
        },
        {
            "nome": "Caroline Weir",
            "rating": 87,
            "clube": "Real Madrid F. / Esc.",
            "tipo": "SBC Fodder",
            "compra": "~750",
            "venda": "~1.900",
            "margem": "+1.055",
            "risco": "🟢 Baixo",
        },
        # SBC Fodder 88-rated
        {
            "nome": "Irene Paredes",
            "rating": 88,
            "clube": "Barcelona F. / Esp.",
            "tipo": "SBC Fodder",
            "compra": "~900",
            "venda": "~2.400",
            "margem": "+1.380",
            "risco": "🟡 Médio",
        },
        {
            "nome": "Gabriel (Arsenal)",
            "rating": 88,
            "clube": "Arsenal / Brasil",
            "tipo": "SBC Fodder",
            "compra": "~1.200",
            "venda": "~2.800",
            "margem": "+1.460",
            "risco": "🟡 Médio",
        },
        # Path to Glory — investimento
        {
            "nome": "Gonçalo Ramos",
            "rating": 93,
            "clube": "PSG / Portugal",
            "tipo": "PTG Invest.",
            "compra": "~39.500",
            "venda": "~60.000",
            "margem": "+17.500",
            "risco": "🟡 Médio",
        },
        {
            "nome": "Lewis Ferguson",
            "rating": 93,
            "clube": "Bologna / Escócia",
            "tipo": "PTG Especul.",
            "compra": "~25.250",
            "venda": "~45.000",
            "margem": "+17.500",
            "risco": "🔴 Alto",
        },
        {
            "nome": "Anthony Elanga",
            "rating": 93,
            "clube": "Nott. Forest / Suécia",
            "tipo": "PTG Invest.",
            "compra": "~35.000",
            "venda": "~55.000",
            "margem": "+17.250",
            "risco": "🟡 Médio",
        },
    ]

    story.append(cards_table(cards))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "* PTG = Path to Glory (carta dinâmica que sobe rating com resultados da Copa). "
        "Valores em coins. k = milhares.",
        SMALL_STYLE))
    story.append(Spacer(1, 14))

    # ── ESTRATÉGIA DE TIMING ───────────────────────────────────
    story.append(section_title("⏰  Estratégia de Timing"))
    story.append(hr())

    timing_rows = [
        (
            "SBC Fodder\n86-88 Bulk",
            "Madrugada (00h-06h BRT)\nou manhã cedo — oferta\nalta, poucos compradores",
            "Evening peak (19h-23h BRT)\nou antes de novo SBC\nser anunciado",
            "12-24h"
        ),
        (
            "PTG Nations\n(Portugal/Suécia)",
            "Antes das partidas da\nCopa (dias de jogo)\nPreços sobem pós-vitória",
            "Quarta-feira (após\nprocessamento de\nupgrade no FUTBIN)",
            "48-72h"
        ),
        (
            "Thursday Flip\n(Sexta-feira)",
            "Quinta-feira à tarde\napós anúncio de\nnovo conteúdo semanal",
            "Sexta-feira peak:\njogadores completando\nSBCs e Evolutions",
            "12-24h"
        ),
        (
            "Weekend League\nPrep",
            "Quarta/quinta — jogadores\ncomprando antes do WL",
            "Sexta-feira noite ou\nno início do Weekend\nLeague (sábado cedo)",
            "24-48h"
        ),
    ]
    story.append(timing_table(timing_rows))
    story.append(Spacer(1, 14))

    # ── ESTIMATIVA DE RETORNO 48H ──────────────────────────────
    story.append(section_title("💰  Estimativa de Retorno em 48h"))
    story.append(hr())

    story.append(body(
        "Projeção baseada em alocação mista: "
        "70% do budget (28.000 coins) em SBC fodder bulk 86-88 rated + "
        "30% (12.000 coins) em PTG ou Thursday flip. "
        "Após taxa EA de 5% sobre todas as vendas."
    ))
    story.append(Spacer(1, 8))

    conservative = {
        "capital_inicial": "40.000",
        "capital_final":   "54.000",
        "lucro":           "+14.000",
        "retorno":         "+35%",
    }
    optimistic = {
        "capital_inicial": "40.000",
        "capital_final":   "72.000",
        "lucro":           "+32.000",
        "retorno":         "+80%",
    }
    story.append(return_table(conservative, optimistic))

    story.append(Spacer(1, 6))
    story.append(body(
        "Cenário Conservador: Fodder sobe 80-100% sobre preço de compra; "
        "PTG cards não recebem upgrade (nação eliminada no grupo). "
        "Cenário Otimista: Fodder vendido no pico de SBC demand (+150%); "
        "Portugal e Suécia avançam, upgrade processado na quarta-feira "
        "(+40-50% sobre preço de compra)."
    ))
    story.append(Spacer(1, 14))

    # ── 8 REGRAS DE OURO ──────────────────────────────────────
    story.append(section_title("🏆  8 Regras de Ouro do Trade"))
    story.append(hr())

    rules = [
        ("Nunca invista o budget total em uma única carta.",
         "Diversifique: no máximo 40% em uma única estratégia. "
         "Concentração = risco de desastre em caso de queda brusca."),
        ("Compre na madrugada, venda no pico.",
         "O mercado tem ciclos diários. Preços mínimos ocorrem entre 00h-06h BRT; "
         "máximos entre 19h-23h BRT quando o mercado europeu e americano se sobrepõem."),
        ("Sempre calcule a margem após a taxa EA de 5%.",
         "A EA cobra 5% sobre o valor de venda. Calcule: Lucro = Venda × 0,95 − Compra. "
         "Nunca esqueça esse desconto na sua matemática."),
        ("PTG: espere 48-72h antes de comprar na abertura do promo.",
         "Preços de lançamento são sempre inflacionados. Aguarde a euforia passar. "
         "Compre antes das partidas importantes, não no dia de lançamento."),
        ("Use o FUTBIN/FUT.GG para verificar price ranges antes de comprar.",
         "Nunca compre sem consultar o histórico de preços. "
         "Se o preço estiver no topo do range, espere ou passe para outra oportunidade."),
        ("Defina seu stop-loss antes de entrar em qualquer trade.",
         "Determine o preço mínimo de saída. Se o mercado cair abaixo desse nível, "
         "venda imediatamente — não espere recuperação que pode nunca vir."),
        ("Nunca segure cards ao final de um evento/promo.",
         "Quando um promo termina, os preços caem bruscamente devido ao excesso de oferta. "
         "Venda sempre 24-48h antes do fim do evento."),
        ("Reinvista consistentemente — compostos fazem a mágica.",
         "Com 35% de retorno semanal, 40.000 coins se transformam em 370.000+ em 4 semanas. "
         "A disciplina de reinvestir é o maior diferencial entre traders mediocres e os melhores."),
    ]
    story.append(golden_rules_table(rules))
    story.append(Spacer(1, 14))

    # ── DISCLAIMER ────────────────────────────────────────────
    story.append(section_title("⚠️  Disclaimer"))
    story.append(hr())
    story.append(Paragraph(
        "Este relatório é gerado com base em dados públicos de mercado do EA FC 26 Ultimate Team "
        "coletados em fontes como FUTBIN, FUT.GG, RealSport101 e Reddit FUT. "
        "Os preços indicados são estimativas e podem variar significativamente entre plataformas "
        "(PS/Xbox vs PC) e ao longo do dia. "
        "O trading em FUT envolve risco de perda de coins — nunca invista mais do que pode perder. "
        "Este documento NÃO constitui aconselhamento financeiro de qualquer natureza. "
        "Sempre verifique preços em tempo real antes de qualquer operação. "
        "Resultados passados não garantem resultados futuros. "
        "O autor não se responsabiliza por perdas decorrentes do uso deste relatório.",
        DISCLAIMER_STYLE))

    story.append(Spacer(1, 10))

    footer_style = style("footer", fontSize=8, alignment=TA_CENTER,
                         textColor=HexColor("#AAAAAA"), fontName="Helvetica-Oblique")
    story.append(Paragraph(
        f"FIFA Trading Bot · EA FC 26 Market Analysis · {report_datetime}  "
        "· github.com/kaiohsferreira/fifa-trading",
        footer_style))

    doc.build(story)
    print(f"PDF gerado: {output_path}")


if __name__ == "__main__":
    report_dt = "06/06/2026 08:04"
    out = "/home/user/fifa-trading/relatorio-trading-2026-06-06-08h.pdf"
    generate_pdf(out, report_dt)
