#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Relatório de Trading EA FC 26 Ultimate Team
Data: 27/05/2026 14:07 UTC
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import HexColor

# ─────────────────────────────────────────────
#  CORES DO TEMA
# ─────────────────────────────────────────────
VERDE_ESCURO  = HexColor("#0D3B1A")
VERDE_MEDIO   = HexColor("#1A6B2F")
VERDE_CLARO   = HexColor("#2E9E50")
VERDE_NEON    = HexColor("#39FF14")
DOURADO       = HexColor("#FFD700")
DOURADO_ESC   = HexColor("#B8860B")
CINZA_ESCURO  = HexColor("#1C1C1C")
CINZA_MEDIO   = HexColor("#2D2D2D")
CINZA_CLARO   = HexColor("#444444")
BRANCO        = HexColor("#FFFFFF")
LARANJA       = HexColor("#FF8C00")
VERMELHO      = HexColor("#E74C3C")
AZUL_CLARO    = HexColor("#3498DB")

OUTPUT_FILE = "relatorio-trading-2026-05-27-14h.pdf"

def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles["titulo"] = ParagraphStyle(
        "titulo",
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=DOURADO,
        alignment=TA_CENTER,
        spaceAfter=4,
        leading=28,
    )
    styles["subtitulo"] = ParagraphStyle(
        "subtitulo",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=VERDE_NEON,
        alignment=TA_CENTER,
        spaceAfter=2,
        leading=16,
    )
    styles["data"] = ParagraphStyle(
        "data",
        fontName="Helvetica",
        fontSize=10,
        textColor=HexColor("#AAAAAA"),
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    styles["secao"] = ParagraphStyle(
        "secao",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=DOURADO,
        alignment=TA_LEFT,
        spaceBefore=14,
        spaceAfter=4,
        leading=16,
    )
    styles["corpo"] = ParagraphStyle(
        "corpo",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=BRANCO,
        alignment=TA_JUSTIFY,
        spaceAfter=5,
        leading=14,
    )
    styles["bullet"] = ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=BRANCO,
        alignment=TA_LEFT,
        spaceBefore=2,
        spaceAfter=2,
        leftIndent=12,
        leading=13,
    )
    styles["destaque"] = ParagraphStyle(
        "destaque",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=VERDE_NEON,
        alignment=TA_LEFT,
        spaceBefore=2,
        spaceAfter=2,
        leftIndent=12,
        leading=13,
    )
    styles["tabela_header"] = ParagraphStyle(
        "tabela_header",
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=CINZA_ESCURO,
        alignment=TA_CENTER,
        leading=10,
    )
    styles["tabela_celula"] = ParagraphStyle(
        "tabela_celula",
        fontName="Helvetica",
        fontSize=8,
        textColor=BRANCO,
        alignment=TA_CENTER,
        leading=10,
    )
    styles["aviso"] = ParagraphStyle(
        "aviso",
        fontName="Helvetica-Oblique",
        fontSize=7.5,
        textColor=HexColor("#888888"),
        alignment=TA_JUSTIFY,
        spaceAfter=3,
        leading=11,
    )
    styles["regra_num"] = ParagraphStyle(
        "regra_num",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=DOURADO,
        alignment=TA_LEFT,
        spaceBefore=4,
        spaceAfter=1,
        leading=13,
    )
    return styles


def header_line(color=VERDE_CLARO, thickness=1.5):
    return HRFlowable(
        width="100%", thickness=thickness,
        color=color, spaceAfter=6, spaceBefore=2
    )


