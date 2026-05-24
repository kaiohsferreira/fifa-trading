#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Image
from reportlab.pdfgen import canvas
import datetime

# === PALETA DE CORES ===
VERDE_ESCURO   = colors.HexColor("#0a3d1f")
VERDE_MEDIO    = colors.HexColor("#1a6e36")
VERDE_CLARO    = colors.HexColor("#2ecc71")
DOURADO        = colors.HexColor("#f1c40f")
DOURADO_ESCURO = colors.HexColor("#d4a017")
BRANCO         = colors.white
CINZA_CLARO    = colors.HexColor("#f4f4f4")
CINZA_MEDIO    = colors.HexColor("#cccccc")
PRETO          = colors.black
VERMELHO       = colors.HexColor("#e74c3c")
LARANJA        = colors.HexColor("#e67e22")
AZUL_CLARO     = colors.HexColor("#3498db")

# === DATA E HORA ===
now = datetime.datetime(2026, 5, 24, 14, 9)  # UTC datetime coletado no início
data_fmt   = now.strftime("%d/%m/%Y %H:%M")
nome_pdf   = f"relatorio-trading-{now.strftime('%Y-%m-%d-%Hh')}.pdf"
hora_utc   = now.strftime("%H:%M UTC")


# ============================================================
#  HEADER / FOOTER customizados via canvas
# ============================================================
class FifaCanvas(canvas.Canvas):
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
        self.saveState()
        w, h = A4
        # Faixa superior
        self.setFillColor(VERDE_ESCURO)
        self.rect(0, h - 18*mm, w, 18*mm, fill=1, stroke=0)
        self.setFillColor(DOURADO)
        self.setFont("Helvetica-Bold", 9)
        self.drawCentredString(w / 2, h - 10*mm, "EA FC 26 ULTIMATE TEAM  |  RELATÓRIO DE TRADING DIÁRIO")
        # Faixa inferior
        self.setFillColor(VERDE_ESCURO)
        self.rect(0, 0, w, 12*mm, fill=1, stroke=0)
        self.setFillColor(DOURADO)
        self.setFont("Helvetica", 7.5)
        self.drawString(14*mm, 4*mm,
            "⚠ Disclaimer: Análise de mercado. Não é garantia de lucro. Preços podem variar.")
        page_num = self._pageNumber
        self.setFont("Helvetica-Bold", 8)
        self.drawRightString(w - 14*mm, 4*mm, f"Pág. {page_num} / {page_count}")
        self.restoreState()


# ============================================================
#  DOCUMENTO
# ============================================================
doc = SimpleDocTemplate(
    nome_pdf,
    pagesize=A4,
    rightMargin=15*mm,
    leftMargin=15*mm,
    topMargin=22*mm,
    bottomMargin=17*mm,
)

styles = getSampleStyleSheet()

# Estilos personalizados
titulo_style = ParagraphStyle(
    "titulo", parent=styles["Title"],
    fontSize=26, textColor=VERDE_ESCURO,
    spaceAfter=4, alignment=TA_CENTER,
    fontName="Helvetica-Bold"
)
subtitulo_style = ParagraphStyle(
    "subtitulo", parent=styles["Normal"],
    fontSize=12, textColor=VERDE_MEDIO,
    spaceAfter=2, alignment=TA_CENTER,
    fontName="Helvetica-Bold"
)
data_style = ParagraphStyle(
    "data", parent=styles["Normal"],
    fontSize=10, textColor=DOURADO_ESCURO,
    spaceAfter=6, alignment=TA_CENTER,
    fontName="Helvetica-Bold"
)
secao_style = ParagraphStyle(
    "secao", parent=styles["Heading1"],
    fontSize=13, textColor=BRANCO,
    spaceBefore=8, spaceAfter=4,
    backColor=VERDE_MEDIO,
    leftIndent=-10, rightIndent=-10,
    leading=20,
    fontName="Helvetica-Bold"
)
corpo_style = ParagraphStyle(
    "corpo", parent=styles["Normal"],
    fontSize=9.5, textColor=PRETO,
    spaceAfter=4, leading=14,
    alignment=TA_JUSTIFY,
    fontName="Helvetica"
)
bullet_style = ParagraphStyle(
    "bullet", parent=styles["Normal"],
    fontSize=9.5, textColor=PRETO,
    spaceAfter=3, leading=14,
    leftIndent=14, fontName="Helvetica",
    bulletIndent=4
)
label_style = ParagraphStyle(
    "label", parent=styles["Normal"],
    fontSize=9, textColor=VERDE_ESCURO,
    spaceAfter=2, leading=12,
    fontName="Helvetica-Bold"
)
aviso_style = ParagraphStyle(
    "aviso", parent=styles["Normal"],
    fontSize=8, textColor=colors.HexColor("#555555"),
    spaceAfter=2, leading=11,
    alignment=TA_CENTER, fontName="Helvetica-Oblique"
)


