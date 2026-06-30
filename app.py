import streamlit as st
import time
import os

st.set_page_config(
    page_title="Metodologia da Pesquisa Educacional",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, header, footer {visibility: hidden;}

.stApp {
    background-color: #000000;
    color: #ffffff;
}

.block-container {
    padding-top: 3rem;
    max-width: 1000px;
}

.titulo {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    letter-spacing: 1px;
}

.jornada {
    text-align: center;
    font-size: 22px;
    color: #cccccc;
    margin-top: 10px;
    margin-bottom: 40px;
}

.avatar-box {
    display: flex;
    justify-content: center;
    margin-bottom: 25px;
}

.avatar-circle {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    background: #111111;
    border: 2px solid #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 82px;
}

.nome {
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 25px;
}

.dialogo {
    background-color: #111111;
    border: 1px solid #444444;
    border-radius: 22px;
    padding: 28px;
    font-size: 23px;
    line-height: 1.7;
    text-align: left;
    min-height: 220px;
}

div.stButton > button {
    background-color: #111111;
    color: #ffffff;
    border: 1px solid #ffffff;
    border-radius: 12px;
    padding: 0.9rem 2.5rem;
    font-size: 19px;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #ffffff;
    color: #000000;
}
</style>
""", unsafe_allow_html=True)

if "tela" not in st.session_state:
    st.session_state.tela = "cena1"

def fala_lenta(texto, velocidade=0.035):
    for palavra in texto.split():
        yield palavra + " "
        time.sleep(velocidade)

if st.session_state.tela == "cena1":

    st.markdown('<div class="titulo">LABORATÓRIO VIRTUAL DE PESQUISA EM EDUCAÇÃO</div>', unsafe_allow_html=True)
    st.markdown('<div class="jornada">Jornada 1 — Ética na Pesquisa Educacional</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="avatar-box">
        <div class="avatar-circle">👩🏾‍🏫</div>
    </div>
    <div class="nome">Profa. Maria</div>
    """, unsafe_allow_html=True)

    texto = """
    Olá! Seja muito bem-vindo(a).

    Eu sou a Profa. Maria e estarei com você ao longo desta jornada.

    Neste ambiente, você vivenciará situações semelhantes às enfrentadas por pesquisadores(as) da área da Educação.

    Ao longo do percurso, faremos escolhas, analisaremos documentos, conversaremos com diferentes pessoas e refletiremos sobre os desafios que fazem parte do trabalho de um(a) pesquisador(a).

    Toda pesquisa começa com uma pergunta.

    Mas, antes de qualquer investigação, existe algo que precisamos compreender.

    Vamos começar?
    """

    with st.container():
        st.markdown('<div class="dialogo">', unsafe_allow_html=True)
        st.write_stream(fala_lenta(texto))
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    col1, col2, col3 = st.columns([1.2, 1, 1.2])
    with col2:
        if st.button("▶ Continuar"):
            st.session_state.tela = "cena2"
            st.rerun()

elif st.session_state.tela == "cena2":
    st.markdown("## Cena 2 — O convite")
    st.info("Aqui construiremos a próxima cena.")
