import os
import pandas as pd

# Caminho para a pasta contendo os arquivos Excel
caminho_pasta = r"C:\dev\roubos_celular_sp\dataset"

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
    'NUM_BO',
    'NUMERO_BOLETIM',
    'BO_EMITIDO',
    'PERIDOOCORRENCIA',
    'DATACOMUNICACAO',
    'DATAELABORACAO',
    'BO_AUTORIA',
    'NUMERO_BOLETIM_PRINCIPAL',
    'EXAME',
    'SOLUCAO',
    'DELEGACIA_CIRCUNSCRICAO',
    'ESPECIE',
    'RUBRICA',
    'DESDOBRAMENTO',
    'STATUS',
    'TIPOPESSOA',
    'NATURALIDADE',
    'NACIONALIDADE',
    'DATANASCIMENTO',
    'IDADE',
    'ESTADOCIVIL',
    'PROFISSAO',
    'GRAUINSTRUCAO',
    'CORCUTIS',
    'NATUREZAVINCULADA',
    'TIPOVINCULO',
    'RELACIONAMENTO',
    'PARENTESCO',
    'UF_VEICULO',
    'CIDADE_VEICULO',
    'DESCR_MARCA_VEICULO',
    'ANO_FABRICACAO',
    'ANO_MODELO',
    'QUANT_CELULAR',
    'ANO_BO'
]

# excluir colunas desnecessárias para análise
df_final = df_final.drop(colunas_para_excluir, axis=1)

# garante que a coluna será considerada como texto
df_final['DATAOCORRENCIA'] = df_final['DATAOCORRENCIA'].astype(str)

# remove espaços vazios da coluna
df_final['DATAOCORRENCIA'] = df_final['DATAOCORRENCIA'].str.strip()

# Recorta apenas a primeira parte que contem a data
df_final['DATAOCORRENCIA'] = df_final['DATAOCORRENCIA'].str.split(" ").str[0]

# exibe a quantidade de numeros não numericos na coluna
# count_nan = df_final['HORAOCORRENCIA'].isna().sum()
# print(f'O numero de valores não numericos na coluna HORAOCORRENCIA é: {count_nan}')

# exclui todos os valores vazios da coluna
df_final = df_final.dropna(subset=['HORAOCORRENCIA'])

# transforma a coluna em texto
df_final['HORAOCORRENCIA'] = df_final['HORAOCORRENCIA'].astype(str)

# remove espaços vazios da coluna
df_final['HORAOCORRENCIA'] = df_final['HORAOCORRENCIA'].str.strip()

# concatena a data e a hora da ocorrencia
df_final['DATA_HORA_OCORRENCIA'] = df_final['DATAOCORRENCIA'] + ' ' + df_final['HORAOCORRENCIA']

# deleta as colunas anteriores desnecessárias
df_final = df_final.drop(['DATAOCORRENCIA', 'HORAOCORRENCIA'], axis=1)

# converte a coluna em formato datetime
df_final['DATA_HORA_OCORRENCIA'] = pd.to_datetime(df_final['DATA_HORA_OCORRENCIA'], dayfirst=True, errors='coerce')

# verifica a quantida de valores vazios da coluna
# nan_count = df_final['DATA_HORA_OCORRENCIA'].isna().sum()
# print(f"Quantidade de linhas com valor NaT: {nan_count}")

# exclui todos os valores vazios da coluna
df_final = df_final.dropna(subset=['DATA_HORA_OCORRENCIA'])

# transforma o formato de data e hora no formato correto
df_final['DATA_HORA_OCORRENCIA'] = df_final['DATA_HORA_OCORRENCIA'].dt.strftime('%d/%m/%Y %H:%M:%S')
df_final['DATA_HORA_OCORRENCIA'] = pd.to_datetime(df_final['DATA_HORA_OCORRENCIA'], dayfirst=True, errors='coerce')