def secao(txt):
    return Paragraph(f"  {txt}", secao_style)

def p(txt, style=corpo_style):
    return Paragraph(txt, style)

def sp(h=4):
    return Spacer(1, h*mm)

def hr():
    return HRFlowable(width="100%", thickness=1, color=VERDE_CLARO, spaceAfter=4)


# ============================================================
#  CONTEÚDO
# ============================================================
story = []

# ------- CAPA -------
story.append(sp(6))
story.append(Paragraph("⚽ EA FC 26", titulo_style))
story.append(Paragraph("RELATÓRIO DE TRADING DIÁRIO", titulo_style))
story.append(sp(2))
story.append(Paragraph("Ultimate Team · Mercado de Jogadores", subtitulo_style))
story.append(sp(3))

# Caixa data destacada
data_table = Table(
    [[f"📅  {data_fmt}  ·  {hora_utc}"]],
    colWidths=[160*mm],
)
data_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), VERDE_ESCURO),
    ("TEXTCOLOR", (0,0), (-1,-1), DOURADO),
    ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 13),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("ROUNDEDCORNERS", [6,6,6,6]),
]))
story.append(data_table)
story.append(sp(4))

# Cards de destaque: budget / meta
destaques = [
    ["💰 Budget", "40.000 coins"],
    ["🎯 Meta", "Crescer capital via SBC Fodder Flip,\nEvo Invest & Thursday Flip"],
    ["📊 Rating Alvo", "83 – 88 rated gold cards"],
    ["⚡ Janela", "Próximas 48h"],
]
dest_table = Table(destaques, colWidths=[45*mm, 120*mm])
dest_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,-1), VERDE_ESCURO),
    ("BACKGROUND", (1,0), (1,-1), CINZA_CLARO),
    ("TEXTCOLOR", (0,0), (0,-1), DOURADO),
    ("TEXTCOLOR", (1,0), (1,-1), PRETO),
    ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTNAME", (1,0), (1,-1), "Helvetica"),
    ("FONTSIZE", (0,0), (-1,-1), 9.5),
    ("ALIGN", (0,0), (0,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("GRID", (0,0), (-1,-1), 0.5, CINZA_MEDIO),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(dest_table)
story.append(sp(6))
story.append(hr())

# =============================
# 1. CONTEXTO DO MERCADO
# =============================
story.append(secao("1.  CONTEXTO DO MERCADO — 24/05/2026"))
story.append(sp(2))

story.append(p(
    "<b>Evento Ativo:</b> <font color='#1a6e36'><b>Ultimate TOTS</b></font> (Team of the Season) — "
    "lançado em 22/05/2026 às 18h BST. Promo em vigor até ~29/05/2026. "
    "Squad de 60 jogadores com cards até <b>99 OVR</b> (Mbappé, Messi, Ronaldo, Yamal, Rice, Gabriel). "
    "Paralelamente rodam os <b>End of an Era SBCs</b> com Salah 95, Robertson 93, "
    "Bernardo Silva 93, Griezmann, Goretzka e Stones 91."
))
story.append(sp(2))

story.append(p(
    "<b>Tendência Geral do Mercado:</b> Estamos na <font color='#e74c3c'><b>janela de market crash "
    "pós-lançamento</b></font>. Abertura massiva de packs floodou o mercado com gold cards, derrubando "
    "o preço de fodder 83–87 para mínimos históricos (700–1.100 coins). "
    "Este é o <b>melhor momento do ciclo para comprar</b>. "
    "A recuperação começa quando os End of an Era SBCs começarem a ser completados em massa "
    "(previsto ~25–27/05), elevando a demanda por 86–88 rated. "
    "Weekend League começa sexta-feira 28/05, criando segundo pico de demanda."
))
story.append(sp(2))

# Tabela de eventos
eventos_data = [
    ["Evento", "Status", "Validade", "Impacto no Mercado"],
    ["Ultimate TOTS (60 jogadores)", "🟢 ATIVO", "~29/05/2026", "Pack flood → preços baixos agora"],
    ["End of an Era SBCs\n(Salah, Robertson, B.Silva…)", "🟢 ATIVO", "~29/05/2026", "Alta demanda fodder 86–88 rated"],
    ["10× 84+ Upgrade SBC", "🟢 ATIVO", "29/05/2026", "Consome fodder 84+ continuamente"],
    ["TOTS Career Path Evo (grátis)", "🟢 ATIVO", "29/05/2026", "Eleva valor de cards 80–85 rated"],
    ["Thursday Rivals Rewards", "🔵 SEMANAL", "Toda quinta ~18h BST", "Dip de preços → janela de compra"],
    ["Weekend League (Champs)", "🔵 SEMANAL", "Sex–Dom", "Pico de demanda meta players"],
]
ev_table = Table(eventos_data, colWidths=[48*mm, 20*mm, 28*mm, 64*mm])
ev_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR", (0,0), (-1,0), DOURADO),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 9),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("BACKGROUND", (0,1), (-1,-1), CINZA_CLARO),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [BRANCO, CINZA_CLARO]),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,1), (-1,-1), 8.5),
    ("ALIGN", (1,1), (2,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("GRID", (0,0), (-1,-1), 0.5, CINZA_MEDIO),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
]))
story.append(ev_table)
story.append(sp(4))
story.append(hr())

# =============================
# 2. TABELA DE CARTAS RECOMENDADAS
# =============================
story.append(secao("2.  OPORTUNIDADES DE COMPRA — TOP 10 CARTAS"))
story.append(sp(2))
story.append(p(
    "Jogadores específicos identificados no período de market crash pós-Ultimate TOTS (24–26/05). "
    "Preços baseados em dados de FUTBIN/FUT.GG. "
    "<b>Margem líquida</b> calculada após dedução da taxa EA de 5%.",
    corpo_style
))
story.append(sp(2))

# Cabeçalho + linhas
# Colunas: Jogador | Pos | Rating | Clube | Compra | Venda | Margem Liq.
cards_data = [
    [
        Paragraph("<b>Jogador</b>", label_style),
        Paragraph("<b>Pos</b>", label_style),
        Paragraph("<b>OVR</b>", label_style),
        Paragraph("<b>Clube</b>", label_style),
        Paragraph("<b>Compra\n(coins)</b>", label_style),
        Paragraph("<b>Venda\n(coins)</b>", label_style),
        Paragraph("<b>Margem\nLíquida</b>", label_style),
    ],
    # 86-rated fodder — principal foco do relatório
    ["Hakan Çalhanoğlu",  "CDM", "86", "Inter Milan",     "900",  "1.900", "+905 (+100%)"],
    ["Sandro Tonali",     "CDM", "86", "Newcastle Utd",   "900",  "1.900", "+905 (+100%)"],
    ["Ibrahima Konaté",   "CB",  "86", "Liverpool FC",    "950",  "2.000", "+950  (+100%)"],
    ["Marc-André ter Stegen", "GK", "86", "Barcelona",    "900",  "1.800", "+810  (+90%)"],
    ["Alexandra Popp",    "ST",  "86", "Wolfsburg (W)",   "750",  "1.700", "+865  (+115%)"],
    # 85-rated — menor margem, maior volume
    ["Fabián Ruiz",       "CM",  "85", "PSG",             "850",  "1.600", "+670  (+79%)"],
    ["Scott McTominay",   "CM",  "85", "Napoli",          "850",  "1.600", "+670  (+79%)"],
    ["Marcus Thuram",     "ST",  "85", "Inter Milan",     "850",  "1.700", "+765  (+90%)"],
    # 87-rated — menor volume, maior valor unitário
    ["Jonathan Tah",      "CB",  "87", "Bayer Leverkusen","1.000","3.200", "+2.040 (+204%)"],
    # 83-rated — alto volume, fácil liquidez
    ["Iago Aspas",        "RW",  "83", "Celta de Vigo",   "750",  "1.400", "+580  (+77%)"],
]

col_ws = [42*mm, 14*mm, 13*mm, 33*mm, 18*mm, 18*mm, 22*mm]
cards_table = Table(cards_data, colWidths=col_ws)
cards_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR",   (0,0), (-1,0), DOURADO),
    ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0), (-1,0), 9),
    ("ALIGN",       (0,0), (-1,0), "CENTER"),
    ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[BRANCO, colors.HexColor("#edf7f1")]),
    ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE",    (0,1), (-1,-1), 8.5),
    ("ALIGN",       (1,1), (-1,-1), "CENTER"),
    ("GRID",        (0,0), (-1,-1), 0.5, CINZA_MEDIO),
    ("TOPPADDING",  (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1), 5),
    # Linha Jonathan Tah (87-rated) — destaque dourado
    ("BACKGROUND",  (0,9), (-1,9), colors.HexColor("#fff8e1")),
    ("TEXTCOLOR",   (6,9), (6,9), colors.HexColor("#b8860b")),
    ("FONTNAME",    (6,9), (6,9), "Helvetica-Bold"),
    # Margem positiva em verde
    ("TEXTCOLOR",   (6,1), (6,-1), VERDE_MEDIO),
]))
story.append(cards_table)
story.append(sp(3))

