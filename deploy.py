import streamlit as st
import pandas as pd
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import pages.separador.pg_1_home as PaginaUm
import pages.separador.pg_2_maps as PaginaDois
import pages.separador.pg_3_dashboard as PaginaTres
import pages.separador.pg_4_storytelling as PaginaQuatro


st.set_page_config(
    page_title='Roubos SP',
    page_icon='👮‍♂️',
    layout='wide'
)

# função que otimiza o carregamento dos dados
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("dataset/dados.csv")
    return tabela

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# animações
with open("animacoes/animacao_lottie.json") as source:
    animacao_1 = json.load(source)

with st.sidebar:
    #exibir animação
    st_lottie(animacao_1, height=100, width=270)
    st.write("---")
    opcao_selecionada = option_menu(
        menu_title="Menu Principal",
        menu_icon="justify",
        options=['Home', 'Maps', 'Dashboard', 'Storytelling'],
        icons=['house-door', 'geo-alt', 'clipboard-data', 'journals'],
        default_index=0,
        orientation='vertical',
    )

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    # footer da barra lateral
    st.write("---")
    st.markdown("<h5 style='text-align: center; color: lightgray;'>Developed By: Huelerssey Rodrigues</h5>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; justify-content: space-between;">
        <div>
            <a href="https://github.com/Huelerssey" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100" />
            </a>
        </div>
        <div>
            <a href="https://www.linkedin.com/in/huelerssey-rodrigues-a3145a261/" target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
            </a>
        </div>
        <div>
            <a href="https://api.whatsapp.com/send?phone=5584999306130" target="_blank">
                <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" width="100" />
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Retorna a pagina 1
if opcao_selecionada == "Home":
    PaginaUm.home()

# Retorna a pagina 2
elif opcao_selecionada == "Maps":
    PaginaDois.maps()

# Retorna a pagina 3
elif opcao_selecionada == "Dashboard":
    PaginaTres.dashboard()

# retorna a pagina 4
elif opcao_selecionada == "Storytelling":
    PaginaQuatro.storytelling()