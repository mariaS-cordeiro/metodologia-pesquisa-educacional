
import streamlit as st

st.set_page_config(
    page_title="Metodologia da Pesquisa Educacional",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    .titulo {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-top: 80px;
    }
    .subtitulo {
        text-align: center;
        font-size: 24px;
        margin-top: 10px;
    }
    .missao {
        text-align: center;
        font-size: 30px;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "tela" not in st.session_state:
    st.session_state.tela = "abertura"

if st.session_state.tela == "abertura":
    st.markdown('<div class="titulo">METODOLOGIA DA PESQUISA EDUCACIONAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo">Laboratório Virtual</div>', unsafe_allow_html=True)
    st.markdown('<div class="missao">MISSÃO 1<br>Ética na Pesquisa Educacional</div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("▶ Iniciar missão"):
            st.session_state.tela = "cena1"
            st.rerun()

elif st.session_state.tela == "cena1":
    st.markdown("## Escola Quero Aprender")
    st.markdown("### Ensino Fundamental I")

    col_avatar, col_video = st.columns([1, 2])

    with col_avatar:
        st.markdown("### 👩‍🏫 Profa. Helena")
        st.write("Professora de Metodologia da Pesquisa")

    with col_video:
        st.markdown("### Vídeo de boas-vindas")
        st.info("Aqui entraremos depois com o vídeo da Profa. Helena.")

    st.markdown("---")

    st.write("""
    Olá! Seja muito bem-vindo(a).

    Eu sou Helena, professora de Metodologia da Pesquisa, e acompanharei você durante esta primeira missão.

    Hoje iniciaremos uma investigação em uma escola de Ensino Fundamental I.

    Antes de conversar com estudantes, professores ou gestores, precisamos compreender um aspecto essencial da pesquisa científica: a ética.

    Entre. O Laboratório Virtual está preparado para receber você.
    """)

    if st.button("▶ Entrar no Laboratório"):
        st.success("Próxima etapa: Cena 2 – O Laboratório Virtual.")
