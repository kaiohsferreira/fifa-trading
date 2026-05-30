#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import PageBreak
import os

REPORT_DATE = "30/05/2026 20:06"
FILENAME = "relatorio-trading-2026-05-30-20h.pdf"
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAME)

# ── Paleta de cores ──────────────────────────────────────────────────────────
VERDE_EA    = colors.HexColor("#00C800")
VERDE_ESCURO= colors.HexColor("#007800")
AMARELO     = colors.HexColor("#FFD700")
LARANJA     = colors.HexColor("#FF8C00")
VERMELHO    = colors.HexColor("#DC143C")
CINZA_ESCURO= colors.HexColor("#1E1E2E")
CINZA_MEDIO = colors.HexColor("#2D2D3F")
CINZA_CLARO = colors.HexColor("#F4F4F8")
BRANCO      = colors.white
PRETO       = colors.black

def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "TituloRelatorio",
        fontName="Helvetica-Bold", fontSize=22,
        textColor=VERDE_EA, alignment=TA_CENTER,
        spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        "SubtituloRelatorio",
        fontName="Helvetica-Bold", fontSize=13,
        textColor=AMARELO, alignment=TA_CENTER,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        "DataRelatorio",
        fontName="Helvetica", fontSize=10,
        textColor=colors.HexColor("#AAAAAA"), alignment=TA_CENTER,
        spaceAfter=12
    ))
    styles.add(ParagraphStyle(
        "SecaoTitulo",
        fontName="Helvetica-Bold", fontSize=13,
        textColor=VERDE_EA, spaceBefore=14, spaceAfter=6,
        borderPad=4
    ))
    styles.add(ParagraphStyle(
        "CorpoTexto",
        fontName="Helvetica", fontSize=9.5,
        textColor=colors.HexColor("#222222"), leading=15,
        spaceAfter=6, alignment=TA_JUSTIFY
    ))
    styles.add(ParagraphStyle(
        "BulletItem",
        fontName="Helvetica", fontSize=9.5,
        textColor=colors.HexColor("#222222"), leading=14,
        leftIndent=12, spaceAfter=3
    ))
    styles.add(ParagraphStyle(
        "Disclaimer",
        fontName="Helvetica-Oblique", fontSize=8,
        textColor=colors.HexColor("#888888"), leading=12,
        alignment=TA_JUSTIFY, spaceBefore=8
    ))
    styles.add(ParagraphStyle(
        "RegrasOuro",
        fontName="Helvetica", fontSize=9.5,
        textColor=colors.HexColor("#1A1A1A"), leading=15,
        leftIndent=10, spaceAfter=3
    ))
    return styles