story.append(p(
    "<b>⭐ Destaque da semana:</b> <b>Jonathan Tah (87 CB, Bayer Leverkusen)</b> — "
    "Peça-chave nos End of an Era SBCs premium. Com Salah 95 e Robertson 93 exigindo "
    "squads de alta média, o Tah a 1.000 coins oferece a melhor margem unitária (>200%). "
    "Compre 10–15 unidades e aguarde a rush de EOAE SBCs.",
    corpo_style
))
story.append(sp(4))
story.append(hr())

# =============================
# 3. ESTRATÉGIA DE ALOCAÇÃO DE BUDGET
# =============================
story.append(secao("3.  ALOCAÇÃO DO BUDGET — 40.000 COINS"))
story.append(sp(2))

alloc_data = [
    ["Cesta",            "Cartas",       "Investimento",  "Jogadores Alvo"],
    ["86-rated Fodder",  "30 unidades",  "≈ 27.000",      "Çalhanoğlu, Tonali, Konaté, ter Stegen"],
    ["87-rated Fodder",  "10 unidades",  "≈ 10.000",      "Jonathan Tah"],
    ["83-rated Volume",  "3 unidades",   "≈  2.250",      "Iago Aspas (liquidez rápida)"],
    ["Reserva Táctica",  "—",            "=  750",        "Para oportunidades flash (< 1h)"],
    ["TOTAL",            "43 cards",     "≈ 40.000",      "—"],
]
alloc_table = Table(alloc_data, colWidths=[40*mm, 26*mm, 28*mm, 66*mm])
alloc_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (-1,0), VERDE_MEDIO),
    ("TEXTCOLOR",   (0,0), (-1,0), BRANCO),
    ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0), (-1,0), 9),
    ("ALIGN",       (0,0), (-1,0), "CENTER"),
    ("ROWBACKGROUNDS",(0,1),(-1,-2),[BRANCO, CINZA_CLARO]),
    ("BACKGROUND",  (0,-1), (-1,-1), VERDE_ESCURO),
    ("TEXTCOLOR",   (0,-1), (-1,-1), DOURADO),
    ("FONTNAME",    (0,-1), (-1,-1), "Helvetica-Bold"),
    ("FONTNAME",    (0,1), (-1,-2), "Helvetica"),
    ("FONTSIZE",    (0,1), (-1,-1), 8.5),
    ("ALIGN",       (1,1), (2,-1), "CENTER"),
    ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
    ("GRID",        (0,0), (-1,-1), 0.5, CINZA_MEDIO),
    ("TOPPADDING",  (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
]))
story.append(alloc_table)
story.append(sp(4))
story.append(hr())

