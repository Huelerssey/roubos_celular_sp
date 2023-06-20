import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title='Roubos',
    page_icon='👮‍♂️',
    layout='wide'
)

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

opcao_selecionada = option_menu(
    menu_title=None,
    options=['Home', 'Previsão', 'Dashboard', 'Storytelling'],
    icons=['house-door', 'building-fill-up', 'clipboard-data', 'journals'],
    default_index=0,
    orientation='horizontal',
)
