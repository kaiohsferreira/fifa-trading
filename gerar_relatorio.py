#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Relatório de Trading EA FC 26 Ultimate Team
Data: 2026-05-26 08:08 UTC
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
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import Flowable
import os

# ─── Configurações ────────────────────────────────────────────────────────────
FILENAME = "relatorio-trading-2026-05-26-08h.pdf"
REPORT_DATE = "26/05/2026 08:08"
REPORT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAME)

# ─── Paleta EA FC ─────────────────────────────────────────────────────────────
C_GREEN_EA   = colors.HexColor("#00D4AA")   # verde EA
C_DARK_BG    = colors.HexColor("#0D1B2A")   # azul escuro fundo
C_NAVY       = colors.HexColor("#1A2F4A")   # azul marinho cards
C_GOLD       = colors.HexColor("#F5A623")   # dourado
C_WHITE      = colors.white
C_LIGHT_GRAY = colors.HexColor("#E8EDF2")
C_MID_GRAY   = colors.HexColor("#8A9BB0")
C_RED        = colors.HexColor("#E74C3C")
C_GREEN_SOFT = colors.HexColor("#27AE60")


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='ReportTitle',
        fontName='Helvetica-Bold',
        fontSize=22,
        textColor=C_WHITE,
        alignment=TA_CENTER,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name='ReportSubtitle',
        fontName='Helvetica',
        fontSize=11,
        textColor=C_GREEN_EA,
        alignment=TA_CENTER,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name='DateLine',
        fontName='Helvetica-Bold',
        fontSize=10,
        textColor=C_GOLD,
        alignment=TA_CENTER,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name='SectionHeader',
        fontName='Helvetica-Bold',
        fontSize=13,
        textColor=C_GREEN_EA,
        spaceBefore=14,
        spaceAfter=6,
        borderPad=4,
    ))
    styles.add(ParagraphStyle(
        name='SubHeader',
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=C_GOLD,
        spaceBefore=8,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name='BodyText2',
        fontName='Helvetica',
        fontSize=9,
        textColor=C_DARK_BG,
        leading=14,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
    ))
    styles.add(ParagraphStyle(
        name='BodyLight',
        fontName='Helvetica',
        fontSize=9,
        textColor=C_MID_GRAY,
        leading=13,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name='BulletItem',
        fontName='Helvetica',
        fontSize=9,
        textColor=C_DARK_BG,
        leading=14,
        leftIndent=14,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name='BulletBold',
        fontName='Helvetica-Bold',
        fontSize=9,
        textColor=C_NAVY,
        leading=14,
        leftIndent=14,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name='RuleText',
        fontName='Helvetica-Bold',
        fontSize=9,
        textColor=C_WHITE,
        leading=13,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name='RuleDesc',
        fontName='Helvetica',
        fontSize=8,
        textColor=C_LIGHT_GRAY,
        leading=12,
        leftIndent=12,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name='Disclaimer',
        fontName='Helvetica-Oblique',
        fontSize=7.5,
        textColor=C_MID_GRAY,
        leading=11,
        alignment=TA_JUSTIFY,
    ))
    styles.add(ParagraphStyle(
        name='TableHeader',
        fontName='Helvetica-Bold',
        fontSize=8,
        textColor=C_WHITE,
        alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        name='TableCell',
        fontName='Helvetica',
        fontSize=8,
        textColor=C_DARK_BG,
        alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        name='ReturnBox',
        fontName='Helvetica-Bold',
        fontSize=10,
        textColor=C_WHITE,
        alignment=TA_CENTER,
        spaceAfter=3,
    ))
    return styles