# =============================
# 4. ESTRATÉGIA DE TIMING
# =============================
story.append(secao("4.  ESTRATÉGIA DE TIMING"))
story.append(sp(2))

timing_data = [
    ["⏱ Horário / Janela",        "📋 Ação",              "💡 Justificativa"],
    ["Hoje (24/05) 14h–17h UTC",  "COMPRAR — 86 e 87\nrated no AH",
     "Pós-Weekend League, mercado ainda inundado. Mínimos históricos disponíveis."],
    ["Hoje (24/05) após 18h UTC",  "COMPRAR — 83 rated\ne 85 rated",
     "Rivals Rewards às 18h BST podem dar leve dip extra."],
    ["25/05 (Seg) tarde",          "MANTER — não listar\nainda",
     "Mercado ainda absorvendo UTOTS. Aguardar pico de demanda por EOAE SBC."],
    ["26/05 (Ter) 12h–18h UTC",   "VENDER — 86 rated\ne 87 rated",
     "Pico esperado de EOAE SBC rush. Demanda máxima. Listar a BIN ideal."],
    ["27/05 (Qua) manhã",          "VENDER — 83–85\nrated restantes",
     "Segundo pico de SBC completes. Bom momento para liquidar volume."],
    ["29/05 (Sex) 17h–20h UTC",   "VENDER — qualquer\nremanesecente",
     "FUT Champs. Players montando squads. Último pico de demanda antes do fim da promo."],
]
timing_table = Table(timing_data, colWidths=[40*mm, 38*mm, 82*mm])
timing_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR",   (0,0), (-1,0), DOURADO),
    ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0), (-1,0), 9),
    ("ALIGN",       (0,0), (-1,0), "CENTER"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[BRANCO, colors.HexColor("#edf7f1")]),
    ("FONTNAME",    (0,1), (1,-1), "Helvetica-Bold"),
    ("FONTNAME",    (2,1), (2,-1), "Helvetica"),
    ("FONTSIZE",    (0,1), (-1,-1), 8.5),
    ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
    ("GRID",        (0,0), (-1,-1), 0.5, CINZA_MEDIO),
    ("TOPPADDING",  (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
]))
story.append(timing_table)
story.append(sp(4))
story.append(hr())

