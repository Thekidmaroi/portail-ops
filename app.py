import streamlit as st

# ════════════════════════════════════════════════════════════════
#  🔗  LIENS — Remplace chaque "..." par ton vrai lien
# ════════════════════════════════════════════════════════════════

LIENS = {
    "Bon de Commande":      "https://www.appsheet.com/start/3cd1ab8e-90f4-4da3-ae76-350d823f079a",

    "Cahier de Charge":     "https://www.appsheet.com/start/57d74643-9e0d-4276-a1a1-086e7410947f",
    "Cahier de Charge V2":  "...",

    "PV Réunion":           "https://www.appsheet.com/start/5831d236-411a-4075-a476-ea344331ae42",

    "Suivi des Stocks":     "...",
    "Fiche Technique":      "...",
    "Rapport Journalier":   "...",
    "Planning Équipe":      "https://docs.google.com/spreadsheets/d/1e2p8CJMdUEkjLa6y-fBONHiFrybwyxRknOeDwkYuH0g/edit?gid=2073079878#gid=2073079878",
    "Demande de Congé":     "...",
}


#  🔑  MOT DE PASSE
MOT_DE_PASSE = st.secrets["MOT_DE_PASSE"]

LOGO_B64 = "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"

# ════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Namaryk – Portail",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ICONES = {
    "Bon de Commande":    "🛒",
    "Cahier de Charge":   "📋",
    "PV Réunion":         "📝",
    "Suivi des Stocks":   "📦",
    "Fiche Technique":    "🔧",
    "Rapport Journalier": "📊",
    "Planning Équipe":    "🗓️",
    "Demande de Congé":   "🏖️",
}

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

:root {
    --bg:     #f0f6ff;
    --white:  #ffffff;
    --border: #dbeafe;
    --blue:   #1d4ed8;
    --text:   #1e3a5f;
    --muted:  #6b8cae;
    --radius: 14px;
}

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: var(--bg) !important;
    font-family: 'Inter', sans-serif;
    color: var(--text);
}
[data-testid="stHeader"]  { display:none !important; }
[data-testid="stSidebar"] { display:none !important; }
.block-container { padding:2rem 3rem 5rem !important; max-width:1280px !important; }

/* topbar */
.topbar {
    display:flex; align-items:center; gap:18px;
    padding-bottom:1.4rem; margin-bottom:2rem;
    border-bottom:1px solid var(--border);
}
.topbar img    { height:52px; object-fit:contain; }
.topbar-sep    { width:1px; height:36px; background:var(--border); }
.topbar-label  { font-size:.78rem; font-weight:600; letter-spacing:.08em;
                 text-transform:uppercase; color:var(--muted); }
.topbar-badge  {
    margin-left:auto; background:#ecfdf5;
    border:1px solid #a7f3d0; color:#065f46;
    font-size:.73rem; font-weight:600;
    padding:4px 14px; border-radius:99px;
}

/* section label */
.section-label {
    font-size:.68rem; font-weight:600; letter-spacing:.12em;
    text-transform:uppercase; color:var(--muted);
    margin-bottom:.6rem;
}

/* card wrapper — visuel uniquement */
.card-box {
    background:var(--white);
    border:1px solid var(--border);
    border-radius:var(--radius);
    padding:1.4rem 1.3rem 1rem;
    position:relative; overflow:hidden;
    box-shadow:0 1px 4px rgba(29,78,216,.06);
    margin-bottom:4px;
}
.card-box::before {
    content:''; position:absolute; top:0; left:0; right:0;
    height:3px; background:var(--c);
}
.card-icon { font-size:1.8rem; margin-bottom:.6rem; display:block; }
.card-name { font-size:.88rem; font-weight:600; color:var(--text);
             margin-bottom:.8rem; }

/* link_button override — full width, styled */
div[data-testid="stLinkButton"] a,
div[data-testid="stLinkButton"] button {
    background: var(--blue) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: .78rem !important;
    font-weight: 600 !important;
    padding: .38rem .8rem !important;
    width: 100% !important;
    text-align: center !important;
    display: block !important;
    transition: opacity .15s !important;
    text-decoration: none !important;
}
div[data-testid="stLinkButton"] a:hover { opacity:.82 !important; }

