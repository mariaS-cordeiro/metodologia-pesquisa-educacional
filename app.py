import streamlit as st

st.set_page_config(
    page_title="Metodologia da Pesquisa Educacional",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

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
    max-width: 980px;
    padding-top: 2.5rem;
}

.titulo {
    text-align: center;
    font-size: 32px;
    font-weight: 900;
    margin-bottom: 8px;
}

.jornada {
    text-align: center;
    font-size: 20px;
    color: #cfcfcf;
    margin-bottom: 28px;
    font-weight: 600;
}

.avatar-centro {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    margin-bottom: 8px;
}

.nome {
    text-align: center;
    font-size: 24px;
    font-weight: 900;
    margin-bottom: 24px;
}

.caixa-dialogo {
    background: #181818;
    border-radius: 30px;
    padding: 34px 42px;
    box-shadow: 0 18px 50px rgba(0,0,0,0.65);
    margin: 0 auto 28px auto;
}

.caixa-dialogo p {
    font-size: 22px;
    line-height: 1.75;
    color: #ffffff;
    font-weight: 600;
    margin: 0;
}

div.stButton > button {
    background-color: #111111;
    color: #ffffff;
    border: 1px solid #ffffff;
    border-radius: 14px;
    padding: 0.9rem 2.8rem;
    font-size: 18px;
    font-weight: 800;
}

div.stButton > button:hover {
    background-color: #ffffff;
    color: #000000;
}
</style>
""", unsafe_allow_html=True)

if "tela" not in st.session_state:
    st.session_state.tela = "cena1"

if st.session_state.tela == "cena1":

    st.markdown(
        '<div class="titulo">Laboratório Virtual de Pesquisa em Educação</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="jornada">Jornada 1 — Ética na Pesquisa Educacional</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="avatar-centro">', unsafe_allow_html=True)
    st.image("assets/imagens/avatar_profa_maria.png", width=220)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="nome">Profa. Maria</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="caixa-dialogo">
            <p>
            Olá! Seja muito bem-vindo(a).<br><br>
            Eu sou a Profa. Maria e estarei com você ao longo desta jornada.<br><br>
            Neste ambiente, você vivenciará situações semelhantes às enfrentadas por pesquisadores(as) da área da Educação.<br><br>
            Ao longo do percurso, faremos escolhas, analisaremos documentos, conversaremos com diferentes pessoas e refletiremos sobre os desafios que fazem parte do trabalho de um(a) pesquisador(a).<br><br>
            Toda pesquisa começa com uma pergunta.<br><br>
            Mas, antes de qualquer investigação, existe algo que precisamos compreender.<br><br>
            Vamos começar?
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1.3, 1, 1.3])
    with col2:
        if st.button("▶ Continuar"):
            st.session_state.tela = "cena2"
            st.rerun()

elif st.session_state.tela == "cena2":
    st.markdown("## Cena 2 — O convite")
    st.info("Aqui construiremos a próxima cena.")