# =============================
# 5. ESTIMATIVA DE RETORNO 48H
# =============================
story.append(secao("5.  ESTIMATIVA DE RETORNO EM 48 HORAS"))
story.append(sp(2))

ret_data = [
    ["", "Conservador 🐢", "Base 📊", "Otimista 🚀"],
    ["Preço médio de venda (86 rated)",   "1.400 c",   "1.900 c",   "2.400 c"],
    ["Preço médio de venda (87 rated)",   "2.200 c",   "3.200 c",   "4.000 c"],
    ["Receita bruta total (43 cards)",    "~50.200 c", "~69.100 c", "~87.200 c"],
    ["Taxa EA 5% descontada",             "−2.510 c",  "−3.455 c",  "−4.360 c"],
    ["Receita líquida",                   "~47.690 c", "~65.645 c", "~82.840 c"],
    ["Custo de aquisição",                "−40.000 c", "−40.000 c", "−40.000 c"],
    ["LUCRO LÍQUIDO",                     "+7.690 c",  "+25.645 c", "+42.840 c"],
    ["RETORNO SOBRE CAPITAL",             "+19%",      "+64%",      "+107%"],
]
ret_table = Table(ret_data, colWidths=[58*mm, 36*mm, 36*mm, 30*mm])
ret_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0),  (-1,0),  VERDE_ESCURO),
    ("TEXTCOLOR",   (0,0),  (-1,0),  DOURADO),
    ("FONTNAME",    (0,0),  (-1,0),  "Helvetica-Bold"),
    ("FONTSIZE",    (0,0),  (-1,0),  9),
    ("ALIGN",       (0,0),  (-1,0),  "CENTER"),
    ("BACKGROUND",  (1,0),  (1,0),   LARANJA),
    ("BACKGROUND",  (2,0),  (2,0),   AZUL_CLARO),
    ("BACKGROUND",  (3,0),  (3,0),   VERDE_CLARO),
    ("ROWBACKGROUNDS",(0,1),(-1,-3),[BRANCO, CINZA_CLARO]),
    ("BACKGROUND",  (0,-2), (-1,-2), colors.HexColor("#d4edda")),
    ("BACKGROUND",  (0,-1), (-1,-1), VERDE_ESCURO),
    ("TEXTCOLOR",   (0,-2), (-1,-2), VERDE_ESCURO),
    ("TEXTCOLOR",   (0,-1), (-1,-1), DOURADO),
    ("FONTNAME",    (0,-2), (-1,-1), "Helvetica-Bold"),
    ("FONTNAME",    (0,1),  (0,-3),  "Helvetica-Bold"),
    ("FONTNAME",    (1,1),  (-1,-3), "Helvetica"),
    ("FONTSIZE",    (0,1),  (-1,-1), 8.5),
    ("ALIGN",       (1,1),  (-1,-1), "CENTER"),
    ("VALIGN",      (0,0),  (-1,-1), "MIDDLE"),
    ("GRID",        (0,0),  (-1,-1), 0.5, CINZA_MEDIO),
    ("TOPPADDING",  (0,0),  (-1,-1), 5),
    ("BOTTOMPADDING",(0,0), (-1,-1), 5),
]))
story.append(ret_table)
story.append(sp(3))
story.append(p(
    "<b>Premissas:</b> Compra de 30 cards 86-rated a 900c avg + 10 cards 87-rated a 1.000c + 3 cards "
    "83-rated a 750c. Cenário conservador: demanda de EOAE SBC fraca (apenas 1 SBC importante). "
    "Cenário base: 2–3 EOAE SBCs ativos gerando demanda consistente. "
    "Cenário otimista: rush de SBCs + conteúdo surpresa quinta-feira elevando preços acima do "
    "esperado. Preços de referência: FUTBIN/FUT.GG (~24/05/2026).",
    aviso_style
))
story.append(sp(4))
story.append(hr())

