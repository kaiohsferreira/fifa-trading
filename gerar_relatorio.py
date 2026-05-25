#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import KeepTogether
import datetime

# ── Constantes ────────────────────────────────────────────────────────────────
DATA_HORA = "25/05/2026 20:07"
NOME_ARQUIVO = "relatorio-trading-2026-05-25-20h.pdf"

# Paleta de cores
VERDE_EA    = colors.HexColor("#00D26A")
VERDE_ESCURO = colors.HexColor("#006B35")
CINZA_ESCURO = colors.HexColor("#1A1A2E")
CINZA_MEDIO = colors.HexColor("#16213E")
CINZA_CLARO = colors.HexColor("#2E2E4E")
AMARELO     = colors.HexColor("#F5A623")
AZUL_CLARO  = colors.HexColor("#4FC3F7")
BRANCO      = colors.white
VERMELHO    = colors.HexColor("#FF4444")
LARANJA     = colors.HexColor("#FF8C00")

# ── Estilos ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def estilo(nome, pai="Normal", **kwargs):
    return ParagraphStyle(nome, parent=styles[pai], **kwargs)

titulo_doc   = estilo("TituloDoc",   pai="Title",   fontSize=26, textColor=VERDE_EA,
                       fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=4)
subtitulo    = estilo("Subtitulo",   pai="Normal",  fontSize=13, textColor=AMARELO,
                       fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=2)
data_hora_st = estilo("DataHora",    pai="Normal",  fontSize=11, textColor=colors.lightgrey,
                       fontName="Helvetica", alignment=TA_CENTER, spaceAfter=6)
secao        = estilo("Secao",       pai="Heading1",fontSize=14, textColor=VERDE_EA,
                       fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=6,
                       borderPad=4)
subsecao     = estilo("Subsecao",    pai="Heading2",fontSize=12, textColor=AMARELO,
                       fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=4)
corpo        = estilo("Corpo",       pai="Normal",  fontSize=9,  textColor=BRANCO,
                       fontName="Helvetica", leading=14, spaceAfter=4, alignment=TA_JUSTIFY)
bullet_st    = estilo("Bullet",      pai="Normal",  fontSize=9,  textColor=BRANCO,
                       fontName="Helvetica", leading=13, leftIndent=14, spaceAfter=3)
nota         = estilo("Nota",        pai="Normal",  fontSize=8,  textColor=colors.lightgrey,
                       fontName="Helvetica-Oblique", leading=12, spaceAfter=3, alignment=TA_JUSTIFY)
rodape_st    = estilo("Rodape",      pai="Normal",  fontSize=8,  textColor=colors.grey,
                       fontName="Helvetica", alignment=TA_CENTER)
alerta       = estilo("Alerta",      pai="Normal",  fontSize=9,  textColor=AMARELO,
                       fontName="Helvetica-Bold", leading=13, leftIndent=10, spaceAfter=3)
destaque     = estilo("Destaque",    pai="Normal",  fontSize=10, textColor=VERDE_EA,
                       fontName="Helvetica-Bold", leading=14, spaceAfter=4)
regra_num    = estilo("RegraNum",    pai="Normal",  fontSize=10, textColor=AMARELO,
                       fontName="Helvetica-Bold", leading=14, spaceAfter=2)
regra_txt    = estilo("RegraTxt",    pai="Normal",  fontSize=9,  textColor=BRANCO,
                       fontName="Helvetica", leading=13, leftIndent=20, spaceAfter=6)

# ── Background preto nas páginas ───────────────────────────────────────────────
def fundo_pagina(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CINZA_ESCURO)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # Barra superior decorativa
    canvas.setFillColor(VERDE_ESCURO)
    canvas.rect(0, A4[1] - 6, A4[0], 6, fill=1, stroke=0)
    # Barra inferior decorativa
    canvas.setFillColor(VERDE_ESCURO)
    canvas.rect(0, 0, A4[0], 6, fill=1, stroke=0)
    # Número da página
    canvas.setFillColor(colors.grey)
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(A4[0]/2, 14, f"Página {doc.page}")
    canvas.restoreState()

