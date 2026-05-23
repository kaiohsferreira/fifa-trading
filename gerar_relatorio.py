#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

FILENAME = "relatorio-trading-2026-05-23-14h.pdf"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), FILENAME)

# ── Paleta de cores ──────────────────────────────────────────────────────────
VERDE_ESCURO  = colors.HexColor("#1B5E20")
VERDE_MEDIO   = colors.HexColor("#2E7D32")
VERDE_CLARO   = colors.HexColor("#4CAF50")
VERDE_FUNDO   = colors.HexColor("#E8F5E9")
AMARELO       = colors.HexColor("#F9A825")
LARANJA       = colors.HexColor("#E65100")
CINZA_ESCURO  = colors.HexColor("#212121")
CINZA_MEDIO   = colors.HexColor("#424242")
CINZA_CLARO   = colors.HexColor("#F5F5F5")
BRANCO        = colors.white

def build_styles():
    base = getSampleStyleSheet()

    titulo_principal = ParagraphStyle(
        "TituloPrincipal",
        parent=base["Title"],
        fontSize=22,
        textColor=BRANCO,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        spaceAfter=4,
    )
    subtitulo = ParagraphStyle(
        "Subtitulo",
        parent=base["Normal"],
        fontSize=11,
        textColor=BRANCO,
        alignment=TA_CENTER,
        fontName="Helvetica",
    )
    secao = ParagraphStyle(
        "Secao",
        parent=base["Heading2"],
        fontSize=13,
        textColor=VERDE_ESCURO,
        fontName="Helvetica-Bold",
        spaceBefore=14,
        spaceAfter=6,
        borderPad=4,
    )
    corpo = ParagraphStyle(
        "Corpo",
        parent=base["Normal"],
        fontSize=9.5,
        textColor=CINZA_ESCURO,
        fontName="Helvetica",
        spaceAfter=5,
        leading=14,
        alignment=TA_JUSTIFY,
    )
    corpo_bold = ParagraphStyle(
        "CorpoBold",
        parent=corpo,
        fontName="Helvetica-Bold",
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=corpo,
        leftIndent=14,
        spaceAfter=3,
    )
    disclaimer = ParagraphStyle(
        "Disclaimer",
        parent=base["Normal"],
        fontSize=8,
        textColor=colors.HexColor("#757575"),
        fontName="Helvetica-Oblique",
        alignment=TA_JUSTIFY,
        leading=11,
    )
    return {
        "titulo_principal": titulo_principal,
        "subtitulo": subtitulo,
        "secao": secao,
        "corpo": corpo,
        "corpo_bold": corpo_bold,
        "bullet": bullet,
        "disclaimer": disclaimer,
    }


def header_block(styles):
    """Bloco de cabeçalho com fundo verde."""
    data = [
        [Paragraph("⚽  RELATÓRIO DE TRADING  ⚽", styles["titulo_principal"])],
        [Paragraph("EA FC 26 · Ultimate Team · Análise de Mercado", styles["subtitulo"])],
        [Paragraph("23/05/2026  14:02 UTC", styles["subtitulo"])],
    ]
    t = Table(data, colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), VERDE_ESCURO),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("RIGHTPADDING",  (0,0), (-1,-1), 12),
        ("ROUNDEDCORNERS", [8]),
    ]))
    return t


def info_box(label, value, styles, bg=VERDE_FUNDO, label_color=VERDE_ESCURO):
    data = [[Paragraph(f"<b>{label}</b>", ParagraphStyle("lbl", parent=styles["corpo"], textColor=label_color)),
             Paragraph(value, styles["corpo"])]]
    t = Table(data, colWidths=[5*cm, 12*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("BOX",           (0,0), (-1,-1), 0.5, VERDE_CLARO),
    ]))
    return t


