import streamlit as st
import json
from datetime import datetime, date

# ══════════════════════════════════════════════════════
#  CONFIG
# ══════════════════════════════════════════════════════
st.set_page_config(
    page_title="Iron Protocol",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════
#  CSS — forçado light, independente do tema do device
# ══════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;0,14..32,700;1,14..32,400&display=swap');

/* ── FORÇA FUNDO E TEXTO ── */
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
.main, .block-container,
section[data-testid="stSidebar"],
[class*="appview"] {
    background-color: #F2F4F8 !important;
    color: #111827 !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stSidebar"] { display: none !important; }
[data-testid="stMainBlockContainer"] {
    padding: 0 12px 60px 12px !important;
    max-width: 700px !important;
    margin: 0 auto !important;
}

/* ── ESCONDE CHROME STREAMLIT ── */
#MainMenu, footer, header,
[data-testid="stDecoration"],
[data-testid="stToolbar"] { display: none !important; }

/* ── BOTÕES — override total ── */
button[kind="secondary"],
button[kind="primary"],
[data-testid="stBaseButton-secondary"],
[data-testid="stBaseButton-primary"],
.stButton > button {
    background-color: #FFFFFF !important;
    color: #111827 !important;
    border: 1.5px solid #E5E7EB !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    padding: 8px 14px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
    transition: all 0.15s !important;
    width: 100% !important;
}
.stButton > button:hover {
    border-color: #F97316 !important;
    color: #EA580C !important;
    background-color: #FFF7ED !important;
}
.stButton > button:active {
    transform: scale(0.98) !important;
}

/* ── SELECTBOX ── */
[data-testid="stSelectbox"] label { display: none !important; }
[data-testid="stSelectbox"] > div > div,
[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border: 1.5px solid #E5E7EB !important;
    border-radius: 12px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: #111827 !important;
}
[data-baseweb="select"] svg { color: #6B7280 !important; }

/* ── TABS ── */
[data-testid="stTabs"] {
    background: transparent !important;
}
button[data-baseweb="tab"] {
    background: transparent !important;
    color: #9CA3AF !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    border: none !important;
    padding: 8px 16px !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: #EA580C !important;
    border-bottom: 2px solid #EA580C !important;
}
[data-testid="stTabPanel"] {
    background: transparent !important;
    padding: 0 !important;
}

/* ── CHECKBOX ── */
[data-testid="stCheckbox"] {
    background: transparent !important;
}
[data-testid="stCheckbox"] label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.8rem !important;
    color: #6B7280 !important;
    font-weight: 500 !important;
}
[data-testid="stCheckbox"] > label > div[data-testid="stMarkdownContainer"] p {
    color: #6B7280 !important;
}

/* ── NUMBER INPUT ── */
[data-testid="stNumberInput"] label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    color: #6B7280 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}
[data-testid="stNumberInput"] input {
    background: #FFFFFF !important;
    color: #111827 !important;
    border: 1.5px solid #E5E7EB !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    text-align: center !important;
}
[data-testid="stNumberInput"] button {
    background: #F9FAFB !important;
    color: #374151 !important;
    border: 1.5px solid #E5E7EB !important;
    width: auto !important;
    padding: 4px 10px !important;
    font-size: 1rem !important;
}

/* ── EXPANDER ── */
[data-testid="stExpander"] {
    background: #FFFFFF !important;
    border: 1.5px solid #F3F4F6 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    margin-bottom: 8px !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
}
[data-testid="stExpander"] summary {
    background: #FFFFFF !important;
    color: #111827 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 12px 16px !important;
}
[data-testid="stExpander"] summary:hover {
    background: #FFF7ED !important;
}
[data-testid="stExpander"] > div {
    background: #FAFAFA !important;
}

/* ── TOAST ── */
[data-testid="stToast"] {
    background: #111827 !important;
    color: #FFFFFF !important;
    border-radius: 10px !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #D1D5DB; border-radius: 99px; }

/* ══ COMPONENTES CUSTOMIZADOS ══ */

.app-header {
    background: linear-gradient(135deg, #EA580C 0%, #F97316 60%, #FB923C 100%);
    border-radius: 20px;
    padding: 22px 20px 18px;
    margin: 12px 0 16px;
    position: relative;
    overflow: hidden;
}
.app-header::after {
    content: '';
    position: absolute;
    top: -30px; right: -30px;
    width: 120px; height: 120px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
}
.app-title {
    font-size: 1.7rem;
    font-weight: 800;
    color: #fff;
    letter-spacing: -0.03em;
    line-height: 1;
    margin: 0;
}
.app-sub {
    font-size: 0.72rem;
    color: rgba(255,255,255,0.75);
    margin-top: 5px;
    font-weight: 500;
    letter-spacing: 0.02em;
}
.app-streak {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    border-radius: 99px;
    padding: 3px 10px;
    font-size: 0.7rem;
    font-weight: 700;
    color: #fff;
    margin-top: 10px;
}

/* PROGRESS CARD */
.prog-card {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}
.prog-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}
.prog-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: #6B7280;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.prog-pct {
    font-size: 1.1rem;
    font-weight: 800;
    color: #EA580C;
}
.prog-bar-bg {
    background: #F3F4F6;
    border-radius: 99px;
    height: 8px;
    overflow: hidden;
}
.prog-bar {
    height: 8px;
    border-radius: 99px;
    background: linear-gradient(90deg, #EA580C, #FBBF24);
    transition: width 0.4s cubic-bezier(.4,0,.2,1);
}
.prog-sub {
    font-size: 0.68rem;
    color: #9CA3AF;
    margin-top: 5px;
    font-weight: 500;
}

/* DAY CARD */
.day-banner {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-left: 4px solid #EA580C;
}
.day-tag {
    font-size: 0.65rem;
    font-weight: 700;
    color: #EA580C;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 4px;
}
.day-foco {
    font-size: 1rem;
    font-weight: 700;
    color: #111827;
    line-height: 1.3;
}
.day-dur {
    text-align: right;
}
.day-dur-val {
    font-size: 1.3rem;
    font-weight: 800;
    color: #EA580C;
    line-height: 1;
}
.day-dur-lbl {
    font-size: 0.6rem;
    color: #9CA3AF;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

/* SECTION HEADER */
.sec-hdr {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 20px 0 10px;
}
.sec-hdr-text {
    font-size: 0.7rem;
    font-weight: 700;
    color: #EA580C;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    white-space: nowrap;
}
.sec-hdr-line {
    flex: 1;
    height: 1px;
    background: #E5E7EB;
}

/* EXERCISE CARD */
.ex-wrap {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 14px 16px 10px;
    margin-bottom: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    border-left: 4px solid #EA580C;
    transition: box-shadow 0.15s, opacity 0.2s;
}
.ex-wrap.done {
    border-left-color: #10B981;
    opacity: 0.6;
}
.ex-wrap.done .ex-name { text-decoration: line-through; color: #6B7280; }

.ex-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 8px;
}
.ex-name {
    font-size: 0.97rem;
    font-weight: 700;
    color: #111827;
    line-height: 1.3;
    flex: 1;
}
.ex-sets-pill {
    background: #FFF7ED;
    color: #EA580C;
    font-size: 0.68rem;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 99px;
    white-space: nowrap;
    flex-shrink: 0;
}
.badges-row { margin: 6px 0; }
.badge {
    display: inline-block;
    font-size: 0.58rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 99px;
    margin-right: 4px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.b-rp  { background: #FEE2E2; color: #DC2626; }
.b-bo  { background: #FEF3C7; color: #D97706; }
.b-str { background: #D1FAE5; color: #059669; }
.b-iso { background: #EDE9FE; color: #7C3AED; }

.ex-desc {
    font-size: 0.8rem;
    color: #6B7280;
    line-height: 1.55;
    margin: 6px 0 8px;
}
.alt-pill {
    background: #FFF7ED;
    border: 1px dashed #FED7AA;
    border-radius: 10px;
    padding: 7px 11px;
    margin-bottom: 8px;
}
.alt-lbl {
    font-size: 0.58rem;
    font-weight: 700;
    color: #EA580C;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 2px;
}
.alt-txt {
    font-size: 0.78rem;
    color: #92400E;
    line-height: 1.4;
}
.yt-link {
    display: inline-block;
    font-size: 0.72rem;
    font-weight: 600;
    color: #6366F1;
    text-decoration: none;
    margin-top: 2px;
}
.yt-link:hover { text-decoration: underline; }

/* LOG SECTION inside card */
.log-section {
    background: #F9FAFB;
    border-radius: 10px;
    padding: 10px 12px;
    margin-top: 8px;
    border: 1px solid #F3F4F6;
}
.log-title {
    font-size: 0.65rem;
    font-weight: 700;
    color: #9CA3AF;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
}
.hist-entry {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 0;
    border-bottom: 1px solid #F3F4F6;
    font-size: 0.75rem;
}
.hist-date { color: #9CA3AF; font-weight: 500; }
.hist-vals { color: #111827; font-weight: 700; }
.hist-pr {
    background: #FEF3C7;
    color: #D97706;
    font-size: 0.6rem;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 99px;
    margin-left: 6px;
}

/* VOLUME */
.vol-card {
    background: #FFFFFF;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.vol-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
}
.vol-muscle { font-size: 0.88rem; font-weight: 600; color: #111827; }
.vol-num { font-size: 0.82rem; font-weight: 700; color: #EA580C; }
.vol-bar-bg { background: #F3F4F6; border-radius: 99px; height: 5px; overflow: hidden; }
.vol-bar-fill { height: 5px; border-radius: 99px; }

.legend-card {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 14px 16px;
    margin-top: 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.legend-title {
    font-size: 0.72rem;
    font-weight: 700;
    color: #6B7280;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
}
.legend-item {
    font-size: 0.8rem;
    color: #374151;
    margin-bottom: 7px;
    line-height: 1.45;
    display: flex;
    gap: 8px;
    align-items: flex-start;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
#  DADOS DO TREINO
# ══════════════════════════════════════════════════════
TRAINING_PLAN = {
    "Segunda — DIA A": {
        "foco": "Costas Largura + Bíceps",
        "dur": "120 min",
        "color": "#3B82F6",
        "emoji": "🔵",
        "blocos": [
            {
                "nome": "Compostos — Back-off Sets",
                "exercicios": [
                    {
                        "nome": "Barra Fixa Pronada (Pull-up)",
                        "series": "5×MAX + 3×6 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Pegada aberta além dos ombros. Retração escapular antes de puxar. Cotovelos apontam para baixo e para os lados. Pausa 1s no topo. Back-off com cinto e anilha.",
                        "alt": "Remada Unilateral no Banco c/ Halter 35–40 kg — 4×10/lado.",
                        "gif": "https://www.youtube.com/results?search_query=pull+up+form+bodybuilding",
                    },
                    {
                        "nome": "Remada Curvada na Barra",
                        "series": "4×8 pesado + 1×15 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Tronco a 45°. Barra para o umbigo, cotovelos junto ao tronco. Pausa 1s na contração. Sem balanço. Back-off em 60%.",
                        "alt": "Remada c/ Halteres 2×30 kg — 4×10, amplitude maior.",
                        "gif": "https://www.youtube.com/results?search_query=barbell+bent+over+row",
                    },
                ],
            },
            {
                "nome": "Largura + Isoladores",
                "exercicios": [
                    {
                        "nome": "Pullover com Halter",
                        "series": "3×12 + rest-pause no último",
                        "metodo": ["iso","rp"],
                        "desc": "Decúbito no banco, halter 20–25 kg. Arco amplo, cotovelo levemente flexionado. Sinta o serrátil e dorsal. Rest-Pause: falha → 15s → 3–5 extras.",
                        "alt": "Pullover no chão — mesma execução, amplitude menor.",
                        "gif": "https://www.youtube.com/results?search_query=dumbbell+pullover+technique",
                    },
                    {
                        "nome": "Remada Unilateral no Banco",
                        "series": "3×12/lado + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Cotovelo em diagonal (não L). Puxe pelo cotovelo. Pausa 1s no topo. Rest-Pause: falha → 15s → nova falha.",
                        "alt": "Remada Cavalinho c/ Halter — apoio bilateral, mais estabilidade.",
                        "gif": "https://www.youtube.com/results?search_query=single+arm+dumbbell+row",
                    },
                ],
            },
            {
                "nome": "Bíceps",
                "exercicios": [
                    {
                        "nome": "Rosca Direta na Barra",
                        "series": "4×10 + 1×20 back-off EZ",
                        "metodo": ["iso","bo"],
                        "desc": "Cotovelos fixos. Supinação total no topo. Excêntrico 3s. Back-off com EZ a 50%: 20 reps pump.",
                        "alt": "Rosca Alternada c/ Halteres — 4×10/lado.",
                        "gif": "https://www.youtube.com/results?search_query=barbell+curl+technique",
                    },
                    {
                        "nome": "Rosca Concentrada",
                        "series": "3×12/lado + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Cotovelo no joelho. Pico de contração 2s. Rest-Pause: falha → 15s → 4–5 reps.",
                        "alt": "Rosca Scott c/ Halter no banco inclinado.",
                        "gif": "https://www.youtube.com/results?search_query=concentration+curl+technique",
                    },
                    {
                        "nome": "Rosca Martelo",
                        "series": "3×15 + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Pegada neutra. Trabalha braquial e braquiorradial — espessura do braço. Alternada.",
                        "alt": "Martelo com toalha no halter — conforto no pulso.",
                        "gif": "https://www.youtube.com/results?search_query=hammer+curl+technique",
                    },
                ],
            },
        ],
        "volume": {"Costas": 15, "Bíceps": 10, "Serrátil": 3},
    },

    "Terça — DIA B": {
        "foco": "Ombros + Trapézio",
        "dur": "120 min",
        "color": "#F97316",
        "emoji": "🟠",
        "blocos": [
            {
                "nome": "Press Overhead — Back-off",
                "exercicios": [
                    {
                        "nome": "Desenvolvimento Militar na Barra",
                        "series": "5×5 + 2×10 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Pegada além dos ombros. Core travado, glúteo contraído. Empurre sobre a cabeça. Back-off: 60%, 10 reps explosivas.",
                        "alt": "Desenvolvimento c/ Halteres sentado — 5×8.",
                        "gif": "https://www.youtube.com/results?search_query=overhead+press+barbell",
                    },
                    {
                        "nome": "Arnold Press",
                        "series": "4×10 + 1×15 back-off",
                        "metodo": ["iso","bo"],
                        "desc": "Palmas para você no início, rotaciona abrindo enquanto sobe. Ativa as 3 porções do deltoide.",
                        "alt": "Press Unilateral com Halter — 4×12/lado.",
                        "gif": "https://www.youtube.com/results?search_query=arnold+press+technique",
                    },
                ],
            },
            {
                "nome": "Lateral — Foco em Largura",
                "exercicios": [
                    {
                        "nome": "Elevação Lateral com Halteres",
                        "series": "5×15–20 + rest-pause nos 2 últimos",
                        "metodo": ["iso","rp"],
                        "desc": "10–15 kg. Polegar para baixo (pronação leve). Até paralelo, excêntrico 3s. Rest-Pause: falha → 10s → 5 reps.",
                        "alt": "Elevação Lateral Unilateral na parede — isolamento total.",
                        "gif": "https://www.youtube.com/results?search_query=lateral+raise+bodybuilding",
                    },
                    {
                        "nome": "Elevação Lateral Inclinada",
                        "series": "4×12/lado + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Segure num poste, incline 20–30°. Eleve com o braço livre. Tensão constante no medial.",
                        "alt": "Lateral deitado de lado no banco.",
                        "gif": "https://www.youtube.com/results?search_query=cable+lateral+raise+lean",
                    },
                ],
            },
            {
                "nome": "Trapézio + Posterior",
                "exercicios": [
                    {
                        "nome": "Encolhimento com Barra (Shrug)",
                        "series": "4×15 + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Sobe o ombro direto para cima. Pausa 2s. Excêntrico 3s. Rest-Pause no último.",
                        "alt": "Shrug com Halteres 2×40 kg.",
                        "gif": "https://www.youtube.com/results?search_query=barbell+shrug",
                    },
                    {
                        "nome": "Crucifixo Invertido com Halteres",
                        "series": "4×15 + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Sentado curvado. 10–15 kg. Abre até paralelo, pince as escápulas no topo.",
                        "alt": "Invertido deitado pronado no banco.",
                        "gif": "https://www.youtube.com/results?search_query=rear+delt+fly",
                    },
                ],
            },
        ],
        "volume": {"Ombro Medial": 18, "Ombro Anterior": 9, "Ombro Posterior": 8, "Trapézio": 8},
    },

    "Quarta — DIA C": {
        "foco": "Peito + Tríceps",
        "dur": "120 min",
        "color": "#10B981",
        "emoji": "🟢",
        "blocos": [
            {
                "nome": "Press Compostos — Back-off",
                "exercicios": [
                    {
                        "nome": "Supino Reto na Barra",
                        "series": "5×5 + 2×10 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Pegada 1,5× ombros. Arco lombar controlado. Excêntrico 3s até tocar o peito. Empurra explosivo.",
                        "alt": "Supino c/ Halteres 2×35–40 kg — amplitude maior.",
                        "gif": "https://www.youtube.com/results?search_query=bench+press+technique",
                    },
                    {
                        "nome": "Supino Inclinado com Halteres",
                        "series": "4×10 + 1×15 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Banco a 30–45°. Halteres em linha com os ombros. Foco no peitoral superior.",
                        "alt": "Crucifixo Inclinado — 4×12.",
                        "gif": "https://www.youtube.com/results?search_query=incline+dumbbell+press",
                    },
                ],
            },
            {
                "nome": "Isoladores de Peito",
                "exercicios": [
                    {
                        "nome": "Crucifixo com Halteres",
                        "series": "4×12 + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Banco plano. Arco amplo, cotovelo levemente flexionado e fixo. Sinta o alongamento. Rest-Pause no último.",
                        "alt": "Crucifixo em pé com halteres leves (10–12 kg).",
                        "gif": "https://www.youtube.com/results?search_query=dumbbell+fly+chest",
                    },
                ],
            },
            {
                "nome": "Tríceps",
                "exercicios": [
                    {
                        "nome": "Tríceps Francês com Barra EZ",
                        "series": "4×12 + 1×20 back-off",
                        "metodo": ["iso","bo"],
                        "desc": "Deitado. Cotovelos fixos para cima. Desce atrás da cabeça. Máximo alongamento da cabeça longa.",
                        "alt": "Francês com Halter unilateral — 4×12/lado.",
                        "gif": "https://www.youtube.com/results?search_query=EZ+skull+crusher",
                    },
                    {
                        "nome": "Mergulho no Banco (Dips)",
                        "series": "4×MAX + 2×10 back-off assistido",
                        "metodo": ["str","bo"],
                        "desc": "Tronco ereto (foco tríceps). Cotovelos paralelos. Desce até 90°.",
                        "alt": "Extensão Overhead + Kickback superset — 3×12.",
                        "gif": "https://www.youtube.com/results?search_query=tricep+dips",
                    },
                    {
                        "nome": "Kickback com Halter",
                        "series": "3×15/lado + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Tronco paralelo ao chão. Cotovelo fixo. Estende até bloquear. Pausa 2s.",
                        "alt": "Extensão Overhead bilateral — mais carga.",
                        "gif": "https://www.youtube.com/results?search_query=tricep+kickback",
                    },
                ],
            },
        ],
        "volume": {"Peito": 16, "Tríceps": 13},
    },

    "Quinta — DIA D": {
        "foco": "Costas Densidade + Ombro Medial",
        "dur": "120 min",
        "color": "#3B82F6",
        "emoji": "🔵",
        "blocos": [
            {
                "nome": "Espessura Dorsal — Back-off",
                "exercicios": [
                    {
                        "nome": "Terra Romeno com Barra",
                        "series": "5×6 + 2×10 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Quadril para trás, coluna neutra. Barra raspa a coxa. Sente o alongamento dos ísquios. Back-off: 60%, 10 reps lentas.",
                        "alt": "Terra Romeno c/ Halteres 2×35–40 kg.",
                        "gif": "https://www.youtube.com/results?search_query=romanian+deadlift",
                    },
                    {
                        "nome": "Remada T (Barra no Canto)",
                        "series": "4×10 + rest-pause",
                        "metodo": ["str","rp"],
                        "desc": "Barra num canto com anilhas. Puxe para o peito com pegada neutra. Alta densidade.",
                        "alt": "Remada c/ Halteres Bilateral no Banco inclinado — 4×12.",
                        "gif": "https://www.youtube.com/results?search_query=T-bar+row",
                    },
                ],
            },
            {
                "nome": "Largura — Rest-Pause",
                "exercicios": [
                    {
                        "nome": "Barra Fixa Supinada (Chin-up)",
                        "series": "4×8 + rest-pause no último",
                        "metodo": ["str","rp"],
                        "desc": "Pegada supinada na largura dos ombros. Cotovelos para o chão. Rest-Pause: falha → 15s → máximo.",
                        "alt": "Remada Curvada Supinada c/ Halteres — 4×10.",
                        "gif": "https://www.youtube.com/results?search_query=chin+up+supinated",
                    },
                ],
            },
            {
                "nome": "Ombro Medial — Pump",
                "exercicios": [
                    {
                        "nome": "Elevação Lateral com Halteres",
                        "series": "5×15 + rest-pause nos 2 últimos",
                        "metodo": ["iso","rp"],
                        "desc": "8–12 kg. Sobe 1s, pausa 2s, desce 3s. Rest-Pause: falha → 10s → mais reps.",
                        "alt": "Lateral Unilateral apoiado.",
                        "gif": "https://www.youtube.com/results?search_query=lateral+raise+tempo",
                    },
                    {
                        "nome": "Remada Alta com Halteres",
                        "series": "4×12 + 1×15 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Cotovelos sobem acima dos ombros. Ativa trapézio médio + deltoide. Se sentir dor, alargue a pegada.",
                        "alt": "Remada Alta na Barra — mais carga.",
                        "gif": "https://www.youtube.com/results?search_query=upright+row+dumbbell",
                    },
                ],
            },
        ],
        "volume": {"Costas": 16, "Ombro Medial": 14, "Trapézio": 8, "Isquiotibiais": 6},
    },

    "Sexta — DIA E": {
        "foco": "Braços Completos + Antebraço",
        "dur": "120 min",
        "color": "#8B5CF6",
        "emoji": "🟣",
        "blocos": [
            {
                "nome": "Bíceps — Rest-Pause + Back-off",
                "exercicios": [
                    {
                        "nome": "Rosca Inclinada com Halteres",
                        "series": "4×10 + rest-pause nos 2 últimos",
                        "metodo": ["iso","rp"],
                        "desc": "Banco 45–60°. Braços pendurados atrás = máximo alongamento. Supina no topo. Excêntrico 4s.",
                        "alt": "Rosca com apoio no banco inclinado (frente).",
                        "gif": "https://www.youtube.com/results?search_query=incline+dumbbell+curl",
                    },
                    {
                        "nome": "Rosca 21s na Barra",
                        "series": "3×21 (7+7+7)",
                        "metodo": ["iso"],
                        "desc": "7 metade inferior + 7 metade superior + 7 completas. Sem pausa. Sem momentum.",
                        "alt": "21s com Halteres Alternado.",
                        "gif": "https://www.youtube.com/results?search_query=21s+bicep+curl",
                    },
                    {
                        "nome": "Rosca Concentrada",
                        "series": "3×12/lado + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Cotovelo no joelho. Supinação forçada. Rest-Pause no último set de cada lado.",
                        "alt": "Rosca Presa no Rack — cotovelo no poste.",
                        "gif": "https://www.youtube.com/results?search_query=concentration+curl",
                    },
                ],
            },
            {
                "nome": "Tríceps — Rest-Pause + Back-off",
                "exercicios": [
                    {
                        "nome": "Tríceps Overhead com Halter (Bilateral)",
                        "series": "4×12 + 1×20 back-off",
                        "metodo": ["iso","bo"],
                        "desc": "Sentado. Halter atrás da cabeça. Cotovelos fixos para cima. Alonga a cabeça longa.",
                        "alt": "Overhead Unilateral — 4×12/lado.",
                        "gif": "https://www.youtube.com/results?search_query=overhead+tricep+extension+dumbbell",
                    },
                    {
                        "nome": "Tríceps Testa com Halteres",
                        "series": "4×12 + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Deitado. Halteres descem ao lado das orelhas. Cotovelos verticais e fixos. Rest-Pause no último.",
                        "alt": "Extensão de Tríceps no Chão.",
                        "gif": "https://www.youtube.com/results?search_query=lying+dumbbell+tricep+extension",
                    },
                ],
            },
            {
                "nome": "Antebraço — Finalizadores",
                "exercicios": [
                    {
                        "nome": "Rosca de Pulso (Wrist Curl)",
                        "series": "4×20 + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Antebraços nos joelhos, palmas para cima. Amplitude total. Pausa 1s no topo. Rest-Pause brutal no último.",
                        "alt": "Wrist Curl na borda do banco.",
                        "gif": "https://www.youtube.com/results?search_query=wrist+curl+forearm",
                    },
                    {
                        "nome": "Rosca Martelo Cruzado",
                        "series": "3×15/lado + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Halter cruza em direção ao ombro oposto. Ativa o braquiorradial diferente do martelo convencional.",
                        "alt": "Martelo Simultâneo com carga menor.",
                        "gif": "https://www.youtube.com/results?search_query=cross+body+hammer+curl",
                    },
                ],
            },
        ],
        "volume": {"Bíceps": 14, "Tríceps": 12, "Antebraço": 8},
    },

    "Sábado — DIA F": {
        "foco": "Pernas (Quad + Posterior + Glúteo + Panturrilha)",
        "dur": "120 min",
        "color": "#EF4444",
        "emoji": "🔴",
        "blocos": [
            {
                "nome": "Compostos Pesados — Back-off",
                "exercicios": [
                    {
                        "nome": "Agachamento Livre na Barra",
                        "series": "5×5 + 2×10 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Pés na largura dos ombros, pontas abertas. Barra no trapézio alto. Coxa paralela ao chão. Joelhos acompanham a ponta do pé. Back-off: 60% da carga.",
                        "alt": "Agachamento Goblet com Halter 30–40 kg — 5×10, postura mais vertical.",
                        "gif": "https://www.youtube.com/results?search_query=barbell+squat+form",
                    },
                    {
                        "nome": "Leg Press 45°",
                        "series": "4×12 + 1×20 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Pés na largura dos ombros no centro da plataforma. Desce até 90° sem tirar o lombar do encosto. Empurra explosivo. Back-off: carga leve, 20 reps de bombeamento.",
                        "alt": "Agachamento Sumô c/ Halter (Goblet) — 4×15, pés bem abertos.",
                        "gif": "https://www.youtube.com/results?search_query=leg+press+45+technique",
                    },
                ],
            },
            {
                "nome": "Quadríceps — Isoladores",
                "exercicios": [
                    {
                        "nome": "Extensora (Leg Extension)",
                        "series": "4×15 + rest-pause nos 2 últimos",
                        "metodo": ["iso","rp"],
                        "desc": "Ajuste o apoio do tornozelo. Extensão completa com pausa de 2s no topo (isometria máxima). Excêntrico controlado de 3s. Rest-Pause: falha → 15s → mais reps.",
                        "alt": "Agachamento Búlgaro c/ Halteres 2×15 kg — 4×10/lado, mais funcional.",
                        "gif": "https://www.youtube.com/results?search_query=leg+extension+technique",
                    },
                    {
                        "nome": "Agachamento Búlgaro (Split Squat)",
                        "series": "3×10/lado + rest-pause",
                        "metodo": ["str","rp"],
                        "desc": "Pé traseiro no banco. Desce o joelho traseiro ao chão. Tronco levemente inclinado à frente. Isola cada perna. Rest-Pause: falha → 15s → mais reps.",
                        "alt": "Avanço c/ Halteres 2×20–25 kg — 4×12/lado, sem banco.",
                        "gif": "https://www.youtube.com/results?search_query=bulgarian+split+squat",
                    },
                ],
            },
            {
                "nome": "Posteriores + Glúteos",
                "exercicios": [
                    {
                        "nome": "Terra Romeno com Barra",
                        "series": "4×10 + 1×15 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Quadril para trás, barra raspa a coxa. Foco no alongamento dos ísquios. Coluna neutra o tempo todo. Back-off: 60%, 15 reps lentas.",
                        "alt": "Terra Romeno c/ Halteres 2×30 kg — mais controle da trajetória.",
                        "gif": "https://www.youtube.com/results?search_query=romanian+deadlift+hamstring",
                    },
                    {
                        "nome": "Elevação Pélvica com Barra (Hip Thrust)",
                        "series": "4×12 + 1×20 back-off",
                        "metodo": ["str","bo"],
                        "desc": "Costas no banco, barra sobre o quadril (use toalha). Empurra até linha reta joelho–quadril–ombro. Pausa 2s no topo. Back-off leve com squeeze.",
                        "alt": "Hip Thrust c/ Halteres 2×25–30 kg — 4×15.",
                        "gif": "https://www.youtube.com/results?search_query=hip+thrust+barbell",
                    },
                ],
            },
            {
                "nome": "Panturrilha — Finalizadores",
                "exercicios": [
                    {
                        "nome": "Calf Raise em Pé no Degrau",
                        "series": "5×20 + rest-pause nos 2 últimos",
                        "metodo": ["iso","rp"],
                        "desc": "Ponta do pé no degrau. Amplitude total: desce até o alongamento máximo, sobe ao máximo. Pausa 2s no topo. Rest-Pause brutal.",
                        "alt": "Calf Raise Unilateral c/ Halter — 5×15/lado.",
                        "gif": "https://www.youtube.com/results?search_query=standing+calf+raise",
                    },
                    {
                        "nome": "Calf Raise Sentado (Sóleo)",
                        "series": "4×20 + rest-pause",
                        "metodo": ["iso","rp"],
                        "desc": "Sentado, anilha sobre os joelhos. Eleva calcanhares. O sóleo só é ativado com joelho flexionado. Rest-Pause no último.",
                        "alt": "Calf Raise Sentado c/ Halter no joelho.",
                        "gif": "https://www.youtube.com/results?search_query=seated+calf+raise",
                    },
                ],
            },
        ],
        "volume": {"Quadríceps": 20, "Glúteos": 14, "Isquiotibiais": 12, "Panturrilha": 14},
    },
}

METHOD = {
    "rp":  ("b-rp",  "Rest-Pause"),
    "bo":  ("b-bo",  "Back-off"),
    "str": ("b-str", "Composto"),
    "iso": ("b-iso", "Isolador"),
}

# ══════════════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════════════
if "checks"  not in st.session_state: st.session_state.checks  = {}
if "logs"    not in st.session_state: st.session_state.logs    = {}   # {key: [{date, series, kg, reps}]}

def get_log(key):
    return st.session_state.logs.get(key, [])

def save_log(key, series, kg, reps):
    entry = {
        "date": date.today().strftime("%d/%m"),
        "series": series,
        "kg": kg,
        "reps": reps,
        "is_pr": False,
    }
    hist = get_log(key)
    # marca PR
    if hist:
        best = max(h["kg"] for h in hist)
        entry["is_pr"] = kg > best
    else:
        entry["is_pr"] = True
    hist.insert(0, entry)
    st.session_state.logs[key] = hist[:10]  # guarda últimas 10

# ══════════════════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════════════════
total_ex = sum(len(b["exercicios"]) for d in TRAINING_PLAN.values() for b in d["blocos"])
done_ex  = sum(1 for v in st.session_state.checks.values() if v)
pct      = int((done_ex / total_ex) * 100) if total_ex else 0

st.markdown(f"""
<div class="app-header">
    <div class="app-title">⚡ Iron Protocol</div>
    <div class="app-sub">Divisão A–B–C–D–E–F · Alta Performance</div>
    <div class="app-streak">🔥 {done_ex}/{total_ex} exercícios concluídos esta semana</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
#  SELETOR DE DIA
# ══════════════════════════════════════════════════════
dias = list(TRAINING_PLAN.keys())
selected_day = st.selectbox("dia", options=dias, label_visibility="collapsed")
day_data = TRAINING_PLAN[selected_day]

# progresso do dia
day_total = sum(len(b["exercicios"]) for b in day_data["blocos"])
day_done  = sum(1 for b in day_data["blocos"]
                for ex in b["exercicios"]
                if st.session_state.checks.get(f"{selected_day}_{ex['nome']}", False))
day_pct   = int((day_done / day_total) * 100) if day_total else 0

st.markdown(f"""
<div class="prog-card">
    <div class="prog-top">
        <span class="prog-label">Progresso do dia</span>
        <span class="prog-pct">{day_pct}%</span>
    </div>
    <div class="prog-bar-bg">
        <div class="prog-bar" style="width:{day_pct}%"></div>
    </div>
    <div class="prog-sub">{day_done} de {day_total} exercícios concluídos</div>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    if st.button("🔄  Resetar dia", use_container_width=True):
        for k in [k for k in st.session_state.checks if k.startswith(selected_day)]:
            del st.session_state.checks[k]
        st.toast("Dia resetado!", icon="✅")
        st.rerun()
with c2:
    if st.button("🗑️  Resetar semana", use_container_width=True):
        st.session_state.checks = {}
        st.toast("Semana zerada!", icon="♻️")
        st.rerun()

# banner do dia
color = day_data["color"]
st.markdown(f"""
<div class="day-banner" style="border-left-color:{color}">
    <div>
        <div class="day-tag" style="color:{color}">{selected_day}</div>
        <div class="day-foco">{day_data['emoji']} {day_data['foco']}</div>
    </div>
    <div class="day-dur">
        <div class="day-dur-lbl">Duração</div>
        <div class="day-dur-val" style="color:{color}">{day_data['dur']}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
#  TABS
# ══════════════════════════════════════════════════════
tab_ex, tab_hist, tab_vol = st.tabs(["🏋️ Treino", "📈 Evolução", "📊 Volume"])

# ─── TAB TREINO ───────────────────────────────────────
with tab_ex:
    for bloco in day_data["blocos"]:
        st.markdown(f"""
        <div class="sec-hdr">
            <span class="sec-hdr-text">{bloco['nome']}</span>
            <div class="sec-hdr-line"></div>
        </div>
        """, unsafe_allow_html=True)

        for ex in bloco["exercicios"]:
            key = f"{selected_day}_{ex['nome']}"
            checked = st.session_state.checks.get(key, False)
            done_cls = "done" if checked else ""
            check_icon = "✅" if checked else "🔲"

            badges = "".join(
                f"<span class='badge {METHOD[m][0]}'>{METHOD[m][1]}</span>"
                for m in ex.get("metodo", []) if m in METHOD
            )

            # histórico resumido (última entrada)
            hist = get_log(key)
            last_html = ""
            if hist:
                h = hist[0]
                pr_icon = " 🏆" if h["is_pr"] else ""
                last_html = (
                    "<div style='font-size:0.75rem;color:#6B7280;margin-bottom:6px;'>"
                    "Último: <b>" + str(h['kg']) + " kg × " + str(h['reps']) + " reps</b>"
                    " (" + h['date'] + ")" + pr_icon +
                    "</div>"
                )

            card_html = (
                "<div class='ex-wrap " + done_cls + "'>"
                "<div class='ex-top'>"
                "<div class='ex-name'>" + check_icon + " " + ex['nome'] + "</div>"
                "<div class='ex-sets-pill'>" + ex['series'] + "</div>"
                "</div>"
                "<div class='badges-row'>" + badges + "</div>"
                "<div class='ex-desc'>" + ex['desc'] + "</div>"
                + last_html +
                "<div class='alt-pill'>"
                "<div class='alt-lbl'>🔄 Academia cheia</div>"
                "<div class='alt-txt'>" + ex['alt'] + "</div>"
                "</div>"
                "<a class='yt-link' href='" + ex['gif'] + "' target='_blank'>🎬 Ver no YouTube ↗</a>"
                "</div>"
            )
            st.markdown(card_html, unsafe_allow_html=True)

            # log inline
            with st.expander(f"📝 Registrar {ex['nome']}", expanded=False):
                col_s, col_kg, col_r = st.columns(3)
                with col_s:
                    n_series = st.number_input("Séries", 1, 20, 3, key=f"s_{key}")
                with col_kg:
                    n_kg = st.number_input("Peso (kg)", 0.0, 300.0, 0.0, 2.5, key=f"kg_{key}")
                with col_r:
                    n_reps = st.number_input("Reps", 1, 100, 10, key=f"r_{key}")

                if st.button("💾  Salvar registro", key=f"log_{key}", use_container_width=True):
                    save_log(key, n_series, n_kg, n_reps)
                    st.session_state.checks[key] = True
                    st.toast(f"Registrado! {'🏆 Novo PR!' if get_log(key)[0]['is_pr'] else ''}", icon="💪")
                    st.rerun()

            new_val = st.checkbox(
                "Marcar como concluído",
                value=checked,
                key=f"cb_{key}",
            )
            if new_val != checked:
                st.session_state.checks[key] = new_val
                st.rerun()

# ─── TAB EVOLUÇÃO ─────────────────────────────────────
with tab_hist:
    st.markdown("""
    <div class="sec-hdr">
        <span class="sec-hdr-text">Histórico de Cargas</span>
        <div class="sec-hdr-line"></div>
    </div>
    """, unsafe_allow_html=True)

    has_any = False
    for day_key, d in TRAINING_PLAN.items():
        for bloco in d["blocos"]:
            for ex in bloco["exercicios"]:
                key = f"{day_key}_{ex['nome']}"
                hist = get_log(key)
                if not hist:
                    continue
                has_any = True

                pr_count = sum(1 for h in hist if h["is_pr"])
                best_kg  = max(h["kg"] for h in hist)

                with st.expander(f"**{ex['nome']}** · 🏆 {best_kg} kg máx", expanded=False):
                    # mini gráfico de evolução
                    if len(hist) >= 2:
                        import streamlit as _st
                        kgs  = [h["kg"]   for h in reversed(hist)]
                        reps = [h["reps"] for h in reversed(hist)]
                        dates = [h["date"] for h in reversed(hist)]
                        _st.line_chart(
                            {"Peso (kg)": kgs},
                            use_container_width=True,
                            height=140,
                        )

                    for h in hist:
                        pr_tag = "<span class='hist-pr'>PR</span>" if h["is_pr"] else ""
                        st.markdown(f"""
                        <div class="hist-entry">
                            <span class="hist-date">{h['date']}</span>
                            <span class="hist-vals">
                                {h['series']} séries · {h['kg']} kg · {h['reps']} reps {pr_tag}
                            </span>
                        </div>
                        """, unsafe_allow_html=True)

    if not has_any:
        st.markdown("""
        <div style="text-align:center; padding:40px 20px; color:#9CA3AF;">
            <div style="font-size:2.5rem; margin-bottom:12px;">📋</div>
            <div style="font-weight:600; font-size:0.95rem; margin-bottom:6px;">Nenhum registro ainda</div>
            <div style="font-size:0.8rem;">Registre seus pesos e reps na aba <b>Treino</b> para acompanhar sua evolução.</div>
        </div>
        """, unsafe_allow_html=True)

# ─── TAB VOLUME ───────────────────────────────────────
with tab_vol:
    weekly_vol: dict = {}
    for d in TRAINING_PLAN.values():
        for muscle, sets in d["volume"].items():
            weekly_vol[muscle] = weekly_vol.get(muscle, 0) + sets

    sorted_vol = sorted(weekly_vol.items(), key=lambda x: x[1], reverse=True)
    max_vol    = max(v for _, v in sorted_vol)

    palette = ["#EA580C","#F97316","#10B981","#3B82F6","#8B5CF6",
               "#EF4444","#F59E0B","#06B6D4","#84CC16","#EC4899","#14B8A6"]

    st.markdown("""
    <div class="sec-hdr">
        <span class="sec-hdr-text">Volume Semanal por Músculo</span>
        <div class="sec-hdr-line"></div>
    </div>
    <div style="font-size:0.75rem; color:#9CA3AF; margin-bottom:12px;">
        Faixa ideal de hipertrofia: <b style="color:#111827">10–20 séries/semana</b> por grupo muscular.
    </div>
    """, unsafe_allow_html=True)

    for i, (muscle, sets) in enumerate(sorted_vol):
        bar_pct = int((sets / max_vol) * 100)
        color   = palette[i % len(palette)]
        if sets < 10:   status, status_color = "⚠️ Abaixo", "#F59E0B"
        elif sets <= 20: status, status_color = "✅ Ideal",  "#10B981"
        else:            status, status_color = "🔥 Alto",   "#EF4444"

        st.markdown(f"""
        <div class="vol-card">
            <div class="vol-top">
                <span class="vol-muscle">{muscle}</span>
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="font-size:0.65rem;font-weight:700;color:{status_color}">{status}</span>
                    <span class="vol-num">{sets} séries</span>
                </div>
            </div>
            <div class="vol-bar-bg">
                <div class="vol-bar-fill" style="width:{bar_pct}%;background:{color};"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="legend-card">
        <div class="legend-title">Legenda de Métodos</div>
        <div class="legend-item">
            <span style="background:#FEE2E2;color:#DC2626;font-size:0.62rem;font-weight:700;padding:2px 8px;border-radius:99px;">Rest-Pause</span>
            Vai até a falha, descansa 10–15s, faz mais reps. Máximo recrutamento.
        </div>
        <div class="legend-item">
            <span style="background:#FEF3C7;color:#D97706;font-size:0.62rem;font-weight:700;padding:2px 8px;border-radius:99px;">Back-off</span>
            Após séries pesadas, reduz 30–40% da carga e soma volume extra.
        </div>
        <div class="legend-item">
            <span style="background:#D1FAE5;color:#059669;font-size:0.62rem;font-weight:700;padding:2px 8px;border-radius:99px;">Composto</span>
            Exercício multiarticular. Base do programa, alta carga neural.
        </div>
        <div class="legend-item">
            <span style="background:#EDE9FE;color:#7C3AED;font-size:0.62rem;font-weight:700;padding:2px 8px;border-radius:99px;">Isolador</span>
            Foco em um músculo. Prioriza amplitude e pico de contração.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────
st.markdown("""
<div style="text-align:center;margin-top:32px;padding-top:16px;
            border-top:1px solid #E5E7EB;font-size:0.65rem;color:#D1D5DB;">
    Iron Protocol v3.0 · Divisão A–B–C–D–E–F · 6 dias/semana · 120 min/sessão
</div>
""", unsafe_allow_html=True)
