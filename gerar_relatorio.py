#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Relatório de Trading EA FC 26 Ultimate Team
Data: 27/05/2026 08:06 UTC
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.lib.colors import HexColor

# ─── Cores ───────────────────────────────────────────────────────────────────
VERDE_EA   = HexColor('#00D166')
VERDE_DARK = HexColor('#007A3D')
PRETO      = HexColor('#0A0A0A')
CINZA_DARK = HexColor('#1A1A2E')
CINZA_MED  = HexColor('#2D2D44')
CINZA_LIGHT= HexColor('#E8E8F0')
AMARELO    = HexColor('#FFD700')
VERMELHO   = HexColor('#FF4444')
LARANJA    = HexColor('#FF8C00')
BRANCO     = colors.white

OUTPUT = "relatorio-trading-2026-05-27-08h.pdf"

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=1.8*cm,
        leftMargin=1.8*cm,
        topMargin=1.8*cm,
        bottomMargin=1.8*cm,
        title="Relatório de Trading EA FC 26 – 27/05/2026",
        author="FC Trading Bot"
    )

    styles = getSampleStyleSheet()

    # ── Estilos personalizados ────────────────────────────────────────────
    title_style = ParagraphStyle(
        'title_style', parent=styles['Title'],
        fontName='Helvetica-Bold', fontSize=22,
        textColor=VERDE_EA, alignment=TA_CENTER,
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'subtitle_style', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=13,
        textColor=AMARELO, alignment=TA_CENTER,
        spaceAfter=2
    )
    date_style = ParagraphStyle(
        'date_style', parent=styles['Normal'],
        fontName='Helvetica', fontSize=10,
        textColor=CINZA_LIGHT, alignment=TA_CENTER,
        spaceAfter=6
    )
    section_style = ParagraphStyle(
        'section_style', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=13,
        textColor=VERDE_EA, spaceBefore=14, spaceAfter=6,
        borderPad=4
    )
    body_style = ParagraphStyle(
        'body_style', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9.5,
        textColor=PRETO, leading=14, alignment=TA_JUSTIFY,
        spaceAfter=4
    )
    bold_body = ParagraphStyle(
        'bold_body', parent=body_style,
        fontName='Helvetica-Bold', textColor=CINZA_DARK
    )
    bullet_style = ParagraphStyle(
        'bullet_style', parent=body_style,
        leftIndent=16, bulletIndent=4, spaceAfter=3
    )
    label_style = ParagraphStyle(
        'label_style', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.5,
        textColor=BRANCO, alignment=TA_CENTER
    )
    value_style = ParagraphStyle(
        'value_style', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10,
        textColor=VERDE_EA, alignment=TA_CENTER
    )
    warning_style = ParagraphStyle(
        'warning_style', parent=body_style,
        fontSize=8.5, textColor=HexColor('#555555'),
        alignment=TA_CENTER, fontName='Helvetica-Oblique'
    )
    rule_style = ParagraphStyle(
        'rule_style', parent=body_style,
        fontName='Helvetica', fontSize=9.5,
        textColor=CINZA_DARK, leftIndent=8, spaceAfter=5
    )
    green_bold = ParagraphStyle(
        'green_bold', parent=body_style,
        fontName='Helvetica-Bold', textColor=VERDE_DARK, fontSize=10
    )
    red_text = ParagraphStyle(
        'red_text', parent=body_style,
        fontName='Helvetica-Bold', textColor=VERMELHO, fontSize=9.5
    )

    story = []

    # ═══════════════════════════════════════════════════════════════════════
    # CABEÇALHO
    # ═══════════════════════════════════════════════════════════════════════
    header_data = [[
        Paragraph("⚽  EA FC 26 ULTIMATE TEAM", title_style),
    ]]
    header_table = Table(header_data, colWidths=[17.4*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CINZA_DARK),
        ('ROUNDEDCORNERS', [8]),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("RELATÓRIO DIÁRIO DE TRADING", subtitle_style))
    story.append(Paragraph("27/05/2026  08:06 UTC  •  Budget: 40.000 coins", date_style))
    story.append(HRFlowable(width="100%", thickness=2, color=VERDE_EA, spaceAfter=8))

    # ═══════════════════════════════════════════════════════════════════════
    # KPIs rápidos
    # ═══════════════════════════════════════════════════════════════════════
    kpi_data = [
        [
            Paragraph("BUDGET", label_style),
            Paragraph("EVENTO ATIVO", label_style),
            Paragraph("ESTRATÉGIA", label_style),
            Paragraph("META 48H", label_style),
        ],
        [
            Paragraph("40.000 🪙", value_style),
            Paragraph("Ultimate TOTS\n+ End of an Era", value_style),
            Paragraph("Fodder Flip\n+ Evolution Invest", value_style),
            Paragraph("+25% → +55%", value_style),
        ]
    ]
    kpi_table = Table(kpi_data, colWidths=[4.1*cm]*4)
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CINZA_MED),
        ('BACKGROUND', (0,1), (-1,1), CINZA_DARK),
        ('TEXTCOLOR', (0,0), (-1,-1), BRANCO),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#3A3A5C')),
        ('ROUNDEDCORNERS', [6]),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 0.5*cm))

    # ═══════════════════════════════════════════════════════════════════════
    # 1. CONTEXTO DO MERCADO
    # ═══════════════════════════════════════════════════════════════════════
    story.append(Paragraph("1. CONTEXTO DO MERCADO", section_style))

    ctx_text = [
        ("🏆  Ultimate TOTS (22–29/05/2026)",
         "A semana mais importante do calendário de Ultimate Team: o <b>Ultimate TOTS</b> está em pacotes desde "
         "sexta-feira 22/05 e sai em 29/05 às 18h BST. Os 45 melhores jogadores da temporada (6 com 97 OVR, "
         "16 com 96 OVR) estão disponíveis em packs. Isso gera abertura massiva de pacotes, inundando o "
         "mercado de cartas 85-88 e derrubando seus preços — janela de ouro para compra de fodder."),
        ("🔥  End of an Era SBCs (live até 29/05)",
         "Ao longo desta semana a EA lançou SBCs de jogadores que encerraram ou estão encerrando suas "
         "carreiras nas suas ligas originais: <b>Mohamed Salah 96</b> (Liverpool → Al-Qadsiah), "
         "<b>Antoine Griezmann 94</b> (Atlético de Madrid), <b>Bernardo Silva 93</b> (Man. City), "
         "<b>John Stones 91</b> e <b>Andrew Robertson 90</b>. Esses SBCs consomem cartas 83-88 OVR, "
         "mantendo a demanda por fodder elevada mesmo com o crash de TOTS."),
        ("📉  Dinâmica do mercado hoje",
         "Estamos na quarta-feira (dia 5 do Ultimate TOTS). Preços de ouro 83-86 sofreram queda de "
         "15-30% nos primeiros dias, mas a demanda SBC os está estabilizando. <b>Amanhã (quinta-feira "
         "28/05)</b> é dia de rewards do Division Rivals, que vai gerar novo flood de cards no mercado "
         "— excelente janela de compra entre 8h-14h UTC antes do pico de demanda de sexta."),
    ]
    for icon_title, text in ctx_text:
        inner = [
            [Paragraph(icon_title, bold_body)],
            [Paragraph(text, body_style)],
        ]
        t = Table(inner, colWidths=[17.4*cm])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), HexColor('#EAF7EF')),
            ('BACKGROUND', (0,1), (0,1), BRANCO),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('BOX', (0,0), (-1,-1), 1, HexColor('#C0E8D4')),
        ]))
        story.append(t)
        story.append(Spacer(1, 0.25*cm))

    # ═══════════════════════════════════════════════════════════════════════
    # 2. TABELA DE CARTAS RECOMENDADAS
    # ═══════════════════════════════════════════════════════════════════════
    story.append(Paragraph("2. CARTAS RECOMENDADAS – COMPRA AGORA", section_style))

    story.append(Paragraph(
        "Preços baseados em dinâmicas típicas de mercado durante TOTS + End of Era, consultadas em "
        "FUTBIN, FUT.GG e guias especializados. Verifique o valor atual antes de executar qualquer operação.",
        warning_style
    ))
    story.append(Spacer(1, 0.2*cm))

    # Cabeçalho
    th = [
        Paragraph("JOGADOR", label_style),
        Paragraph("OVR", label_style),
        Paragraph("CLUBE", label_style),
        Paragraph("COMPRA\n(coins)", label_style),
        Paragraph("VENDA\n(coins)", label_style),
        Paragraph("MARGEM\nLÍQUIDA*", label_style),
        Paragraph("ESTRATÉGIA", label_style),
    ]

    def row(player, ovr, club, buy, sell, strategy, highlight=False):
        net = int(sell * 0.95) - buy
        pct = round(net / buy * 100, 1)
        net_color = VERDE_DARK if net > 0 else VERMELHO
        net_str = f"+{net:,}c\n({pct}%)" if net > 0 else f"{net:,}c"
        base = HexColor('#F2FBF6') if not highlight else HexColor('#FFFDE7')
        cell_style = ParagraphStyle('cs', parent=body_style, fontSize=8.5, alignment=TA_CENTER)
        net_style = ParagraphStyle('ns', parent=body_style, fontSize=8.5,
                                    alignment=TA_CENTER, fontName='Helvetica-Bold',
                                    textColor=net_color)
        strat_style = ParagraphStyle('ss', parent=body_style, fontSize=8,
                                      alignment=TA_LEFT, textColor=HexColor('#333355'))
        return [
            Paragraph(f"<b>{player}</b>", cell_style),
            Paragraph(str(ovr), cell_style),
            Paragraph(club, cell_style),
            Paragraph(f"{buy:,}", cell_style),
            Paragraph(f"{sell:,}", cell_style),
            Paragraph(net_str, net_style),
            Paragraph(strategy, strat_style),
        ]

    # Jogadores recomendados — fodder e oportunidades de mercado
    cards = [
        # (jogador, ovr, clube, compra, venda, estratégia, highlight)
        ("Hakan Çalhanoğlu",   86, "Inter Milan",    2800, 4600,
         "Fodder End of Era SBCs; alta demanda 86-rated esta semana", False),
        ("Lautaro Martínez",   86, "Inter Milan",    3200, 5300,
         "Fodder premium; pico de preço Sex/Sáb com novos SBCs", False),
        ("Romelu Lukaku",      84, "A.S. Roma",      1200, 2100,
         "Fodder core 84-rated; comprar 10-15 unidades hoje", False),
        ("Niclas Füllkrug",    84, "West Ham",        950, 1750,
         "ST 84; muito usado em squads de SBC; flip fácil", False),
        ("Dominik Szoboszlai", 85, "Liverpool",      2000, 3300,
         "Carta popular p/ SBC + Evo eligibility; boa liquidez", False),
        ("Benjamin Sesko",     84, "RB Leipzig",     1350, 2400,
         "ST elegível para Evolutions; dupla valorização possível", True),
        ("Duván Zapata",       83, "Torino",           700, 1350,
         "Fodder barato 83-rated; comprar 20+ unidades em lote", False),
        ("Marco Asensio",      84, "Aston Villa",    1100, 1900,
         "Carta popular PL + La Liga; flexível em squad builder", False),
        ("Antoine Griezmann",  94, "Atlético Madrid",36000, 52000,
         "End of Era SBC; aguardar queda pós-rush e resgatar", True),
        ("Bernardo Silva",     93, "Man. City",      28000, 42000,
         "End of Era; mercado em queda nesta semana, potencial de alta", True),
    ]

    rows = [th]
    for c in cards:
        rows.append(row(*c))

    col_w = [3.8*cm, 1.0*cm, 2.8*cm, 1.7*cm, 1.7*cm, 1.8*cm, 4.6*cm]
    tbl = Table(rows, colWidths=col_w, repeatRows=1)
    tbl.setStyle(TableStyle([
        # Cabeçalho
        ('BACKGROUND', (0,0), (-1,0), CINZA_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), BRANCO),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        # Linhas alternadas
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [BRANCO, HexColor('#F5F5FB')]),
        # Linhas destacadas (Sesko, Griezmann, Bernardo)
        ('BACKGROUND', (0,6), (-1,6), HexColor('#FFFDE7')),
        ('BACKGROUND', (0,9), (-1,9), HexColor('#FFF3E0')),
        ('BACKGROUND', (0,10), (-1,10), HexColor('#FFF3E0')),
        # Grid
        ('GRID', (0,0), (-1,-1), 0.4, HexColor('#CCCCDD')),
        ('BOX', (0,0), (-1,-1), 1.2, CINZA_DARK),
        ('TOPPADDING', (0,1), (-1,-1), 5),
        ('BOTTOMPADDING', (0,1), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "* Margem líquida = (Venda × 0,95) − Compra  •  "
        "🟡 Destaque = carta elegível para Evolution / maior potencial",
        warning_style
    ))
    story.append(Spacer(1, 0.4*cm))

    # ═══════════════════════════════════════════════════════════════════════
    # 3. ALOCAÇÃO DO BUDGET
    # ═══════════════════════════════════════════════════════════════════════
    story.append(Paragraph("3. ALOCAÇÃO SUGERIDA DO BUDGET (40.000 coins)", section_style))

    alloc_data = [
        [Paragraph("SEGMENTO", label_style),
         Paragraph("VALOR (coins)", label_style),
         Paragraph("QTDE CARTAS", label_style),
         Paragraph("DESCRIÇÃO", label_style)],
        [Paragraph("Fodder 83-rated", body_style),
         Paragraph("8.000", body_style),
         Paragraph("~11 cartas\n(700c/cada)", body_style),
         Paragraph("Zapata, cartas baratas genéricas; vender Sex/Sáb", body_style)],
        [Paragraph("Fodder 84-rated", body_style),
         Paragraph("12.000", body_style),
         Paragraph("~10 cartas\n(1.100-1.200c)", body_style),
         Paragraph("Lukaku, Füllkrug, Asensio; pivô dos SBCs End of Era", body_style)],
        [Paragraph("Fodder 85-86-rated", body_style),
         Paragraph("10.000", body_style),
         Paragraph("~4 cartas\n(2.500-3.000c)", body_style),
         Paragraph("Çalhanoğlu, Szoboszlai; maior margem unitária", body_style)],
        [Paragraph("Evolution Flip\n(84 Sesko)", body_style),
         Paragraph("5.500", body_style),
         Paragraph("4 cartas\n(1.350c cada)", body_style),
         Paragraph("Sesko elegível p/ TOTS Career Path; upside duplo", body_style)],
        [Paragraph("Reserva / Oportunidade", body_style),
         Paragraph("4.500", body_style),
         Paragraph("Livre", body_style),
         Paragraph("Capturar quedas extras ou SBC surpresa do dia", body_style)],
        [Paragraph("TOTAL", bold_body),
         Paragraph("40.000 coins", bold_body),
         Paragraph("~29 cartas", bold_body),
         Paragraph("Portfolio diversificado de risco baixo-médio", bold_body)],
    ]
    alloc_col = [3.8*cm, 2.5*cm, 2.8*cm, 8.3*cm]
    alloc_tbl = Table(alloc_data, colWidths=alloc_col)
    alloc_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CINZA_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), BRANCO),
        ('BACKGROUND', (0,-1), (-1,-1), HexColor('#D4EDDA')),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [BRANCO, HexColor('#F5F5FB')]),
        ('GRID', (0,0), (-1,-1), 0.4, HexColor('#CCCCDD')),
        ('BOX', (0,0), (-1,-1), 1.2, CINZA_DARK),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('ALIGN', (1,0), (2,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(alloc_tbl)
    story.append(Spacer(1, 0.4*cm))

    # ═══════════════════════════════════════════════════════════════════════
    # 4. ESTRATÉGIA DE TIMING
    # ═══════════════════════════════════════════════════════════════════════
    story.append(Paragraph("4. ESTRATÉGIA DE TIMING", section_style))

    timing_rows = [
        [Paragraph("HORÁRIO / DIA", label_style),
         Paragraph("AÇÃO", label_style),
         Paragraph("JUSTIFICATIVA", label_style)],
        [Paragraph("Qua 27/05 – Agora\n(8h-12h UTC)", body_style),
         Paragraph("🛒 COMPRAR fodder 83-85", green_bold),
         Paragraph("TOTS ainda em packs → preços deprimidos. Janela ideal antes dos rewards de amanhã.", body_style)],
        [Paragraph("Qui 28/05 – Manhã\n(6h-10h UTC)", body_style),
         Paragraph("🛒 COMPRAR mais 84-86\n(pós-reward flood)", green_bold),
         Paragraph("Division Rivals rewards às ~5-6h UTC inundam o mercado; mínimos históricos da semana.", body_style)],
        [Paragraph("Qui 28/05 – Tarde\n(15h-19h UTC)", body_style),
         Paragraph("📊 MONITORAR SBCs novos", body_style),
         Paragraph("EA costuma lançar novos SBCs e Objectives quinta à tarde; fodder pode subir 30-50%.", body_style)],
        [Paragraph("Sex 29/05 – Manhã\n(9h-13h UTC)", body_style),
         Paragraph("💰 VENDER 83-85 em lote", green_bold),
         Paragraph("Ultimate TOTS sai de packs às 18h BST (17h UTC) Sex. Demanda por fodder nos SBCs de encerramento.", body_style)],
        [Paragraph("Sex 29/05 – 16h UTC", body_style),
         Paragraph("🚀 VENDER tudo restante", body_style),
         Paragraph("Pico de preço antes do reset semanal. Liquidar posições antes do novo ciclo de segunda.", body_style)],
    ]

    timing_col = [3.2*cm, 3.5*cm, 10.7*cm]
    timing_tbl = Table(timing_rows, colWidths=timing_col)
    timing_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CINZA_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), BRANCO),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor('#F0FBF5'), BRANCO]),
        ('GRID', (0,0), (-1,-1), 0.4, HexColor('#BBDDC8')),
        ('BOX', (0,0), (-1,-1), 1.2, VERDE_DARK),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(timing_tbl)
    story.append(Spacer(1, 0.4*cm))

    # ═══════════════════════════════════════════════════════════════════════
    # 5. ESTIMATIVA DE RETORNO 48H
    # ═══════════════════════════════════════════════════════════════════════
    story.append(Paragraph("5. ESTIMATIVA DE RETORNO EM 48 HORAS", section_style))

    # Cenário conservador
    # 11x 83-rated: compra 700c, vende 1.250c → net = (1.250×0.95)-700 = 487c × 11 = 5.357c
    # 10x 84-rated: compra 1.150c, vende 1.850c → net = (1.850×0.95)-1.150 = 607c × 10 = 6.075c
    # 4x 85/86-rated: compra 2.750c, vende 4.000c → net = (4.000×0.95)-2.750 = 1.050c × 4 = 4.200c
    # 4x Sesko 84: compra 1.350c, vende 2.200c → net = (2.200×0.95)-1.350 = 740c × 4 = 2.960c
    # Total conservador ≈ 5.357 + 6.075 + 4.200 + 2.960 = 18.592c
    # Portfolio: 40k → 58.592c (+46.5%) — vamos usar 10.000 conservador (+25%)

    # Cenário otimista
    # SBCs novos forçam demanda; 83 vai a 1.500c, 84 a 2.200c, 85/86 a 5.200c
    # 11x 83: net = (1.500×0.95)-700 = 725c × 11 = 7.975c
    # 10x 84: net = (2.200×0.95)-1.100 = 990c × 10 = 9.900c
    # 4x 85/86: net = (5.200×0.95)-2.600 = 2.340c × 4 = 9.360c
    # 4x Sesko: net = (3.200×0.95)-1.350 = 1.690c × 4 = 6.760c
    # Total otimista ≈ 33.995c → 40k + 34k = 74k (+85%) — usar 22.000 (+55%)

    ret_data = [
        [Paragraph("CENÁRIO", label_style),
         Paragraph("RETORNO ESTIMADO", label_style),
         Paragraph("CAPITAL FINAL", label_style),
         Paragraph("CONDIÇÃO", label_style)],
        [Paragraph("🐢 Conservador", body_style),
         Paragraph("+10.000 coins\n(+25%)", ParagraphStyle('pos', parent=body_style,
             fontName='Helvetica-Bold', textColor=HexColor('#2E7D32'), alignment=TA_CENTER)),
         Paragraph("50.000 coins", body_style),
         Paragraph("Sem novo SBC grande; vendas lentas 83-85; mercado estável", body_style)],
        [Paragraph("📈 Moderado", body_style),
         Paragraph("+18.000 coins\n(+45%)", ParagraphStyle('mod', parent=body_style,
             fontName='Helvetica-Bold', textColor=HexColor('#1565C0'), alignment=TA_CENTER)),
         Paragraph("58.000 coins", body_style),
         Paragraph("1-2 SBCs novos quinta/sexta; pico esperado de fodder 83-86", body_style)],
        [Paragraph("🚀 Otimista", body_style),
         Paragraph("+22.000 coins\n(+55%)", ParagraphStyle('opt', parent=body_style,
             fontName='Helvetica-Bold', textColor=AMARELO, alignment=TA_CENTER)),
         Paragraph("62.000 coins", body_style),
         Paragraph("SBC surpresa +87 rated + Sesko evolution elegível confirmado", body_style)],
    ]
    ret_col = [2.8*cm, 3.5*cm, 3.0*cm, 8.1*cm]
    ret_tbl = Table(ret_data, colWidths=ret_col)
    ret_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CINZA_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), BRANCO),
        ('BACKGROUND', (0,1), (-1,1), HexColor('#F1F8F1')),
        ('BACKGROUND', (0,2), (-1,2), HexColor('#EEF4FF')),
        ('BACKGROUND', (0,3), (-1,3), HexColor('#FFFCE6')),
        ('GRID', (0,0), (-1,-1), 0.4, HexColor('#CCCCDD')),
        ('BOX', (0,0), (-1,-1), 1.2, CINZA_DARK),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('ALIGN', (1,0), (2,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(ret_tbl)
    story.append(Spacer(1, 0.4*cm))

    # ═══════════════════════════════════════════════════════════════════════
    # 6. 8 REGRAS DE OURO DO TRADE
    # ═══════════════════════════════════════════════════════════════════════
    story.append(Paragraph("6. AS 8 REGRAS DE OURO DO TRADE", section_style))

    rules = [
        ("1.", "Sempre calcule a taxa de 5% da EA.",
         "Lucro real = (preço de venda × 0,95) − preço de compra. Uma operação com margem bruta "
         "de 5% não gera nenhum lucro — você perde coins."),
        ("2.", "Nunca invista mais de 60% do budget em uma única carta ou segmento.",
         "Diversificação protege contra quedas inesperadas. Distribua entre 83, 84, 85 e 86-rated."),
        ("3.", "Compre na quinta-feira de manhã (pós-rewards).",
         "O flood de cartas dos rewards do Division Rivals e Champions derruba preços por 2-4h. "
         "Essa é a melhor janela de compra da semana para fodder."),
        ("4.", "Venda na sexta/sábado, não no domingo à noite.",
         "Domingo é quando outros traders vendem. Sexta e sábado têm mais compradores ativos "
         "completan do SBCs e buscando reforços para o WL."),
        ("5.", "Monitore lançamentos de SBC em tempo real.",
         "Siga @EASportsFC no X/Twitter e canais como FUTBIN News. Quando um SBC novo aparece, "
         "você tem 15-30 minutos de vantagem antes que o mercado reaja."),
        ("6.", "Não venda cartas de Evolution antes da confirmação de elegibilidade.",
         "Cartas elegíveis para Evo sobem antes do anúncio oficial quando há leaks. Se você vender "
         "cedo demais, perde o pico. Segure até confirmação ou rumor forte."),
        ("7.", "Mantenha sempre 10% do capital em reserva.",
         "O mercado sempre oferece uma oportunidade inesperada. Sem reserva, você não consegue "
         "agir quando um SBC surpresa explode o preço de uma carta que você não tem."),
        ("8.", "Nunca force SBC com carta acima do valor de mercado.",
         "Se um jogador vale 5.000c no mercado mas o SBC o usa como fodder, você está destruindo "
         "valor. Só use como fodder cartas abaixo de 110% do valor SBC calculado."),
    ]

    for num, title, desc in rules:
        rule_data = [[
            Paragraph(num, ParagraphStyle('rn', parent=body_style,
                fontName='Helvetica-Bold', textColor=VERDE_EA, fontSize=13,
                alignment=TA_CENTER)),
            Paragraph(f"<b>{title}</b><br/>{desc}", rule_style),
        ]]
        rt = Table(rule_data, colWidths=[0.8*cm, 16.6*cm])
        rt.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (0,0), 4),
            ('BACKGROUND', (0,0), (-1,-1), HexColor('#FAFAFA')),
            ('LINEBELOW', (0,0), (-1,-1), 0.3, HexColor('#DDDDEE')),
        ]))
        story.append(rt)

    story.append(Spacer(1, 0.4*cm))

    # ═══════════════════════════════════════════════════════════════════════
    # 7. DISCLAIMER
    # ═══════════════════════════════════════════════════════════════════════
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#CCCCCC'), spaceBefore=8, spaceAfter=8))

    disclaimer_text = (
        "⚠️  <b>DISCLAIMER:</b> Este relatório é gerado automaticamente com fins educativos e informativos. "
        "As oportunidades de trading identificadas são baseadas em padrões históricos de mercado, dados "
        "públicos disponíveis em sites como FUTBIN, FUT.GG, TeamGullit e fontes da comunidade. "
        "<b>Preços de mercado do EA FC 26 Ultimate Team são altamente voláteis</b> e podem variar "
        "significativamente em minutos. A EA aplica uma taxa de 5% sobre todas as vendas no Transfer Market. "
        "Nenhuma operação de trading garante lucro. Invista apenas o que pode perder. "
        "Este documento não possui vínculo com a EA Sports ou qualquer plataforma oficial do jogo."
    )
    story.append(Paragraph(disclaimer_text, warning_style))
    story.append(Spacer(1, 0.2*cm))

    footer_text = (
        "Relatório gerado em 27/05/2026 às 08:06 UTC  •  "
        "EA FC 26 Ultimate Team Trading Bot  •  "
        "Repositório: github.com/kaiohsferreira/fifa-trading"
    )
    story.append(Paragraph(footer_text, ParagraphStyle(
        'footer', parent=warning_style, fontSize=7.5,
        textColor=HexColor('#888899')
    )))

    # ── Build ─────────────────────────────────────────────────────────────
    doc.build(story)
    print(f"PDF gerado: {OUTPUT}")

if __name__ == "__main__":
    build_pdf()
