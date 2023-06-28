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

# Pagina de storytelling do projeto
if opcao_selecionada == 'Storytelling':
    
    # Organiza as colunas
    coluna1, coluna2, coluna3 = st.columns(3)

    # Coloca o texto no centro da pagina
    with coluna2:

        # Introdução
        st.title('Storytelling do Projeto')

        # Introdução
        st.header("1. Introdução")
        st.write("Bem-vindo ao storytelling do projeto de análise de dados de roubos de celular no estado de São Paulo. Aqui, embarcaremos em uma jornada de exploração dos dados e apresentação de insights interessantes sobre essa problemática.")
        st.write("O objetivo deste projeto é obter uma compreensão abrangente desse cenário e identificar padrões significativos. Através deste storytelling, vou compartilhar descobertas valiosas que poderão contribuir para a compreensão do problema, apoio em tomadas de decisão e busca por soluções efetivas.")
        st.write("")

        st.header("2. Obtenção de dados")
        st.write("Os dados sobre os crimes foram obtidos por meio do site do governo de São Paulo. Utilizei a plataforma de transparência da Secretaria de Segurança Pública de São Paulo, acessível através do [link](http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx). Essa fonte confiável fornece informações detalhadas sobre os registros de ocorrências de crimes, incluindo os casos de roubo de celular.")
        st.write("Além disso, para enriquecer a análise e desenvolver a funcionalidade da 'Mancha Criminal', fiz o uso de dados geográficos de todos os municípios de São Paulo. Esses dados foram adquiridos no site do Instituto Brasileiro de Geografia e Estatística (IBGE) por meio do seguinte [link](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html?=&t=downloads).")
        st.write("Em ambos os casos, não foi possível acessar os dados por meio de uma API, então realizei o download manual dos arquivos disponibilizados pelas respectivas plataformas.")
        st.write("")

        st.header("3. Data Cleaning & Loading")
        st.write("Ainda que, em uma apresentação formal esse tópico possa não ser relevante, as etapas de limpeza, tratamento e carregamento tem um papel fundamental. Como este é um projeto de portfólio, vou compartilhar algumas das etapas de ETL, para demonstrar minhas habilidades no assunto. Caso queira explorar o código completo do projeto, ele está disponível no meu GitHub: [link](https://github.com/Huelerssey/roubos_celular_sp). No entanto, se isso não for do seu interesse, sinta-se à vontade para pular para a próxima seção.")
        st.write("")

        st.subheader("Limpeza e tratamento de dados")
        codigo1 = """
        # Lista para armazenar os DataFrames
        dataframes = []

        # Itera sobre os arquivos na pasta
        for arquivo in os.listdir(caminho_pasta):
            if arquivo.endswith(".xlsx"):
                # Lê o arquivo Excel e armazena em um DataFrame
                df = pd.read_excel(os.path.join(caminho_pasta, arquivo))
                dataframes.append(df)

        # Concatena os DataFrames em um único DataFrame
        df_final = pd.concat(dataframes, ignore_index=True)

        # lista de colunas a serem excluidas
        colunas_para_excluir = [
            "NUM_BO",
            "NUMERO_BOLETIM",
            "BO_EMITIDO",
            "PERIDOOCORRENCIA",
            "DATACOMUNICACAO",
            "DATAELABORACAO",
            "BO_AUTORIA",
            "NUMERO_BOLETIM_PRINCIPAL",
            "EXAME",
            "SOLUCAO",
            "DELEGACIA_CIRCUNSCRICAO",
            "ESPECIE",
            "RUBRICA",
            "DESDOBRAMENTO",
            "STATUS",
            "TIPOPESSOA",
            "NATURALIDADE",
            "NACIONALIDADE",
            "DATANASCIMENTO",
            "IDADE",
            "ESTADOCIVIL",
            "PROFISSAO",
            "GRAUINSTRUCAO",
            "CORCUTIS",
            "NATUREZAVINCULADA",
            "TIPOVINCULO",
            "RELACIONAMENTO",
            "PARENTESCO",
            "UF_VEICULO",
            "CIDADE_VEICULO",
            "DESCR_MARCA_VEICULO",
            "ANO_FABRICACAO",
            "ANO_MODELO",
            "QUANT_CELULAR",
            "ANO_BO",
        ]

        # excluir colunas desnecessárias para análise
        df_final = df_final.drop(colunas_para_excluir, axis=1)

        # garante que a coluna será considerada como texto
        df_final["DATAOCORRENCIA"] = df_final["DATAOCORRENCIA"].astype(str)

        # remove espaços vazios da coluna
        df_final["DATAOCORRENCIA"] = df_final["DATAOCORRENCIA"].str.strip()

        # Recorta apenas a primeira parte que contem a data
        df_final["DATAOCORRENCIA"] = df_final["DATAOCORRENCIA"].str.split(" ").str[0]

        # exibe a quantidade de numeros não numericos na coluna
        # count_nan = df_final['HORAOCORRENCIA'].isna().sum()
        # print(f'O numero de valores não numericos na coluna HORAOCORRENCIA é: {count_nan}')

        # exclui todos os valores vazios da coluna
        df_final = df_final.dropna(subset=["HORAOCORRENCIA"])

        # transforma a coluna em texto
        df_final["HORAOCORRENCIA"] = df_final["HORAOCORRENCIA"].astype(str)

        # remove espaços vazios da coluna
        df_final["HORAOCORRENCIA"] = df_final["HORAOCORRENCIA"].str.strip()

        # concatena a data e a hora da ocorrencia
        df_final["DATA_HORA_OCORRENCIA"] = (
            df_final["DATAOCORRENCIA"] + " " + df_final["HORAOCORRENCIA"]
        )

        # deleta as colunas anteriores desnecessárias
        df_final = df_final.drop(["DATAOCORRENCIA", "HORAOCORRENCIA"], axis=1)

        # converte a coluna em formato datetime
        df_final["DATA_HORA_OCORRENCIA"] = pd.to_datetime(
            df_final["DATA_HORA_OCORRENCIA"], dayfirst=True, errors="coerce"
        )

        # verifica a quantida de valores vazios da coluna
        # nan_count = df_final['DATA_HORA_OCORRENCIA'].isna().sum()
        # print(f"Quantidade de linhas com valor NaT: {nan_count}")

        # exclui todos os valores vazios da coluna
        df_final = df_final.dropna(subset=["DATA_HORA_OCORRENCIA"])

        # transforma o formato de data e hora no formato correto
        df_final["DATA_HORA_OCORRENCIA"] = df_final["DATA_HORA_OCORRENCIA"].dt.strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        df_final["DATA_HORA_OCORRENCIA"] = pd.to_datetime(
            df_final["DATA_HORA_OCORRENCIA"], dayfirst=True, errors="coerce"
        )

        # exclui todos os valores vazios da coluna
        df_final = df_final.dropna(subset=["LATITUDE", "LONGITUDE"])

        # exclui todos os valores vazios da coluna
        df_final = df_final.dropna(subset=["MARCA_CELULAR"])

        # exclui todos os valores vazios da coluna
        df_final = df_final.dropna(subset=["BAIRRO"])

        # Padronizar com True e False
        df_final["FLAGRANTE"] = df_final["FLAGRANTE"].replace({"Sim": True, "Não": False})

        # lista de colunas a serem transformadas em bool
        colunas = [
            "VITIMAFATAL",
            "SEXO",
            "PLACA_VEICULO",
            "DESCR_COR_VEICULO",
            "DESCR_TIPO_VEICULO",
        ]

        # loop para transformar colunas em True ou False
        for coluna in colunas:
            df_final[coluna] = df_final[coluna].fillna("").astype(bool)

        # Cria uma nova coluna contendo o País
        df_final["PAÍS"] = "BRASIL"

        # Cria uma coluna única com o endereço completo
        df_final["ENDERECO"] = (
            df_final["LOGRADOURO"].astype(str)
            + " - "
            + df_final["NUMERO"].astype(str)
            + " - "
            + df_final["BAIRRO"].astype(str)
            + " - "
            + df_final["CIDADE"].astype(str)
            + " - "
            + df_final["UF"].astype(str)
            + " - "
            + df_final["PAÍS"].astype(str)
        )

        # deleta as colunas anteriores desnecessárias
        df_final = df_final.drop(
            ["LOGRADOURO", "NUMERO", "BAIRRO", "CIDADE", "UF", "PAÍS"], axis=1
        )

        # Demonstra os valores da coluna
        # print(df_final['DELEGACIA_NOME'].value_counts())

        # Cria valores para subistituição na coluna DELEGACIA_NOME
        mapeamento = {
            "DELEGACIA ELETRONICA": "DELEGACIA_VIRTUAL",
            "DELEGACIA ELETRONICA 1": "DELEGACIA_VIRTUAL",
        }

        # Subistitui valores de delegacia eletronica por delegacia virtual
        df_final["DELEGACIA_NOME"] = df_final["DELEGACIA_NOME"].replace(mapeamento)

        # Subistitui valores restantes por delegacia física
        df_final.loc[
            df_final["DELEGACIA_NOME"] != "DELEGACIA_VIRTUAL", "DELEGACIA_NOME"
        ] = "DELEGACIA_FÍSICA"

        # Padroniza a coluna de marca_celular
        df_final["MARCA_CELULAR"] = df_final["MARCA_CELULAR"].str.title()

        # Substitui os valores na coluna DESCRICAOLOCAL
        df_final["DESCRICAOLOCAL"] = df_final["DESCRICAOLOCAL"].replace(
            "Via pública", "Via Pública"
        )

        # Agrupa todos os valores menores que 6 mil
        colunas_agrupar = []
        for marca, quantidade in df_final["MARCA_CELULAR"].value_counts().items():
            if quantidade < 6000:
                colunas_agrupar.append(marca)

        # agrupa todos os valores menores que 6mil em "Outros"
        for marca in colunas_agrupar:
            df_final.loc[df_final["MARCA_CELULAR"] == marca, "MARCA_CELULAR"] = "Outros"


        # função para definir uma parte do dia para cada faiza de horário
        def obter_parte_do_dia(data_hora):
            hora = pd.to_datetime(data_hora).hour

            if 6 <= hora <= 11:
                return "Manhã"
            elif 12 <= hora <= 17:
                return "Tarde"
            elif 18 <= hora <= 23:
                return "Noite"
            else:
                return "Madrugada"


        # cria uma nova coluna com as faixas de horarios definidas
        df_final["PARTE_DO_DIA"] = df_final["DATA_HORA_OCORRENCIA"].apply(obter_parte_do_dia)
        """
        st.code(codigo1, language="python")
        st.write("")

        st.subheader("Carregando os dados tratados em um banco Cloud AWS")
        codigo2 = """
        # Constrói a string de conexão com o banco de dados
        db_connection_string = (
            f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )

        # Estabelece a conexão com o banco de dados
        engine = create_engine(db_connection_string)

        try:
            # Insere os dados do DataFrame na tabela
            df_final.to_sql(name="roubos", con=engine, if_exists="append", index=False)
            print("Dados inseridos com sucesso!")

        except Exception as e:
            print("Erro ao inserir os dados:", str(e))

        finally:
            # Fecha a conexão com o banco de dados
            engine.dispose()
        """
        st.code(codigo2, language="python")
        st.write("")

        st.subheader("Visualização no banco de dados")
        st.image("imagens/1.jpeg")
        st.write("")

        st.header("4. Análise exploratória")
        
