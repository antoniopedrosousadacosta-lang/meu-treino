import streamlit as st
import json

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="IRON PROTOCOL",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── DARK MODE CSS ──────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rajdhani:wght@400;600;700&family=Share+Tech+Mono&display=swap');

/* RESET & BASE */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0a0a0f !important;
    color: #e8e8f0 !important;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0d1a 0%, #0a0a12 100%) !important;
    border-right: 1px solid #ff3d00 !important;
}
[data-testid="stSidebar"] * { color: #e8e8f0 !important; }

/* HEADER */
.iron-header {
    font-family: 'Bebas Neue', cursive;
    font-size: clamp(2.5rem, 8vw, 5rem);
    letter-spacing: 0.12em;
    background: linear-gradient(135deg, #ff3d00 0%, #ff8c00 50%, #ffd700 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    line-height: 1;
}
.iron-sub {
    font-family: 'Share Tech Mono', monospace;
    color: #ff3d00;
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-top: 4px;
}

/* CARDS */
.day-badge {
    font-family: 'Bebas Neue', cursive;
    font-size: 0.85rem;
    letter-spacing: 0.2em;
    color: #ff3d00;
    border: 1px solid #ff3d0044;
    padding: 2px 10px;
    border-radius: 2px;
    display: inline-block;
    margin-bottom: 8px;
}
.section-title {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.6rem;
    letter-spacing: 0.1em;
    color: #ffd700;
    border-bottom: 2px solid #ff3d0066;
    padding-bottom: 4px;
    margin-top: 20px;
    margin-bottom: 10px;
}
.exercise-card {
    background: linear-gradient(135deg, #111118 0%, #15151f 100%);
    border: 1px solid #1e1e2e;
    border-left: 3px solid #ff3d00;
    border-radius: 6px;
    padding: 14px 16px;
    margin-bottom: 10px;
    transition: border-color 0.2s;
}
.exercise-card:hover { border-left-color: #ffd700; }
.exercise-name {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 700;
    font-size: 1.05rem;
    color: #ffffff;
    letter-spacing: 0.05em;
}
.exercise-sets {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.78rem;
    color: #ff8c00;
    margin-top: 2px;
}
.exercise-tech {
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.88rem;
    color: #9090b0;
    margin-top: 6px;
    line-height: 1.5;
}
.alt-box {
    background: #0d0d1a;
    border: 1px dashed #ff3d0055;
    border-radius: 4px;
    padding: 8px 10px;
    margin-top: 8px;
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.84rem;
    color: #ffb347;
}
.alt-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.68rem;
    color: #ff3d00;
    letter-spacing: 0.15em;
    display: block;
    margin-bottom: 2px;
}
.gif-placeholder {
    background: #0a0a12;
    border: 1px solid #1e1e2e;
    border-radius: 4px;
    padding: 6px 12px;
    margin-top: 6px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.72rem;
    color: #4040cc;
}
.gif-placeholder a { color: #6060ff; text-decoration: none; }
.gif-placeholder a:hover { color: #8888ff; text-decoration: underline; }

/* METHOD BADGES */
.method-badge {
    display: inline-block;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.62rem;
    padding: 2px 7px;
    border-radius: 2px;
    margin-right: 5px;
    margin-top: 4px;
    letter-spacing: 0.1em;
}
.badge-rp  { background: #ff3d0022; color: #ff6644; border: 1px solid #ff3d0055; }
.badge-bo  { background: #ffd70022; color: #ffd700; border: 1px solid #ffd70055; }
.badge-str { background: #00ff8822; color: #00ff88; border: 1px solid #00ff8855; }
.badge-iso { background: #aa44ff22; color: #cc88ff; border: 1px solid #aa44ff55; }

/* VOLUME PANEL */
.vol-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid #1e1e2e;
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.95rem;
}
.vol-muscle { color: #e8e8f0; font-weight: 600; }
.vol-count {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.9rem;
    color: #ff8c00;
}
.vol-bar {
    height: 4px;
    border-radius: 2px;
    background: linear-gradient(90deg, #ff3d00, #ffd700);
    margin-top: 4px;
}

/* SIDEBAR BUTTONS */
div[data-testid="stSidebar"] button {
    background: #0d0d1a !important;
    border: 1px solid #ff3d0066 !important;
    color: #ff3d00 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    width: 100%;
}
div[data-testid="stSidebar"] button:hover {
    border-color: #ffd700 !important;
    color: #ffd700 !important;
}

/* CHECKBOX STYLE */
[data-testid="stCheckbox"] label {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.9rem !important;
    color: #e8e8f0 !important;
}

/* HIDE STREAMLIT BRANDING */
#MainMenu, footer, header { visibility: hidden; }

/* SCROLLBAR */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #ff3d00; border-radius: 2px; }
</style>
""", unsafe_allow_html=True)

# ─── TREINO DATA ─────────────────────────────────────────────────────────────

TRAINING_PLAN = {
    "Segunda — DIA A": {
        "foco": "COSTAS (LARGURA) + BÍCEPS",
        "duracao": "120 min",
        "blocos": [
            {
                "nome": "BLOCO 1 — COMPOSTOS (Back-off Sets)",
                "exercicios": [
                    {
                        "nome": "Barra Fixa Pronada (Pull-up)",
                        "series": "5x MAX | Back-off: 3x6 com cinto",
                        "metodo": ["bo", "str"],
                        "metodo_label": ["BACK-OFF", "COMPOSTO"],
                        "desc": "Pegada aberta (além dos ombros). Retração escapular total antes de puxar. Cotovelos apontando para baixo e para os lados. Pausa de 1s no topo. Back-off sets: adicione cinto com anilha para controlar o volume.",
                        "alt": "Remada Unilateral no Banco c/ Halter 35-40kg — 4x10/lado (mesma retração escapular)",
                        "gif": "https://www.youtube.com/results?search_query=pull+up+form+bodybuilding",
                    },
                    {
                        "nome": "Remada Curvada na Barra (Pronada)",
                        "series": "4x8 pesado | Back-off: 1x15 leve",
                        "metodo": ["bo", "str"],
                        "metodo_label": ["BACK-OFF", "COMPOSTO"],
                        "desc": "Tronco a ~45°. Puxe a barra para o umbigo, cotovelos próximos ao tronco. Pausa de 1s na contração. Sem balanço de quadril. Back-off set em 60% da carga máxima.",
                        "alt": "Remada Curvada c/ Halteres 2x30kg — 4x10 (maior amplitude de movimento)",
                        "gif": "https://www.youtube.com/results?search_query=barbell+bent+over+row+form",
                    },
                ]
            },
            {
                "nome": "BLOCO 2 — LARGURA (Isoladores + Rest-Pause)",
                "exercicios": [
                    {
                        "nome": "Pullover com Halter",
                        "series": "3x12 | Rest-Pause final",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Decúbito no banco, halter 20-25kg. Arco amplo, cotovelo levemente flexionado. Sinta o alongamento do serrátil e grande dorsal. Rest-Pause: falha > descanso 15s > 3-5 reps extras.",
                        "alt": "Pullover no chão com halter — mesmo movimento, menor amplitude mas seguro",
                        "gif": "https://www.youtube.com/results?search_query=dumbbell+pullover+technique",
                    },
                    {
                        "nome": "Remada Unilateral no Banco",
                        "series": "3x12/lado | Rest-Pause final",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Cotovelo traça linha diagonal (não sobe em L). Puxe pensando no cotovelo, não na mão. Pausa 1s em cima. Rest-Pause no último set: falha > 15s > reps até nova falha.",
                        "alt": "Remada Cavalinho c/ Halter — apoio bilateral, mais estabilidade em academia cheia",
                        "gif": "https://www.youtube.com/results?search_query=single+arm+dumbbell+row",
                    },
                ]
            },
            {
                "nome": "BLOCO 3 — BÍCEPS (Isoladores + Rest-Pause)",
                "exercicios": [
                    {
                        "nome": "Rosca Direta na Barra",
                        "series": "4x10 | Back-off: 1x20 EZ",
                        "metodo": ["bo", "iso"],
                        "metodo_label": ["BACK-OFF", "ISOLADOR"],
                        "desc": "Cotovelos fixos ao longo do tronco. Supinação total no topo. Excêntrico de 3s. Back-off com barra EZ a 50% da carga: 20 reps pump.",
                        "alt": "Rosca Alternada c/ Halteres — 4x10/lado, permite maior amplitude e controle",
                        "gif": "https://www.youtube.com/results?search_query=barbell+curl+technique",
                    },
                    {
                        "nome": "Rosca Concentrada",
                        "series": "3x12/lado | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Cotovelo no joelho. Sem compensação de ombro. Pico de contração forçado no topo por 2s. Rest-Pause: falha > 15s > 4-5 reps. Queima garantida.",
                        "alt": "Rosca Scott c/ Halter num lado do banco inclinado — simula a máquina",
                        "gif": "https://www.youtube.com/results?search_query=concentration+curl+technique",
                    },
                    {
                        "nome": "Rosca Martelo",
                        "series": "3x15 | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Neutro (polegar para cima). Trabalha braquial e braquiorradial — dá espessura ao braço. Alternada ou simultânea. Rest-Pause no último set.",
                        "alt": "Martelo na Corda (simule com toalha ao redor do halter) — mais conforto no pulso",
                        "gif": "https://www.youtube.com/results?search_query=hammer+curl+technique",
                    },
                ]
            },
        ],
        "volume": {"Costas": 15, "Bíceps": 10, "Serrátil": 3},
    },

    "Terça — DIA B": {
        "foco": "OMBROS (LARGURA + ANTERIOR) + TRAPÉZIO",
        "duracao": "120 min",
        "blocos": [
            {
                "nome": "BLOCO 1 — PRESS OVERHEAD (Back-off Sets)",
                "exercicios": [
                    {
                        "nome": "Desenvolvimento Militar na Barra (em pé)",
                        "series": "5x5 pesado | Back-off: 2x10",
                        "metodo": ["bo", "str"],
                        "metodo_label": ["BACK-OFF", "COMPOSTO"],
                        "desc": "Pegada levemente além dos ombros. Core braced, glúteo contraído. Empurre a barra sobre a cabeça, não para frente. Back-off: 60% da carga, 10 reps explosivas.",
                        "alt": "Desenvolvimento com Halteres sentado — 5x8 com halteres até 35kg/lado",
                        "gif": "https://www.youtube.com/results?search_query=overhead+press+barbell+technique",
                    },
                    {
                        "nome": "Arnold Press",
                        "series": "4x10 | Back-off: 1x15",
                        "metodo": ["bo", "iso"],
                        "metodo_label": ["BACK-OFF", "ISOLADOR"],
                        "desc": "Começa com palmas para você (como rosca). Rotaciona para fora enquanto sobe. Ativa as 3 porções do deltoide. Não trave os cotovelos no topo. Back-off: halteres mais leves.",
                        "alt": "Press Unilateral com Halter — foco na rotação, 4x12/lado",
                        "gif": "https://www.youtube.com/results?search_query=arnold+press+technique",
                    },
                ]
            },
            {
                "nome": "BLOCO 2 — LATERAL (Foco em Largura)",
                "exercicios": [
                    {
                        "nome": "Elevação Lateral com Halteres",
                        "series": "5x15-20 | Rest-Pause nos 2 últimos",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Halteres 10-15kg. Cotovelo levemente flexionado. Polegar levemente para baixo (pronação). Sobe até paralelo, excêntrico de 3s. Rest-Pause: falha > 10s > 5 reps.",
                        "alt": "Elevação Lateral Unilateral apoiado na parede — permite isolamento total",
                        "gif": "https://www.youtube.com/results?search_query=lateral+raise+technique+bodybuilding",
                    },
                    {
                        "nome": "Elevação Lateral Inclinada (Crucifixo Lateral)",
                        "series": "4x12/lado | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Segure em um poste/rack com uma mão. Incline o corpo 20-30°. Eleve o halter com o braço livre. Tensão constante no deltoide medial. Mágico para largura.",
                        "alt": "Elevação Lateral com Halter deitado de lado no banco — mesma ativação",
                        "gif": "https://www.youtube.com/results?search_query=cable+lateral+raise+lean+away",
                    },
                ]
            },
            {
                "nome": "BLOCO 3 — TRAPÉZIO + POSTERIOR DE OMBRO",
                "exercicios": [
                    {
                        "nome": "Encolhimento com Barra (Shrug)",
                        "series": "4x15 | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Agarre largo. Sobe o ombro direto para cima (não rotacione). Pausa de 2s no topo. Excêntrico controlado de 3s. Rest-Pause no último set.",
                        "alt": "Shrug com Halteres (2x40kg) — maior amplitude e controle da rotação",
                        "gif": "https://www.youtube.com/results?search_query=barbell+shrug+technique",
                    },
                    {
                        "nome": "Crucifixo Invertido com Halteres",
                        "series": "4x15 | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Sentado curvado para frente. Halteres 10-15kg. Abra os braços em arco até paralelo. Pince as escápulas no topo. Deltoide posterior = equilíbrio e postura.",
                        "alt": "Crucifixo Invertido deitado pronado no banco — maior estabilidade",
                        "gif": "https://www.youtube.com/results?search_query=rear+delt+fly+technique",
                    },
                ]
            },
        ],
        "volume": {"Ombro Medial": 18, "Ombro Anterior": 9, "Ombro Posterior": 8, "Trapézio": 8},
    },

    "Quarta — DIA C": {
        "foco": "PEITO + TRÍCEPS",
        "duracao": "120 min",
        "blocos": [
            {
                "nome": "BLOCO 1 — PRESS COMPOSTOS (Back-off Sets)",
                "exercicios": [
                    {
                        "nome": "Supino Reto na Barra",
                        "series": "5x5 | Back-off: 2x10",
                        "metodo": ["bo", "str"],
                        "metodo_label": ["BACK-OFF", "COMPOSTO"],
                        "desc": "Pegada 1,5x ombros. Arco lombar controlado. Desce até tocar o peito (excêntrico 3s). Empurra explosivo. Back-off em 60%: 2 séries de 10 para pump e volume.",
                        "alt": "Supino com Halteres 2x35-40kg — amplitude maior, mais estabilidade natural",
                        "gif": "https://www.youtube.com/results?search_query=bench+press+technique+powerlifting",
                    },
                    {
                        "nome": "Supino Inclinado com Halteres",
                        "series": "4x10 | Back-off: 1x15",
                        "metodo": ["bo", "iso"],
                        "metodo_label": ["BACK-OFF", "ISOLADOR"],
                        "desc": "Banco a 30-45°. Halteres descem em linha com os ombros. Foco no peitoral superior. Back-off: reduz 30% da carga, 15 reps com squeeze no topo.",
                        "alt": "Crucifixo Inclinado com Halteres — 4x12, substitui se banco inclinado não estiver disponível",
                        "gif": "https://www.youtube.com/results?search_query=incline+dumbbell+press+technique",
                    },
                ]
            },
            {
                "nome": "BLOCO 2 — ISOLADORES DE PEITO",
                "exercicios": [
                    {
                        "nome": "Crucifixo com Halteres",
                        "series": "4x12 | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Banco plano. Desça os halteres em arco amplo. Cotovelo fixo levemente flexionado. Sinta o alongamento na parte inferior do movimento. Rest-Pause no último set.",
                        "alt": "Crucifixo em pé com halteres leves (10-12kg) — mais ROM, menos peso",
                        "gif": "https://www.youtube.com/results?search_query=dumbbell+fly+chest+technique",
                    },
                ]
            },
            {
                "nome": "BLOCO 3 — TRÍCEPS (Isoladores + Rest-Pause)",
                "exercicios": [
                    {
                        "nome": "Tríceps Francês com Barra EZ",
                        "series": "4x12 | Back-off: 1x20",
                        "metodo": ["bo", "iso"],
                        "metodo_label": ["BACK-OFF", "ISOLADOR"],
                        "desc": "Deitado no banco. Cotovelos apontados para cima, fixos. Desce a barra atrás da cabeça. Máximo alongamento da cabeça longa. Back-off com peso leve, 20 reps pump.",
                        "alt": "Tríceps Francês com Halter (skull crusher unilateral) — 4x12/lado",
                        "gif": "https://www.youtube.com/results?search_query=EZ+bar+skull+crusher+technique",
                    },
                    {
                        "nome": "Mergulho no Banco (Dips)",
                        "series": "4x MAX | Back-off: 2x10 assistido",
                        "metodo": ["bo", "str"],
                        "metodo_label": ["BACK-OFF", "COMPOSTO"],
                        "desc": "Tronco ereto (foco no tríceps). Cotovelos paralelos. Desce até ângulo de 90°. Se não tiver paralelas: use costas de dois bancos. Back-off assistido ou com elástico.",
                        "alt": "Tríceps com Halter na Testa (unilateral) + Extensão Overhead com Halter — superset",
                        "gif": "https://www.youtube.com/results?search_query=tricep+dips+technique",
                    },
                    {
                        "nome": "Kickback com Halter",
                        "series": "3x15/lado | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Tronco paralelo ao chão, cotovelo fixo ao lado do tronco. Estende até bloquear completamente. Pausa de 2s. Rest-Pause no último set para queimar as fibras restantes.",
                        "alt": "Extensão de Tríceps Overhead com Halter bilateral — mais carga, mesmo conceito",
                        "gif": "https://www.youtube.com/results?search_query=tricep+kickback+technique",
                    },
                ]
            },
        ],
        "volume": {"Peito": 16, "Tríceps": 13},
    },

    "Quinta — DIA D": {
        "foco": "COSTAS (DENSIDADE) + OMBRO MEDIAL",
        "duracao": "120 min",
        "blocos": [
            {
                "nome": "BLOCO 1 — ESPESSURA DE COSTAS (Back-off Sets)",
                "exercicios": [
                    {
                        "nome": "Terra Romeno com Barra",
                        "series": "5x6 | Back-off: 2x10",
                        "metodo": ["bo", "str"],
                        "metodo_label": ["BACK-OFF", "COMPOSTO"],
                        "desc": "Quadril para trás, coluna neutra. Barra raspa a canela/coxa. Sente o alongamento dos ísquios. Não arredonde a lombar. Back-off: 60% da carga, 10 reps lentas.",
                        "alt": "Terra Romeno com Halteres 2x35-40kg — maior controle da trajetória",
                        "gif": "https://www.youtube.com/results?search_query=romanian+deadlift+technique",
                    },
                    {
                        "nome": "Remada Alta na Barra (Upright Row)",
                        "series": "4x12 | Back-off: 1x15",
                        "metodo": ["bo", "str"],
                        "metodo_label": ["BACK-OFF", "COMPOSTO"],
                        "desc": "Pegada fechada (1 punho de distância). Cotovelos sobem ACIMA dos ombros. Ativa trapézio médio + deltoide. Evite dor: se sentir no ombro, alargue a pegada.",
                        "alt": "Remada Alta com Halteres — maior liberdade de movimento, menos impingimento",
                        "gif": "https://www.youtube.com/results?search_query=upright+row+technique",
                    },
                ]
            },
            {
                "nome": "BLOCO 2 — DENSIDADE DORSAL (Rest-Pause)",
                "exercicios": [
                    {
                        "nome": "Barra Fixa Supinada (Chin-up)",
                        "series": "4x8 | Rest-Pause final",
                        "metodo": ["rp", "str"],
                        "metodo_label": ["REST-PAUSE", "COMPOSTO"],
                        "desc": "Pegada supinada na largura dos ombros. Foco em puxar os cotovelos para o chão. Ativa mais o bíceps que a pronada. Rest-Pause no último set: falha > 15s > máximo.",
                        "alt": "Remada Curvada Supinada com Halteres — 4x10, foco na parte inferior do dorsal",
                        "gif": "https://www.youtube.com/results?search_query=chin+up+supinated+technique",
                    },
                    {
                        "nome": "Remada Cavalinho com Barra T",
                        "series": "4x10 | Rest-Pause",
                        "metodo": ["rp", "str"],
                        "metodo_label": ["REST-PAUSE", "COMPOSTO"],
                        "desc": "Coloque a barra num canto. Adicione anilhas. Puxe para o peito com pegada neutra. Alta densidade e espessura. Se não tiver suporte: use o canto da academia.",
                        "alt": "Remada com Halteres Bilateral no Banco inclinado (pronado) — 4x12",
                        "gif": "https://www.youtube.com/results?search_query=T-bar+row+technique",
                    },
                ]
            },
            {
                "nome": "BLOCO 3 — OMBRO MEDIAL (Pump)",
                "exercicios": [
                    {
                        "nome": "Elevação Lateral c/ Pausa (Tempo)",
                        "series": "5x15 | Rest-Pause nos 2 últimos",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Halteres leves (8-12kg). Sobe em 1s, pausa 2s no topo, desce em 3s. Brutaliza as fibras de resistência do deltoide medial. Rest-Pause: falha > 10s > mais reps.",
                        "alt": "Elevação Lateral com garrafa d'água cheia de areia — se academia super lotada",
                        "gif": "https://www.youtube.com/results?search_query=lateral+raise+tempo+technique",
                    },
                ]
            },
        ],
        "volume": {"Costas": 16, "Ombro Medial": 10, "Trapézio": 8, "Isquiotibiais": 6},
    },

    "Sexta — DIA E": {
        "foco": "BRAÇOS COMPLETOS (BÍCEPS + TRÍCEPS) + ANTEBRAÇO",
        "duracao": "120 min",
        "blocos": [
            {
                "nome": "BLOCO 1 — BÍCEPS PESADO (Back-off + Rest-Pause)",
                "exercicios": [
                    {
                        "nome": "Rosca Inclinada com Halteres",
                        "series": "4x10 | Rest-Pause nos 2 últimos",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Banco inclinado a 45-60°. Braços pendurados atrás do corpo = alongamento máximo da cabeça longa. Supina completamente no topo. Excêntrico de 4s. Rest-Pause brutaliza o pico.",
                        "alt": "Rosca com apoio no banco inclinado (frente) — simula o ângulo de alongamento",
                        "gif": "https://www.youtube.com/results?search_query=incline+dumbbell+curl+technique",
                    },
                    {
                        "nome": "Rosca 21s na Barra",
                        "series": "3x21 (7+7+7)",
                        "metodo": ["iso"],
                        "metodo_label": ["INTENSIDADE"],
                        "desc": "7 reps metade inferior (baixo → 90°) + 7 reps metade superior (90° → topo) + 7 reps completas. Sem pausa entre as 3 fases. Destroça o bíceps em amplitude total.",
                        "alt": "21s com Halteres Alternado — mesmo conceito, maior amplitude por braço",
                        "gif": "https://www.youtube.com/results?search_query=21s+bicep+curl+technique",
                    },
                    {
                        "nome": "Rosca Direta c/ Halter (Unilateral)",
                        "series": "3x12/lado | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Cotovelo no joelho (Scott improvisado). Supinação forçada no topo. Rest-Pause no último set de cada braço. Foco no pico de contração.",
                        "alt": "Rosca Presa no Rack (barra) — 3x12, cotovelo no poste como apoio",
                        "gif": "https://www.youtube.com/results?search_query=preacher+curl+dumbbell",
                    },
                ]
            },
            {
                "nome": "BLOCO 2 — TRÍCEPS VOLUME (Rest-Pause + Back-off)",
                "exercicios": [
                    {
                        "nome": "Tríceps Overhead com Halter (Bilateral)",
                        "series": "4x12 | Back-off: 1x20",
                        "metodo": ["bo", "iso"],
                        "metodo_label": ["BACK-OFF", "ISOLADOR"],
                        "desc": "Sentado. Halter atrás da cabeça com ambas as mãos. Cotovelos apontados para cima. Alonga completamente a cabeça longa. Não deixe os cotovelos alargarem. Back-off: peso leve, 20 reps.",
                        "alt": "Tríceps Overhead Unilateral — 4x12/lado, mais controle de postura",
                        "gif": "https://www.youtube.com/results?search_query=overhead+tricep+extension+dumbbell",
                    },
                    {
                        "nome": "Tríceps Testa com Halteres",
                        "series": "4x12 | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Deitado. Halteres descem ao lado das orelhas. Cotovelos fixos verticais. Foca no alongamento da cabeça longa. Rest-Pause no último set.",
                        "alt": "Extensão de Tríceps no Chão com Halteres — elimina necessidade do banco",
                        "gif": "https://www.youtube.com/results?search_query=lying+dumbbell+tricep+extension",
                    },
                ]
            },
            {
                "nome": "BLOCO 3 — ANTEBRAÇO + FINALIZADORES",
                "exercicios": [
                    {
                        "nome": "Rosca Punho (Wrist Curl) com Halteres",
                        "series": "4x20 | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Sentado, antebraços nos joelhos (palmas para cima). Flexiona o pulso completamente. Amplitude máxima. 20 reps com pausa de 1s no topo. Rest-Pause brutal no último set.",
                        "alt": "Wrist Curl na borda do banco — mesma posição, referência fixa",
                        "gif": "https://www.youtube.com/results?search_query=wrist+curl+forearm+exercise",
                    },
                    {
                        "nome": "Rosca Martelo Cruzado",
                        "series": "3x15/lado | Rest-Pause",
                        "metodo": ["rp", "iso"],
                        "metodo_label": ["REST-PAUSE", "ISOLADOR"],
                        "desc": "Halter cruza o corpo em direção ao ombro oposto. Ativa o braquiorradial de forma diferente do martelo convencional. Rest-Pause no último set de cada lado.",
                        "alt": "Martelo Simultâneo com menor carga — foco na contração, menos no peso",
                        "gif": "https://www.youtube.com/results?search_query=cross+body+hammer+curl",
                    },
                ]
            },
        ],
        "volume": {"Bíceps": 14, "Tríceps": 12, "Antebraço": 8},
    },
}

METHOD_COLORS = {
    "rp": ("badge-rp", "REST-PAUSE"),
    "bo": ("badge-bo", "BACK-OFF"),
    "str": ("badge-str", "COMPOSTO"),
    "iso": ("badge-iso", "ISOLADOR"),
}

# ─── SESSION STATE ────────────────────────────────────────────────────────────
if "checks" not in st.session_state:
    st.session_state.checks = {}

# ─── HEADER ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style='padding: 10px 0 20px 0;'>
    <div class='iron-header'>IRON PROTOCOL</div>
    <div class='iron-sub'>⚡ Sistema de Treino de Alta Performance — Divisão A-B-C-D-E</div>
</div>
""", unsafe_allow_html=True)

# ─── SIDEBAR ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='font-family: Bebas Neue, cursive; font-size: 1.3rem; color: #ff3d00;
                letter-spacing: 0.15em; margin-bottom: 16px; border-bottom: 1px solid #ff3d0033; padding-bottom: 8px;'>
        NAVEGAÇÃO
    </div>
    """, unsafe_allow_html=True)

    dias = list(TRAINING_PLAN.keys())
    selected_day = st.radio(
        "Selecionar Dia:",
        options=dias,
        format_func=lambda x: x,
        label_visibility="collapsed",
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔄  RESETAR DIA", use_container_width=True):
        keys_to_del = [k for k in st.session_state.checks if k.startswith(selected_day)]
        for k in keys_to_del:
            del st.session_state.checks[k]
        st.toast(f"Treino do dia resetado!", icon="✅")

    if st.button("🗑️  RESETAR SEMANA", use_container_width=True):
        st.session_state.checks = {}
        st.toast("Semana completa resetada!", icon="♻️")

    st.markdown("<br>", unsafe_allow_html=True)

    # Progress sidebar
    total_ex = sum(
        len(b["exercicios"])
        for d in TRAINING_PLAN.values()
        for b in d["blocos"]
    )
    done_ex = len([v for v in st.session_state.checks.values() if v])
    pct = int((done_ex / total_ex) * 100) if total_ex > 0 else 0

    st.markdown(f"""
    <div style='font-family: Share Tech Mono, monospace; font-size: 0.7rem;
                color: #9090b0; letter-spacing: 0.1em; margin-bottom: 6px;'>
        PROGRESSO SEMANAL
    </div>
    <div style='font-family: Bebas Neue, cursive; font-size: 2rem; color: #ff8c00;
                line-height: 1;'>
        {pct}%
    </div>
    <div style='background: #1e1e2e; border-radius: 2px; height: 6px; margin-top: 6px;'>
        <div style='background: linear-gradient(90deg, #ff3d00, #ffd700);
                    height: 6px; border-radius: 2px; width: {pct}%;'></div>
    </div>
    <div style='font-family: Share Tech Mono, monospace; font-size: 0.65rem;
                color: #606080; margin-top: 4px;'>
        {done_ex}/{total_ex} EXERCÍCIOS
    </div>
    """, unsafe_allow_html=True)

# ─── MAIN CONTENT ─────────────────────────────────────────────────────────────
day_data = TRAINING_PLAN[selected_day]

col_title, col_info = st.columns([3, 1])
with col_title:
    st.markdown(f"""
    <div class='day-badge'>{selected_day}</div>
    <div style='font-family: Bebas Neue, cursive; font-size: 2rem; color: #ffffff; line-height: 1;'>
        {day_data['foco']}
    </div>
    """, unsafe_allow_html=True)
with col_info:
    st.markdown(f"""
    <div style='text-align: right; margin-top: 10px;'>
        <div style='font-family: Share Tech Mono, monospace; font-size: 0.65rem; color: #606080;'>DURAÇÃO</div>
        <div style='font-family: Bebas Neue, cursive; font-size: 1.8rem; color: #ff8c00;'>{day_data['duracao']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-color: #1e1e2e; margin: 16px 0;'>", unsafe_allow_html=True)

# ─── TABS ─────────────────────────────────────────────────────────────────────
tab_treino, tab_volume = st.tabs(["🏋️ EXERCÍCIOS", "📊 VOLUME SEMANAL"])

with tab_treino:
    for bloco in day_data["blocos"]:
        st.markdown(f"<div class='section-title'>{bloco['nome']}</div>", unsafe_allow_html=True)

        for ex in bloco["exercicios"]:
            check_key = f"{selected_day}_{ex['nome']}"

            badges_html = ""
            for m in ex.get("metodo", []):
                cls, label = METHOD_COLORS.get(m, ("badge-iso", m.upper()))
                badges_html += f"<span class='method-badge {cls}'>{label}</span>"

            checked = st.session_state.checks.get(check_key, False)
            card_opacity = "opacity: 0.5;" if checked else ""
            check_icon = "✅" if checked else "⬜"

            st.markdown(f"""
            <div class='exercise-card' style='{card_opacity}'>
                <div class='exercise-name'>{check_icon} {ex['nome']}</div>
                <div class='exercise-sets'>{ex['series']}</div>
                <div style='margin: 4px 0;'>{badges_html}</div>
                <div class='exercise-tech'>📋 {ex['desc']}</div>
                <div class='alt-box'>
                    <span class='alt-label'>🔄 ACADEMIA CHEIA — VARIAÇÃO</span>
                    {ex['alt']}
                </div>
                <div class='gif-placeholder'>
                    🎬 <a href='{ex['gif']}' target='_blank'>Ver demonstração no YouTube ↗</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

            new_val = st.checkbox(
                f"Marcar '{ex['nome']}' como concluído",
                value=checked,
                key=f"cb_{check_key}",
            )
            st.session_state.checks[check_key] = new_val

with tab_volume:
    st.markdown("""
    <div style='font-family: Rajdhani, sans-serif; color: #9090b0; font-size: 0.9rem; margin-bottom: 20px;'>
        Volume calculado por grupo muscular — baseado no número de séries semanais totais.
        Faixas recomendadas: <span style='color:#ff8c00'>10-20 séries/semana</span> para crescimento.
    </div>
    """, unsafe_allow_html=True)

    # Aggregate weekly volume
    weekly_vol = {}
    for day_key, day_info in TRAINING_PLAN.items():
        for muscle, sets in day_info["volume"].items():
            weekly_vol[muscle] = weekly_vol.get(muscle, 0) + sets

    sorted_vol = sorted(weekly_vol.items(), key=lambda x: x[1], reverse=True)
    max_vol = max(v for _, v in sorted_vol)

    priority_muscles = ["Ombro Medial", "Bíceps", "Tríceps", "Costas", "Trapézio", "Ombro Anterior", "Ombro Posterior"]

    st.markdown("<div class='section-title'>GRUPOS PRIORITÁRIOS</div>", unsafe_allow_html=True)
    for muscle, sets in sorted_vol:
        if muscle in priority_muscles:
            bar_pct = int((sets / max_vol) * 100)
            color = "#ff3d00" if sets < 10 else "#ffd700" if sets <= 20 else "#00ff88"
            st.markdown(f"""
            <div class='vol-row'>
                <div>
                    <span class='vol-muscle'>{muscle}</span>
                    <div class='vol-bar' style='width: {bar_pct}%; background: linear-gradient(90deg, {color}, {color}88);'></div>
                </div>
                <span class='vol-count'>{sets} séries</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='section-title' style='margin-top: 24px;'>OUTROS GRUPOS</div>", unsafe_allow_html=True)
    for muscle, sets in sorted_vol:
        if muscle not in priority_muscles:
            bar_pct = int((sets / max_vol) * 100)
            st.markdown(f"""
            <div class='vol-row'>
                <div>
                    <span class='vol-muscle' style='color: #9090b0;'>{muscle}</span>
                    <div class='vol-bar' style='width: {bar_pct}%; background: #2a2a4a;'></div>
                </div>
                <span class='vol-count' style='color: #6060a0;'>{sets} séries</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div style='margin-top: 28px; background: #0d0d1a; border: 1px solid #ff3d0033;
                border-radius: 6px; padding: 16px;
                font-family: Rajdhani, sans-serif; font-size: 0.9rem;'>
        <div style='font-family: Bebas Neue, cursive; color: #ff3d00; letter-spacing: 0.15em;
                    font-size: 1.1rem; margin-bottom: 10px;'>📌 LEGENDA DE MÉTODOS</div>
        <div style='color: #ff6644; margin-bottom: 6px;'>🔴 <b>REST-PAUSE</b> — Vai até a falha, descansa 10-15s, faz mais reps. Usado em isoladores para máximo recrutamento.</div>
        <div style='color: #ffd700; margin-bottom: 6px;'>🟡 <b>BACK-OFF SETS</b> — Após séries pesadas, reduz 30-40% da carga e faz mais volume. Usado em compostos.</div>
        <div style='color: #00ff88; margin-bottom: 6px;'>🟢 <b>COMPOSTO</b> — Exercícios multiarticulares. Base do programa. Alta carga.</div>
        <div style='color: #cc88ff;'>🟣 <b>ISOLADOR</b> — Foco em um músculo específico. Amplitude e contração máximas.</div>
    </div>
    """, unsafe_allow_html=True)

# ─── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align: center; margin-top: 40px; padding: 16px;
            font-family: Share Tech Mono, monospace; font-size: 0.65rem;
            color: #303050; border-top: 1px solid #1e1e2e;'>
    IRON PROTOCOL v1.0 — DIVISÃO ANTAGONISTA A-B-C-D-E — 120 MIN / SESSÃO
</div>
""", unsafe_allow_html=True)