# ─── Canvas com fundo e rodapé ────────────────────────────────────────────────
class FooterCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_elements(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_elements(self, page_count):
        width, height = A4
        # Fundo escuro no header
        self.setFillColor(C_DARK_BG)
        self.rect(0, height - 3.8*cm, width, 3.8*cm, fill=1, stroke=0)

        # Linha decorativa verde EA
        self.setStrokeColor(C_GREEN_EA)
        self.setLineWidth(2.5)
        self.line(1*cm, height - 3.8*cm, width - 1*cm, height - 3.8*cm)

        # Rodapé
        self.setFillColor(C_NAVY)
        self.rect(0, 0, width, 1.2*cm, fill=1, stroke=0)
        self.setStrokeColor(C_GREEN_EA)
        self.setLineWidth(1)
        self.line(1*cm, 1.2*cm, width - 1*cm, 1.2*cm)

        self.setFillColor(C_MID_GRAY)
        self.setFont("Helvetica", 7)
        page_num = self._pageNumber
        self.drawCentredString(width/2, 0.45*cm,
            f"EA FC 26 Ultimate Team Trading Report  •  {REPORT_DATE} UTC  •  Página {page_num}/{page_count}")
        self.drawString(1*cm, 0.45*cm, "© 2026 FIFA Trading Analytics")
        self.drawRightString(width - 1*cm, 0.45*cm, "Uso interno — confidencial")


def build_pdf():
    styles = build_styles()

    doc = SimpleDocTemplate(
        REPORT_PATH,
        pagesize=A4,
        rightMargin=1.8*cm,
        leftMargin=1.8*cm,
        topMargin=4.5*cm,
        bottomMargin=2*cm,
        title="Relatório Trading EA FC 26",
        author="FIFA Trading Analytics",
    )

    story = []
    W = A4[0] - 3.6*cm  # largura útil

    # ── CABEÇALHO ─────────────────────────────────────────────────────────────
    story.append(Paragraph("⚽  EA FC 26 ULTIMATE TEAM", styles['ReportTitle']))
    story.append(Paragraph("RELATÓRIO DIÁRIO DE TRADING", styles['ReportSubtitle']))
    story.append(Paragraph(f"📅  {REPORT_DATE} UTC", styles['DateLine']))
    story.append(HRFlowable(width="100%", thickness=1, color=C_GREEN_EA, spaceAfter=10))

    # ── RESUMO EXECUTIVO ───────────────────────────────────────────────────────
    story.append(Paragraph("🎯 RESUMO EXECUTIVO", styles['SectionHeader']))
    story.append(Paragraph(
        "Budget disponível: <b>40.000 coins</b>. Período de análise: 26/05/2026 — 28/05/2026. "
        "Evento ativo: <b>Ultimate TOTS + End of Era SBCs</b>. "
        "A janela atual combina demanda alta por fodder (84–88 rated) impulsionada pelos SBCs "
        "End of Era com oportunidade de compra em cards de ligas anteriores do TOTS que sofreram "
        "crash de preço. Estratégias: <b>SBC Fodder Flipping</b>, "
        "<b>Evolution Investing</b> e <b>Thursday Flip</b>.",
        styles['BodyText2']
    ))

    # ── CONTEXTO DE MERCADO ────────────────────────────────────────────────────
    story.append(Paragraph("📊 CONTEXTO DO MERCADO", styles['SectionHeader']))

    ctx_data = [
        ["PARÂMETRO", "DETALHE"],
        ["Evento Principal", "Ultimate TOTS (22/05 → 29/05/2026)"],
        ["End of Era SBCs Ativos", "Salah 96 OVR, Griezmann 94 OVR, Robertson 93 OVR"],
        ["TOTS Career Path Evo", "Gratuita — ativa desde 15/05/2026"],
        ["Week 5 TOTS Upgrade SBC", "Repeatable 3x/dia — requer 86 rated squad"],
        ["Tendência dos Fodder 83–85", "Alta demanda → preços elevados vs discard price"],
        ["Tendência dos Fodder 86–88", "Demanda moderada → janela de compra a ~1.3–9K"],
        ["Dia do Relatório", "Segunda-feira (pré-Thursday flip window)"],
        ["Próximo Champs Weekend", "Sexta-feira 29/05 — pico de venda"],
    ]

    ctx_table = Table(ctx_data, colWidths=[5.5*cm, W - 5.5*cm])
    ctx_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), C_GREEN_EA),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_LIGHT_GRAY, C_WHITE]),
        ('TEXTCOLOR', (0,1), (0,-1), C_NAVY),
        ('TEXTCOLOR', (1,1), (1,-1), C_DARK_BG),
        ('GRID', (0,0), (-1,-1), 0.4, C_MID_GRAY),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('ROUNDEDCORNERS', [4]),
    ]))
    story.append(ctx_table)
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph(
        "<b>Por que agora?</b> Com o Ultimate TOTS em packs, há grande influxo de cards 92–96 OVR, "
        "forçando crash dos TOTS de ligas anteriores (EPL, La Liga, Bundesliga). Ao mesmo tempo, "
        "os SBCs End of Era exigem squads de alta qualidade, aumentando demanda por fodder 84–88. "
        "Comprar fodder barato hoje (Seg/Ter) e vender quando novos SBCs saírem (Qua/Qui) é a estratégia "
        "de menor risco com budget de 40K.",
        styles['BodyText2']
    ))

    # ── TABELA DE OPORTUNIDADES ────────────────────────────────────────────────
    story.append(Paragraph("💼 CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA", styles['SectionHeader']))
    story.append(Paragraph(
        "Preços em coins (console PS/Xbox). Taxa EA = 5%. Margem líquida já descontada. "
        "Fontes: FUTBIN, FUT.GG, operationsports.com (mai/2026).",
        styles['BodyLight']
    ))

    hdr = ['Jogador', 'Rat.', 'Clube / Liga', 'Compra\n(max)', 'Venda\nAlvo', 'Margem\nLíquida', 'Estratégia']
    rows = [
        # Estratégia 1 – SBC Fodder Flipping 86-rated
        ['Hakan Çalhanoğlu', '86', 'Inter / Serie A', '1.400', '2.200', '+690', 'Fodder SBC'],
        ['Rúben Dias',       '86', 'Man City / EPL', '1.400', '2.100', '+595', 'Fodder SBC'],
        ['Bruno Guimarães',  '86', 'Newcastle / EPL','1.500', '2.300', '+685', 'Fodder SBC'],
        ['Paulo Dybala',     '86', 'Roma / Serie A', '1.500', '2.300', '+685', 'Fodder SBC'],
        ['Marc ter Stegen',  '86', 'Barcelona / LaLiga','1.600','2.500', '+775', 'Fodder SBC'],
        # Estratégia 2 – 87-rated fodder
        ['Martin Ødegaard',  '87', 'Arsenal / EPL',  '2.000', '3.500', '+1.325','Fodder SBC'],
        ['Alessandro Bastoni','87','Inter / Serie A', '2.100', '3.600', '+1.320','Fodder SBC'],
        ['Kevin De Bruyne',  '87', 'Man City / EPL', '2.200', '3.800', '+1.410','Fodder SBC'],
        # Estratégia 3 – Thursday Flip (crash pós-rewards)
        ['Lauren Hemp',      '87', 'Man City / FAWSL','1.900','3.400', '+1.330','Thu Flip'],
        ['Rose Lavelle',     '87', 'Portland / NWSL', '2.000','3.500', '+1.325','Thu Flip'],
        # Estratégia 4 – 88-rated (maior investimento)
        ['Christiane Endler','88', 'Lyon / D1 Arkema','6.500','9.000', '+2.050','Fodder SBC'],
        ['Irene Paredes',    '88', 'Barcelona / Liga F','6.500','9.200', '+2.240','Fodder SBC'],
        # Estratégia 5 – Evolution Investing
        ['Ferland Mendy',    '84', 'Real Madrid / LaLiga','3.200','6.500','+2.975','Evo Trade'],
        ['Theo Hernández',   '85', 'AC Milan / Serie A','5.500','9.000', '+3.050','Evo Trade'],
    ]

    table_data = [hdr] + rows
    col_widths = [3.8*cm, 1.0*cm, 3.5*cm, 1.6*cm, 1.6*cm, 1.8*cm, 2.3*cm]

    opp_table = Table(table_data, colWidths=col_widths, repeatRows=1)
    opp_table.setStyle(TableStyle([
        # Header
        ('BACKGROUND',   (0,0), (-1,0),   C_DARK_BG),
        ('TEXTCOLOR',    (0,0), (-1,0),   C_GREEN_EA),
        ('FONTNAME',     (0,0), (-1,0),   'Helvetica-Bold'),
        ('FONTSIZE',     (0,0), (-1,0),   7.5),
        ('ALIGN',        (0,0), (-1,0),   'CENTER'),
        ('VALIGN',       (0,0), (-1,0),   'MIDDLE'),
        # Body
        ('FONTNAME',     (0,1), (-1,-1),  'Helvetica'),
        ('FONTSIZE',     (0,1), (-1,-1),  7.5),
        ('ALIGN',        (1,1), (-1,-1),  'CENTER'),
        ('ALIGN',        (0,1), (0,-1),   'LEFT'),
        ('ALIGN',        (2,1), (2,-1),   'LEFT'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),  [C_WHITE, C_LIGHT_GRAY]),
        ('TEXTCOLOR',    (0,1), (-1,-1),  C_DARK_BG),
        # Rating badge
        ('BACKGROUND',   (1,1), (1,-1),   C_NAVY),
        ('TEXTCOLOR',    (1,1), (1,-1),   C_GOLD),
        ('FONTNAME',     (1,1), (1,-1),   'Helvetica-Bold'),
        # Margem líquida verde
        ('TEXTCOLOR',    (5,1), (5,-1),   C_GREEN_SOFT),
        ('FONTNAME',     (5,1), (5,-1),   'Helvetica-Bold'),
        # Estratégia
        ('TEXTCOLOR',    (6,1), (6,-1),   C_NAVY),
        ('FONTNAME',     (6,1), (6,-1),   'Helvetica-Bold'),
        # Grade
        ('GRID',         (0,0), (-1,-1),  0.4, C_MID_GRAY),
        ('TOPPADDING',   (0,0), (-1,-1),  4),
        ('BOTTOMPADDING',(0,0), (-1,-1),  4),
        ('LEFTPADDING',  (0,0), (-1,-1),  5),
        ('RIGHTPADDING', (0,0), (-1,-1),  4),
    ]))
    story.append(opp_table)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "* Margem líquida = (Preço Venda × 0,95) − Preço Compra. "
        "Preços de compra baseados em médias de horário não-peak (off-peak). "
        "Verificar sempre no FUTBIN/FUT.GG antes de executar.",
        styles['BodyLight']
    ))

    # ── ALOCAÇÃO DO BUDGET ─────────────────────────────────────────────────────
    story.append(Paragraph("💰 ALOCAÇÃO SUGERIDA DO BUDGET (40.000 coins)", styles['SectionHeader']))

    alloc_data = [
        ['Estratégia', 'Coins Investidos', 'Qtd. Cards', 'Retorno Estimado'],
        ['SBC Fodder 86-rated\n(Çalhanoğlu, Dias, Guimarães…)', '12.000', '~8 cards', '+5.520 a +6.200'],
        ['SBC Fodder 87-rated\n(Ødegaard, De Bruyne, Bastoni…)', '12.000', '~5 cards', '+6.625 a +7.050'],
        ['SBC Fodder 88-rated\n(Endler, Paredes)', '13.000', '2 cards', '+4.100 a +4.480'],
        ['Evolution Trade\n(Mendy, T. Hernández)', '3.000', '1 card', '+2.975 a +3.050'],
        ['Reserva de emergência', '0 (hold)', '—', 'Liquidez'],
    ]

    alloc_table = Table(alloc_data, colWidths=[5.5*cm, 3*cm, 2.2*cm, W-10.7*cm])
    alloc_table.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  C_NAVY),
        ('TEXTCOLOR',     (0,0), (-1,0),  C_GOLD),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 8),
        ('ALIGN',         (1,0), (-1,-1), 'CENTER'),
        ('ALIGN',         (0,0), (0,-1),  'LEFT'),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [C_LIGHT_GRAY, C_WHITE]),
        ('TEXTCOLOR',     (3,1), (3,-1),  C_GREEN_SOFT),
        ('FONTNAME',      (3,1), (3,-1),  'Helvetica-Bold'),
        ('GRID',          (0,0), (-1,-1), 0.4, C_MID_GRAY),
        ('TOPPADDING',    (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING',   (0,0), (-1,-1), 7),
    ]))
    story.append(alloc_table)

    # ── TIMING ────────────────────────────────────────────────────────────────
    story.append(Paragraph("⏱️ ESTRATÉGIA DE TIMING", styles['SectionHeader']))

    timing_data = [
        ['DIA / HORA (UTC)', 'AÇÃO', 'MOTIVO'],
        ['Seg 26/05 — Agora\n06h–10h',
         'COMPRAR fodder 86–87 rated\n(off-peak, menor volume)',
         'Preços no piso semanal;\nSBCs ativos criam demanda'],
        ['Seg/Ter 26–27/05\n18h–22h',
         'MONITORAR novos SBCs\nEnd of Era (Bernardo Silva, Goretzka)',
         'Cada SBC novo = spike fodder\n→ vender em 30–60 min pós-release'],
        ['Qua 27/05\n14h–18h',
         'VERIFICAR preços fodder;\nVENDER se +40% vs compra',
         'Midweek prep FUT Champs;\ndemanda por squads sobe'],
        ['Qui 28/05\n13h–15h',
         'Thursday Flip:\nCOMPRAR após Rivals rewards',
         'Influxo de cards pós-rewards\npressiona preços para baixo'],
        ['Sex 29/05\n06h–10h',
         'VENDER tudo antes de\nUltimate TOTS sair de packs',
         'Champs prep = pico de demanda;\nUTOTS expira Sexta 29/05'],
    ]

    timing_table = Table(timing_data, colWidths=[3.5*cm, 5.5*cm, W-9*cm])
    timing_table.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  C_DARK_BG),
        ('TEXTCOLOR',     (0,0), (-1,0),  C_GREEN_EA),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 8),
        ('ALIGN',         (0,0), (-1,-1), 'LEFT'),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [C_WHITE, C_LIGHT_GRAY]),
        ('TEXTCOLOR',     (0,1), (0,-1),  C_NAVY),
        ('FONTNAME',      (0,1), (0,-1),  'Helvetica-Bold'),
        ('TEXTCOLOR',     (1,1), (1,-1),  C_DARK_BG),
        ('TEXTCOLOR',     (2,1), (2,-1),  colors.HexColor("#555555")),
        ('GRID',          (0,0), (-1,-1), 0.4, C_MID_GRAY),
        ('TOPPADDING',    (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING',   (0,0), (-1,-1), 7),
    ]))
    story.append(timing_table)

    # ── ESTIMATIVA DE RETORNO 48H ──────────────────────────────────────────────
    story.append(Paragraph("📈 ESTIMATIVA DE RETORNO EM 48H", styles['SectionHeader']))

    ret_data = [
        ['', 'CENÁRIO CONSERVADOR', 'CENÁRIO OTIMISTA'],
        ['Capital Inicial', '40.000 coins', '40.000 coins'],
        ['Retorno Bruto', '+18.000 coins', '+27.200 coins'],
        ['Taxa EA (5%)', '−1.900 coins', '−2.860 coins'],
        ['Capital Final', '56.100 coins', '64.340 coins'],
        ['Lucro Líquido', '+16.100 coins (+40%)', '+24.340 coins (+61%)'],
        ['Premissa', 'Fodder +40% em 48h;\n3–4 SBCs novos', 'Fodder +60% em 48h;\n5+ SBCs End of Era'],
    ]

    ret_table = Table(ret_data, colWidths=[3.8*cm, (W-3.8*cm)/2, (W-3.8*cm)/2])
    ret_table.setStyle(TableStyle([
        ('BACKGROUND',    (1,0), (1,0),  colors.HexColor("#2471A3")),
        ('BACKGROUND',    (2,0), (2,0),  C_GREEN_SOFT),
        ('TEXTCOLOR',     (0,0), (-1,0), C_WHITE),
        ('FONTNAME',      (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1),8.5),
        ('ALIGN',         (0,0), (-1,-1),'CENTER'),
        ('VALIGN',        (0,0), (-1,-1),'MIDDLE'),
        ('BACKGROUND',    (0,1), (0,-1), C_NAVY),
        ('TEXTCOLOR',     (0,1), (0,-1), C_GOLD),
        ('FONTNAME',      (0,1), (0,-1), 'Helvetica-Bold'),
        ('ROWBACKGROUNDS',(1,1), (-1,-1),[C_LIGHT_GRAY, C_WHITE]),
        ('TEXTCOLOR',     (1,1), (-1,-1),C_DARK_BG),
        # Lucro líquido destaque
        ('BACKGROUND',    (1,5), (1,5),  colors.HexColor("#D6EAF8")),
        ('BACKGROUND',    (2,5), (2,5),  colors.HexColor("#D5F5E3")),
        ('TEXTCOLOR',     (1,5), (1,5),  colors.HexColor("#2471A3")),
        ('TEXTCOLOR',     (2,5), (2,5),  C_GREEN_SOFT),
        ('FONTNAME',      (1,5), (2,5),  'Helvetica-Bold'),
        ('GRID',          (0,0), (-1,-1),0.4, C_MID_GRAY),
        ('TOPPADDING',    (0,0), (-1,-1),6),
        ('BOTTOMPADDING', (0,0), (-1,-1),6),
    ]))
    story.append(ret_table)
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "⚠️ Cenário conservador assume execução parcial (70% das ordens preenchidas) e apenas "
        "3–4 SBCs novos no período. Cenário otimista assume alta adesão aos End of Era SBCs "
        "e plena execução com todos os cards vendidos antes da sexta-feira.",
        styles['BodyLight']
    ))

    # ── 8 REGRAS DE OURO ──────────────────────────────────────────────────────
    story.append(Paragraph("🏆 8 REGRAS DE OURO DO TRADE", styles['SectionHeader']))

    rules = [
        ("1. Nunca pague acima do preço de pico",
         "Sempre compre em horários off-peak (madrugada/manhã UTC). Preços sobem 20–40% em peak hours."),
        ("2. Respeite a taxa EA de 5%",
         "Calcule sempre: lucro = (preço de venda × 0,95) − preço de compra. Nunca ignore essa taxa."),
        ("3. Compre na quinta-feira, venda na sexta",
         "Rivals rewards às 13h UTC na quinta derrubam preços. Champs prep na sexta eleva a demanda."),
        ("4. Aguarde 30–60 min após novos SBCs",
         "No lançamento, preços dos cards necessários sobem 50–100%. Espere a histeria passar."),
        ("5. Diversifique por rating",
         "Distribua budget entre 86, 87 e 88 rated. Se um tier travar, outros podem se valorizar."),
        ("6. Nunca invista 100% do budget",
         "Mantenha 10–15% de liquidez para aproveitar oportunidades inesperadas ou stop-loss."),
        ("7. Acompanhe leaks de SBCs",
         "Twitter/X @FUT_Scoreboard e @FutSheriff avisam SBCs antes do lançamento. Posicione-se antes."),
        ("8. Saiba a hora de sair",
         "Se um card não vendeu em 2h, baixe 5–8%. Nunca segure fodder por mais de 72h em período de evento."),
    ]

    rules_data = []
    for title, desc in rules:
        rules_data.append([
            Paragraph(title, styles['RuleText']),
            Paragraph(desc, styles['RuleDesc']),
        ])

    rules_table_data = [[Paragraph(t, styles['RuleText']), Paragraph(d, styles['RuleDesc'])]
                         for t, d in rules]

    # Dividir em 2 colunas de 4 regras
    left_rules  = rules[:4]
    right_rules = rules[4:]

    for (lt, ld), (rt, rd) in zip(left_rules, right_rules):
        row_data = [
            [Paragraph(lt, styles['RuleText']),
             Paragraph(ld, styles['RuleDesc'])],
            [Paragraph(rt, styles['RuleText']),
             Paragraph(rd, styles['RuleDesc'])],
        ]

    # Tabela simples de regras em fundo escuro
    rules_content = []
    for i, (title, desc) in enumerate(rules):
        bg = C_NAVY if i % 2 == 0 else C_DARK_BG
        rules_content.append(
            Table(
                [[Paragraph(title, styles['RuleText'])],
                 [Paragraph(desc, styles['RuleDesc'])]],
                colWidths=[W],
            )
        )

    # Criar tabela de 2 colunas com as regras
    col_w = (W - 0.4*cm) / 2
    rules_pairs = []
    for i in range(0, 8, 2):
        t_title, t_desc = rules[i]
        r_title, r_desc = rules[i+1]
        left_cell = [
            Paragraph(f"<b>{t_title}</b>", ParagraphStyle(
                'rt', fontName='Helvetica-Bold', fontSize=8.5,
                textColor=C_GOLD, leading=12, spaceAfter=2)),
            Paragraph(t_desc, ParagraphStyle(
                'rd', fontName='Helvetica', fontSize=8,
                textColor=C_LIGHT_GRAY, leading=12)),
        ]
        right_cell = [
            Paragraph(f"<b>{r_title}</b>", ParagraphStyle(
                'rt2', fontName='Helvetica-Bold', fontSize=8.5,
                textColor=C_GOLD, leading=12, spaceAfter=2)),
            Paragraph(r_desc, ParagraphStyle(
                'rd2', fontName='Helvetica', fontSize=8,
                textColor=C_LIGHT_GRAY, leading=12)),
        ]
        rules_pairs.append([left_cell, right_cell])

    from reportlab.platypus import ListFlowable, ListItem

    rules_table = Table(
        [[lc, rc] for lc, rc in [(rules_pairs[i][0], rules_pairs[i][1]) for i in range(4)]],
        colWidths=[col_w, col_w],
    )
    rules_table.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), C_DARK_BG),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING',    (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING',   (0,0), (-1,-1), 10),
        ('RIGHTPADDING',  (0,0), (-1,-1), 10),
        ('LINEABOVE',     (0,1), (-1,-1), 0.5, C_NAVY),
        ('LINEABOVE',     (0,0), (-1,0),  0,   C_DARK_BG),
        ('LINEBETWEEN',   (0,0), (0,-1),  0.5, C_NAVY),
        ('ROUNDEDCORNERS',[6]),
    ]))
    story.append(rules_table)

    # ── DISCLAIMER ────────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.5*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_MID_GRAY, spaceAfter=8))
    story.append(Paragraph("⚠️  DISCLAIMER", styles['SubHeader']))
    story.append(Paragraph(
        "Este relatório é gerado automaticamente com base em dados públicos de mercado coletados "
        "de FUTBIN, FUT.GG, TeamGullit, RealSport101 e fontes especializadas em EA FC 26 Ultimate Team. "
        "Os preços apresentados são estimativas baseadas em médias históricas e tendências de mercado; "
        "NÃO constituem garantia de lucro. O mercado de EA FC 26 é altamente volátil e pode sofrer "
        "alterações bruscas por ação da EA Sports (price ranges, pack weights, SBC releases). "
        "O autor não se responsabiliza por perdas decorrentes de decisões de trading baseadas neste "
        "relatório. Sempre valide os preços em tempo real antes de executar qualquer operação. "
        "EA SPORTS FC 26 é marca registrada da Electronic Arts Inc.",
        styles['Disclaimer']
    ))

    # ── BUILD ──────────────────────────────────────────────────────────────────
    doc.build(story, canvasmaker=FooterCanvas)
    print(f"✅ PDF gerado: {REPORT_PATH}")
    return REPORT_PATH


if __name__ == "__main__":
    build_pdf()