def header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    # Cabeçalho
    canvas.setFillColor(CINZA_ESCURO)
    canvas.rect(0, h - 28*mm, w, 28*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.setFillColor(VERDE_EA)
    canvas.drawString(18*mm, h - 14*mm, "EA FC 26 ULTIMATE TEAM — TRADING REPORT")
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#AAAAAA"))
    canvas.drawRightString(w - 18*mm, h - 14*mm, f"Gerado em: {REPORT_DATE} UTC")
    canvas.setFillColor(VERDE_ESCURO)
    canvas.rect(0, h - 30*mm, w, 2*mm, fill=1, stroke=0)

    # Rodapé
    canvas.setFillColor(CINZA_ESCURO)
    canvas.rect(0, 0, w, 16*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#AAAAAA"))
    canvas.drawString(18*mm, 6*mm, "© 2026 FIFA Trading Report — Uso pessoal | Budget: 40.000 coins")
    canvas.drawRightString(w - 18*mm, 6*mm, f"Página {doc.page}")
    canvas.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        topMargin=34*mm,
        bottomMargin=22*mm,
        leftMargin=18*mm,
        rightMargin=18*mm,
    )
    styles = build_styles()
    story = []

    # ── CAPA / CABEÇALHO ────────────────────────────────────────────────────
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("RELATÓRIO DIÁRIO DE TRADING", styles["TituloRelatorio"]))
    story.append(Paragraph("EA FC 26 Ultimate Team — Análise de Mercado", styles["SubtituloRelatorio"]))
    story.append(Paragraph(f"Data: {REPORT_DATE} UTC  |  Budget: 40.000 coins  |  Estratégia: Fodder Flip + Evo Invest + Thursday Flip", styles["DataRelatorio"]))
    story.append(HRFlowable(width="100%", thickness=2, color=VERDE_EA, spaceAfter=10))

    # ── 1. CONTEXTO DO MERCADO ───────────────────────────────────────────────
    story.append(Paragraph("1. CONTEXTO DO MERCADO (30/05/2026)", styles["SecaoTitulo"]))

    contexto = [
        ["Evento Ativo", "Status / Detalhes"],
        ["TOTS Ultimate", "Encerrado em 29/05 — cartas TOTS saindo de packs"],
        ["UEFA RTTF", "Ativo até 30/05 — cartas live-upgrade (Champions/Europa League finais)"],
        ["Festival of Football", "INICIA 05/06 às 19h BRT — Path to Glory (World Cup live cards)"],
        ["Showdown Berbatov", "SBC Soccer Aid ativo — demanda por fodder 83-87 alta"],
        ["Divisional Rivals Rewards", "Sexta-feira 30/05 — pico de abertura de packs hoje à noite"],
        ["Thursday Flip Window", "Amanhã 31/05 (sábado) — mercado absorve novos packs, preços sobem"],
    ]

    t = Table(contexto, colWidths=[65*mm, 105*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, 0),  CINZA_ESCURO),
        ("TEXTCOLOR",   (0, 0), (-1, 0),  VERDE_EA),
        ("FONTNAME",    (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, 0),  9),
        ("BACKGROUND",  (0, 1), (-1, -1), CINZA_CLARO),
        ("FONTNAME",    (0, 1), (0, -1),  "Helvetica-Bold"),
        ("FONTSIZE",    (0, 1), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("GRID",        (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("ALIGN",       (0, 0), (-1, -1), "LEFT"),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",  (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.append(t)
    story.append(Spacer(1, 3*mm))

    analise = (
        "O mercado está em janela de <b>pós-TOTS e pré-Festival of Football</b>. Com o TOTS Ultimate "
        "encerrado ontem (29/05), os preços de cartas ouro 83-88 sofreram pressão de venda mas já "
        "começam a se estabilizar. Em <b>6 dias</b> começa o Path to Glory (05/06), "
        "que vai gerar nova demanda por fodder para os SBCs de lançamento. "
        "Esta janela de 30/05 a 04/06 é ideal para acumular fodder barato. "
        "O Rivals Reward desta sexta-feira tende a deprimir preços temporariamente durante a noite — "
        "o melhor momento para comprar é <b>hoje entre 23h e 05h BRT</b>. "
        "Amanhã (sábado) o mercado se recupera parcialmente, e na segunda-feira (01/06) o preço "
        "costuma subir mais 15-25% em média."
    )
    story.append(Paragraph(analise, styles["CorpoTexto"]))

    # ── 2. TABELA DE OPORTUNIDADES ───────────────────────────────────────────
    story.append(Paragraph("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA", styles["SecaoTitulo"]))

    story.append(Paragraph(
        "Preços de compra-alvo baseados em janela pós-TOTS (30/05). "
        "<b>Margem líquida</b> já descontada a taxa de 5% da EA. "
        "Ordenadas por retorno esperado no curto prazo.",
        styles["CorpoTexto"]
    ))

    cabecalho = [
        "Jogador", "Rating", "Clube", "Compra\n(coins)", "Venda-Alvo\n(coins)",
        "Margem\nLíquida", "Horizonte", "Prioridade"
    ]

    dados = [
        # [Jogador, Rating, Clube, Compra, Venda, Margem, Horizonte, Prioridade]
        ["Jonathan Tah",       "87", "Bayer Leverkusen", "9.500",  "13.500", "+3.325",  "24-48h",  "ALTA ★★★"],
        ["Rubén Dias",         "86", "Man. City",        "5.800",  "8.200",  "+1.990",  "24-48h",  "ALTA ★★★"],
        ["Ona Batlle",         "86", "Barcelona (F)",    "6.200",  "8.800",  "+2.160",  "24-48h",  "ALTA ★★★"],
        ["Youri Tielemans",    "85", "Aston Villa",      "4.200",  "6.000",  "+1.500",  "24-48h",  "ALTA ★★★"],
        ["Alejandro Grimaldo", "85", "Bayer Leverkusen", "4.500",  "6.400",  "+1.580",  "24-48h",  "ALTA ★★★"],
        ["Ferdi Kadioglu",     "84", "Brighton",         "2.400",  "3.600",  "+1.020",  "24h",     "MÉDIA ★★"],
        ["Raúl Jiménez",       "84", "Fulham",           "2.200",  "3.300",  "+935",    "24h",     "MÉDIA ★★"],
        ["Brais Méndez",       "83", "Real Sociedad",    "1.400",  "2.100",  "+595",    "24h",     "MÉDIA ★★"],
        ["Sergi Roberto",      "83", "Barcelona",        "1.300",  "1.950",  "+552",    "24h",     "MÉDIA ★★"],
        ["Eder Militão (Gold)","85", "Real Madrid",      "4.000",  "6.500",  "+2.175",  "5-7 dias","PTG ★★★"],
        ["Endrick (Gold)",     "84", "Real Madrid",      "3.500",  "6.000",  "+2.200",  "5-7 dias","PTG ★★★"],
        ["Eduardo Camavinga",  "85", "Real Madrid",      "4.800",  "7.500",  "+2.325",  "5-7 dias","PTG ★★★"],
    ]

    table_data = [cabecalho] + dados
    col_widths = [36*mm, 14*mm, 30*mm, 18*mm, 20*mm, 16*mm, 18*mm, 20*mm]

    tab = Table(table_data, colWidths=col_widths, repeatRows=1)
    tab.setStyle(TableStyle([
        # Cabeçalho
        ("BACKGROUND",    (0, 0), (-1, 0),  CINZA_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  VERDE_EA),
        ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0),  7.5),
        ("ALIGN",         (0, 0), (-1, 0),  "CENTER"),
        # Dados
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 7.5),
        ("ALIGN",         (1, 1), (-1, -1), "CENTER"),
        ("ALIGN",         (0, 1), (0, -1),  "LEFT"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        # Margem positiva em verde
        ("TEXTCOLOR",     (5, 1), (5, -1),  VERDE_ESCURO),
        ("FONTNAME",      (5, 1), (5, -1),  "Helvetica-Bold"),
        # Prioridade ALTA em destaque
        ("TEXTCOLOR",     (7, 1), (7, 6),   colors.HexColor("#007800")),
        ("TEXTCOLOR",     (7, 7), (7, 9),   colors.HexColor("#CC6600")),
        ("TEXTCOLOR",     (7, 10),(7, -1),  colors.HexColor("#0055AA")),
        ("FONTNAME",      (7, 1), (7, -1),  "Helvetica-Bold"),
        # Grade
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 4),
        # Separador acima dos PTG
        ("LINEABOVE",     (0, 10),(-1, 10), 1.5, AMARELO),
    ]))
    story.append(tab)

    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "<b>PTG</b> = Pre-investment para Path to Glory (Festival of Football — inicia 05/06/2026). "
        "Cartas ouro desses jogadores tendem a valorizar quando saírem suas versões especiais e "
        "novos SBCs demandem fodder de liga Premier League, La Liga e Bundesliga.",
        styles["BulletItem"]
    ))

    # ── 3. ALOCAÇÃO DO BUDGET ────────────────────────────────────────────────
    story.append(Paragraph("3. ALOCAÇÃO DO BUDGET (40.000 coins)", styles["SecaoTitulo"]))

    budget_data = [
        ["Estratégia", "Coins Alocados", "Qtd. Estimada", "Objetivo"],
        ["SBC Fodder Flip (83-87)\nJonathan Tah, Rubén Dias, Grimaldo, Tielemans",
         "18.000", "~3-4 cartas 85-87\nou ~8-10 cartas 83-84",
         "Vender no pico 31/05-03/06\nRetorno esperado: +5.000 a +8.000"],
        ["Path to Glory Pre-Invest\nMilitão, Endrick, Camavinga",
         "12.500", "~3 cartas gold 84-85",
         "Vender 05-08/06 no lançamento PTG\nRetorno esperado: +5.000 a +7.500"],
        ["Thursday / Weekend Flip\nFodder barato 83-84",
         "6.000",  "~4-6 cartas 83-84",
         "Comprar hoje noite, vender dom/seg\nRetorno esperado: +1.500 a +3.000"],
        ["Reserva de Liquidez",
         "3.500",  "—",
         "Oportunidades espontâneas\ne cobrir bid losses"],
    ]

    tb = Table(budget_data, colWidths=[55*mm, 28*mm, 42*mm, 47*mm], repeatRows=1)
    tb.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),   CINZA_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0),   AMARELO),
        ("FONTNAME",      (0, 0), (-1, 0),   "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0),   8.5),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1),  [BRANCO, CINZA_CLARO]),
        ("FONTNAME",      (0, 1), (-1, -1),  "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1),  8),
        ("FONTNAME",      (1, 1), (1, -1),   "Helvetica-Bold"),
        ("TEXTCOLOR",     (1, 1), (1, -1),   VERDE_ESCURO),
        ("GRID",          (0, 0), (-1, -1),  0.4, colors.HexColor("#CCCCCC")),
        ("ALIGN",         (1, 0), (1, -1),   "CENTER"),
        ("ALIGN",         (2, 0), (2, -1),   "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1),  "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1),  5),
        ("BOTTOMPADDING", (0, 0), (-1, -1),  5),
        ("LEFTPADDING",   (0, 0), (-1, -1),  6),
    ]))
    story.append(tb)

    # ── 4. ESTRATÉGIA DE TIMING ──────────────────────────────────────────────
    story.append(Paragraph("4. ESTRATÉGIA DE TIMING — QUANDO COMPRAR E VENDER", styles["SecaoTitulo"]))

    timing_data = [
        ["Horário / Data", "Ação", "Justificativa"],
        ["Hoje 23h–05h BRT (30-31/05)",
         "COMPRAR fodder 83-87 e cards gold PTG",
         "Pico de abertura de packs pós-Rivals Rewards → preços mais baixos da semana"],
        ["Sábado 09h–14h BRT (31/05)",
         "Monitorar preços; comprar 2ª leva se caiu mais",
         "Mercado ainda absorvendo supply; oportunidade de bid war"],
        ["Sábado 18h–22h BRT (31/05)",
         "VENDER lote 1 de fodder 83-84",
         "Demanda volta com jogadores online no fim de tarde"],
        ["Dom 10h–16h BRT (01/06)",
         "VENDER lote 2 de fodder 85-87",
         "Domingo = pico de usuários → maior liquidez e preços mais altos"],
        ["Segunda–Quarta (02-04/06)",
         "Manter pre-invest PTG; vender fodder residual",
         "Mercado estável pré-Festival; preços fodder em topo semanal"],
        ["Qui–Sex (05-06/06)",
         "VENDER cards PTG (Militão, Endrick, Camavinga)",
         "Path to Glory lançado: demanda por base cards e fodder da LaLiga/EPL explode"],
    ]

    tt = Table(timing_data, colWidths=[42*mm, 57*mm, 73*mm], repeatRows=1)
    tt.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  CINZA_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  VERDE_EA),
        ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0),  8.5),
        ("FONTNAME",      (0, 1), (0, -1),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 1), (-1, -1), 8),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ]))
    story.append(tt)

    # ── 5. ESTIMATIVA DE RETORNO EM 48H ─────────────────────────────────────
    story.append(Paragraph("5. ESTIMATIVA DE RETORNO EM 48H", styles["SecaoTitulo"]))

    retorno_data = [
        ["Cenário", "Entradas\n(coins)", "Saídas Esperadas\n(após taxa 5%)", "Lucro Líquido", "ROI"],
        ["Conservador\n(preços sobem 20%)",
         "36.500", "43.100", "+6.600", "+18%"],
        ["Base\n(preços sobem 35%)",
         "36.500", "48.200", "+11.700", "+32%"],
        ["Otimista\n(Path to Glory + novo SBC drop)",
         "36.500", "54.500", "+18.000", "+49%"],
    ]

    tr = Table(retorno_data, colWidths=[42*mm, 28*mm, 40*mm, 28*mm, 22*mm], repeatRows=1)
    tr.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  CINZA_ESCURO),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  AMARELO),
        ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0),  9),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 9),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
        ("TEXTCOLOR",     (3, 1), (3, -1),  VERDE_ESCURO),
        ("TEXTCOLOR",     (4, 1), (4, -1),  VERDE_ESCURO),
        ("FONTNAME",      (3, 1), (4, -1),  "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("ALIGN",         (1, 0), (-1, -1), "CENTER"),
        ("ALIGN",         (0, 0), (0, -1),  "LEFT"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ]))
    story.append(tr)

    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "<b>Nota:</b> Valores calculados sobre 36.500 coins investidos (3.500 em reserva). "
        "Cenário conservador assume apenas fodder flip 83-87 nos dias 31/05-01/06. "
        "Cenário otimista inclui valorização PTG completa dos cards de base em 05-06/06. "
        "Todos os valores já refletem a taxa de 5% cobrada pela EA em cada transação de venda.",
        styles["BulletItem"]
    ))

    # ── 6. REGRAS DE OURO ────────────────────────────────────────────────────
    story.append(Paragraph("6. 8 REGRAS DE OURO DO TRADE", styles["SecaoTitulo"]))

    regras = [
        ("1", "Nunca invista mais de 30% do budget em um único jogador ou aposta.",
         "Diversificação protege de crashes inesperados."),
        ("2", "Compre sempre via BID durante pico de packs (quinta–sexta, Rivals Rewards).",
         "Reduz custo médio em 20-35% vs. Buy Now."),
        ("3", "Venda antes de grandes eventos de pack (lightning rounds, novos SBCs).",
         "Preços caem durante packs pesados — saia antes."),
        ("4", "Respeite a janela de 5% da EA: defina venda-alvo = custo × 1.0 ÷ 0.95 + lucro.",
         "Calcule sempre o breakeven antes de comprar."),
        ("5", "Nunca entre em pânico e venda abaixo do custo — a não ser que precise do capital.",
         "Fodder gold sempre tem piso (acima do discard)."),
        ("6", "Mantenha 10-15% do capital em coins líquidas para oportunidades relâmpago.",
         "Mercado cria janelas de 5-10 min que exigem ação rápida."),
        ("7", "Monitore Reddit (r/fut), FUT.GG e FUTBIN para leaks de SBCs antes de investir.",
         "Informação antecipada = vantagem de 2-6h sobre o mercado."),
        ("8", "Registre cada trade (entrada, saída, lucro) para calcular seu ROI real.",
         "Sem dados, você repete os mesmos erros sem perceber."),
    ]

    for num, regra, detalhe in regras:
        story.append(Paragraph(
            f"<b>Regra {num}:</b> {regra} <font color='#666666'><i>→ {detalhe}</i></font>",
            styles["RegrasOuro"]
        ))
    story.append(Spacer(1, 2*mm))

    # ── 7. DISCLAIMER ────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CCCCCC"), spaceAfter=6))
    story.append(Paragraph("DISCLAIMER", ParagraphStyle(
        "DisclaimerTitulo", fontName="Helvetica-Bold", fontSize=8.5,
        textColor=colors.HexColor("#888888"), alignment=TA_CENTER
    )))
    disclaimer_text = (
        "Este relatório é gerado com fins educacionais e informativos para uso pessoal em EA FC 26 Ultimate Team. "
        "Os preços indicados são estimativas baseadas em dados históricos de mercado e tendências observadas — "
        "não constituem garantia de lucro. O mercado de FUT é volátil e influenciado por fatores imprevisíveis "
        "(novos SBCs, crashes, eventos surpresa, decisões da EA). "
        "O autor não se responsabiliza por perdas de coins decorrentes das estratégias aqui descritas. "
        "Opere sempre dentro do que é permitido pelos Termos de Serviço da EA Sports. "
        "Nunca utilize scripts, bots ou automações — isso viola os ToS e pode resultar em banimento permanente da conta."
    )
    story.append(Paragraph(disclaimer_text, styles["Disclaimer"]))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"PDF gerado: {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    build_pdf()
