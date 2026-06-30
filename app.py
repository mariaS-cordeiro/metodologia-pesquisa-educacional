import streamlit as st
import time

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
    max-width: 1000px;
    padding-top: 3rem;
}

.titulo {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 8px;
}

.jornada {
    text-align: center;
    font-size: 22px;
    color: #cccccc;
    margin-bottom: 35px;
}

.avatar-video {
    display: flex;
    justify-content: center;
    margin-bottom: 12px;
}

.avatar-video video {
    width: 190px;
    height: 190px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #ffffff;
}

.nome {
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 25px;
}

.caixa-dialogo {
    background-color: #111111;
    border: 1px solid #555555;
    border-radius: 24px;
    padding: 30px 36px;
    font-size: 23px;
    line-height: 1.7;
    color: #ffffff;
    min-height: 260px;
    box-shadow: 0 0 25px rgba(255,255,255,0.08);
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

def fala_lenta(texto, velocidade=0.03):
    for palavra in texto.split():
        yield palavra + " "
        time.sleep(velocidade)

if st.session_state.tela == "cena1":

    st.markdown('<div class="titulo">LABORATÓRIO VIRTUAL DE PESQUISA EM EDUCAÇÃO</div>', unsafe_allow_html=True)
    st.markdown('<div class="jornada">Jornada 1 — Ética na Pesquisa Educacional</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="avatar-video">
        <video autoplay loop muted playsinline>
            <source src="assets/videos/helena_cena1_sem_audio.mp4" type="video/mp4">
        </video>
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

    caixa = st.empty()

    with caixa.container():
        st.markdown('<div class="caixa-dialogo">', unsafe_allow_html=True)
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
