import streamlit as st


def dashboard():
    # Definir altura e largura do iframe
    height = 800
    width = 1316

    # Centralizar o iframe
    html_code = f"""
    <div style="display: flex; justify-content: center;">
        <iframe src="https://app.powerbi.com/view?r=eyJrIjoiODZhNWEwNmItYWY4My00OTQ5LThmMmEtMDM2YmNiOTcwNTk5IiwidCI6ImE5M2YyOTk3LTRjNGMtNDk2ZS05OTk5LTZkNTEzY2Y1ODFjZiJ9" 
                height={height} width={width}></iframe>
    </div>
    """

    # Exibe o dashboard na página
    st.markdown(html_code, unsafe_allow_html=True)
