import pandas as pd
import streamlit as st


# função que otimiza o carregamento dos dados
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("dataset/dados.csv")
    return tabela