# =============================
# 6. ESTRATÉGIA EVO INVESTING
# =============================
story.append(secao("6.  BÔNUS: EVOLUTION INVESTING — TOTS CAREER PATH"))
story.append(sp(2))
story.append(p(
    "A evolução <b>TOTS Career Path (I → III)</b> é gratuita e eleva cards até <b>90 OVR</b>. "
    "Cards base 80–83 rated de ligas secundárias podem chegar a 88–90 OVR após evolução completa. "
    "Se você possui cards já evoluídos, este é o momento ideal para listá-los: "
    "a demanda por cards meta evolúídos é máxima durante TOTS."
))
story.append(sp(2))
evo_data = [
    ["Tipo de Evo",             "Custo",     "Cards Ideais",                       "Valor Pós-Evo"],
    ["TOTS Career Path I",      "Grátis",    "Jogadores 80–83 rated base",         "84–86 OVR"],
    ["TOTS Career Path II",     "Grátis",    "Jogadores 83–85 rated pós-path I",   "86–88 OVR"],
    ["TOTS Career Path III",    "Grátis",    "Jogadores 85–87 rated pós-path II",  "88–90 OVR"],
    ["El Tiburon Evo (CB)",     "≈ 65.000 c","CBs com pace/físico base adequado",  "90–92 OVR (meta)"],
]
evo_table = Table(evo_data, colWidths=[42*mm, 24*mm, 54*mm, 40*mm])
evo_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0),  (-1,0), VERDE_MEDIO),
    ("TEXTCOLOR",   (0,0),  (-1,0), BRANCO),
    ("FONTNAME",    (0,0),  (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0),  (-1,-1), 8.5),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[BRANCO, CINZA_CLARO]),
    ("GRID",        (0,0),  (-1,-1), 0.5, CINZA_MEDIO),
    ("VALIGN",      (0,0),  (-1,-1), "MIDDLE"),
    ("ALIGN",       (1,1),  (1,-1), "CENTER"),
    ("TOPPADDING",  (0,0),  (-1,-1), 4),
    ("BOTTOMPADDING",(0,0), (-1,-1),4),
]))
story.append(evo_table)
story.append(sp(2))
story.append(p(
    "<b>Nota:</b> El Tiburon Evo (65k coins) está fora do budget atual de 40k. "
    "Após acumular lucros desta semana, considere este investimento para a próxima janela.",
    aviso_style
))
story.append(sp(4))
story.append(hr())

