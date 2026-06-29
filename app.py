import streamlit as st

st.set_page_config(
    page_title="Metodologia da Pesquisa Educacional",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background-color: #000000;
        color: #ffffff;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .fade-in {
        animation: fadeIn 2.5s ease-in;
    }

    @keyframes fadeIn {
        0% {opacity: 0; transform: translateY(10px);}
        100% {opacity: 1; transform: translateY(0);}
    }

    .titulo {
        text-align: center;
        font-size: 44px;
        font-weight: 800;
        letter-spacing: 2px;
        margin-top: 100px;
    }

    .subtitulo {
        text-align: center;
        font-size: 24px;
        margin-top: 20px;
        color: #dddddd;
    }

    .missao {
        text-align: center;
        font-size: 30px;
        margin-top: 60px;
        line-height: 1.6;
    }

    .botao-centro {
        display: flex;
        justify-content: center;
        margin-top: 45px;
    }

    div.stButton > button {
        background-color: #111111;
        color: #ffffff;
        border: 1px solid #ffffff;
        border-radius: 10px;
        padding: 0.8rem 2rem;
        font-size: 18px;
        font-weight: 600;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #ffffff;
    }

    .cena-escola {
        border: 1px solid #333333;
        border-radius: 18px;
        padding: 30px;
        margin-top: 30px;
        background: linear-gradient(135deg, #0c0c0c, #1a1a1a);
    }

    .avatar-card {
        border: 1px solid #444444;
        border-radius: 18px;
        padding: 25px;
        background-color: #111111;
        text-align: center;
        min-height: 360px;
    }

    .avatar {
        font-size: 90px;
        margin-bottom: 15px;
    }

    .nome-avatar {
        font-size: 24px;
        font-weight: 700;
    }

    .funcao-avatar {
        color: #cccccc;
        font-size: 16px;
        margin-top: 8px;
    }

    .video-card {
        border: 1px solid #444444;
        border-radius: 18px;
        padding: 25px;
        background-color: #111111;
        min-height: 360px;
    }

    .fala {
        font-size: 20px;
        line-height: 1.8;
        color: #f2f2f2;
    }

    .escola-titulo {
        font-size: 34px;
        font-weight: 800;
        text-align: center;
    }

    .escola-subtitulo {
        font-size: 22px;
        color: #cccccc;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "tela" not in st.session_state:
    st.session_state.tela = "abertura"

if st.session_state.tela == "abertura":
    st.markdown(
        """
        <div class="fade-in">
            <div class="titulo">METODOLOGIA DA PESQUISA EDUCACIONAL</div>
            <div class="subtitulo">Laboratório Virtual</div>
            <div class="missao">
                MISSÃO 1<br>
                Ética na Pesquisa Educacional
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    col1, col2, col3 = st.columns([1.2, 1, 1.2])
    with col2:
        if st.button("▶ Iniciar missão"):
            st.session_state.tela = "cena1"
            st.rerun()

elif st.session_state.tela == "cena1":
    st.markdown(
        """
        <div class="fade-in cena-escola">
            <div class="escola-titulo">Escola Quero Aprender</div>
            <div class="escola-subtitulo">Ensino Fundamental I</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_avatar, col_video = st.columns([1, 2])

    with col_avatar:
        st.markdown(
            """
            <div class="fade-in avatar-card">
                <div class="avatar">👩‍🏫</div>
                <div class="nome-avatar">Profa. Helena</div>
                <div class="funcao-avatar">Professora de Metodologia da Pesquisa</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_video:
        st.markdown(
            """
            <div class="fade-in video-card">
                <h3>Vídeo de boas-vindas</h3>
                <p class="fala">
                Olá! Seja muito bem-vindo(a).<br><br>
                Eu sou Helena, professora de Metodologia da Pesquisa, e acompanharei você durante esta primeira missão.<br><br>
                Hoje iniciaremos uma investigação em uma escola de Ensino Fundamental I.<br><br>
                Antes de conversar com estudantes, professores ou gestores, precisamos compreender um aspecto essencial da pesquisa científica: a ética.<br><br>
                Entre. O Laboratório Virtual está preparado para receber você.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    col1, col2, col3 = st.columns([1.2, 1, 1.2])
    with col2:
        if st.button("▶ Entrar no Laboratório"):
            st.info("Próxima etapa: Cena 2 – O Laboratório Virtual.")
