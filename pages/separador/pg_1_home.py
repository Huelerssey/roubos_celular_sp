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
    
    # programing
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
        st.markdown("<h5 style='text-align: justfy;'> Boas vindas ao projeto Mancha Criminal de SP </h5>", unsafe_allow_html=True)
    with col1:
        st_lottie(hello, height=400, width=300)
    
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
        st.markdown("<h5 style='text-align: justfy;'> Este é um projeto de análise de dados que utiliza a geolocalização de celulares registrados em boletins de ocorrência para determinar a localização exata do crime, fornecendo insights valiosos para auxiliar na tomada de decisões estratégicas.</h5>", unsafe_allow_html=True)
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
        st.write("")
        st_lottie(programing, height=400, width=300)