# =============================
# 7. THURSDAY FLIP GUIDE
# =============================
story.append(secao("7.  THURSDAY FLIP — PRÓXIMA JANELA: 28/05 (QUI) ~18h BST"))
story.append(sp(2))
story.append(p(
    "Todo <b>Quinta-Feira às 18h BST</b> (19h CET / 13h BRT) os rewards do <b>Division Rivals</b> "
    "são distribuídos. O flood de novos cards derruba os preços por 1–3 horas. "
    "É a janela semanal mais confiável para comprar fodder e cards meta abaixo do preço de equilíbrio."
))
story.append(sp(2))
thursday_data = [
    ["Fase",           "Horário (UTC)",   "Ação"],
    ["Pre-dip",        "16h–17h30",       "Vender cartas que você já tem listadas. Liquidar posições abertas."],
    ["Dip (compra)",   "18h–19h30",       "Comprar agressivamente: 85–87 rated no mínimo. Buscar BIN abaixo de 1.000c."],
    ["Estabilização",  "20h–23h",         "Aguardar. Não vender ainda; mercado ainda absorvendo."],
    ["Recuperação",    "Sexta 08h–12h",   "Listar cartas a preço de mercado (+60–80% sobre custo)."],
    ["Pico WL",        "Sexta 17h–20h",   "Venda final. Players preparando squad para Champs."],
]
thu_table = Table(thursday_data, colWidths=[28*mm, 30*mm, 102*mm])
thu_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0),  (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR",   (0,0),  (-1,0), DOURADO),
    ("FONTNAME",    (0,0),  (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0),  (-1,0), 9),
    ("ALIGN",       (0,0),  (-1,0), "CENTER"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[BRANCO, colors.HexColor("#edf7f1")]),
    ("FONTNAME",    (0,1),  (0,-1), "Helvetica-Bold"),
    ("FONTNAME",    (1,1),  (-1,-1),"Helvetica"),
    ("FONTSIZE",    (0,1),  (-1,-1), 8.5),
    ("VALIGN",      (0,0),  (-1,-1), "MIDDLE"),
    ("GRID",        (0,0),  (-1,-1), 0.5, CINZA_MEDIO),
    ("TOPPADDING",  (0,0),  (-1,-1), 5),
    ("BOTTOMPADDING",(0,0), (-1,-1),5),
]))
story.append(thu_table)
story.append(sp(4))
story.append(hr())

# =============================
# 8. AS 8 REGRAS DE OURO
# =============================
story.append(secao("8.  AS 8 REGRAS DE OURO DO TRADER"))
story.append(sp(2))

regras = [
    ("1", "Nunca compre no pico.",
     "Após um anúncio de SBC ou promo, preços sobem rapidamente. Espere 30–60 minutos para os preços normalizarem antes de comprar."),
    ("2", "Compre com liquidez em mente.",
     "Cards de ligas populares (Premier League, La Liga, Serie A) vendem mais rápido. Prefira eles ao mesmo preço de ligas obscuras."),
    ("3", "Diversifique o portfolio de ratings.",
     "Não coloque tudo em 86-rated. Balanceie entre 83, 85, 86 e 87 para cobrir múltiplos SBCs simultâneos."),
    ("4", "Defina preço-alvo antes de comprar.",
     "Calcule a margem líquida (após 5% EA) antes de qualquer compra. Mínimo aceitável: +30% de margem líquida."),
    ("5", "Respeite o Stop Loss.",
     "Se um card cair 30% abaixo do preço de compra e não houver catalisador de recuperação em 24h, venda e corte o prejuízo."),
    ("6", "Nunca liste todas as cartas de uma vez.",
     "Listar 30 cards iguais ao mesmo tempo afunda o preço da listagem. Divida em lotes de 5–8 a cada 2 horas."),
    ("7", "Monitore futbin.com/fut.gg em tempo real.",
     "Alertas de preço e histórico gráfico são seus melhores aliados. Atualize a cada 2–4h durante picos de atividade."),
    ("8", "Preserve 10% de capital como reserva.",
     "Sempre guarde 4.000–5.000 coins livres para aproveitar oportunidades flash (cards abaixo do piso por erro de listagem)."),
]

for num, titulo, desc in regras:
    rule_data = [[
        Paragraph(f"<b>{num}</b>", ParagraphStyle("rn", fontName="Helvetica-Bold",
            fontSize=14, textColor=DOURADO, alignment=TA_CENTER)),
        Paragraph(f"<b>{titulo}</b><br/><font size='8.5'>{desc}</font>",
            ParagraphStyle("rd", fontName="Helvetica", fontSize=9, leading=13,
                textColor=PRETO, leftIndent=4))
    ]]
    rt = Table(rule_data, colWidths=[12*mm, 147*mm])
    rt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), VERDE_ESCURO),
        ("BACKGROUND", (1,0), (1,0), CINZA_CLARO if int(num) % 2 == 0 else BRANCO),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("GRID",       (0,0), (-1,-1), 0.5, CINZA_MEDIO),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ]))
    story.append(rt)
    story.append(sp(1))

story.append(sp(4))
story.append(hr())

