import streamlit as st
import json
from streamlit_lottie import st_lottie


def home():
    # colunas de organização do site
    col1, col2, col3 = st.columns(3)

    # >>animações<<

    # hello
    with open('animacoes/hello.json') as source:
        hello=json.load(source)
    with open('animacoes/programing.json') as source:
        programing=json.load(source)
    
    # boas vindas ao projeto
    with col2:
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
        st.subheader("Boas vindas ao projeto Mancha Criminal de SP")
    with col1:
        st_lottie(hello, height=400, width=700)
    
    # resumo do projeto
    with col2:
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
        st.subheader("Este é um projeto de análise de dados que utiliza a geolocalização de celulares registrados em boletins de ocorrência para determinar a localização exata do crime, fornecendo insights valiosos para auxiliar na tomada de decisões estratégicas.")
    with col3:
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
        st_lottie(programing, height=400, width=400)