# ── Utilitários ────────────────────────────────────────────────────────────────
def hr(cor=VERDE_ESCURO, espessura=1):
    return HRFlowable(width="100%", thickness=espessura, color=cor, spaceAfter=6, spaceBefore=4)

def caixa_info(titulo_caixa, linhas, cor_titulo=AMARELO):
    """Bloco de destaque com fundo cinza."""
    data = [[Paragraph(titulo_caixa, estilo("ci_t", fontSize=10, textColor=cor_titulo,
                                              fontName="Helvetica-Bold"))]]
    for l in linhas:
        data.append([Paragraph(l, estilo("ci_l", fontSize=9, textColor=BRANCO,
                                          fontName="Helvetica", leading=13))])
    t = Table(data, colWidths=[16.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, 0),  CINZA_CLARO),
        ("BACKGROUND",  (0, 1), (-1, -1), colors.HexColor("#1E1E3E")),
        ("TOPPADDING",  (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0,0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",(0, 0), (-1, -1), 8),
        ("BOX",         (0, 0), (-1, -1), 1, VERDE_ESCURO),
        ("LINEBELOW",   (0, 0), (0, 0),   1, VERDE_EA),
    ]))
    return t

# ══════════════════════════════════════════════════════════════════════════════
#  CONSTRUÇÃO DO DOCUMENTO
# ══════════════════════════════════════════════════════════════════════════════
def build_pdf():
    doc = SimpleDocTemplate(
        NOME_ARQUIVO,
        pagesize=A4,
        leftMargin=2.2*cm,
        rightMargin=2.2*cm,
        topMargin=2.5*cm,
        bottomMargin=2*cm,
    )

    story = []

    # ── CABEÇALHO ──────────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("⚽ EA FC 26 ULTIMATE TEAM", titulo_doc))
    story.append(Paragraph("RELATÓRIO DE TRADING — ANÁLISE DE MERCADO", subtitulo))
    story.append(Paragraph(f"Gerado em: {DATA_HORA} UTC", data_hora_st))
    story.append(hr(VERDE_EA, 2))
    story.append(Spacer(1, 0.2*cm))

    # ── 1. CONTEXTO DO MERCADO ─────────────────────────────────────────────────
    story.append(Paragraph("1. CONTEXTO DO MERCADO — MAI/2026", secao))
    story.append(hr())

    story.append(Paragraph(
        "Estamos na semana mais crítica do calendário FUT: o <b>Ultimate TOTS (Team of the Season)</b> "
        "está ativo desde 22/05 e encerra em <b>29/05/2026 às 18h BST</b>. Esta é a última semana da "
        "temporada FUT 26 com todos os melhores TOTS de todas as ligas disponíveis em packs "
        "simultaneamente. O mercado está em <b>crash profundo</b> — queda de 30 a 70% em cartas "
        "meta — criando a janela de compra mais favorável do ano.",
        corpo))

    story.append(Paragraph("📌 Eventos Ativos Agora (25/05/2026):", subsecao))

    eventos = [
        ["Evento", "Status", "Encerra em"],
        ["Ultimate TOTS (todos os TOTS em packs)", "🟢 ATIVO", "29/05 · 18h BST"],
        ["End of Era SBC — Mohamed Salah (95 OVR)", "🟢 ATIVO", "29/05 · 18h BST"],
        ["End of Era SBC — Antoine Griezmann (94 OVR)", "🟢 ATIVO", "29/05 · 18h BST"],
        ["End of Era — Bernardo Silva / Robertson", "🟢 ATIVO", "29/05 · 18h BST"],
        ["Bundesliga TOTS Upgrade SBC (85+86 rated)", "🟢 ATIVO", "31/05 · 18h BST"],
        ["91+ EFIGS/EFUGS TOTS Upgrade SBC (86+87)", "🟢 ATIVO", "29/05 · 18h BST"],
        ["LaLiga TOTS Upgrade SBC", "🔴 EXPIRA HOJE", "26/05 · 18h BST"],
        ["TOTS Career Path EVO (Starter → III)", "🟢 ATIVO", "05/06 · 18h BST"],
        ["Sterling Ascension Evolution", "🟢 ATIVO", "A confirmar"],
        ["Live TOTS — UEFA + Ligas Nacionais", "🟢 ATIVO", "30/05 · 18h BST"],
    ]

    t_eventos = Table(eventos, colWidths=[8.5*cm, 4*cm, 4*cm])
    t_eventos.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  CINZA_CLARO),
        ("TEXTCOLOR",     (0,0), (-1,0),  VERDE_EA),
        ("FONTNAME",      (0,0), (-1,0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("BACKGROUND",    (0,1), (-1,-1), colors.HexColor("#12122A")),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.HexColor("#12122A"), colors.HexColor("#1A1A30")]),
        ("TEXTCOLOR",     (0,1), (-1,-1), BRANCO),
        ("ALIGN",         (1,0), (-1,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("BOX",           (0,0), (-1,-1), 1, VERDE_ESCURO),
        ("INNERGRID",     (0,0), (-1,-1), 0.5, CINZA_CLARO),
        ("TEXTCOLOR",     (1,7), (1,7),   VERMELHO),
    ]))
    story.append(t_eventos)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("📈 Tendência Geral do Mercado:", subsecao))
    tendencias = [
        "• <b>CRASH ATIVO:</b> Mercado em queda desde 22/05 com abertura massiva de packs TOTS.",
        "• <b>Fodder 83-87 rated em baixa histórica</b> — cartas sendo vendidas no piso para completar SBCs.",
        "• <b>Demanda de fodder alta:</b> End of Era SBCs de Salah e Griezmann exigem muitos 85-87 rated.",
        "• <b>Janela de compra:</b> 25-26/05 (hoje e amanhã) são os melhores dias para comprar.",
        "• <b>Recuperação esperada:</b> 28-29/05 quando a quinta-feira de rewards aquece o mercado.",
        "• <b>Post-TOTS:</b> Após 29/05 os preços sobem com escassez de novos packs.",
    ]
    for t in tendencias:
        story.append(Paragraph(t, bullet_st))
    story.append(Spacer(1, 0.2*cm))

    # ── 2. TABELA DE OPORTUNIDADES ──────────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("2. CARTAS RECOMENDADAS — OPORTUNIDADES DE COMPRA", secao))
    story.append(hr())
    story.append(Paragraph(
        "Cartas selecionadas com base na análise de SBCs ativos, demanda de fodder e perfil de risco "
        "compatível com budget de <b>40.000 coins</b>. Margem líquida já deduz a taxa de 5% da EA.",
        corpo))
    story.append(Spacer(1, 0.2*cm))

    # Cabeçalho da tabela
    cabecalho = [
        Paragraph("<b>Jogador</b>", estilo("th", fontSize=8, textColor=VERDE_EA, fontName="Helvetica-Bold")),
        Paragraph("<b>OVR</b>",    estilo("th", fontSize=8, textColor=VERDE_EA, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Clube</b>",  estilo("th", fontSize=8, textColor=VERDE_EA, fontName="Helvetica-Bold")),
        Paragraph("<b>Compra\n(máx.)</b>",  estilo("th", fontSize=8, textColor=VERDE_EA, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Venda\n(alvo)</b>",   estilo("th", fontSize=8, textColor=VERDE_EA, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Margem\nLíquida</b>", estilo("th", fontSize=8, textColor=VERDE_EA, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("<b>Estratégia</b>",      estilo("th", fontSize=8, textColor=VERDE_EA, fontName="Helvetica-Bold")),
    ]

    def linha(jogador, ovr, clube, compra, venda, margem, estrategia, cor_margem=VERDE_EA):
        return [
            Paragraph(jogador,    estilo("td", fontSize=8, textColor=BRANCO, fontName="Helvetica-Bold")),
            Paragraph(str(ovr),   estilo("td", fontSize=9, textColor=AMARELO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
            Paragraph(clube,      estilo("td", fontSize=8, textColor=colors.lightgrey, fontName="Helvetica")),
            Paragraph(compra,     estilo("td", fontSize=8, textColor=BRANCO, fontName="Helvetica", alignment=TA_CENTER)),
            Paragraph(venda,      estilo("td", fontSize=8, textColor=AZUL_CLARO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
            Paragraph(margem,     estilo("td", fontSize=8, textColor=cor_margem, fontName="Helvetica-Bold", alignment=TA_CENTER)),
            Paragraph(estrategia, estilo("td", fontSize=7.5, textColor=BRANCO, fontName="Helvetica", leading=10)),
        ]

    linhas_tabela = [
        cabecalho,
        # ── SBC FODDER 85 RATED ──
        linha("Karim Benzema",     85, "Al-Qadsiah FC",    "900c",  "1.400c", "+430c",  "SBC Fodder · Vender 27-28/05"),
        linha("N'Golo Kanté",      85, "Al-Ittihad FC",   "950c",  "1.500c", "+475c",  "SBC Fodder · Alta demanda Salah SBC"),
        linha("Dani Olmo",         85, "FC Barcelona",    "1.000c","1.600c", "+520c",  "SBC Fodder · LaLiga link"),
        linha("Heung-min Son",     85, "Tottenham",       "1.100c","1.700c", "+515c",  "SBC Fodder · Vender pós-quinta"),
        linha("Delphine Cascarino",85, "Olympique Lyon",  "850c",  "1.400c", "+480c",  "SBC Fodder · Feminino em alta"),
        # ── SBC FODDER 86 RATED ──
        linha("Rúben Dias",        86, "Man. City",       "950c",  "1.600c", "+570c",  "SBC Fodder · 86 mais barato do mercado",  VERDE_EA),
        linha("Bruno Guimarães",   86, "Newcastle Utd",   "1.200c","1.900c", "+605c",  "SBC Fodder · Mid req 86+87 SBC"),
        linha("Lea Schüller",      86, "FC Bayern Fem.",  "1.200c","1.850c", "+558c",  "SBC Fodder · Bundesliga TOTS SBC"),
        linha("Hakan Çalhanoğlu",  86, "Inter de Milão",  "1.400c","2.100c", "+595c",  "SBC Fodder · Serie A link"),
        linha("Paulo Dybala",      86, "AS Roma",         "1.400c","2.200c", "+690c",  "SBC Fodder · Melhor margem 86 rated"),
        # ── SBC FODDER 87 RATED ──
        linha("Leah Williamson",   87, "Arsenal Fem.",    "1.300c","2.100c", "+695c",  "SBC Fodder · 87 mais barato do mercado", AMARELO),
        linha("Ada Hegerberg",     87, "Olympique Lyon",  "1.500c","2.400c", "+780c",  "SBC Fodder · Alta demanda 87 rated"),
        linha("Yann Sommer",       87, "Inter de Milão",  "2.000c","3.000c", "+850c",  "SBC Fodder · Bundesliga TOTS SBC"),
        linha("Marquinhos",        87, "PSG",             "2.100c","3.200c", "+940c",  "SBC Fodder · EOE SBCs + 91+ req"),
        # ── INVEST EVOLUÇÃO ──
        linha("Raheem Sterling",   78, "Chelsea",         "1.200c","8.000c", "+6.400c","Evo invest · Sterling Ascension EVO", LARANJA),
        # ── THURSDAY FLIP ──
        linha("Bruno Fernandes",   89, "Man. United",     "4.500c","6.500c", "+1.675c","Thursday Flip · Comprar 28/05 manhã", AZUL_CLARO),
        linha("Virgil van Dijk",   89, "Liverpool",       "5.000c","7.500c", "+2.125c","Thursday Flip · Div. Rivals rewards", AZUL_CLARO),
        linha("Pedri",             88, "FC Barcelona",    "3.000c","4.800c", "+1.560c","Thursday Flip · Weekend League demand", AZUL_CLARO),
    ]

    col_widths = [3.5*cm, 1.1*cm, 2.8*cm, 1.7*cm, 1.7*cm, 1.8*cm, 4.0*cm]
    tabela = Table(linhas_tabela, colWidths=col_widths, repeatRows=1)
    tabela.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),  (-1,0),  CINZA_CLARO),
        ("ROWBACKGROUNDS",(0,1),  (-1,-1), [colors.HexColor("#12122A"), colors.HexColor("#1A1A30")]),
        ("ALIGN",         (0,0),  (-1,-1), "LEFT"),
        ("VALIGN",        (0,0),  (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),  (-1,-1), 5),
        ("BOTTOMPADDING", (0,0),  (-1,-1), 5),
        ("LEFTPADDING",   (0,0),  (-1,-1), 5),
        ("RIGHTPADDING",  (0,0),  (-1,-1), 4),
        ("BOX",           (0,0),  (-1,-1), 1, VERDE_ESCURO),
        ("INNERGRID",     (0,0),  (-1,-1), 0.4, CINZA_CLARO),
        ("LINEBELOW",     (0,0),  (-1,0),  1.5, VERDE_EA),
        # Separadores por categoria
        ("LINEABOVE",     (0,6),  (-1,6),  0.8, AMARELO),
        ("LINEABOVE",     (0,11), (-1,11), 0.8, AZUL_CLARO),
        ("LINEABOVE",     (0,15), (-1,15), 0.8, LARANJA),
        ("LINEABOVE",     (0,16), (-1,16), 0.8, AZUL_CLARO),
    ]))
    story.append(tabela)
    story.append(Spacer(1, 0.2*cm))

    # Legenda
    leg_data = [[
        Paragraph("🟢 85-86 Rated Fodder", estilo("lg", fontSize=8, textColor=VERDE_EA, fontName="Helvetica")),
        Paragraph("🟡 87 Rated Fodder", estilo("lg", fontSize=8, textColor=AMARELO, fontName="Helvetica")),
        Paragraph("🟠 Evo Invest", estilo("lg", fontSize=8, textColor=LARANJA, fontName="Helvetica")),
        Paragraph("🔵 Thursday Flip", estilo("lg", fontSize=8, textColor=AZUL_CLARO, fontName="Helvetica")),
    ]]
    leg = Table(leg_data, colWidths=[4.1*cm]*4)
    leg.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), CINZA_CLARO),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),6),
        ("BOX",(0,0),(-1,-1),1,VERDE_ESCURO),
    ]))
    story.append(leg)
    story.append(Spacer(1, 0.3*cm))

    # ── 3. ESTRATÉGIA DE TIMING ────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("3. ESTRATÉGIA DE TIMING", secao))
    story.append(hr())

    timing_data = [
        ["Período", "Ação", "Justificativa"],
        ["Hoje · 25/05 · 20h-23h UTC", "🟢 COMPRAR fodder 85-87",
         "Crash ativo, pior momento do ciclo para os vendedores → melhor janela de compra"],
        ["Amanhã · 26/05 · Madrugada", "🟢 COMPRAR Sterling (EVO)",
         "Procurar Raheem Sterling 78 OVR abaixo de 1.200c antes da corrida da evolução"],
        ["26/05 até 12h BST", "⚠️ URGENTE: LaLiga SBC",
         "LaLiga TOTS Upgrade expira hoje às 18h BST — última chance de usar fodder neste SBC"],
        ["27/05 · Quarta-feira", "⏳ AGUARDAR",
         "Mercado ainda fraco. Boa hora para monitorar preços e recomprar se houver queda adicional"],
        ["28/05 · Quinta-feira", "🔵 THURSDAY FLIP",
         "Division Rivals rewards abrem → flood de cartas no mercado → comprar 89 OVR no piso"],
        ["28/05 · 16h-23h UTC", "🔵 VENDER Thursday Flip",
         "4-5h após o pico de oferta, demanda de Weekend League empurra preços para cima"],
        ["29/05 · Última hora TOTS", "💰 VENDER fodder 85-87",
         "Último dia TOTS → SBC rush final → demanda máxima por fodder → vender antes das 18h BST"],
        ["29/05 · Pós 18h BST", "📊 AVALIAR",
         "TOTS encerra → mercado estabiliza → analisar resultados e planejar pós-temporada"],
    ]

    t_timing = Table(timing_data, colWidths=[4.5*cm, 4.0*cm, 8.0*cm])
    t_timing.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),  (-1,0),  CINZA_CLARO),
        ("TEXTCOLOR",     (0,0),  (-1,0),  VERDE_EA),
        ("FONTNAME",      (0,0),  (-1,0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0,0),  (-1,-1), 8),
        ("ROWBACKGROUNDS",(0,1),  (-1,-1), [colors.HexColor("#12122A"), colors.HexColor("#1A1A30")]),
        ("TEXTCOLOR",     (0,1),  (-1,-1), BRANCO),
        ("VALIGN",        (0,0),  (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),  (-1,-1), 6),
        ("BOTTOMPADDING", (0,0),  (-1,-1), 6),
        ("LEFTPADDING",   (0,0),  (-1,-1), 6),
        ("BOX",           (0,0),  (-1,-1), 1, VERDE_ESCURO),
        ("INNERGRID",     (0,0),  (-1,-1), 0.4, CINZA_CLARO),
        ("LINEBELOW",     (0,0),  (-1,0),  1.5, VERDE_EA),
    ]))
    story.append(t_timing)
    story.append(Spacer(1, 0.4*cm))

    # ── Caixas de estratégia ───────────────────────────────────────────────────
    story.append(caixa_info("📦 Estratégia SBC Fodder Flipping (85-87 Rated)",
        [
            "→ Compre cartas 85-87 rated no crash de hoje/amanhã (piso de mercado).",
            "→ Foque nos jogadores mais baratos de cada rating (Dias 86 a 950c, Williamson 87 a 1.300c).",
            "→ Aloque até 25.000c aqui: compre ~15 cartas 85 rated + ~8 cartas 86 rated + ~4 cartas 87 rated.",
            "→ Venda em lotes antes das 18h BST do dia 29/05 (rush final de SBCs).",
            "→ Retorno esperado: 500c-940c por carta após taxa → +7.000c a +12.000c no total.",
        ]))
    story.append(Spacer(1, 0.2*cm))

    story.append(caixa_info("🧬 Estratégia Evolution Investing (Raheem Sterling)",
        [
            "→ Procure Raheem Sterling 78 OVR no mercado abaixo de 1.200c.",
            "→ Sterling Ascension EVO eleva o card para ~90 OVR — procura dispara após o EVO.",
            "→ Compre hoje para estar posicionado antes do rush de jogadores querendo a evolução.",
            "→ Risco: se Sterling não for meta, o preço pode não subir tanto. Budget máximo: 3.000c.",
            "→ Potencial de retorno: 5x-8x o investimento se o card virar meta.",
        ], cor_titulo=LARANJA))
    story.append(Spacer(1, 0.2*cm))

    story.append(caixa_info("🔵 Estratégia Thursday Flipping (28/05)",
        [
            "→ Reservar ~12.000c para o Thursday Flip de 28/05 (Division Rivals rewards).",
            "→ Alvo: Bruno Fernandes 89 OVR (Meta CDM/CAM) e Virgil van Dijk 89 OVR.",
            "→ Comprar entre 8h-12h UTC quando o mercado estiver saturado de rewards abertos.",
            "→ Vender entre 16h-21h UTC quando a demanda de Weekend League aquece.",
            "→ Margem líquida esperada: +1.675c (Bruno) e +2.125c (VVD) por carta.",
        ], cor_titulo=AZUL_CLARO))
    story.append(Spacer(1, 0.3*cm))

    # ── 4. ESTIMATIVA DE RETORNO ───────────────────────────────────────────────
    story.append(Paragraph("4. ESTIMATIVA DE RETORNO EM 48H", secao))
    story.append(hr())

    retorno_data = [
        ["Estratégia", "Coins\nInvestidos", "Retorno\nConservador", "Retorno\nOtimista", "Lucro\nConservador", "Lucro\nOtimista"],
        ["SBC Fodder 85-87 rated\n(~27 cartas)", "25.000c", "32.000c", "38.500c", "+7.000c", "+13.500c"],
        ["Evolution Invest\n(Raheem Sterling x2)", "2.400c", "10.000c", "16.000c", "+7.600c", "+13.600c"],
        ["Thursday Flip\n(Bruno F. + VVD + Pedri)", "12.500c", "16.800c", "21.300c", "+4.300c", "+8.800c"],
        ["TOTAL (Budget: 39.900c)", "39.900c", "58.800c", "75.800c", "+18.900c", "+35.900c"],
    ]

    t_retorno = Table(retorno_data, colWidths=[4.5*cm, 2.2*cm, 2.5*cm, 2.5*cm, 2.3*cm, 2.3*cm])
    t_retorno.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),  (-1,0),  CINZA_CLARO),
        ("TEXTCOLOR",     (0,0),  (-1,0),  VERDE_EA),
        ("FONTNAME",      (0,0),  (-1,0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0,0),  (-1,-1), 8),
        ("ROWBACKGROUNDS",(0,1),  (-1,-2), [colors.HexColor("#12122A"), colors.HexColor("#1A1A30")]),
        ("BACKGROUND",    (0,-1), (-1,-1), VERDE_ESCURO),
        ("TEXTCOLOR",     (0,1),  (-1,-1), BRANCO),
        ("TEXTCOLOR",     (0,-1), (-1,-1), VERDE_EA),
        ("FONTNAME",      (0,-1), (-1,-1), "Helvetica-Bold"),
        ("ALIGN",         (1,0),  (-1,-1), "CENTER"),
        ("VALIGN",        (0,0),  (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),  (-1,-1), 6),
        ("BOTTOMPADDING", (0,0),  (-1,-1), 6),
        ("LEFTPADDING",   (0,0),  (-1,-1), 6),
        ("BOX",           (0,0),  (-1,-1), 1, VERDE_EA),
        ("INNERGRID",     (0,0),  (-1,-1), 0.4, CINZA_CLARO),
        ("LINEBELOW",     (0,0),  (-1,0),  1.5, VERDE_EA),
        ("LINEABOVE",     (0,-1), (-1,-1), 1.5, VERDE_EA),
        # Lucros em verde
        ("TEXTCOLOR",     (4,1),  (5,-2), VERDE_EA),
        ("FONTNAME",      (4,1),  (5,-1), "Helvetica-Bold"),
    ]))
    story.append(t_retorno)
    story.append(Spacer(1, 0.3*cm))

    # Notas
    story.append(Paragraph(
        "⚠️ <b>Cenário Conservador:</b> Supõe que apenas 70% das cartas são vendidas ao preço alvo, "
        "restante com desconto de 20%. EVO não valoriza mais de 7x.",
        nota))
    story.append(Paragraph(
        "🚀 <b>Cenário Otimista:</b> Todas as cartas vendidas ao preço alvo ou acima durante o rush "
        "do último dia TOTS (29/05). EVO valoriza 10x+.",
        nota))
    story.append(Paragraph(
        f"📊 <b>Crescimento do Capital:</b> De 40.000c para ~58.800c-75.800c em 48h "
        "(+47% a +90% de retorno). Meta de 48h bem acima da média de mercado.",
        destaque))
    story.append(Spacer(1, 0.3*cm))

    # ── 5. 8 REGRAS DE OURO ───────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("5. AS 8 REGRAS DE OURO DO TRADE", secao))
    story.append(hr())

    regras = [
        ("01", "NUNCA COMPRE NO TOPO",
         "Cartas acabaram de subir? Aguarde. O mercado do FUT é cíclico — o que subiu, cai. "
         "Comprar no topo é o erro número um do trader iniciante. Use o ciclo a seu favor."),
        ("02", "TAXA DE 5%: SEMPRE CALCULE ANTES",
         "Toda venda cobra 5% da EA. Se você comprar por 950c e vender por 1.000c, "
         "recebe apenas 950c — prejuízo. Fórmula: Preço de Venda × 0.95 − Preço de Compra = Lucro Real."),
        ("03", "DIVERSIFIQUE O PORTFÓLIO",
         "Não coloque tudo em uma carta. Distribua o budget em diferentes ratings e estratégias "
         "(fodder, evo, thursday flip). Se uma trade falhar, as outras compensam."),
        ("04", "DEFINA STOP-LOSS",
         "Se uma carta cair 20% abaixo do preço de compra e não houver SBCs novos à vista, "
         "venda e aceite o prejuízo. Preservar capital é mais importante do que recuperar uma trade ruim."),
        ("05", "MONITORE O CALENDÁRIO FUT",
         "Cada SBC novo gera demanda imediata de fodder. Cada promo nova gera crash de preços. "
         "Conhecer as datas de eventos é a principal vantagem do trader informado."),
        ("06", "VENDA ANTES DO PRAZO FINAL",
         "Evite vender na última hora de um evento. O mercado fica imprevisível. "
         "Venda de 2 a 4 horas antes do encerramento quando a demanda ainda está ativa e o pânico não chegou."),
        ("07", "PACIÊNCIA É LUCRO",
         "O Thursday Flip funciona porque os impacientes vendem barato na manhã e os pacientes "
         "vendem caro à tarde. Aguarde 4-6 horas após o pico de oferta para vender no pico de demanda."),
        ("08", "REINVISTA OS LUCROS GRADUALMENTE",
         "A cada trade lucrativa, reinvista 80% do lucro e guarde 20% como reserva. "
         "Crescimento exponencial requer consistência, não apostas altas. Proteja o capital base."),
    ]

    for num, titulo_r, texto_r in regras:
        bloco = [
            Paragraph(f"Regra #{num} — {titulo_r}", regra_num),
            Paragraph(texto_r, regra_txt),
        ]
        story.append(KeepTogether(bloco))

    story.append(Spacer(1, 0.3*cm))
    story.append(hr())

    # ── DISCLAIMER ────────────────────────────────────────────────────────────
    story.append(Paragraph("⚠️ DISCLAIMER", estilo("disc_t", fontSize=11, textColor=VERMELHO,
                             fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=6)))
    story.append(Paragraph(
        "Este relatório foi gerado por um sistema automatizado de análise de mercado para fins "
        "exclusivamente educativos e informativos. As estratégias e preços apresentados são baseados "
        "em dados históricos, tendências observadas e fontes públicas disponíveis no momento da geração "
        "(25/05/2026 20:07 UTC). <b>Preços no mercado FUT flutuam constantemente</b> e podem diferir "
        "dos valores indicados no momento da leitura deste documento.",
        nota))
    story.append(Paragraph(
        "O trading em EA FC 26 Ultimate Team envolve risco de perda de coins. Não há garantia de lucro. "
        "O autor/sistema não se responsabiliza por perdas decorrentes do uso destas informações. "
        "<b>Verifique sempre os preços em tempo real no FUTBIN ou FUT.GG antes de executar qualquer trade.</b> "
        "Nunca invista coins que não possa se dar ao luxo de perder.",
        nota))
    story.append(Spacer(1, 0.2*cm))
    story.append(hr(colors.grey))
    story.append(Paragraph(
        "Fontes consultadas: FUTBIN.com · FUT.GG · TeamGullit.com · FUTMind.com · RealSport101.com · "
        "OperationSports.com · EA SPORTS Official (ea.com) · ItemD2R.com · MMOPIXEL.com",
        rodape_st))
    story.append(Paragraph(
        f"Relatório gerado em {DATA_HORA} UTC · EA FC 26 Ultimate Team Trading Report · v1.0",
        rodape_st))

    # ── GERAR PDF ──────────────────────────────────────────────────────────────
    doc.build(story, onFirstPage=fundo_pagina, onLaterPages=fundo_pagina)
    print(f"✅ PDF gerado com sucesso: {NOME_ARQUIVO}")

if __name__ == "__main__":
    build_pdf()
