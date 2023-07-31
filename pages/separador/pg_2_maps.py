import streamlit as st


def maps():
    #organização da pagina
    col1, col2, col3 = st.columns(3)

    # Opções do selectbox
    opcoes_graficos = [
        'Mancha Criminal Cluster - Estado de São Paulo 2022',
        'Mancha Criminal Heat - Estado de São Paulo 2022',
        'Mancha Criminal Cluster - Capital de São Paulo 2022',
        'Mancha Criminal Heat - Capital de São Paulo 2022'    
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
        st.components.v1.html(conteudo_html, width=1400, height=800, scrolling=True)

    # Mapeia a opção selecionada para o caminho do arquivo correspondente
    mapeamento_graficos = {
        'Mancha Criminal Cluster - Estado de São Paulo 2022': 'mapas_estado/mapa_cluster_estado.html',
        'Mancha Criminal Heat - Estado de São Paulo 2022': 'mapas_estado/mapa_heatmap_estado.html',
        'Mancha Criminal Cluster - Capital de São Paulo 2022': 'mapas_capital/mapa_cluster_capital.html',
        'Mancha Criminal Heat - Capital de São Paulo 2022': 'mapas_capital/mapa_heatmap_capital.html'        
    }

    # Verifica se a opção selecionada é válida e exibe o gráfico correspondente
    if grafico_selecionado in mapeamento_graficos:
        caminho_arquivo = mapeamento_graficos[grafico_selecionado]
        exibir_grafico(caminho_arquivo)
    else:
        st.warning('Selecione uma opção válida.')