import streamlit as st

st.set_page_config(
    page_title="Metodologia da Pesquisa Educacional",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Nunito', sans-serif;
}

#MainMenu, header, footer {
    visibility: hidden;
}

.stApp {
    background-color: #000000;
    color: #ffffff;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.titulo {
    text-align: center;
    font-size: 36px;
    font-weight: 900;
    margin-bottom: 4px;
}

.jornada {
    text-align: center;
    font-size: 21px;
    color: #d0d0d0;
    margin-bottom: 35px;
}

.nome {
    text-align: center;
    font-size: 24px;
    font-weight: 900;
    margin-top: 10px;
}

.caixa {
    background-color: #181818;
    border-radius: 28px;
    padding: 35px;
    font-size: 22px;
    line-height: 1.75;
    font-weight: 600;
    box-shadow: 0 18px 45px rgba(0,0,0,0.65);
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

if "cena" not in st.session_state:
    st.session_state.cena = "cena1"

if st.session_state.cena == "cena1":

    st.markdown('<div class="titulo">Laboratório Virtual de Pesquisa em Educação</div>', unsafe_allow_html=True)
    st.markdown('<div class="jornada">Jornada 1 — Ética na Pesquisa Educacional</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("assets/videos/avatar_profa_maria.png", width=260)
        st.markdown('<div class="nome">Profa. Maria</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="caixa">
            Olá! Seja muito bem-vindo(a).<br><br>

            Eu sou a Profa. Maria e estarei com você ao longo desta jornada.<br><br>

            Neste ambiente, você vivenciará situações semelhantes às enfrentadas por pesquisadores(as) da área da Educação.<br><br>

            Ao longo do percurso, faremos escolhas, analisaremos documentos, conversaremos com diferentes pessoas e refletiremos sobre os desafios que fazem parte do trabalho de um(a) pesquisador(a).<br><br>

            Toda pesquisa começa com uma pergunta.<br><br>

            Mas, antes de qualquer investigação, existe algo que precisamos compreender.<br><br>

            Vamos começar?
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    col_a, col_b, col_c = st.columns([1.3, 1, 1.3])
    with col_b:
        if st.button("▶ Continuar"):
            st.session_state.cena = "cena2"
            st.rerun()

elif st.session_state.cena == "cena2":
    st.markdown("## Cena 2 — O convite")
    st.info("Aqui construiremos a próxima cena.")