def build_cards_table(styles):
    header = [
        Paragraph("<b>Jogador</b>", ParagraphStyle("th", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER)),
        Paragraph("<b>OVR</b>",     ParagraphStyle("th", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER)),
        Paragraph("<b>Clube</b>",   ParagraphStyle("th", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER)),
        Paragraph("<b>Compra\n(max)</b>", ParagraphStyle("th", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER)),
        Paragraph("<b>Venda\n(alvo)</b>", ParagraphStyle("th", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER)),
        Paragraph("<b>Margem\nLíquida*</b>", ParagraphStyle("th", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER)),
        Paragraph("<b>ROI</b>",     ParagraphStyle("th", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER)),
        Paragraph("<b>Estratégia</b>", ParagraphStyle("th", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER)),
    ]

    cstyle = ParagraphStyle("cell", parent=styles["corpo"], fontSize=8.5, alignment=TA_CENTER)
    cstyle_l = ParagraphStyle("celll", parent=styles["corpo"], fontSize=8.5, alignment=TA_LEFT)

    rows = [
        # Jogador, OVR, Clube, Compra, Venda, Margem, ROI%, Estratégia
        ("R. Gravenberch", "85", "Liverpool", "950",  "1.250",  "+238",  "25%", "SBC Fodder"),
        ("P. Schick",      "85", "B. Leverkusen", "1.000", "1.350", "+283", "28%", "SBC Fodder"),
        ("Iñigo Martínez", "85", "Barcelona", "1.000", "1.300", "+235", "24%", "SBC Fodder"),
        ("Alexander-Arnold","86","Liverpool", "1.100", "1.500", "+325", "30%", "SBC Fodder"),
        ("H. Çalhanoğlu",  "86", "Inter Milan", "1.050", "1.450", "+328", "31%", "SBC Fodder"),
        ("S. Tonali",      "86", "Newcastle", "1.150", "1.650", "+418", "36%", "SBC Fodder"),
        ("V. Osimhen",     "87", "Napoli",    "1.450", "2.000", "+450", "31%", "SBC Fodder"),
        ("J. Sommer",      "87", "Inter Milan","1.400","1.950", "+453", "32%", "SBC Fodder"),
        ("R. Lewandowski", "88", "Barcelona", "8.500","11.000","1.950","23%", "SBC Fodder"),
        ("B. Saka RTTF",   "91", "Arsenal",   "5.000","7.500","2.125","43%", "RTTF Final"),
        ("O. Dembele RTTF","91", "PSG",       "4.800","7.200","2.040","43%", "RTTF Final"),
    ]

    def make_row(r, bg):
        return [
            Paragraph(r[0], cstyle_l),
            Paragraph(r[1], cstyle),
            Paragraph(r[2], cstyle_l),
            Paragraph(r[3], cstyle),
            Paragraph(r[4], cstyle),
            Paragraph(f"<b>{r[5]}</b>", ParagraphStyle("mg", parent=cstyle, textColor=VERDE_MEDIO, fontName="Helvetica-Bold")),
            Paragraph(f"<b>{r[6]}</b>", ParagraphStyle("roi", parent=cstyle, textColor=VERDE_ESCURO, fontName="Helvetica-Bold")),
            Paragraph(r[7], cstyle),
        ]

    table_data = [header] + [make_row(r, CINZA_CLARO if i%2==0 else BRANCO) for i, r in enumerate(rows)]

    col_w = [3.8*cm, 1.3*cm, 3.0*cm, 1.8*cm, 1.8*cm, 1.9*cm, 1.3*cm, 2.1*cm]
    t = Table(table_data, colWidths=col_w, repeatRows=1)

    style = TableStyle([
        # Header
        ("BACKGROUND",    (0,0), (-1,0), VERDE_ESCURO),
        ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
        ("ALIGN",         (0,0), (-1,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 8.5),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 4),
        ("RIGHTPADDING",  (0,0), (-1,-1), 4),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#BDBDBD")),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [CINZA_CLARO, BRANCO]),
        # Destacar linhas RTTF
        ("BACKGROUND",    (0,9), (-1,10), colors.HexColor("#FFF8E1")),
        ("TEXTCOLOR",     (6,9), (6,10), LARANJA),
    ])
    t.setStyle(style)
    return t