def build_document():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        leftMargin=1.8*cm, rightMargin=1.8*cm,
        topMargin=1.5*cm, bottomMargin=1.5*cm,
    )
    story = []
    S = build_styles()

    # ─── FUNDO / CABEÇALHO ─────────────────────────
    story.append(Spacer(1, 0.2*cm))

    # Box de título
    title_data = [
        [Paragraph("⚽  EA FC 26 ULTIMATE TEAM", S["titulo"])],
        [Paragraph("RELATÓRIO DE TRADING — ANÁLISE DE MERCADO", S["subtitulo"])],
        [Paragraph("27/05/2026  14:07 UTC  |  Budget: 40.000 coins  |  Plataforma: PS/Xbox", S["data"])],
    ]
    title_table = Table(title_data, colWidths=[17.4*cm])
    title_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), VERDE_ESCURO),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [VERDE_ESCURO]),
        ("BOX", (0,0), (-1,-1), 2, DOURADO),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ]))
    story.append(title_table)
    story.append(Spacer(1, 0.4*cm))

    # ─── SEÇÃO 1: CONTEXTO DE MERCADO ─────────────────
    story.append(Paragraph("1. CONTEXTO DO MERCADO", S["secao"]))
    story.append(header_line(DOURADO))

    contexto_data = [
        [
            Paragraph("🏆 EVENTO ATIVO", S["tabela_header"]),
            Paragraph("📅 PERÍODO", S["tabela_header"]),
            Paragraph("📊 TENDÊNCIA", S["tabela_header"]),
        ],
        [
            Paragraph("Ultimate TOTS + End of an Era SBCs", S["tabela_celula"]),
            Paragraph("22/05 → 29/05/2026", S["tabela_celula"]),
            Paragraph("Crash de preços → Fundo do mercado", S["tabela_celula"]),
        ],
    ]
    ctx_table = Table(contexto_data, colWidths=[6.5*cm, 5*cm, 5.9*cm])
    ctx_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DOURADO_ESC),
        ("BACKGROUND", (0,1), (-1,1), CINZA_MEDIO),
        ("BOX", (0,0), (-1,-1), 1.2, DOURADO),
        ("INNERGRID", (0,0), (-1,-1), 0.5, CINZA_CLARO),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    story.append(ctx_table)
    story.append(Spacer(1, 0.25*cm))

    story.append(Paragraph(
        "A semana de <b>27 a 29 de maio de 2026</b> marca os últimos dias do evento "
        "<b>Ultimate TOTS</b> — o maior evento de fim de temporada do EA FC 26. "
        "Todos os principais pacotes estão liberando cartas TOTS, inundando o mercado "
        "de cartas raras e especiais. Paralelamente, os <b>End of an Era SBCs</b> "
        "(Salah 95, Griezmann 94, Bernardo Silva 93, Goretzka, Robertson) estão ativos, "
        "consumindo grandes quantidades de fodder de alta avaliação.",
        S["corpo"]
    ))
    story.append(Paragraph(
        "O padrão histórico durante o Ultimate TOTS é claro: <b>preços de cartas gold "
        "comuns (83–87) atingem o piso absoluto</b> enquanto os pacotes são abertos em "
        "massa, depois <b>recuperam 40–120% após o evento encerrar</b> (29/05) quando "
        "a oferta colapsa e a demanda por SBC fodder continua. "
        "Este é o momento ideal para acumulação massiva de fodder barato.",
        S["corpo"]
    ))

    # Destaques rápidos
    bullets_ctx = [
        ("🟢", "TOTS acaba em 48h (29/05) → janela de compra está ABERTA agora"),
        ("🟢", "End of Era SBCs ativos → demanda elevada por 84–87 rated"),
        ("🟡", "Novos SBCs podem ser lançados quinta-feira (28/05) → spike de preços"),
        ("🔴", "Não comprar cartas TOTS caras agora — supply ainda alto até 29/05"),
    ]
    for icon, text in bullets_ctx:
        story.append(Paragraph(f"{icon}  {text}", S["bullet"]))

    story.append(Spacer(1, 0.3*cm))

    # ─── SEÇÃO 2: CARTAS RECOMENDADAS ──────────────────
    story.append(Paragraph("2. CARTAS RECOMENDADAS PARA COMPRA", S["secao"]))
    story.append(header_line(DOURADO))

    story.append(Paragraph(
        "Tabela com os melhores alvos de compra para o budget de <b>40.000 coins</b>. "
        "Margem líquida já descontando a taxa de 5% da EA na venda. "
        "Preços referentes ao mercado PS/Xbox em 27/05/2026.",
        S["corpo"]
    ))
    story.append(Spacer(1, 0.15*cm))

    # Cabeçalho da tabela
    h = S["tabela_header"]
    c = S["tabela_celula"]

    def hdr(t): return Paragraph(t, h)
    def cel(t, color=None):
        if color:
            style = ParagraphStyle("c2", parent=S["tabela_celula"], textColor=color)
            return Paragraph(t, style)
        return Paragraph(t, c)

    table_data = [
        [hdr("JOGADOR"), hdr("OVR"), hdr("CLUBE"), hdr("COMPRA\n(coins)"),
         hdr("VENDA\n(coins)"), hdr("MARGEM\nLÍQ. 5%"), hdr("ESTRATÉGIA")],

        # SBC FODDER — 84 RATED
        [cel("Manuel Neuer"), cel("84"), cel("Bayern München"),
         cel("750"), cel("1.300"), cel("+487", VERDE_NEON), cel("Mass Buy")],

        [cel("Francesco Acerbi"), cel("84"), cel("Inter Milan"),
         cel("750"), cel("1.300"), cel("+487", VERDE_NEON), cel("Mass Buy")],

        [cel("Jordan Pickford"), cel("84"), cel("Everton"),
         cel("750"), cel("1.300"), cel("+487", VERDE_NEON), cel("Mass Buy")],

        [cel("Cody Gakpo"), cel("84"), cel("Liverpool"),
         cel("750"), cel("1.300"), cel("+487", VERDE_NEON), cel("Mass Buy")],

        # SBC FODDER — 85 RATED
        [cel("Karim Benzema"), cel("85"), cel("Al-Ittihad"),
         cel("900"), cel("1.900"), cel("+905", VERDE_NEON), cel("Flip/SBC")],

        [cel("N'Golo Kanté"), cel("85"), cel("Al-Ittihad"),
         cel("950"), cel("1.900"), cel("+855", VERDE_NEON), cel("Flip/SBC")],

        [cel("Delphine Cascarino"), cel("85"), cel("Lyon (W)"),
         cel("850"), cel("1.700"), cel("+765", VERDE_NEON), cel("Flip/SBC")],

        # SBC FODDER — 86 RATED
        [cel("Ibrahima Konaté"), cel("86"), cel("Liverpool"),
         cel("1.500"), cel("3.000"), cel("+1.350", DOURADO), cel("Investimento")],

        [cel("Ruben Dias"), cel("86"), cel("Man. City"),
         cel("1.600"), cel("3.200"), cel("+1.440", DOURADO), cel("Investimento")],

        [cel("Lea Schüller"), cel("86"), cel("Bayern München (W)"),
         cel("1.100"), cel("2.400"), cel("+1.180", DOURADO), cel("Flip/SBC")],

        # 87 RATED — menor quantidade
        [cel("Jonathan Tah"), cel("87"), cel("Bayer Leverkusen"),
         cel("10.000"), cel("17.000"), cel("+6.150", LARANJA), cel("Hold 48h")],
    ]

    col_widths = [3.8*cm, 1.1*cm, 3.6*cm, 1.8*cm, 1.8*cm, 2.0*cm, 2.4*cm]
    cards_table = Table(table_data, colWidths=col_widths, repeatRows=1)

    row_colors = [
        CINZA_MEDIO, CINZA_ESCURO, CINZA_MEDIO, CINZA_ESCURO, CINZA_MEDIO,
        HexColor("#252510"), HexColor("#1E1E0A"), HexColor("#252510"),
        HexColor("#0A1A25"), HexColor("#0A1A25"),
        HexColor("#1A250A"),
        HexColor("#1A1200"),
    ]

    style_cmds = [
        ("BACKGROUND", (0,0), (-1,0), DOURADO_ESC),
        ("TEXTCOLOR", (0,0), (-1,0), CINZA_ESCURO),
        ("BOX", (0,0), (-1,-1), 1.5, DOURADO),
        ("INNERGRID", (0,0), (-1,-1), 0.4, CINZA_CLARO),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        # Separadores visuais entre grupos
        ("LINEABOVE", (0,5), (-1,5), 1, VERDE_CLARO),   # início dos 85
        ("LINEABOVE", (0,8), (-1,8), 1, AZUL_CLARO),    # início dos 86
        ("LINEABOVE", (0,11), (-1,11), 1, LARANJA),     # início dos 87
    ]
    for i, bg in enumerate(row_colors, start=1):
        style_cmds.append(("BACKGROUND", (0,i), (-1,i), bg))

    cards_table.setStyle(TableStyle(style_cmds))
    story.append(cards_table)
    story.append(Spacer(1, 0.2*cm))

    # Legenda
    legenda_data = [[
        Paragraph("🟢 Mass Buy = comprar 20–30 cartas | 🟡 Flip/SBC = comprar 10–15 | 🟠 Hold 48h = comprar 2–3 cartas | Margem = (venda × 0,95) − compra", S["aviso"])
    ]]
    leg_table = Table(legenda_data, colWidths=[17.4*cm])
    leg_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#111111")),
        ("BOX", (0,0), (-1,-1), 0.5, CINZA_CLARO),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
    ]))
    story.append(leg_table)
    story.append(Spacer(1, 0.3*cm))

    # ─── SEÇÃO 3: ALOCAÇÃO DO BUDGET ──────────────────
    story.append(Paragraph("3. ALOCAÇÃO SUGERIDA DO BUDGET (40.000 coins)", S["secao"]))
    story.append(header_line(DOURADO))

    alloc_data = [
        [hdr("FAIXA"), hdr("JOGADORES-ALVO"), hdr("QTD."), hdr("CUSTO TOTAL"), hdr("% DO BUDGET")],
        [cel("84 rated"), cel("Neuer / Acerbi / Pickford / Gakpo"), cel("28 cartas"), cel("21.000"), cel("52,5%")],
        [cel("85 rated"), cel("Benzema / Kanté / Cascarino"), cel("10 cartas"), cel("9.000"), cel("22,5%")],
        [cel("86 rated"), cel("Konaté / Dias / Schüller"), cel("5 cartas"), cel("7.500"), cel("18,75%")],
        [cel("87 rated"), cel("Jonathan Tah"), cel("1 carta"), cel("10.000"), cel("25,0%")],
        [cel("Reserva"), cel("Relisting / reentrada rápida"), cel("—"), cel("2.500"), cel("6,25%")],
    ]
    alloc_table = Table(alloc_data, colWidths=[2.8*cm, 6.5*cm, 2.2*cm, 2.9*cm, 3.0*cm], repeatRows=1)
    alloc_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DOURADO_ESC),
        ("TEXTCOLOR", (0,0), (-1,0), CINZA_ESCURO),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CINZA_ESCURO, CINZA_MEDIO]),
        ("BOX", (0,0), (-1,-1), 1.2, DOURADO),
        ("INNERGRID", (0,0), (-1,-1), 0.4, CINZA_CLARO),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BACKGROUND", (0,4), (-1,4), CINZA_ESCURO),
        ("TEXTCOLOR", (3,4), (3,4), LARANJA),
    ]))
    story.append(alloc_table)

    # Nota sobre Jonathan Tah
    story.append(Spacer(1, 0.1*cm))
    story.append(Paragraph(
        "⚠️ <b>Nota sobre Jonathan Tah (87):</b> O custo de 10.000 coins ultrapassa "
        "o budget remanescente após as outras compras — priorize os grupos 84–86 primeiro. "
        "Compre Tah apenas se sobrar budget ou substituir parte dos 85-rated.",
        S["aviso"]
    ))
    story.append(Spacer(1, 0.3*cm))

    # ─── SEÇÃO 4: ESTRATÉGIA DE TIMING ─────────────────
    story.append(Paragraph("4. ESTRATÉGIA DE TIMING", S["secao"]))
    story.append(header_line(DOURADO))

    timing_data = [
        [hdr("FASE"), hdr("QUANDO"), hdr("AÇÃO"), hdr("MOTIVO")],
        [
            cel("COMPRA", VERDE_NEON),
            cel("Agora → Qui 28/05 manhã"),
            cel("Mass buy 84–86 rated\nSnipe abaixo do preço médio"),
            cel("Piso de mercado TOTS\nMáxima oferta, mínima demanda"),
        ],
        [
            cel("MONITORAR", DOURADO),
            cel("Qui 28/05 tarde"),
            cel("Verificar novos SBCs\ne requisitos de fodder"),
            cel("EA costuma soltar\nSBC quinta/sexta"),
        ],
        [
            cel("RELISTING", LARANJA),
            cel("Sex 29/05 madrugada\n(00h–06h UTC)"),
            cel("Recolocar cards\npróximo preço médio"),
            cel("Último dia de TOTS\nDemanda por completar SBCs"),
        ],
        [
            cel("VENDA FINAL", VERDE_CLARO),
            cel("Sex 29/05 após 18h\nou Sab 30/05"),
            cel("Vender pelo preço-alvo\nou acima"),
            cel("Fim de TOTS = supply cai\nPreços se recuperam"),
        ],
    ]
    timing_table = Table(timing_data, colWidths=[2.8*cm, 3.9*cm, 5.2*cm, 5.5*cm], repeatRows=1)
    timing_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DOURADO_ESC),
        ("TEXTCOLOR", (0,0), (-1,0), CINZA_ESCURO),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CINZA_ESCURO, CINZA_MEDIO]),
        ("BOX", (0,0), (-1,-1), 1.2, DOURADO),
        ("INNERGRID", (0,0), (-1,-1), 0.4, CINZA_CLARO),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    story.append(timing_table)
    story.append(Spacer(1, 0.3*cm))

    # ─── SEÇÃO 5: ESTIMATIVA DE RETORNO ─────────────────
    story.append(Paragraph("5. ESTIMATIVA DE RETORNO EM 48 HORAS", S["secao"]))
    story.append(header_line(DOURADO))

    story.append(Paragraph(
        "Projeção baseada na alocação sugerida (investimento total: <b>~37.500 coins</b>). "
        "Cenários calculados após desconto de 5% de taxa EA sobre cada venda.",
        S["corpo"]
    ))

    retorno_data = [
        [hdr("CENÁRIO"), hdr("PREMISSA"), hdr("RETORNO\nBRUTO"), hdr("RETORNO\nLÍQUIDO"), hdr("CAPITAL\nFINAL"), hdr("LUCRO\n(%)")]  ,
        [
            cel("🔵 Conservador", AZUL_CLARO),
            cel("Venda ~30% acima\ndo custo médio"),
            cel("+10.500"),
            cel("+9.975", VERDE_NEON),
            cel("49.975"),
            cel("+24,9%", VERDE_NEON),
        ],
        [
            cel("🟢 Base", VERDE_CLARO),
            cel("Venda 50–70% acima\n(padrão pós-TOTS)"),
            cel("+18.750"),
            cel("+17.812", VERDE_NEON),
            cel("57.812"),
            cel("+44,5%", VERDE_NEON),
        ],
        [
            cel("🟡 Otimista", DOURADO),
            cel("Novo SBC quinta +\nrecuperação pós-TOTS"),
            cel("+28.000"),
            cel("+26.600", DOURADO),
            cel("66.600"),
            cel("+66,5%", DOURADO),
        ],
    ]
    retorno_table = Table(retorno_data, colWidths=[3.2*cm, 4.5*cm, 2.4*cm, 2.7*cm, 2.5*cm, 2.1*cm], repeatRows=1)
    retorno_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DOURADO_ESC),
        ("TEXTCOLOR", (0,0), (-1,0), CINZA_ESCURO),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CINZA_ESCURO, CINZA_MEDIO, HexColor("#1A1A0D")]),
        ("BOX", (0,0), (-1,-1), 1.2, DOURADO),
        ("INNERGRID", (0,0), (-1,-1), 0.4, CINZA_CLARO),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    story.append(retorno_table)
    story.append(Spacer(1, 0.15*cm))

    story.append(Paragraph(
        "💡 <b>Recomendação:</b> Trabalhar com expectativa do cenário Base (+44,5%) "
        "— isso transformaria 40.000 coins em ~57.800 coins em 48h. "
        "Se um novo SBC for lançado quinta (28/05) com requisito de 85–87 rated, "
        "o cenário Otimista se torna muito provável.",
        S["destaque"]
    ))
    story.append(Spacer(1, 0.3*cm))

    # ─── SEÇÃO 6: OPORTUNIDADES ADICIONAIS ─────────────
    story.append(Paragraph("6. OPORTUNIDADES ADICIONAIS", S["secao"]))
    story.append(header_line(DOURADO))

    oport_items = [
        ("End of Era SBC — Griezmann 94",
         "SBC com múltiplos squads de 86–88 rated. "
         "Monitorar requisitos exatos no jogo. "
         "Se exigir 86 rated sem carta especial, vender Konaté/Dias imediatamente."),
        ("Evolutions ativas",
         "Com budget restante após o flip, verificar se há Evolution barata "
         "(abaixo de 20.000 coins) para um centroavante 81 rated. "
         "Evoluções de CDM/CB tendem a valorizar 3–5x o custo de base após upgrade."),
        ("Thursday Flip — 28/05",
         "Amanhã à tarde (18h UTC), EA normalmente anuncia/lança novo conteúdo. "
         "Ter o budget investido antes das 14h UTC de quinta garante "
         "que as cartas já estejam em listagem quando o spike acontecer."),
        ("Post-TOTS Recovery — 30/05 em diante",
         "Após encerramento do TOTS (29/05 18h BST), "
         "os 84-rated devem subir para 1.200–1.500 e os 86-rated para 2.500–3.500. "
         "Não vender apressado — aguardar o pico de demanda no fim de semana."),
    ]
    for titulo, texto in oport_items:
        story.append(Paragraph(f"▸  <b>{titulo}</b>", S["destaque"]))
        story.append(Paragraph(texto, S["corpo"]))
    story.append(Spacer(1, 0.3*cm))

    # ─── SEÇÃO 7: 8 REGRAS DE OURO ──────────────────────
    story.append(Paragraph("7. AS 8 REGRAS DE OURO DO TRADE", S["secao"]))
    story.append(header_line(DOURADO))

    regras = [
        ("Compre no pico de oferta, venda no pico de demanda",
         "TOTS = pico de abertura de pacotes = preços no chão. "
         "Fim de TOTS = demanda por SBCs sem oferta nova = preços sobem."),
        ("Nunca gaste 100% do budget de uma vez",
         "Reserve ao menos 10–15% para recompras oportunistas "
         "e para cobrir listings não vendidos."),
        ("Taxa de 5% EA é custo real — calcule sempre",
         "Uma venda de 2.000 coins traz apenas 1.900 coins. "
         "O preço de venda alvo deve cobrir compra + 5% + margem desejada."),
        ("Monitore os SBCs antes de vender",
         "Um novo SBC lançado pode dobrar o valor do seu fodder em horas. "
         "Cheque o jogo e o FUTBIN antes de listar."),
        ("Paciência supera velocidade na maioria dos flips",
         "Listing de 1h gera menos lucro que listing de 6–12h. "
         "Não cancele listings prematuramente por ansiedade."),
        ("Diversifique entre ratings (84, 85, 86)",
         "Cada rating tem perfil diferente de liquidez e margem. "
         "Mass buy em 84 gera giro rápido; 86+ gera maior lucro por unidade."),
        ("Acompanhe o calendário de conteúdo",
         "Quinta-feira e sexta cedo (antes das 18h BST) são os momentos-chave "
         "para compras estratégicas antes de novos drops de SBC/conteúdo."),
        ("Registre todas as operações",
         "Anotar compra, venda e lucro de cada batch permite "
         "identificar quais ratings e jogadores rendem mais no longo prazo."),
    ]
    for i, (titulo, descricao) in enumerate(regras, start=1):
        story.append(Paragraph(f"{i}. {titulo}", S["regra_num"]))
        story.append(Paragraph(descricao, S["corpo"]))
    story.append(Spacer(1, 0.3*cm))

    # ─── DISCLAIMER ─────────────────────────────────────
    story.append(header_line(CINZA_CLARO, 1))
    disc_data = [[
        Paragraph(
            "⚠️ DISCLAIMER — Este relatório é gerado com base em dados públicos de mercado "
            "(FUTBIN, FUT.GG, Football Gaming Zone, FIFAUltimateTeam.it) e padrões históricos "
            "do mercado FUT. Os preços e margens apresentados são estimativas e podem variar "
            "significativamente devido à volatilidade do mercado de transferências do EA FC 26. "
            "Nenhuma operação de trading é garantida. Invista apenas o que está disposto a "
            "perder. EA Sports pode alterar mecânicas de mercado, lançar conteúdo inesperado "
            "ou modificar price ranges a qualquer momento. Relatório gerado em 27/05/2026 às "
            "14:07 UTC. Válido por até 24 horas a partir desta data.",
            S["aviso"]
        )
    ]]
    disc_table = Table(disc_data, colWidths=[17.4*cm])
    disc_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#111111")),
        ("BOX", (0,0), (-1,-1), 0.8, CINZA_CLARO),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ]))
    story.append(disc_table)

    # ─── FOOTER ─────────────────────────────────────────
    story.append(Spacer(1, 0.15*cm))
    story.append(Paragraph(
        "📊 EA FC 26 Trading Report  •  27/05/2026  •  github.com/kaiohsferreira/fifa-trading",
        S["data"]
    ))

    # Build
    doc.build(story)
    print(f"✅ PDF gerado: {OUTPUT_FILE}")


if __name__ == "__main__":
    build_document()
