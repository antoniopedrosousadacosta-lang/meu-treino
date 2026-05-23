import streamlit as st

st.set_page_config(
    page_title="Iron Protocol",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── LIGHT THEME CSS ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=DM+Sans:wght@400;500;700&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background-color: #f5f6fa !important;
    color: #1a1a2e !important;
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stSidebar"] { display: none !important; }
[data-testid="stMainBlockContainer"] { padding: 16px 12px 40px 12px !important; max-width: 680px !important; }

/* HEADER */
.app-header {
    background: linear-gradient(135deg, #e85d04 0%, #f48c06 100%);
    border-radius: 16px;
    padding: 20px 22px 16px 22px;
    margin-bottom: 18px;
}
.app-title {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 1.9rem;
    color: #ffffff;
    letter-spacing: -0.02em;
    line-height: 1;
    margin: 0;
}
.app-sub {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.8);
    margin-top: 4px;
    letter-spacing: 0.05em;
    font-weight: 500;
}

/* DAY HEADER CARD */
.day-card {
    background: #ffffff;
    border-radius: 14px;
    padding: 16px 18px;
    margin-bottom: 14px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.07);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.day-foco {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 1.15rem;
    color: #1a1a2e;
    line-height: 1.2;
}
.day-label {
    font-size: 0.7rem;
    font-weight: 600;
    color: #e85d04;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.day-duracao {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 1.4rem;
    color: #e85d04;
    text-align: right;
}
.dur-label {
    font-size: 0.65rem;
    color: #999;
    text-align: right;
    letter-spacing: 0.06em;
    font-weight: 500;
}

/* SECTION */
.section-header {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 0.78rem;
    color: #e85d04;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin: 20px 0 8px 2px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-line {
    flex: 1;
    height: 1px;
    background: #e8e8f0;
}

/* EXERCISE CARD */
.ex-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 10px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    border-left: 4px solid #e85d04;
    transition: box-shadow 0.15s;
}
.ex-card.done {
    border-left-color: #10b981;
    opacity: 0.65;
}
.ex-name {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    color: #1a1a2e;
    margin-bottom: 2px;
}
.ex-sets {
    font-size: 0.78rem;
    font-weight: 600;
    color: #e85d04;
    margin-bottom: 6px;
    font-family: 'Inter', monospace;
}
.badges { margin-bottom: 8px; }
.badge {
    display: inline-block;
    font-size: 0.6rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 99px;
    margin-right: 4px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.badge-rp  { background: #fee2e2; color: #dc2626; }
.badge-bo  { background: #fef3c7; color: #d97706; }
.badge-str { background: #d1fae5; color: #059669; }
.badge-iso { background: #ede9fe; color: #7c3aed; }

.ex-desc {
    font-size: 0.84rem;
    color: #555;
    line-height: 1.55;
    margin-bottom: 8px;
}
.alt-block {
    background: #fff7ed;
    border: 1px dashed #f48c06;
    border-radius: 8px;
    padding: 8px 12px;
    margin-bottom: 7px;
}
.alt-title {
    font-size: 0.62rem;
    font-weight: 700;
    color: #e85d04;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 3px;
}
.alt-text {
    font-size: 0.82rem;
    color: #92400e;
    line-height: 1.45;
}
.gif-link {
    font-size: 0.75rem;
    color: #6366f1;
    text-decoration: none;
    font-weight: 500;
}
.gif-link:hover { text-decoration: underline; }

/* PROGRESS */
.progress-wrap {
    background: #ffffff;
    border-radius: 12px;
    padding: 12px 16px;
    margin-bottom: 10px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}
.progress-bar-bg {
    background: #f0f0f5;
    border-radius: 99px;
    height: 8px;
    margin: 6px 0 4px 0;
    overflow: hidden;
}
.progress-bar-fill {
    height: 8px;
    border-radius: 99px;
    background: linear-gradient(90deg, #e85d04, #f48c06);
    transition: width 0.3s;
}
.progress-meta {
    display: flex;
    justify-content: space-between;
    font-size: 0.72rem;
    color: #888;
    font-weight: 500;
}

/* BUTTONS */
[data-testid="stColumns"] button {
    background: #ffffff !important;
    border: 1.5px solid #e8e8f0 !important;
    color: #444 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    border-radius: 8px !important;
    padding: 6px 12px !important;
}
[data-testid="stColumns"] button:hover {
    border-color: #e85d04 !important;
    color: #e85d04 !important;
}

/* SELECT BOX */
[data-testid="stSelectbox"] > div > div {
    background: #ffffff !important;
    border: 1.5px solid #e8e8f0 !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    color: #1a1a2e !important;
}

/* TABS */
[data-testid="stTabs"] button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    color: #888 !important;
}
[data-testid="stTabs"] button[aria-selected="true"] {
    color: #e85d04 !important;
    border-bottom-color: #e85d04 !important;
}

/* CHECKBOX */
[data-testid="stCheckbox"] label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.83rem !important;
    color: #555 !important;
    font-weight: 500 !important;
}

/* VOLUME */
.vol-row {
    background: #fff;
    border-radius: 10px;
    padding: 10px 14px;
    margin-bottom: 7px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.vol-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 5px;
}
.vol-muscle { font-weight: 600; font-size: 0.9rem; color: #1a1a2e; }
.vol-count { font-weight: 700; font-size: 0.85rem; color: #e85d04; }
.vol-mini-bar-bg { background: #f0f0f5; border-radius: 99px; height: 5px; }
.vol-mini-bar { height: 5px; border-radius: 99px; }

/* LEGEND CARD */
.legend-card {
    background: #fff;
    border-radius: 12px;
    padding: 14px 16px;
    margin-top: 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.legend-title {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 0.85rem;
    color: #1a1a2e;
    margin-bottom: 10px;
    letter-spacing: 0.03em;
}
.legend-item {
    font-size: 0.82rem;
    color: #555;
    margin-bottom: 6px;
    line-height: 1.4;
}

/* HIDE STREAMLIT UI */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
div[data-testid="stToolbar"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ─── DADOS DO TREINO ──────────────────────────────────────────────────────────
TRAINING_PLAN = {
    "Segunda — DIA A": {
        "foco": "Costas Largura + Bíceps",
        "duracao": "120 min",
        "emoji": "🔵",
        "blocos": [
            {
                "nome": "Compostos — Back-off Sets",
                "exercicios": [
                    {
                        "nome": "Barra Fixa Pronada (Pull-up)",
                        "series": "5 × MAX | Back-off: 3 × 6 c/ cinto",
                        "metodo": ["str", "bo"],
                        "desc": "Pegada aberta além dos ombros. Retração escapular total antes de puxar. Cotovelos apontam para baixo e para os lados. Pausa de 1s no topo. Back-off com anilha no cinto.",
                        "alt": "Remada Unilateral no Banco c/ Halter 35–40 kg — 4 × 10/lado, mesma retração escapular.",
                        "gif": "https://www.youtube.com/results?search_query=pull+up+form+bodybuilding",
                    },
                    {
                        "nome": "Remada Curvada na Barra (Pronada)",
                        "series": "4 × 8 pesado | Back-off: 1 × 15 leve",
                        "metodo": ["str", "bo"],
                        "desc": "Tronco a ~45°. Puxe a barra para o umbigo, cotovelos próximos ao tronco. Pausa de 1s na contração. Sem balanço de quadril. Back-off em 60% da carga.",
                        "alt": "Remada Curvada c/ Halteres 2 × 30 kg — 4 × 10, maior amplitude.",
                        "gif": "https://www.youtube.com/results?search_query=barbell+bent+over+row+form",
                    },
                ],
            },
            {
                "nome": "Largura — Isoladores + Rest-Pause",
                "exercicios": [
                    {
                        "nome": "Pullover com Halter",
                        "series": "3 × 12 | Rest-Pause no último set",
                        "metodo": ["iso", "rp"],
                        "desc": "Decúbito no banco, halter 20–25 kg. Arco amplo, cotovelo levemente flexionado. Sinta o alongamento do serrátil e grande dorsal. Rest-Pause: falha → 15s → 3–5 reps extras.",
                        "alt": "Pullover no chão com halter — mesmo movimento, amplitude menor mas seguro.",
                        "gif": "https://www.youtube.com/results?search_query=dumbbell+pullover+technique",
                    },
                    {
                        "nome": "Remada Unilateral no Banco",
                        "series": "3 × 12/lado | Rest-Pause no último set",
                        "metodo": ["iso", "rp"],
                        "desc": "Cotovelo em linha diagonal (não sobe em L). Puxe pensando no cotovelo. Pausa 1s no topo. Rest-Pause: falha → 15s → reps até nova falha.",
                        "alt": "Remada Cavalinho c/ Halter — apoio bilateral, mais estabilidade.",
                        "gif": "https://www.youtube.com/results?search_query=single+arm+dumbbell+row",
                    },
                ],
            },
            {
                "nome": "Bíceps — Rest-Pause",
                "exercicios": [
                    {
                        "nome": "Rosca Direta na Barra",
                        "series": "4 × 10 | Back-off: 1 × 20 EZ",
                        "metodo": ["iso", "bo"],
                        "desc": "Cotovelos fixos ao tronco. Supinação total no topo. Excêntrico de 3s. Back-off com barra EZ a 50% da carga: 20 reps pump.",
                        "alt": "Rosca Alternada c/ Halteres — 4 × 10/lado, amplitude e controle maiores.",
                        "gif": "https://www.youtube.com/results?search_query=barbell+curl+technique",
                    },
                    {
                        "nome": "Rosca Concentrada",
                        "series": "3 × 12/lado | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Cotovelo no joelho. Sem compensação de ombro. Pico de contração forçado no topo por 2s. Rest-Pause: falha → 15s → 4–5 reps.",
                        "alt": "Rosca Scott c/ Halter num lado do banco inclinado.",
                        "gif": "https://www.youtube.com/results?search_query=concentration+curl+technique",
                    },
                    {
                        "nome": "Rosca Martelo",
                        "series": "3 × 15 | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Pegada neutra (polegar para cima). Trabalha braquial e braquiorradial — espessura do braço. Alternada ou simultânea. Rest-Pause no último set.",
                        "alt": "Martelo na Corda (toalha ao redor do halter) — conforto no pulso.",
                        "gif": "https://www.youtube.com/results?search_query=hammer+curl+technique",
                    },
                ],
            },
        ],
        "volume": {"Costas": 15, "Bíceps": 10, "Serrátil": 3},
    },

    "Terça — DIA B": {
        "foco": "Ombros (Largura + Anterior) + Trapézio",
        "duracao": "120 min",
        "emoji": "🟠",
        "blocos": [
            {
                "nome": "Press Overhead — Back-off Sets",
                "exercicios": [
                    {
                        "nome": "Desenvolvimento Militar na Barra (em pé)",
                        "series": "5 × 5 pesado | Back-off: 2 × 10",
                        "metodo": ["str", "bo"],
                        "desc": "Pegada levemente além dos ombros. Core travado, glúteo contraído. Empurre sobre a cabeça, não para frente. Back-off: 60% da carga, 10 reps explosivas.",
                        "alt": "Desenvolvimento com Halteres sentado — 5 × 8 com até 35 kg/lado.",
                        "gif": "https://www.youtube.com/results?search_query=overhead+press+barbell+technique",
                    },
                    {
                        "nome": "Arnold Press",
                        "series": "4 × 10 | Back-off: 1 × 15",
                        "metodo": ["iso", "bo"],
                        "desc": "Começa com palmas para você. Rotaciona para fora enquanto sobe. Ativa as 3 porções do deltoide. Não trave os cotovelos. Back-off: halteres mais leves.",
                        "alt": "Press Unilateral com Halter — 4 × 12/lado, foco na rotação.",
                        "gif": "https://www.youtube.com/results?search_query=arnold+press+technique",
                    },
                ],
            },
            {
                "nome": "Lateral — Foco em Largura",
                "exercicios": [
                    {
                        "nome": "Elevação Lateral com Halteres",
                        "series": "5 × 15–20 | Rest-Pause nos 2 últimos",
                        "metodo": ["iso", "rp"],
                        "desc": "Halteres 10–15 kg. Polegar levemente para baixo (pronação). Sobe até paralelo, excêntrico de 3s. Rest-Pause: falha → 10s → 5 reps.",
                        "alt": "Elevação Lateral Unilateral apoiado na parede — isolamento total.",
                        "gif": "https://www.youtube.com/results?search_query=lateral+raise+technique+bodybuilding",
                    },
                    {
                        "nome": "Elevação Lateral Inclinada",
                        "series": "4 × 12/lado | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Segure em um poste com uma mão. Incline o corpo 20–30°. Eleve com o braço livre. Tensão constante no deltoide medial.",
                        "alt": "Elevação Lateral deitado de lado no banco — mesma ativação.",
                        "gif": "https://www.youtube.com/results?search_query=cable+lateral+raise+lean+away",
                    },
                ],
            },
            {
                "nome": "Trapézio + Posterior de Ombro",
                "exercicios": [
                    {
                        "nome": "Encolhimento com Barra (Shrug)",
                        "series": "4 × 15 | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Sobe o ombro direto para cima (não rotacione). Pausa de 2s no topo. Excêntrico de 3s. Rest-Pause no último set.",
                        "alt": "Shrug com Halteres 2 × 40 kg — amplitude maior e controle da rotação.",
                        "gif": "https://www.youtube.com/results?search_query=barbell+shrug+technique",
                    },
                    {
                        "nome": "Crucifixo Invertido com Halteres",
                        "series": "4 × 15 | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Sentado curvado. Halteres 10–15 kg. Abre os braços até paralelo. Pince as escápulas no topo. Deltoide posterior = equilíbrio e postura.",
                        "alt": "Crucifixo Invertido deitado pronado no banco — mais estabilidade.",
                        "gif": "https://www.youtube.com/results?search_query=rear+delt+fly+technique",
                    },
                ],
            },
        ],
        "volume": {"Ombro Medial": 18, "Ombro Anterior": 9, "Ombro Posterior": 8, "Trapézio": 8},
    },

    "Quarta — DIA C": {
        "foco": "Peito + Tríceps",
        "duracao": "120 min",
        "emoji": "🟢",
        "blocos": [
            {
                "nome": "Press Compostos — Back-off Sets",
                "exercicios": [
                    {
                        "nome": "Supino Reto na Barra",
                        "series": "5 × 5 | Back-off: 2 × 10",
                        "metodo": ["str", "bo"],
                        "desc": "Pegada 1,5× ombros. Arco lombar controlado. Desce até tocar o peito (excêntrico 3s). Empurra explosivo. Back-off em 60%.",
                        "alt": "Supino com Halteres 2 × 35–40 kg — amplitude maior, mais seguro.",
                        "gif": "https://www.youtube.com/results?search_query=bench+press+technique",
                    },
                    {
                        "nome": "Supino Inclinado com Halteres",
                        "series": "4 × 10 | Back-off: 1 × 15",
                        "metodo": ["str", "bo"],
                        "desc": "Banco a 30–45°. Halteres descem em linha com os ombros. Foco no peitoral superior. Back-off: 70% da carga, 15 reps com squeeze.",
                        "alt": "Crucifixo Inclinado com Halteres — 4 × 12, substitui se banco não disponível.",
                        "gif": "https://www.youtube.com/results?search_query=incline+dumbbell+press+technique",
                    },
                ],
            },
            {
                "nome": "Isoladores de Peito",
                "exercicios": [
                    {
                        "nome": "Crucifixo com Halteres",
                        "series": "4 × 12 | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Banco plano. Desce em arco amplo. Cotovelo levemente flexionado e fixo. Sinta o alongamento na parte inferior. Rest-Pause no último set.",
                        "alt": "Crucifixo em pé com halteres leves (10–12 kg) — mais ROM.",
                        "gif": "https://www.youtube.com/results?search_query=dumbbell+fly+chest+technique",
                    },
                ],
            },
            {
                "nome": "Tríceps — Rest-Pause + Back-off",
                "exercicios": [
                    {
                        "nome": "Tríceps Francês com Barra EZ",
                        "series": "4 × 12 | Back-off: 1 × 20",
                        "metodo": ["iso", "bo"],
                        "desc": "Deitado. Cotovelos fixos apontados para cima. Desce a barra atrás da cabeça. Máximo alongamento da cabeça longa. Back-off leve, 20 reps pump.",
                        "alt": "Tríceps Francês com Halter unilateral — 4 × 12/lado.",
                        "gif": "https://www.youtube.com/results?search_query=EZ+bar+skull+crusher+technique",
                    },
                    {
                        "nome": "Mergulho no Banco (Dips)",
                        "series": "4 × MAX | Back-off: 2 × 10 assistido",
                        "metodo": ["str", "bo"],
                        "desc": "Tronco ereto (foco no tríceps). Cotovelos paralelos. Desce até 90°. Back-off assistido ou com elástico.",
                        "alt": "Extensão Overhead com Halter + Kickback — superset 3 × 12.",
                        "gif": "https://www.youtube.com/results?search_query=tricep+dips+technique",
                    },
                    {
                        "nome": "Kickback com Halter",
                        "series": "3 × 15/lado | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Tronco paralelo ao chão, cotovelo fixo. Estende até bloquear. Pausa de 2s. Rest-Pause no último set.",
                        "alt": "Extensão de Tríceps Overhead com Halter bilateral — mais carga.",
                        "gif": "https://www.youtube.com/results?search_query=tricep+kickback+technique",
                    },
                ],
            },
        ],
        "volume": {"Peito": 16, "Tríceps": 13},
    },

    "Quinta — DIA D": {
        "foco": "Costas Densidade + Ombro Medial",
        "duracao": "120 min",
        "emoji": "🔵",
        "blocos": [
            {
                "nome": "Espessura de Costas — Back-off Sets",
                "exercicios": [
                    {
                        "nome": "Terra Romeno com Barra",
                        "series": "5 × 6 | Back-off: 2 × 10",
                        "metodo": ["str", "bo"],
                        "desc": "Quadril para trás, coluna neutra. Barra raspa a coxa. Sente o alongamento dos ísquios. Não arredonde a lombar. Back-off: 60%, 10 reps lentas.",
                        "alt": "Terra Romeno com Halteres 2 × 35–40 kg — maior controle.",
                        "gif": "https://www.youtube.com/results?search_query=romanian+deadlift+technique",
                    },
                    {
                        "nome": "Remada Alta na Barra (Upright Row)",
                        "series": "4 × 12 | Back-off: 1 × 15",
                        "metodo": ["str", "bo"],
                        "desc": "Pegada fechada. Cotovelos sobem acima dos ombros. Ativa trapézio médio + deltoide. Se sentir dor no ombro, alargue a pegada.",
                        "alt": "Remada Alta com Halteres — liberdade de movimento, menos impingimento.",
                        "gif": "https://www.youtube.com/results?search_query=upright+row+technique",
                    },
                ],
            },
            {
                "nome": "Densidade Dorsal — Rest-Pause",
                "exercicios": [
                    {
                        "nome": "Barra Fixa Supinada (Chin-up)",
                        "series": "4 × 8 | Rest-Pause no último",
                        "metodo": ["str", "rp"],
                        "desc": "Pegada supinada na largura dos ombros. Puxe os cotovelos para o chão. Mais bíceps que a pronada. Rest-Pause: falha → 15s → máximo.",
                        "alt": "Remada Curvada Supinada com Halteres — 4 × 10.",
                        "gif": "https://www.youtube.com/results?search_query=chin+up+supinated+technique",
                    },
                    {
                        "nome": "Remada T (Barra no Canto)",
                        "series": "4 × 10 | Rest-Pause",
                        "metodo": ["str", "rp"],
                        "desc": "Barra num canto com anilhas. Puxe para o peito com pegada neutra. Alta densidade de costas. Rest-Pause no último set.",
                        "alt": "Remada com Halteres Bilateral no Banco inclinado (pronado) — 4 × 12.",
                        "gif": "https://www.youtube.com/results?search_query=T-bar+row+technique",
                    },
                ],
            },
            {
                "nome": "Ombro Medial — Pump",
                "exercicios": [
                    {
                        "nome": "Elevação Lateral c/ Tempo (2-1-3)",
                        "series": "5 × 15 | Rest-Pause nos 2 últimos",
                        "metodo": ["iso", "rp"],
                        "desc": "Halteres 8–12 kg. Sobe em 1s, pausa 2s no topo, desce em 3s. Rest-Pause: falha → 10s → mais reps. Brutalmente eficaz.",
                        "alt": "Elevação Lateral Unilateral apoiado — controle total do movimento.",
                        "gif": "https://www.youtube.com/results?search_query=lateral+raise+tempo+technique",
                    },
                ],
            },
        ],
        "volume": {"Costas": 16, "Ombro Medial": 10, "Trapézio": 8, "Isquiotibiais": 6},
    },

    "Sexta — DIA E": {
        "foco": "Braços Completos (Bíceps + Tríceps + Antebraço)",
        "duracao": "120 min",
        "emoji": "🟣",
        "blocos": [
            {
                "nome": "Bíceps — Back-off + Rest-Pause",
                "exercicios": [
                    {
                        "nome": "Rosca Inclinada com Halteres",
                        "series": "4 × 10 | Rest-Pause nos 2 últimos",
                        "metodo": ["iso", "rp"],
                        "desc": "Banco inclinado a 45–60°. Braços pendurados atrás = máximo alongamento da cabeça longa. Supina completamente no topo. Excêntrico de 4s.",
                        "alt": "Rosca com apoio no banco inclinado (frente) — simula o ângulo de alongamento.",
                        "gif": "https://www.youtube.com/results?search_query=incline+dumbbell+curl+technique",
                    },
                    {
                        "nome": "Rosca 21s na Barra",
                        "series": "3 × 21 (7+7+7)",
                        "metodo": ["iso"],
                        "desc": "7 reps metade inferior + 7 reps metade superior + 7 reps completas. Sem pausa entre fases. Amplitude total, sem momentum.",
                        "alt": "21s com Halteres Alternado — mesma lógica, amplitude maior por braço.",
                        "gif": "https://www.youtube.com/results?search_query=21s+bicep+curl+technique",
                    },
                    {
                        "nome": "Rosca Concentrada (Scott Improvisado)",
                        "series": "3 × 12/lado | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Cotovelo no joelho. Supinação forçada no topo. Rest-Pause no último set de cada braço.",
                        "alt": "Rosca Presa no Rack — cotovelo no poste como apoio fixo.",
                        "gif": "https://www.youtube.com/results?search_query=preacher+curl+dumbbell",
                    },
                ],
            },
            {
                "nome": "Tríceps — Rest-Pause + Back-off",
                "exercicios": [
                    {
                        "nome": "Tríceps Overhead com Halter (Bilateral)",
                        "series": "4 × 12 | Back-off: 1 × 20",
                        "metodo": ["iso", "bo"],
                        "desc": "Sentado. Halter atrás da cabeça. Cotovelos para cima e fixos. Alonga a cabeça longa. Back-off: peso leve, 20 reps pump.",
                        "alt": "Overhead Unilateral — 4 × 12/lado, mais controle postural.",
                        "gif": "https://www.youtube.com/results?search_query=overhead+tricep+extension+dumbbell",
                    },
                    {
                        "nome": "Tríceps Testa com Halteres",
                        "series": "4 × 12 | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Deitado. Halteres descem ao lado das orelhas. Cotovelos fixos verticais. Foco no alongamento da cabeça longa. Rest-Pause no último set.",
                        "alt": "Extensão de Tríceps no Chão com Halteres — sem necessidade de banco.",
                        "gif": "https://www.youtube.com/results?search_query=lying+dumbbell+tricep+extension",
                    },
                ],
            },
            {
                "nome": "Antebraço — Finalizadores",
                "exercicios": [
                    {
                        "nome": "Rosca de Pulso (Wrist Curl)",
                        "series": "4 × 20 | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Antebraços nos joelhos, palmas para cima. Flexiona o pulso completamente. 20 reps, pausa de 1s no topo. Rest-Pause brutal no último set.",
                        "alt": "Wrist Curl na borda do banco — posição idêntica.",
                        "gif": "https://www.youtube.com/results?search_query=wrist+curl+forearm+exercise",
                    },
                    {
                        "nome": "Rosca Martelo Cruzado",
                        "series": "3 × 15/lado | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Halter cruza em direção ao ombro oposto. Ativa o braquiorradial de forma diferente do martelo convencional. Rest-Pause no último set.",
                        "alt": "Martelo Simultâneo com carga menor — foco na contração.",
                        "gif": "https://www.youtube.com/results?search_query=cross+body+hammer+curl",
                    },
                ],
            },
        ],
        "volume": {"Bíceps": 14, "Tríceps": 12, "Antebraço": 8},
    },

    "Sábado — DIA F": {
        "foco": "Pernas (Quadríceps + Posteriores + Glúteos + Panturrilha)",
        "duracao": "120 min",
        "emoji": "🔴",
        "blocos": [
            {
                "nome": "Compostos de Perna — Back-off Sets",
                "exercicios": [
                    {
                        "nome": "Agachamento Livre na Barra",
                        "series": "5 × 5 pesado | Back-off: 2 × 10",
                        "metodo": ["str", "bo"],
                        "desc": "Pés na largura dos ombros, pontas levemente para fora. Barra na parte alta do trapézio. Desça até coxa paralela ao chão. Joelhos acompanham a ponta do pé. Não deixe os calcanhares saírem do chão. Back-off em 60% da carga: 2 séries de 10 controladas.",
                        "alt": "Agachamento Goblet com Halter 30–40 kg — 5 × 10, postura mais vertical e fácil de executar sozinho.",
                        "gif": "https://www.youtube.com/results?search_query=barbell+squat+form+technique",
                    },
                    {
                        "nome": "Terra Convencional na Barra",
                        "series": "4 × 5 pesado | Back-off: 1 × 8",
                        "metodo": ["str", "bo"],
                        "desc": "Pés na largura do quadril. Barra sobre o meio do pé. Ombros levemente à frente da barra. Empurre o chão, não puxe a barra. Coluna neutra o tempo todo. Back-off: 70% da carga, foco na técnica.",
                        "alt": "Terra Sumô com Halteres 2 × 35–40 kg — postura mais aberta, menos estresse na lombar.",
                        "gif": "https://www.youtube.com/results?search_query=conventional+deadlift+form+technique",
                    },
                ],
            },
            {
                "nome": "Quadríceps — Isoladores + Rest-Pause",
                "exercicios": [
                    {
                        "nome": "Agachamento Búlgaro (Split Squat)",
                        "series": "4 × 10/lado | Rest-Pause no último",
                        "metodo": ["str", "rp"],
                        "desc": "Pé de trás no banco, pé da frente à frente do quadril. Desce o joelho traseiro em direção ao chão. Tronco levemente inclinado à frente. Ótimo para isolar cada perna. Rest-Pause: falha → 15s → mais reps.",
                        "alt": "Avanço com Halteres 2 × 20–25 kg — 4 × 12/lado, sem necessidade de banco.",
                        "gif": "https://www.youtube.com/results?search_query=bulgarian+split+squat+technique",
                    },
                    {
                        "nome": "Agachamento Sumô com Halter (Goblet)",
                        "series": "3 × 15 | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Pés mais afastados, pontas bem abertas. Halter seguro verticalmente na frente do peito. Desce profundo mantendo tronco ereto. Foco no glúteo e adutor. Rest-Pause no último set.",
                        "alt": "Agachamento Sumô com Barra — mesma amplitude, mais carga.",
                        "gif": "https://www.youtube.com/results?search_query=goblet+squat+sumo+technique",
                    },
                ],
            },
            {
                "nome": "Posteriores + Glúteos — Rest-Pause",
                "exercicios": [
                    {
                        "nome": "Stiff (Terra Romeno Unilateral)",
                        "series": "3 × 12/lado | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Em pé, um halter na mão oposta à perna de trabalho. Incline o tronco à frente enquanto a perna traseira sobe em linha reta. Ativa isquiotibiais e glúteo com equilíbrio. Rest-Pause no último set.",
                        "alt": "Terra Romeno Bilateral com Halteres 2 × 30 kg — 3 × 12, mais estabilidade.",
                        "gif": "https://www.youtube.com/results?search_query=single+leg+romanian+deadlift+technique",
                    },
                    {
                        "nome": "Elevação Pélvica com Barra (Hip Thrust)",
                        "series": "4 × 12 | Back-off: 1 × 20",
                        "metodo": ["str", "bo"],
                        "desc": "Costas apoiadas num banco, barra sobre o quadril (use toalha). Empurra o quadril para cima até formar uma linha reta joelho–quadril–ombro. Pausa de 2s no topo. Back-off leve com squeeze intenso.",
                        "alt": "Hip Thrust com Halteres 2 × 25–30 kg — 4 × 15, sem necessidade de barra.",
                        "gif": "https://www.youtube.com/results?search_query=hip+thrust+barbell+technique",
                    },
                ],
            },
            {
                "nome": "Panturrilha — Finalizadores",
                "exercicios": [
                    {
                        "nome": "Elevação de Panturrilha em Pé (Calf Raise)",
                        "series": "5 × 20 | Rest-Pause nos 2 últimos",
                        "metodo": ["iso", "rp"],
                        "desc": "Ponta do pé no degrau ou anilha. Amplitude total: desce até sentir o alongamento, sobe até o máximo. Pausa de 2s no topo. Panturrilha responde bem a volume alto. Rest-Pause brutal.",
                        "alt": "Calf Raise Unilateral segurando um halter — 5 × 15/lado, mais isolamento.",
                        "gif": "https://www.youtube.com/results?search_query=standing+calf+raise+technique",
                    },
                    {
                        "nome": "Calf Raise Sentado (Sóleo)",
                        "series": "4 × 20 | Rest-Pause",
                        "metodo": ["iso", "rp"],
                        "desc": "Sentado, anilha sobre os joelhos. Eleva os calcanhares. O sóleo (músculo profundo) só é ativado com joelho flexionado. Fundamental para panturrilha cheia. Rest-Pause no último set.",
                        "alt": "Calf Raise Sentado no banco com halter no joelho — idêntico.",
                        "gif": "https://www.youtube.com/results?search_query=seated+calf+raise+technique",
                    },
                ],
            },
        ],
        "volume": {"Quadríceps": 18, "Glúteos": 14, "Isquiotibiais": 12, "Panturrilha": 14},
    },
}

METHOD_COLORS = {
    "rp":  ("badge-rp",  "Rest-Pause"),
    "bo":  ("badge-bo",  "Back-off"),
    "str": ("badge-str", "Composto"),
    "iso": ("badge-iso", "Isolador"),
}

# ─── SESSION STATE ────────────────────────────────────────────────────────────
if "checks" not in st.session_state:
    st.session_state.checks = {}

# ─── HEADER ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class='app-header'>
    <div class='app-title'>⚡ Iron Protocol</div>
    <div class='app-sub'>Divisão A–B–C–D–E–F · Alta Performance · 6 Dias</div>
</div>
""", unsafe_allow_html=True)

# ─── SELECTOR + PROGRESSO ────────────────────────────────────────────────────
dias = list(TRAINING_PLAN.keys())
selected_day = st.selectbox("Dia:", options=dias, label_visibility="collapsed")

total_ex = sum(len(b["exercicios"]) for d in TRAINING_PLAN.values() for b in d["blocos"])
done_ex  = sum(1 for v in st.session_state.checks.values() if v)
pct = int((done_ex / total_ex) * 100) if total_ex else 0

st.markdown(f"""
<div class='progress-wrap'>
    <div class='progress-meta'>
        <span>Progresso semanal</span>
        <span><b>{done_ex}</b>/{total_ex} exercícios · <b>{pct}%</b></span>
    </div>
    <div class='progress-bar-bg'>
        <div class='progress-bar-fill' style='width:{pct}%'></div>
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 Resetar dia", use_container_width=True):
        for k in [k for k in st.session_state.checks if k.startswith(selected_day)]:
            del st.session_state.checks[k]
        st.toast("Dia resetado!", icon="✅")
with c2:
    if st.button("🗑️ Resetar semana", use_container_width=True):
        st.session_state.checks = {}
        st.toast("Semana zerada!", icon="♻️")

# ─── DIA HEADER ──────────────────────────────────────────────────────────────
day_data = TRAINING_PLAN[selected_day]
st.markdown(f"""
<div class='day-card'>
    <div>
        <div class='day-label'>{selected_day}</div>
        <div class='day-foco'>{day_data['emoji']} {day_data['foco']}</div>
    </div>
    <div>
        <div class='dur-label'>DURAÇÃO</div>
        <div class='day-duracao'>{day_data['duracao']}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── TABS ─────────────────────────────────────────────────────────────────────
tab_ex, tab_vol = st.tabs(["🏋️ Exercícios", "📊 Volume Semanal"])

with tab_ex:
    for bloco in day_data["blocos"]:
        st.markdown(f"""
        <div class='section-header'>
            {bloco['nome']}
            <div class='section-line'></div>
        </div>
        """, unsafe_allow_html=True)

        for ex in bloco["exercicios"]:
            key = f"{selected_day}_{ex['nome']}"
            checked = st.session_state.checks.get(key, False)
            done_cls = "done" if checked else ""

            badges = "".join(
                f"<span class='badge {METHOD_COLORS[m][0]}'>{METHOD_COLORS[m][1]}</span>"
                for m in ex.get("metodo", [])
                if m in METHOD_COLORS
            )
            check_icon = "✅" if checked else "🔲"

            st.markdown(f"""
            <div class='ex-card {done_cls}'>
                <div class='ex-name'>{check_icon} {ex['nome']}</div>
                <div class='ex-sets'>{ex['series']}</div>
                <div class='badges'>{badges}</div>
                <div class='ex-desc'>{ex['desc']}</div>
                <div class='alt-block'>
                    <div class='alt-title'>🔄 Academia cheia — variação</div>
                    <div class='alt-text'>{ex['alt']}</div>
                </div>
                <a class='gif-link' href='{ex['gif']}' target='_blank'>🎬 Ver demonstração no YouTube ↗</a>
            </div>
            """, unsafe_allow_html=True)

            new_val = st.checkbox(
                f"Concluído: {ex['nome']}",
                value=checked,
                key=f"cb_{key}",
            )
            st.session_state.checks[key] = new_val

with tab_vol:
    weekly_vol: dict = {}
    for d in TRAINING_PLAN.values():
        for muscle, sets in d["volume"].items():
            weekly_vol[muscle] = weekly_vol.get(muscle, 0) + sets

    sorted_vol = sorted(weekly_vol.items(), key=lambda x: x[1], reverse=True)
    max_vol = max(v for _, v in sorted_vol)

    priority = {"Ombro Medial", "Bíceps", "Tríceps", "Costas", "Trapézio",
                "Ombro Anterior", "Ombro Posterior", "Quadríceps", "Glúteos",
                "Isquiotibiais", "Panturrilha"}

    palette = ["#e85d04","#f48c06","#10b981","#6366f1","#ec4899",
               "#0ea5e9","#84cc16","#f43f5e","#a855f7","#14b8a6","#f59e0b"]

    st.markdown("""
    <div style='font-size:0.8rem; color:#888; margin-bottom:14px; line-height:1.5;'>
        Volume total por grupo muscular (séries/semana). Faixa ideal de crescimento: <b>10–20 séries</b>.
    </div>
    """, unsafe_allow_html=True)

    for i, (muscle, sets) in enumerate(sorted_vol):
        bar_pct = int((sets / max_vol) * 100)
        color = palette[i % len(palette)]
        tag = "✅" if 10 <= sets <= 20 else ("⚠️" if sets < 10 else "🔥")
        st.markdown(f"""
        <div class='vol-row'>
            <div class='vol-top'>
                <span class='vol-muscle'>{tag} {muscle}</span>
                <span class='vol-count'>{sets} séries</span>
            </div>
            <div class='vol-mini-bar-bg'>
                <div class='vol-mini-bar' style='width:{bar_pct}%; background:{color};'></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class='legend-card'>
        <div class='legend-title'>📌 Legenda de Métodos de Treino</div>
        <div class='legend-item'>🔴 <b>Rest-Pause</b> — vai até a falha, descansa 10–15s, faz mais reps. Máximo recrutamento muscular em isoladores.</div>
        <div class='legend-item'>🟡 <b>Back-off Sets</b> — após séries pesadas, reduz 30–40% da carga e soma mais volume. Usado nos compostos.</div>
        <div class='legend-item'>🟢 <b>Composto</b> — exercício multiarticular. Base do programa, alta carga, grande estímulo neural.</div>
        <div class='legend-item'>🟣 <b>Isolador</b> — foco em um músculo específico. Prioriza amplitude máxima e pico de contração.</div>
        <div class='legend-item' style='margin-top:8px; color:#555;'>✅ Volume ideal (10–20 séries) &nbsp;|&nbsp; ⚠️ Abaixo do mínimo &nbsp;|&nbsp; 🔥 Acima (fase de especialização)</div>
    </div>
    """, unsafe_allow_html=True)

# ─── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; margin-top:36px; padding-top:16px;
            border-top:1px solid #e8e8f0; font-size:0.7rem; color:#bbb;'>
    Iron Protocol v2.0 · Divisão A–B–C–D–E–F · 6 dias · 120 min/sessão
</div>
""", unsafe_allow_html=True)
