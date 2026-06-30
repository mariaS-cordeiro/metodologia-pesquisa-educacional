import streamlit as st
import time

st.set_page_config(
    page_title="Metodologia da Pesquisa Educacional",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

#MainMenu, header, footer {
    visibility: hidden;
}

html, body, [class*="css"], .stApp {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background-color: #000000;
    color: #ffffff;
}

.block-container {
    max-width: 1050px;
    padding-top: 3rem;
}

.titulo {
    text-align: center;
    font-size: 32px;
    font-weight: 800;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}

.jornada {
    text-align: center;
    font-size: 21px;
    color: #cfcfcf;
    margin-bottom: 34px;
    font-weight: 600;
}

.avatar-box {
    display: flex;
    justify-content: center;
    margin-bottom: 12px;
}

.avatar-img {
    width: 210px;
    height: 210px;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: 0 10px 35px rgba(255,255,255,0.12);
}

.nome {
    text-align: center;
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 28px;
}

.caixa-dialogo {
    background: #171717;
    border-radius: 30px;
    padding: 38px 44px;
    min-height: 260px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.55);
}

.texto-dialogo {
    font-size: 23px;
    line-height: 1.75;
    color: #ffffff;
    font-weight: 500;
}

div.stButton > button {
    background-color: #111111;
    color: #ffffff;
    border: 1px solid #ffffff;
    border-radius: 14px;
    padding: 0.9rem 2.8rem;
    font-size: 19px;
    font-weight: 700;
}

div.stButton > button:hover {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #ffffff;
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

    st.markdown(
        '<div class="titulo">Laboratório Virtual de Pesquisa em Educação</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="jornada">Jornada 1 — Ética na Pesquisa Educacional</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="avatar-box">
            <img class="avatar-img" src="assets/imagens/avatar_profa_maria.png">
        </div>
        <div class="nome">Profa. Maria</div>
        """,
        unsafe_allow_html=True
    )

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
        st.markdown('<div class="texto-dialogo">', unsafe_allow_html=True)
        st.write_stream(fala_lenta(texto))
        st.markdown('</div>', unsafe_allow_html=True)
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