# =============================
# 9. RESUMO EXECUTIVO
# =============================
story.append(secao("9.  RESUMO EXECUTIVO — PLANO DE AÇÃO"))
story.append(sp(2))

resumo_data = [
    ["#", "Ação",                                              "Prazo",       "Coins"],
    ["1", "Comprar 30× 86-rated (Çalhanoğlu, Tonali, Konaté)", "HOJE 14–17h", "≈ 27.000"],
    ["2", "Comprar 10× Jonathan Tah 87 CB",                   "HOJE 14–17h", "≈ 10.000"],
    ["3", "Comprar 3× Iago Aspas 83 RW",                      "HOJE após 18h","≈ 2.250"],
    ["4", "Aguardar rush EOAE SBC",                           "25–26/05",    "—"],
    ["5", "Listar 86+87 rated em lotes de 5–8",               "26/05 12–18h","💸 venda"],
    ["6", "Liquidar 83–85 rated restantes",                   "27/05 manhã", "💸 venda"],
    ["7", "Reaplicar lucros: novo ciclo Thursday Flip",        "28/05 18h",   "♻️ reinvest"],
]
res_table = Table(resumo_data, colWidths=[8*mm, 80*mm, 30*mm, 42*mm])
res_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR",   (0,0), (-1,0), DOURADO),
    ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0), (-1,-1), 9),
    ("ALIGN",       (0,0), (0,-1), "CENTER"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[BRANCO, CINZA_CLARO]),
    ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
    ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
    ("GRID",        (0,0), (-1,-1), 0.5, CINZA_MEDIO),
    ("TOPPADDING",  (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
]))
story.append(res_table)
story.append(sp(4))
story.append(hr())

# =============================
# 10. DISCLAIMER
# =============================
story.append(secao("⚠  DISCLAIMER"))
story.append(sp(2))
story.append(p(
    "Este relatório foi gerado por um agente de IA para fins educacionais e de análise de mercado "
    "do jogo EA FC 26 Ultimate Team. <b>Não constitui garantia de lucro.</b> "
    "Os preços de cartas são voláteis e podem mudar em minutos. "
    "O mercado do Ultimate Team é influenciado por fatores imprevisíveis como novos conteúdos, "
    "mudanças de preços-piso pela EA Sports, bugs e eventos não anunciados. "
    "Todo o capital em coins pode ser perdido. Opere apenas com o que você pode perder. "
    "Dados de preços baseados em FUTBIN, FUT.GG, RealSport101, TeamGullit e outras fontes públicas "
    "disponíveis em 24/05/2026. <b>EA Sports, EA FC 26 e Ultimate Team são marcas registradas da "
    "Electronic Arts Inc.</b> Este relatório não tem afiliação com a EA Sports.",
    aviso_style
))
story.append(sp(2))

fontes_data = [
    ["📎 Fontes Consultadas"],
    ["futbin.com/players · fut.gg · realsport101.com · teamgullit.com/ea-fc-26/best-trading-methods"],
    ["mmopixel.com · lootbar.gg · khelnow.com · operationsports.com · iggm.com"],
    ["fifaultimateteam.it · gamer.org · itemd2r.com · cheapgoals.com · coinlooting.com"],
]
f_table = Table(fontes_data, colWidths=[160*mm])
f_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (-1,0),  VERDE_ESCURO),
    ("TEXTCOLOR",   (0,0), (-1,0),  DOURADO),
    ("BACKGROUND",  (0,1), (-1,-1), CINZA_CLARO),
    ("TEXTCOLOR",   (0,1), (-1,-1), colors.HexColor("#444444")),
    ("FONTNAME",    (0,0), (-1,0),  "Helvetica-Bold"),
    ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE",    (0,0), (-1,-1), 8),
    ("ALIGN",       (0,0), (-1,-1), "CENTER"),
    ("GRID",        (0,0), (-1,-1), 0.3, CINZA_MEDIO),
    ("TOPPADDING",  (0,0), (-1,-1), 4),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),
]))
story.append(f_table)
story.append(sp(3))
story.append(p(
    f"Relatório gerado automaticamente em {data_fmt} UTC · EA FC 26 Trading Agent",
    aviso_style
))

# ============================================================
#  BUILD
# ============================================================
doc.build(story, canvasmaker=FifaCanvas)
print(f"✅  PDF gerado: {nome_pdf}")
