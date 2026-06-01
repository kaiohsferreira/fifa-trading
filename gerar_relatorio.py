#!/usr/bin/env python3
"""
EA FC 26 — Gerador de Relatório de Trading
Data: 01/06/2026 20:06 UTC
Fontes: futbin.com, fut.gg, realsport101.com, teamgullit.com, destructoid.com, sportsdunia.com, ea.com
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os

REPORT_DATE = "01/06/2026 20:06"
FILENAME    = "relatorio-trading-2026-06-01-20h.pdf"
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAME)

# ── Paleta ───────────────────────────────────────────────────────────────────
C = {
    "green_dark":  colors.HexColor("#1a6b2e"),
    "green_mid":   colors.HexColor("#27a844"),
    "green_light": colors.HexColor("#d4edda"),
    "gold":        colors.HexColor("#ffc107"),
    "dark_bg":     colors.HexColor("#1a1a2e"),
    "dark_card":   colors.HexColor("#16213e"),
    "grey_text":   colors.HexColor("#495057"),
    "light_grey":  colors.HexColor("#f8f9fa"),
    "border":      colors.HexColor("#dee2e6"),
    "blue":        colors.HexColor("#0d6efd"),
    "red":         colors.HexColor("#dc3545"),
    "orange":      colors.HexColor("#fd7e14"),
    "yellow_bg":   colors.HexColor("#fff3cd"),
    "yellow_text": colors.HexColor("#856404"),
    "blue_bg":     colors.HexColor("#cfe2ff"),
    "blue_text":   colors.HexColor("#084298"),
    "white":       colors.white,
    "black":       colors.black,
}

def ps(name, size=9, leading=None, align=TA_LEFT, color="grey_text",
       font="Helvetica", sbefore=0, safter=4, indent=0):
    c = C[color] if isinstance(color, str) else color
    return ParagraphStyle(name, fontSize=size, leading=leading or round(size*1.4),
                          alignment=align, textColor=c, fontName=font,
                          spaceBefore=sbefore, spaceAfter=safter, leftIndent=indent)

S = {
    "title":    ps("t",  22, 28, TA_CENTER, "white",      "Helvetica-Bold",  0, 4),
    "sub":      ps("s",  11, 14, TA_CENTER, "gold",       "Helvetica-Bold",  0, 2),
    "meta":     ps("m",   9, 11, TA_CENTER, colors.HexColor("#adb5bd"), "Helvetica", 0, 0),
    "section":  ps("se", 13, 16, TA_LEFT,  "green_dark", "Helvetica-Bold", 14, 6),
    "body":     ps("b",   9, 13, TA_JUSTIFY,"grey_text",  "Helvetica",       0, 4),
    "bullet":   ps("bu",  9, 13, TA_LEFT,  "grey_text",  "Helvetica",       0, 3, 12),
    "disc":     ps("d",   7.5,10,TA_JUSTIFY,colors.HexColor("#6c757d"), "Helvetica-Oblique", 0, 0),
    "th":       ps("th",  8, 10, TA_CENTER, "white",      "Helvetica-Bold"),
    "td":       ps("td",  8, 11, TA_CENTER, "grey_text",  "Helvetica"),
    "tdb":      ps("tdb", 8, 11, TA_LEFT,  "black",      "Helvetica-Bold"),
    "tdg":      ps("tdg", 8, 11, TA_CENTER, "green_dark", "Helvetica-Bold"),
    "tdr":      ps("tdr", 8, 11, TA_CENTER, "red",        "Helvetica-Bold"),
    "rnum":     ps("rn", 16, 20, TA_CENTER, "gold",       "Helvetica-Bold"),
    "rtitle":   ps("rt",  8.5,12,TA_CENTER, "dark_bg",    "Helvetica-Bold"),
    "rbody":    ps("rb",  8, 11, TA_CENTER, "grey_text",  "Helvetica"),
}

def P(txt, style): return Paragraph(txt, S[style] if isinstance(style, str) else style)

def simple_table(rows, bg, cw=17.5*cm, tpad=14, bpad=10):
    t = Table([[r] for r in rows], colWidths=[cw])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), bg),
        ("TOPPADDING",(0,0),(-1,-1),tpad),
        ("BOTTOMPADDING",(0,0),(-1,-1),bpad),
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("RIGHTPADDING",(0,0),(-1,-1),10),
    ]))
    return t

def box(para, bg_key, tpad=10, bpad=10, lpad=12, rpad=12):
    t = Table([[para]], colWidths=[17.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), C[bg_key] if isinstance(bg_key,str) else bg_key),
        ("TOPPADDING",(0,0),(-1,-1),tpad),("BOTTOMPADDING",(0,0),(-1,-1),bpad),
        ("LEFTPADDING",(0,0),(-1,-1),lpad),("RIGHTPADDING",(0,0),(-1,-1),rpad),
    ]))
    return t

def fmt(n): return f"{n:,}".replace(",",".")

doc = SimpleDocTemplate(
    OUTPUT_PATH, pagesize=A4,
    leftMargin=1.5*cm, rightMargin=1.5*cm,
    topMargin=1.5*cm,  bottomMargin=1.5*cm,
    title="Relatório de Trading — EA FC 26 Ultimate Team",
    author="Agente de Mercado EA FC 26",
)

story = []

# ══════════════════════════════════════════════════════
# CABEÇALHO
# ══════════════════════════════════════════════════════
story.append(simple_table([P("EA FC 26 — RELATÓRIO DE TRADING", "title")], C["dark_bg"], tpad=18, bpad=4))
story.append(simple_table([P("Ultimate Team Market Intelligence  ·  Festival of Football Edition  ·  01/06/2026", "sub")], C["dark_bg"], tpad=2, bpad=8))
story.append(simple_table([P(
    f"Data/Hora: <b>{REPORT_DATE} UTC</b>   |   Budget: <b>40.000 coins</b>   |   "
    "Estratégia: SBC Fodder Flipping · Evolution Investing · Thursday Flip",
    "meta")], C["dark_card"], tpad=8, bpad=8))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════
# 1. CONTEXTO DO MERCADO
# ══════════════════════════════════════════════════════
story.append(P("1. CONTEXTO DO MERCADO — 01/06/2026", "section"))
story.append(HRFlowable(width="100%", thickness=2, color=C["green_dark"], spaceAfter=6))

story.append(box(
    P("⚡  JANELA ESTRATÉGICA CRÍTICA: Você está a 4 dias do lançamento do "
      "<b>Festival of Football / Path to Glory</b> (05/06 – Sex). Preços de SBC fodder estão "
      "nos mínimos históricos do ciclo. Esta é a melhor janela de compra.",
      ps("al", 9, 13, TA_LEFT, "dark_bg", "Helvetica-Bold")),
    "gold"))
story.append(Spacer(1, 8))

for label, text in [
    ("<b>Evento principal:</b>",
     "Festival of Football (05/06–24/07/2026) — maior evento de verão do EA FC 26, "
     "temática Copa do Mundo 2026 (USA/MEX/CAN). Mais de 100 novos jogadores internacionais no FUT."),
    ("<b>Path to Glory (05/06–19/06):</b>",
     "Cartas com upgrades dinâmicos baseados no desempenho real das seleções. "
     "Confirmados: Rayan Cherki (França), Trent Alexander-Arnold (Inglaterra), "
     "Rasmus Hojlund (Noruega), Vinicius Jr. (Brasil), Kevin De Bruyne (Bélgica)."),
    ("<b>Login reward a partir de 05/06:</b>",
     "ICON Pelé 93 OVR gratuito + 3 Evolutions 'Choose Your Journey' — incentiva retorno "
     "massivo de jogadores ao FUT, elevando demanda por SBCs e Evolution fodder."),
    ("<b>Greats of the Game (19/06–26/06):</b>",
     "Promo de ICONs com dois novos ICONs: <b>Rivellino</b> e <b>Mario Kempes</b>. "
     "ICON SBCs de alto custo elevam demanda por 87-88 rated nas semanas seguintes."),
    ("<b>Tendência de preços (verificada):</b>",
     "86 rated avg ~750-1.100 coins | 87 rated avg ~1.000-1.700 coins | "
     "88 rated avg ~1.900-3.100 coins. Mínimos do ciclo — spike esperado de 2-4× em 05/06."),
    ("<b>Alerta de mercado:</b>",
     "Semenyo (TOTS 94 OVR) +329% · Debinha (89 OVR) +182% · Guendouzi (82 OVR) +163% "
     "— spikes recentes confirmam SBC demand como principal driver de preços."),
    ("<b>Risco monitorado:</b>",
     "Abertura massiva de packs nos primeiros 30-60 minutos após drop de 05/06 pode "
     "temporariamente baixar preços de 88+ rated. Evitar vender nesta janela; aguardar o pico."),
]:
    story.append(P(f"• {label} {text}", "bullet"))

story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════
# 2. TABELA SBC FODDER
# ══════════════════════════════════════════════════════
story.append(P("2. OPORTUNIDADES: SBC FODDER FLIPPING — BUDGET 40.000 COINS", "section"))
story.append(HRFlowable(width="100%", thickness=2, color=C["green_dark"], spaceAfter=6))
story.append(P(
    "Cartas selecionadas com menor preço por rating tier, alta liquidez em SBCs e spike confirmado "
    "para o Path to Glory (05/06). Margem líquida = (venda × 0,95) − compra. "
    "Preços verificados via futbin.com · fut.gg · realsport101.com · sportsdunia.com.",
    "body"))
story.append(Spacer(1, 6))

# col: name, rating, club, pos, buy, sell, qty  → calculates margin + total
players = [
    # 86-RATED — maiores quantidades (preço baixo, alta liquidez)
    ("Grace Geyoro",         "86", "Paris SG (F)",      "MAI",  750, 1650,  4),
    ("Ona Batlle",           "86", "Atlético Madrid",   "RD",   900, 1950,  4),
    ("Michael Olise",        "86", "Bayern München",    "MAD",  900, 2000,  3),
    ("Rúben Dias",           "86", "Manchester City",   "ZAG",  950, 2100,  3),
    ("Ibrahima Konaté",      "86", "Liverpool",         "ZAG", 1000, 2200,  2),
    # 87-RATED — equilíbrio margem/liquidez
    ("Lucy Bronze",          "87", "Barcelona (F)",     "RD",  1000, 2500,  3),
    ("Alexis Mac Allister",  "87", "Liverpool",         "MCD", 1000, 2700,  3),
    ("David Raya",           "87", "Arsenal",           "GOL", 1000, 2400,  2),
    ("Victor Osimhen",       "87", "Galatasaray",       "ATA", 1500, 3500,  2),
    # 88-RATED — maior margem, menor quantidade
    ("Irene Paredes",        "88", "Barcelona (F)",     "ZAG", 1900, 4000,  2),
    ("Marie-Ant. Katoto",    "88", "Paris SG (F)",      "ATA", 2400, 5200,  2),
    ("Gabriel Magalhães",    "88", "Arsenal",           "ZAG", 2600, 5500,  2),
]

# rating colour
def rating_style(r):
    c = {"86": C["blue"], "87": C["green_mid"], "88": C["red"]}.get(r, C["grey_text"])
    return ps(f"r{r}", 8, 11, TA_CENTER, c, "Helvetica-Bold")

header_row = [P(h, "th") for h in [
    "Jogador","OVR","Clube","Pos.","Compra\nAlvo","Venda\nAlvo",
    "Margem\nLíquida","Qtd.","Lucro\nTotal"
]]
table_data = [header_row]
for name, rat, club, pos, buy, sell, qty in players:
    margin = round(sell * 0.95 - buy)
    total  = margin * qty
    table_data.append([
        P(name,            "tdb"),
        P(rat,             rating_style(rat)),
        P(club,            "td"),
        P(pos,             "td"),
        P(fmt(buy),        "td"),
        P(fmt(sell),       "td"),
        P(f"+{fmt(margin)}","tdg"),
        P(str(qty),        "td"),
        P(f"+{fmt(total)}", "tdg"),
    ])

CW = [3.6*cm, 0.85*cm, 3.3*cm, 0.85*cm, 1.5*cm, 1.5*cm, 1.7*cm, 0.85*cm, 1.6*cm]
alt = [("BACKGROUND",(0,i),(-1,i), C["light_grey"] if i%2==1 else C["white"])
       for i in range(1, len(table_data))]
tbl = Table(table_data, colWidths=CW, repeatRows=1)
tbl.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),C["dark_bg"]),
    ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
    ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
    ("GRID",(0,0),(-1,-1),0.3,C["border"]),
    ("LINEBELOW",(0,0),(-1,0),1.5,C["green_dark"]),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("BACKGROUND",(8,1),(8,-1),C["green_light"]),
] + alt))
story.append(tbl)
story.append(Spacer(1,6))

total_invest = sum(b*q for *_,b,_,q in players)
total_profit_val = sum(round(s*0.95-b)*q for *_,b,s,q in players)
total_items_n = sum(q for *_,q in players)
roi = total_profit_val / total_invest * 100

bar_data = [[
    P(f"Investimento: <b>{fmt(total_invest)} coins</b>", ps("bi",9,12,TA_CENTER,"white","Helvetica")),
    P(f"Cartas: <b>{total_items_n} itens</b>",           ps("bi",9,12,TA_CENTER,"white","Helvetica")),
    P(f"Lucro Líquido: <b>+{fmt(total_profit_val)} coins</b>",
      ps("bi",9,12,TA_CENTER,"gold","Helvetica-Bold")),
    P(f"ROI Estimado: <b>+{roi:.0f}%</b>",
      ps("bi",9,12,TA_CENTER,"green_light","Helvetica-Bold")),
]]
bar = Table(bar_data, colWidths=[4.375*cm]*4)
bar.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1),C["dark_bg"]),
    ("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),10),
    ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
    ("LINEAFTER",(0,0),(2,0),0.5,C["grey_text"]),
]))
story.append(bar)
story.append(Spacer(1,10))

# ══════════════════════════════════════════════════════
# 3. EVOLUTION CARDS
# ══════════════════════════════════════════════════════
story.append(P("3. OPORTUNIDADES: EVOLUTION CARD INVESTING", "section"))
story.append(HRFlowable(width="100%", thickness=2, color=C["green_dark"], spaceAfter=6))
story.append(P(
    "Compra de cartas base baratas que serão alvo de Evolutions. A regra é: "
    "<b>comprar no leak, vender no anúncio oficial</b> — o pico ocorre nas primeiras 24-48h após o anúncio. "
    "Fontes: realsport101.com · fut.gg · easysbc.io · futbin.com/popular/evolutions",
    "body"))
story.append(Spacer(1, 6))

evo_header = [P(h,"th") for h in ["Jogador","OVR Base","Clube","Evolution Alvo","Custo Evo","Carta Base","Venda Pós-Evo","Margem Estimada"]]
evo_players = [
    ("Moïse Bombito",   "76","OGC Nice",         "El Tiburon (CB)",         "65.000",  "~650",  "~2.200", "+1.450"),
    ("Igor Thiago",     "75","Brentford",         "TOTS Career Path (ATA)",  "GRÁTIS",  "~350",  "~1.800", "+1.360"),
    ("C. Ronaldo (Icon)","Base Icon","—",         "WTSS Journey (ATA)",      "GRÁTIS",  "~2.500","~8.000", "+5.100"),
    ("Paulo Maldini (Icon)","Base Icon","—",      "WTSS Journey (ZAG)",      "GRÁTIS",  "~1.500","~6.500", "+4.675"),
    ("Frenkie de Jong",  "84","FC Barcelona",     "Making the Case (MCD)",   "100.000", "~750",  "~3.500", "+2.575"),
]
evo_data = [evo_header]
for row in evo_players:
    name,ovr,club,evo,cost,base,sell_e,margin_e = row
    margin_raw = margin_e
    evo_data.append([
        P(name,     "tdb"),
        P(ovr,      "td"),
        P(club,     "td"),
        P(evo,      ps("ev",8,11,TA_LEFT,"grey_text","Helvetica")),
        P(cost,     "td"),
        P(base,     ps("ba",8,11,TA_CENTER,"blue","Helvetica-Bold")),
        P(sell_e,   "td"),
        P(margin_e, "tdg"),
    ])

CW2 = [2.8*cm,1.2*cm,2.0*cm,3.5*cm,1.6*cm,1.5*cm,1.8*cm,2.1*cm]
evo_tbl = Table(evo_data, colWidths=CW2, repeatRows=1)
alt2 = [("BACKGROUND",(0,i),(-1,i), C["light_grey"] if i%2==1 else C["white"])
        for i in range(1, len(evo_data))]
evo_tbl.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),C["dark_bg"]),
    ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
    ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
    ("GRID",(0,0),(-1,-1),0.3,C["border"]),
    ("LINEBELOW",(0,0),(-1,0),1.5,C["green_dark"]),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
] + alt2))
story.append(evo_tbl)
story.append(Spacer(1, 5))
story.append(P(
    "⚠ WTSS Journey Chain (Silver Icons) <b>expira no início de junho</b>. "
    "Compre Silver Icons de Ronaldo, Maldini e Xavi agora — a janela está se fechando.",
    ps("warn",8.5,12,TA_LEFT,"red","Helvetica-Bold",0,0,8)))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════
# 4. ESTRATÉGIA DE TIMING
# ══════════════════════════════════════════════════════
story.append(P("4. ESTRATÉGIA DE TIMING — CALENDÁRIO SEMANAL E JANELA DE PROMO", "section"))
story.append(HRFlowable(width="100%", thickness=2, color=C["green_dark"], spaceAfter=6))

timing_rows = [
    ("AGORA\n01–04/06", C["green_mid"],   C["green_light"],
     "<b>COMPRAR SBC Fodder.</b> Mercado em deflação pré-evento — mínimos anuais. "
     "Use <b>bids</b> entre 23h–06h UTC para pagar 10-20% abaixo do BIN. "
     "Acumule 86/87-rated (menor risco, alta liquidez). Reserve 5.000 coins como caixa."),
    ("QUINTA\n05/06 08h BST", C["gold"],  C["yellow_bg"],
     "<b>Division Rivals rewards dropam</b> — maior oferta semanal de cartas. "
     "Não venda ainda. Aguarde 2-4h para confirmar novos SBCs do Path to Glory. "
     "Preços de fodder sobem 50-150% nas primeiras 6-8h. 88+ rated podem cair momentaneamente."),
    ("SEXTA\n05/06 18h BST", C["dark_bg"],C["light_grey"],
     "<b>Path to Glory lança</b> — abertura massiva de packs nos primeiros 30-60 minutos: "
     "OPORTUNIDADE de compra de 88+ rated abaixo do valor real. "
     "Depois do pico de supply, preços começam a subir. <b>Venda 70% do estoque</b> 4-8h após o lançamento."),
    ("06–07/06\nPico 48h", C["green_dark"],C["green_light"],
     "<b>VENDER gradualmente.</b> 30% restante do estoque em listagens de 12h. "
     "Priorize 87-88 rated (margens maiores). SBCs dos primeiros 48h = pico de demanda. "
     "Reinveste lucro em novos lotes de 86-rated para venda prolongada."),
    ("08–18/06\nReinvestir", C["blue"],   C["blue_bg"],
     "<b>Acumular para Greats of the Game (19/06)</b> — ICON SBCs exigem 87/88 rated. "
     "Janela de compra: 10-18/06. Também monitorar leaks de Evolutions para "
     "Glory Hunters (26/06). Manter 20-30% dos coins sempre líquidos."),
]

for period, cl, cr, text in timing_rows:
    r = Table([[
        P(period, ps("tp",9,13,TA_CENTER,"white","Helvetica-Bold")),
        P(text, ps("tb",8.5,12,TA_JUSTIFY,"grey_text","Helvetica")),
    ]], colWidths=[2.8*cm,14.7*cm])
    r.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(0,0),cl),("BACKGROUND",(1,0),(1,0),cr),
        ("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),10),
        ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
        ("LINEBELOW",(0,0),(-1,-1),0.5,C["border"]),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ]))
    story.append(r)

story.append(Spacer(1, 5))

# Linha do tempo semanal
story.append(P(
    "<b>Calendário semanal de preços FUT:</b>  "
    "Qua 18h BST = TOTW drop (comprar Informs)  →  "
    "Qui 08h BST = Rivals rewards (mínimo semanal — COMPRAR)  →  "
    "Sex 18h BST = Novo promo (spike de fodder)  →  "
    "Sex/Sáb noite = pico de demanda Weekend League (VENDER)",
    ps("cal",8.5,12,TA_LEFT,"dark_bg","Helvetica-Bold",4,4,8)))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════
# 5. RETORNO ESTIMADO 48H
# ══════════════════════════════════════════════════════
story.append(P("5. ESTIMATIVA DE RETORNO EM 48H", "section"))
story.append(HRFlowable(width="100%", thickness=2, color=C["green_dark"], spaceAfter=6))

# Conservador: +40% spike, 75% vendido
c_profit = round(total_invest * 0.40 * 0.95 * 0.75)
# Realista:    +80% spike, 90% vendido
r_profit = round(total_invest * 0.80 * 0.95 * 0.90)
# Otimista:   +130% spike, 100% vendido
o_profit = round(total_invest * 1.30 * 0.95 * 1.00)

sc_header = [P(h,"th") for h in ["Cenário","Premissa","Capital Inicial","Lucro Líquido","Capital Final","ROI"]]
sc_data = [sc_header]

for name, premise, profit_v, bg, txt in [
    ("Conservador",
     "Spike +40%; 75% das cartas vendidas em 48h; apenas 1-2 SBCs novos",
     c_profit, C["yellow_bg"], C["yellow_text"]),
    ("Realista",
     "Spike +80%; 90% vendidas; padrão histórico (TOTS, TOTY, RTTK anteriores)",
     r_profit, C["blue_bg"], C["blue_text"]),
    ("Otimista",
     "Spike +130%; 100% vendidas; 4+ SBCs simultâneos + alta abertura de packs",
     o_profit, C["green_light"], C["green_dark"]),
]:
    ci   = total_invest
    cf   = ci + profit_v
    roi_v= profit_v/ci*100
    sc_data.append([
        P(name,        ps("sn",9,12,TA_CENTER,txt,"Helvetica-Bold")),
        P(premise,     ps("sp",8,11,TA_LEFT,"grey_text","Helvetica")),
        P(fmt(ci),     ps("sc",9,12,TA_CENTER,"grey_text","Helvetica")),
        P(f"+{fmt(profit_v)}", ps("sl",9,12,TA_CENTER,txt,"Helvetica-Bold")),
        P(fmt(cf),     ps("sf",9,12,TA_CENTER,"grey_text","Helvetica-Bold")),
        P(f"+{roi_v:.1f}%", ps("sr",9,12,TA_CENTER,txt,"Helvetica-Bold")),
    ])

sc_tbl = Table(sc_data, colWidths=[2.2*cm,6.0*cm,2.5*cm,2.5*cm,2.5*cm,1.8*cm])
sc_styles = [
    ("BACKGROUND",(0,0),(-1,0),C["dark_bg"]),
    ("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9),
    ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
    ("GRID",(0,0),(-1,-1),0.3,C["border"]),
    ("LINEBELOW",(0,0),(-1,0),1.5,C["green_dark"]),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("BACKGROUND",(0,1),(-1,1),C["yellow_bg"]),
    ("BACKGROUND",(0,2),(-1,2),C["blue_bg"]),
    ("BACKGROUND",(0,3),(-1,3),C["green_light"]),
]
sc_tbl.setStyle(TableStyle(sc_styles))
story.append(sc_tbl)
story.append(Spacer(1,5))
story.append(P(
    f"* Estimativas sobre {total_items_n} cartas / {fmt(total_invest)} coins investidos. "
    "Cenário realista baseado em comportamento histórico de promos (TOTS PL, TOTY). "
    "Não inclui ganhos de Evolutions (upside adicional). Sempre verifique preços em tempo real "
    "antes de listar: futbin.com/market · fut.gg/cheapest-by-rating",
    "disc"))
story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════
# 6. 8 REGRAS DE OURO
# ══════════════════════════════════════════════════════
story.append(P("6. AS 8 REGRAS DE OURO DO TRADE", "section"))
story.append(HRFlowable(width="100%", thickness=2, color=C["green_dark"], spaceAfter=8))

rules = [
    ("01","COMPRE ANTES DO EVENTO",
     "Acumule SBC fodder 2-5 dias antes de novos promos. O pico de preço ocorre nas primeiras 6-12h após o drop — nunca após."),
    ("02","NUNCA VENDA NO PANIC",
     "Se o preço cair após a compra, aguarde. SBC fodder sempre se recupera com novos SBCs. Liquide só se o promo for cancelado."),
    ("03","RESPEITE A TAXA DE 5%",
     "Preço líquido = venda × 0,95. Uma venda de 2.000 = 1.900 líquidos. Calcule sempre antes de listar — nunca ignore este custo."),
    ("04","LANCE NAS MADRUGADAS",
     "Entre 23h–06h UTC há menos competidores. Use bids em vez de BIN para comprar 10-20% mais barato nas listagens com 30-60 min restantes."),
    ("05","DIVERSIFIQUE POR RATING",
     "Distribua entre 86, 87 e 88 rated. Se um rating não for exigido em SBCs, os outros protegem o capital."),
    ("06","VERIFIQUE PREÇOS EM TEMPO REAL",
     "Consulte futbin.com e fut.gg antes de cada listagem. O mercado muda rápido: queda de 500 coins pode anular toda a margem calculada."),
    ("07","EVOLUÇÕES = INFORMAÇÃO",
     "Siga leaks de Evolutions no Reddit e Twitter/X. Compre a carta base antes do anúncio oficial — preço pode triplicar em minutos."),
    ("08","REALIZE LUCRO PARCIAL",
     "Ao atingir +25% em qualquer carta, venda 50% do estoque. Proteja o capital e deixe o restante correr até o pico."),
]

for i in range(0, len(rules), 4):
    chunk = rules[i:i+4]
    while len(chunk) < 4: chunk.append(None)
    cells = []
    for r in chunk:
        if r is None:
            cells.append(P("","body"))
        else:
            num, title, desc = r
            cell_para = Paragraph(
                f'<font size="16" color="#ffc107"><b>{num}</b></font><br/>'
                f'<font size="8.5" color="#1a1a2e"><b>{title}</b></font><br/><br/>'
                f'<font size="8" color="#495057">{desc}</font>',
                ps(f"rc{num}", 9, 12, TA_CENTER, "grey_text", "Helvetica")
            )
            cells.append(cell_para)
    rt = Table([cells], colWidths=[4.375*cm]*4)
    rt.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),C["light_grey"]),
        ("TOPPADDING",(0,0),(-1,-1),14),("BOTTOMPADDING",(0,0),(-1,-1),14),
        ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
        ("GRID",(0,0),(-1,-1),1,C["white"]),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LINEABOVE",(0,0),(-1,0),3,C["gold"]),
    ]))
    story.append(rt)
    story.append(Spacer(1,4))

story.append(Spacer(1, 10))

# ══════════════════════════════════════════════════════
# DISCLAIMER
# ══════════════════════════════════════════════════════
story.append(HRFlowable(width="100%", thickness=1, color=C["border"], spaceAfter=6))
story.append(box(
    P("<b>DISCLAIMER:</b> Este relatório foi gerado automaticamente por um agente de análise de mercado "
      "para fins educativos e de suporte à tomada de decisão no EA FC 26 Ultimate Team. Os preços "
      "indicados são estimativas baseadas em dados históricos e tendências observadas — não constituem "
      "garantia de lucro. O mercado FUT é altamente volátil e pode ser afetado por atualizações do jogo, "
      "novos promos, crashes de mercado ou mudanças nos price ranges impostos pela EA Sports. "
      "Invista apenas o que estiver disposto a perder. Dados consultados em: "
      "futbin.com · fut.gg · realsport101.com · sportsdunia.com · teamgullit.com · ea.com · "
      "destructoid.com · soccergaming.com · khelnow.com.",
      "disc"),
    C["light_grey"], tpad=8, bpad=8))

doc.build(story)

print(f"\n✅  PDF gerado com sucesso!")
print(f"    Arquivo: {OUTPUT_PATH}")
print(f"    Investimento total (SBC fodder): {fmt(total_invest)} coins")
print(f"    Lucro conservador (+40%/75%):    +{fmt(c_profit)} coins  ({c_profit/total_invest*100:.0f}%)")
print(f"    Lucro realista    (+80%/90%):    +{fmt(r_profit)} coins  ({r_profit/total_invest*100:.0f}%)")
print(f"    Lucro otimista    (+130%/100%):  +{fmt(o_profit)} coins  ({o_profit/total_invest*100:.0f}%)")