# exclui todos os valores vazios da coluna
df_final = df_final.dropna(subset=['LATITUDE', 'LONGITUDE'])

# exclui todos os valores vazios da coluna
df_final = df_final.dropna(subset=['MARCA_CELULAR'])

# exclui todos os valores vazios da coluna
df_final = df_final.dropna(subset=['BAIRRO'])

# Padronizar com True e False
df_final['FLAGRANTE'] = df_final['FLAGRANTE'].replace({'Sim': True, 'Não': False})

# lista de colunas a serem transformadas em bool
colunas = [
    'VITIMAFATAL', 
    'SEXO', 
    'PLACA_VEICULO', 
    'DESCR_COR_VEICULO', 
    'DESCR_TIPO_VEICULO'
]

# loop para transformar colunas em True ou False
for coluna in colunas:
    df_final[coluna] = df_final[coluna].fillna('').astype(bool)

# Cria uma nova coluna contendo o País
df_final['PAÍS'] = 'Brasil'

# Cria uma coluna única com o endereço completo
df_final['ENDEREÇO'] = df_final['LOGRADOURO'].astype(str) + ' - ' + df_final['NUMERO'].astype(str) + ' - ' + df_final['BAIRRO'].astype(str) + ' - ' + df_final['CIDADE'].astype(str) + ' - ' + df_final['UF'].astype(str) + ' - ' + df_final['PAÍS'].astype(str)

# deleta as colunas anteriores desnecessárias
df_final = df_final.drop(['LOGRADOURO', 'NUMERO', 'BAIRRO', 'CIDADE', 'UF', 'PAÍS' ], axis=1)

# Demonstra os valores da coluna
# print(df_final['DELEGACIA_NOME'].value_counts())

# Cria valores para subistituição na coluna DELEGACIA_NOME
mapeamento = {
    'DELEGACIA ELETRONICA': 'DELEGACIA_VIRTUAL',
    'DELEGACIA ELETRONICA 1': 'DELEGACIA_VIRTUAL'
}

# Subistitui valores de delegacia eletronica por delegacia virtual
df_final['DELEGACIA_NOME'] = df_final['DELEGACIA_NOME'].replace(mapeamento)

# Subistitui valores restantes por delegacia física
df_final.loc[df_final['DELEGACIA_NOME'] != 'DELEGACIA_VIRTUAL', 'DELEGACIA_NOME'] = 'DELEGACIA_FÍSICA'

# Padroniza a coluna de marca_celular
df_final['MARCA_CELULAR'] = df_final['MARCA_CELULAR'].str.title()

# print(df_final.info())
# Index: 191850 entries, 0 to 241238
# Data columns (total 14 columns):
#  #   Column                Non-Null Count   Dtype
# ---  ------                --------------   -----
#  0   BO_INICIADO           191850 non-null  datetime64[ns]
#  1   FLAGRANTE             191850 non-null  bool
#  2   LATITUDE              191850 non-null  float64       
#  3   LONGITUDE             191850 non-null  float64
#  4   DESCRICAOLOCAL        191850 non-null  object
#  5   DELEGACIA_NOME        191850 non-null  object
#  6   VITIMAFATAL           191850 non-null  bool
#  7   SEXO                  191850 non-null  bool
#  8   PLACA_VEICULO         191850 non-null  bool
#  9   DESCR_COR_VEICULO     191850 non-null  bool
#  10  DESCR_TIPO_VEICULO    191850 non-null  bool
#  11  MARCA_CELULAR         191850 non-null  object
#  12  DATA_HORA_OCORRENCIA  191850 non-null  datetime64[ns]
#  13  ENDEREÇO              191850 non-null  object
# dtypes: bool(6), datetime64[ns](2), float64(2), object(4)

# salvar os arquivos tratados em csv
# nome_do_arquivo = r"C:\dev\roubos_celular_sp\dataset\dados.csv"
# df_final.to_csv(nome_do_arquivo, index=False)