def build_pdf():
    styles = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=1.5*cm, bottomMargin=1.5*cm,
        title="Relatório Trading EA FC 26 – 23/05/2026",
        author="Agente de Trading EA FC 26",
    )

    story = []

    # ── CABEÇALHO ─────────────────────────────────────────────────────────────
    story.append(header_block(styles))
    story.append(Spacer(1, 0.5*cm))

    # ── DADOS RÁPIDOS ────────────────────────────────────────────────────────
    story.append(info_box("Budget disponível", "40.000 coins", styles))
    story.append(Spacer(1, 2))
    story.append(info_box("Janela de análise", "23/05/2026 (sábado) → 25/05/2026 (segunda)", styles))
    story.append(Spacer(1, 2))
    story.append(info_box("Próximo evento-chave", "UCL Final: PSG × Arsenal – 30/05/2026 (Puskás Aréna, Budapest)", styles, bg=colors.HexColor("#FFF8E1"), label_color=LARANJA))
    story.append(Spacer(1, 0.4*cm))

    # ── 1. CONTEXTO DO MERCADO ───────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1.5, color=VERDE_CLARO))
    story.append(Paragraph("1. Contexto do Mercado", styles["secao"]))
    story.append(Paragraph(
        "<b>Evento dominante: Team of the Season (TOTS)</b> — 17/04 a 12/06/2026. "
        "O Ultimate TOTS foi lançado em 22/05/2026 (ontem), inundando o mercado "
        "com pacotes premium e derrubando preços de cartas meta nas últimas 24h. "
        "Este é o melhor momento para comprar fodder barato, pois a oferta está "
        "alta e a demanda de SBCs está crescendo exponencialmente.",
        styles["corpo"]
    ))
    story.append(Paragraph(
        "<b>Fantasy FC</b> termina em 29/05/2026 — SBCs dessas cartas ainda ativas, "
        "mantendo demanda por fodder 85–87 elevada. "
        "<b>UEFA RTTF</b> encerra em 30/05/2026 (dia da Final da UCL PSG × Arsenal). "
        "Cartas RTTF de finalistas já estão no upgrade máximo de semifinalista e "
        "receberão o upgrade de <i>Finalista</i>, tornando-as extremamente valiosas.",
        styles["corpo"]
    ))

    story.append(Paragraph("<b>Tendências de preço observadas:</b>", styles["corpo_bold"]))
    for b in [
        "📉 Cartas 85–88 rated caíram 10–15% nas últimas 24h pós-Ultimate TOTS → janela de compra aberta",
        "📈 Demanda por SBC fodder deve subir quinta-feira (28/05) após rewards de Division Rivals",
        "🔥 RTTF de PSG e Arsenal já precificados como finalistas, mas upgrade de campeão (30/05) pode disparar preços mais 30–50%",
        "⚠️ Mercado fecha o ciclo do TOTS em 12/06 — sell window ideal: 28–31/05",
    ]:
        story.append(Paragraph(f"• {b}", styles["bullet"]))

    story.append(Spacer(1, 0.3*cm))

    # ── 2. TABELA DE OPORTUNIDADES ───────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1.5, color=VERDE_CLARO))
    story.append(Paragraph("2. Oportunidades de Compra Recomendadas", styles["secao"]))
    story.append(Paragraph(
        "Todas as margens líquidas já descontam a taxa de 5% da EA na venda. "
        "Preços em coins baseados nos dados de mercado de 23/05/2026. "
        "Linhas em amarelo = cartas RTTF (maior risco, maior retorno).",
        styles["corpo"]
    ))
    story.append(Spacer(1, 0.2*cm))
    story.append(build_cards_table(styles))
    story.append(Paragraph(
        "* Margem líquida = (Preço de venda × 0,95) − Preço de compra  |  "
        "Preços sujeitos a variação — consulte FUTBIN/FUT.GG antes de cada operação.",
        styles["disclaimer"]
    ))

    # ── 3. ESTRATÉGIA DE TIMING ──────────────────────────────────────────────
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width="100%", thickness=1.5, color=VERDE_CLARO))
    story.append(Paragraph("3. Estratégia de Timing", styles["secao"]))

    timing_data = [
        [Paragraph("<b>Quando</b>", ParagraphStyle("th2", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
         Paragraph("<b>Ação</b>",   ParagraphStyle("th2", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
         Paragraph("<b>Motivo</b>", ParagraphStyle("th2", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER))],
        ["Sáb 23/05 – hoje (14h–20h UTC)", "COMPRAR fodder 85–87", "Pós-lançamento TOTS: oferta máxima, preços no fundo"],
        ["Dom 24/05 – manhã",              "COMPRAR complementar", "Preços ainda baixos antes da recuperação semanal"],
        ["Seg–Qua 26–28/05",               "SEGURAR / monitorar",  "Mercado começa a absorver o choque; preços sobem gradualmente"],
        ["Qui 28/05 – 17h–20h UTC",        "SEGUNDA COMPRA (flash dip)", "Rewards Division Rivals → novo dip temporário de 2–3h"],
        ["Sex 29/05 – 08h–14h UTC",        "VENDER fodder SBC",    "Pico de demanda antes do Fantasy FC encerrar (29/05)"],
        ["Sáb 30/05 – pré-jogo (12h–17h)", "VENDER RTTF finalistas","Máximo de hype pré-Final UCL PSG × Arsenal"],
        ["Sáb 30/05 – pós-jogo (22h+)",   "ATENÇÃO: upgrade campeão", "Cartas do vencedor sobem 30–50%; perdedor despenca"],
    ]

    ts_col_w = [4.2*cm, 4.5*cm, 8.3*cm]
    ts_table = Table(timing_data, colWidths=ts_col_w, repeatRows=1)
    ts_table.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), VERDE_MEDIO),
        ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
        ("FONTSIZE",      (0,0), (-1,-1), 8.5),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("RIGHTPADDING",  (0,0), (-1,-1), 6),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#BDBDBD")),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [CINZA_CLARO, BRANCO]),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        # destaque linha pós-jogo
        ("BACKGROUND",    (0,7), (-1,7), colors.HexColor("#FFF8E1")),
        ("FONTNAME",      (0,7), (0,7), "Helvetica-Bold"),
    ]))
    story.append(ts_table)

    # ── 4. ESTIMATIVA DE RETORNO EM 48H ──────────────────────────────────────
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width="100%", thickness=1.5, color=VERDE_CLARO))
    story.append(Paragraph("4. Estimativa de Retorno em 48h", styles["secao"]))

    ret_data = [
        [Paragraph("<b>Alocação sugerida</b>", ParagraphStyle("th3", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
         Paragraph("<b>Investimento</b>",      ParagraphStyle("th3", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
         Paragraph("<b>Cenário Conservador</b>",ParagraphStyle("th3", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER)),
         Paragraph("<b>Cenário Otimista</b>",  ParagraphStyle("th3", parent=styles["corpo"], textColor=BRANCO, fontName="Helvetica-Bold", alignment=TA_CENTER))],
        ["Fodder 85–87 (×20 cartas)",  "≈ 22.000",  "+4.500–5.500",  "+7.000–8.500"],
        ["Fodder 88 Lewandowski (×1)", "≈ 8.500",   "+1.500–1.950",  "+2.500–3.000"],
        ["RTTF Arsenal/PSG (×2)",      "≈ 9.800",   "+3.000–4.000",  "+5.000–7.000"],
        ["RESERVA (liquidez)",         "≈ 700",      "—",             "—"],
        [Paragraph("<b>TOTAL</b>", ParagraphStyle("tot", parent=styles["corpo"], fontName="Helvetica-Bold", alignment=TA_CENTER)),
         Paragraph("<b>40.000</b>", ParagraphStyle("tot", parent=styles["corpo"], fontName="Helvetica-Bold", alignment=TA_CENTER)),
         Paragraph("<b>+9.000 – 11.450</b>", ParagraphStyle("tot", parent=styles["corpo"], fontName="Helvetica-Bold", textColor=VERDE_MEDIO, alignment=TA_CENTER)),
         Paragraph("<b>+14.500 – 18.500</b>", ParagraphStyle("tot", parent=styles["corpo"], fontName="Helvetica-Bold", textColor=VERDE_ESCURO, alignment=TA_CENTER))],
    ]

    ret_col_w = [4.5*cm, 3.0*cm, 4.5*cm, 5.0*cm]
    ret_table = Table(ret_data, colWidths=ret_col_w, repeatRows=1)
    ret_table.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), VERDE_MEDIO),
        ("TEXTCOLOR",     (0,0), (-1,0), BRANCO),
        ("FONTSIZE",      (0,0), (-1,-1), 8.5),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("RIGHTPADDING",  (0,0), (-1,-1), 6),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#BDBDBD")),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [CINZA_CLARO, BRANCO]),
        ("BACKGROUND",    (0,5), (-1,5), VERDE_FUNDO),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ]))
    story.append(ret_table)
    story.append(Paragraph(
        "Cenário conservador: spread de 20–25% | Cenário otimista: spread de 35–45% + upgrade RTTF campeão. "
        "Capital de reserva garante liquidez para oportunidades de snipe.",
        styles["disclaimer"]
    ))

    # ── 5. 8 REGRAS DE OURO ──────────────────────────────────────────────────
    story.append(Spacer(1, 0.3*cm))
    story.append(HRFlowable(width="100%", thickness=1.5, color=VERDE_CLARO))
    story.append(Paragraph("5. As 8 Regras de Ouro do Trade", styles["secao"]))

    regras = [
        ("1", "Nunca invista mais de 70% do budget em uma única estratégia",
         "Diversificação protege contra crashes inesperados de mercado."),
        ("2", "Sempre verifique o preço atual no FUTBIN/FUT.GG antes de comprar",
         "Preços mudam em minutos durante promos ativas. Este relatório é ponto de partida, não verdade absoluta."),
        ("3", "Respeite a taxa de 5% da EA em todos os cálculos",
         "Margem bruta ≠ lucro real. Sempre calcule: (Venda × 0,95) − Compra."),
        ("4", "Compre na quinta após os rewards de Division Rivals (17h–20h UTC)",
         "O dip dura 2–4 horas. Aja rápido, venda no dia seguinte."),
        ("5", "Nunca segure RTTF de times eliminados",
         "Cartas de times eliminados caem 40–80% em questão de horas após a derrota."),
        ("6", "Venda 1–2h antes do pico, não durante",
         "Quando todos estão vendendo, o preço já caiu. Antecipe a onda."),
        ("7", "Limite ordens de venda a 5% abaixo do preço médio listado",
         "Facilita a venda rápida sem prejudicar o mercado geral."),
        ("8", "Mantenha sempre 5–10% do budget em reserva para oportunidades de snipe",
         "As melhores oportunidades aparecem sem aviso. Liquidez é poder."),
    ]

    for num, titulo, desc in regras:
        regra_data = [[
            Paragraph(f"<b>{num}</b>",
                      ParagraphStyle("rnum", parent=styles["corpo"], textColor=BRANCO,
                                     fontName="Helvetica-Bold", fontSize=13, alignment=TA_CENTER)),
            Paragraph(f"<b>{titulo}</b><br/><font size=8 color='#424242'>{desc}</font>",
                      ParagraphStyle("rdesc", parent=styles["corpo"], fontSize=9))
        ]]
        rt = Table(regra_data, colWidths=[1.0*cm, 16*cm])
        rt.setStyle(TableStyle([
            ("BACKGROUND",    (0,0), (0,0), VERDE_CLARO),
            ("BACKGROUND",    (1,0), (1,0), VERDE_FUNDO),
            ("TOPPADDING",    (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("LEFTPADDING",   (0,0), (-1,-1), 6),
            ("RIGHTPADDING",  (0,0), (-1,-1), 6),
            ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
            ("BOX",           (0,0), (-1,-1), 0.5, VERDE_CLARO),
        ]))
        story.append(rt)
        story.append(Spacer(1, 3))

    # ── DISCLAIMER ────────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.4*cm))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#BDBDBD")))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "<b>DISCLAIMER:</b> Este relatório tem caráter exclusivamente informativo e educacional. "
        "Preços do mercado de EA FC 26 Ultimate Team são altamente voláteis e podem mudar em minutos. "
        "As estimativas de retorno são baseadas em dados históricos de mercado e análise de tendências, "
        "não constituindo garantia de lucro. Antes de executar qualquer operação, verifique os preços "
        "atuais em FUTBIN (futbin.com) ou FUT.GG (fut.gg). O autor não se responsabiliza por perdas "
        "decorrentes de decisões baseadas neste documento. Trade com responsabilidade.",
        styles["disclaimer"]
    ))
    story.append(Spacer(1, 0.15*cm))
    story.append(Paragraph(
        "Gerado automaticamente por Agente de Trading EA FC 26  |  23/05/2026 14:02 UTC  |  "
        "Fontes: futbin.com · fut.gg · teamgullit.com · football-talk.co.uk · espn.com · uefa.com",
        styles["disclaimer"]
    ))

    doc.build(story)
    print(f"PDF gerado: {OUTPUT_PATH}")
    return OUTPUT_PATH


if __name__ == "__main__":
    build_pdf()
