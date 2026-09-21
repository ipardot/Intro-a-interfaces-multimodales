import streamlit as st
from PIL import Image

st.set_page_config(page_title="IPARDOT.EXE", page_icon="👾", layout="centered")

# ---------------------------------------------------------------
# PANTALLA DE INICIO
# ---------------------------------------------------------------
st.title("PLAYER 1: IPARDOT")

st.header("NIVEL 1 - MI COMIENZO CON APPS")
st.write("CLASE DE PERSONAJE: TRANSMEDIA. Mi build mezcla narrativa, codigo e interfaz en un solo mundo.")

image = Image.open('IsaPixel.png')
st.image(image, caption='>> SPRITE DEL JUGADOR: Esta soy yo')

texto = st.text_input('SELECCIONA TU PARTY - dime con quien andas', 'INSERTA NOMBRE')
st.write('>> COMPAÑERO REGISTRADO:', texto)

# ---------------------------------------------------------------
# PANTALLA DE SELECCION
# ---------------------------------------------------------------
st.subheader("PANTALLA DE SELECCION - 2 RANURAS")
col1, col2 = st.columns(2)

with col1:
    st.subheader("RANURA 1: LA MISION")
    st.write("REGLA DEL JUEGO: las interfaces multimodales suben la XP de la experiencia de usuario.")
    resp = st.checkbox('ACEPTO LA MISION')
    if resp:
        st.write("MISION ACEPTADA +100 XP")

with col2:
    st.subheader("RANURA 2: ESTADISTICA PRINCIPAL")
    modo = st.radio("Que modalidad domina tu interfaz", ('Visual', 'Auditiva', 'Tactil'))
    if modo == 'Visual':
        st.write('VISION +10 >> la vista es fundamental para tu interfaz')
    if modo == 'Auditiva':
        st.write('OIDO +10 >> la audicion es fundamental para tu interfaz')
    if modo == 'Tactil':
        st.write('TACTO +10 >> el tacto es fundamental para tu interfaz')

# ---------------------------------------------------------------
# TEMA 8-BIT (solo estilo, no cambia la logica de arriba)
# ---------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');

.stApp {
    background-color: #0f0f23;
    background-image:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 24px 24px;
}

h1, h2, h3 {
    font-family: 'Press Start 2P', cursive !important;
    color: #ffd700 !important;
    text-shadow: 3px 3px 0px #ff2e63;
    line-height: 1.6 !important;
}
h1 { font-size: 1.6rem !important; }
h2 { font-size: 1.1rem !important; color: #00e5ff !important; text-shadow: 2px 2px 0px #1b1b3a; }
h3 { font-size: 0.9rem !important; color: #7CFC00 !important; text-shadow: 2px 2px 0px #1b1b3a; }

p, li, label, .stMarkdown, div[data-testid="stMarkdownContainer"] {
    font-family: 'VT323', monospace !important;
    font-size: 1.35rem !important;
    color: #eaeaea !important;
}

input, .stTextInput input {
    font-family: 'VT323', monospace !important;
    font-size: 1.25rem !important;
    background-color: #1b1b3a !important;
    color: #7CFC00 !important;
    border: 3px solid #00e5ff !important;
    border-radius: 0 !important;
}

div[data-testid="stImage"] img {
    image-rendering: pixelated;
    border: 4px solid #ff2e63;
    border-radius: 0 !important;
}

div[data-testid="column"] {
    background-color: rgba(27,27,58,0.7);
    border: 3px solid #00e5ff;
    padding: 16px;
}
</style>
""", unsafe_allow_html=True)