/* disabled card */
.card-off {
    background:#f4f8ff; border:1px dashed #c7d9f0;
    border-radius:var(--radius); padding:1.4rem 1.3rem 1rem;
    opacity:.5;
}
.card-off .card-icon { filter:grayscale(1); }

/* login */
.login-wrap { text-align:center; padding:5rem 0 1.5rem; }
.login-logo img { height:70px; margin-bottom:1.8rem; }
.login-sub  { color:var(--muted); font-size:.9rem; margin:.3rem 0 2rem; }
.login-line { width:36px; height:2px; background:var(--blue);
              margin:.8rem auto 0; border-radius:99px; }

/* login button */
.stButton > button {
    background:var(--blue) !important; color:#fff !important;
    border:none !important; border-radius:9px !important;
    font-weight:600 !important; font-size:.88rem !important;
    transition:opacity .15s !important;
}
.stButton > button:hover { opacity:.85 !important; }

/* input */
.stTextInput input {
    background:var(--white) !important;
    border:1px solid var(--border) !important;
    border-radius:9px !important; color:var(--text) !important;
}

/* footer */
.footer {
    margin-top:3rem; text-align:center; color:var(--muted);
    font-size:.72rem; border-top:1px solid var(--border); padding-top:1.2rem;
}
</style>
"""

COULEURS = ["#1a56db","#0891b2","#0369a1","#1d4ed8",
            "#2563eb","#0284c7","#1e40af","#0ea5e9"]


def check_password():
    if st.session_state.get("authenticated"):
        return True

    st.markdown(CSS, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="login-wrap">
        <div class="login-logo">
            <img src="data:image/png;base64,{LOGO_B64}" />
        </div>
        <p class="login-sub">Portail interne — accès collaborateurs</p>
        <div class="login-line"></div>
    </div>
    """, unsafe_allow_html=True)

    _, c2, _ = st.columns([1, 1, 1])
    with c2:
        pwd = st.text_input("", type="password", placeholder="Mot de passe",
                            label_visibility="collapsed")
        if st.button("Accéder →", use_container_width=True):
            if pwd == MOT_DE_PASSE:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Mot de passe incorrect.")
    return False


def render_dashboard():
    st.markdown(CSS, unsafe_allow_html=True)

    # Topbar
    st.markdown(f"""
    <div class="topbar">
        <img src="data:image/png;base64,{LOGO_B64}" />
        <div class="topbar-sep"></div>
        <div class="topbar-label">Portail Opérations</div>
        <div class="topbar-badge">● Connecté</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Outils &amp; Automatisations</div>',
                unsafe_allow_html=True)

    items        = list(LIENS.items())
    cols_per_row = 4

    for row_start in range(0, len(items), cols_per_row):
        row_items = items[row_start: row_start + cols_per_row]
        cols = st.columns(cols_per_row, gap="medium")

        for i, (nom, lien) in enumerate(row_items):
            couleur = COULEURS[(row_start + i) % len(COULEURS)]
            icone   = ICONES.get(nom, "🔗")
            with cols[i]:
                if lien and lien != "...":
                    # Visuel de la card
                    st.markdown(f"""
                    <div class="card-box" style="--c:{couleur}">
                        <span class="card-icon">{icone}</span>
                        <div class="card-name">{nom}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    # Bouton natif Streamlit — vraiment cliquable
                    st.link_button("Ouvrir ↗", lien, use_container_width=True)
                else:
                    st.markdown(f"""
                    <div class="card-off">
                        <span class="card-icon">{icone}</span>
                        <div class="card-name" style="color:#8ca7c8">{nom}</div>
                        <div style="font-size:.72rem;color:#a0b8d0;margin-top:.3rem">
                            Lien à configurer
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _, c2, _ = st.columns([1, 0.7, 1])
    with c2:
        if st.button("Se déconnecter", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()

    st.markdown('<div class="footer">Namaryk — Usage interne uniquement</div>',
                unsafe_allow_html=True)


if check_password():
    render_dashboard()