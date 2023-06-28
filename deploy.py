import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title='Roubos SP',
    page_icon='👮‍♂️',
    layout='wide'
)

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

opcao_selecionada = option_menu(
    menu_title=None,
    options=['Home', 'Maps', 'Dashboard', 'Storytelling'],
    icons=['house-door', 'geo-alt', 'clipboard-data', 'journals'],
    default_index=0,
    orientation='horizontal',
)

# Renderizar conteúdo com base na opção selecionada
if opcao_selecionada == 'Home':

    # colunas de organização do site
    col1, col2, col3 = st.columns(3)

    # >>animações<<

    # hello
    with open('hello.json') as source:
        hello=json.load(source)
    with open('programing.json') as source:
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
        st_lottie(hello, height=400, width=800)
    
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
        st.subheader("Este é um projeto de análise de dados que utiliza a geolocalização de celulares registrados em boletins de ocorrência para determinar a localização exata de roubos em um mapa, fornecendo insights valiosos para auxiliar na tomada de decisões estratégicas.")
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

# Página dos mapas
if opcao_selecionada == 'Maps':

    #organização da pagina
    col1, col2, col3 = st.columns(3)

    # Opções do selectbox
    opcoes_graficos = [
        'Mapa Clusterizado - Estado de São Paulo 2022',
        'Mapa de Calor - Estado de São Paulo 2022',
        'Mapa Clusterizado - Capital de São Paulo 2022',
        'Mapa de Calor - Capital de São Paulo 2022'    
        
    ]

    with col2:
        # Selectbox para selecionar o gráfico a ser exibido
        grafico_selecionado = st.selectbox('Selecione o gráfico a ser exibido', opcoes_graficos, label_visibility='hidden')

    # Função para exibir o gráfico selecionado
    def exibir_grafico(caminho_arquivo):
        # Abre o arquivo HTML e lê o conteúdo como uma string
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo_html = arquivo.read()

        # Exibe o gráfico no Streamlit usando o Markdown
        st.components.v1.html(conteudo_html, width=1700, height=700, scrolling=True)

    # Mapeia a opção selecionada para o caminho do arquivo correspondente
    mapeamento_graficos = {
        'Mapa Clusterizado - Estado de São Paulo 2022': r'C:\dev\roubos_celular_sp\mapas_estado\mapa_cluster_estado.html',
        'Mapa de Calor - Estado de São Paulo 2022': r'C:\dev\roubos_celular_sp\mapas_estado\mapa_heatmap_estado.html',
        'Mapa Clusterizado - Capital de São Paulo 2022': r'C:\dev\roubos_celular_sp\mapas_capital\mapa_cluster_capital.html',
        'Mapa de Calor - Capital de São Paulo 2022': r'C:\dev\roubos_celular_sp\mapas_capital\mapa_heatmap_capital.html'
        
    }

    # Verifica se a opção selecionada é válida e exibe o gráfico correspondente
    if grafico_selecionado in mapeamento_graficos:
        caminho_arquivo = mapeamento_graficos[grafico_selecionado]
        exibir_grafico(caminho_arquivo)
    else:
        st.warning('Selecione uma opção válida.')

# Pagina do dashboard power bi
if opcao_selecionada == 'Dashboard':

    # Definir altura e largura do iframe
    height = 800
    width = 1300

    # Centralizar o iframe
    html_code = f"""
    <div style="display: flex; justify-content: center;">
        <iframe src="https://app.powerbi.com/view?r=eyJrIjoiODZhNWEwNmItYWY4My00OTQ5LThmMmEtMDM2YmNiOTcwNTk5IiwidCI6ImE5M2YyOTk3LTRjNGMtNDk2ZS05OTk5LTZkNTEzY2Y1ODFjZiJ9" 
                height={height} width={width}></iframe>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
