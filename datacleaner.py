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
    'QUANT_CELULAR'
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

# preenche valores vazios com string vazia para padronizar com true or false
df_final['VITIMAFATAL'] = df_final['VITIMAFATAL'].fillna('').astype(bool)

print(df_final['VITIMAFATAL'])

# print(df_final.info())
# Index: 191850 entries, 0 to 241238
# Data columns (total 19 columns):
#  #   Column                Non-Null Count   Dtype
# ---  ------                --------------   -----
#  0   ANO_BO                191850 non-null  int64
#  1   BO_INICIADO           191850 non-null  datetime64[ns]
#  2   FLAGRANTE             191850 non-null  object        
#  3   LOGRADOURO            191850 non-null  object        
#  4   NUMERO                191850 non-null  float64
#  5   BAIRRO                191850 non-null  object
#  6   CIDADE                191850 non-null  object
#  7   UF                    191850 non-null  object
#  8   LATITUDE              191850 non-null  float64
#  9   LONGITUDE             191850 non-null  float64
#  10  DESCRICAOLOCAL        191850 non-null  object
#  11  DELEGACIA_NOME        191850 non-null  object
#  12  VITIMAFATAL           599 non-null     object
#  13  SEXO                  599 non-null     object
#  14  PLACA_VEICULO         41400 non-null   object
#  15  DESCR_COR_VEICULO     41373 non-null   object
#  16  DESCR_TIPO_VEICULO    41362 non-null   object
#  17  MARCA_CELULAR         191850 non-null  object
#  18  DATA_HORA_OCORRENCIA  191850 non-null  datetime64[ns]
# dtypes: datetime64[ns](2), float64(3), int64(1), object(13)

# salvar os arquivos tratados em csv
# nome_do_arquivo = r"C:\dev\roubos_celular_sp\dataset\dados.csv"
# df_final.to_csv(nome_do_arquivo, index=False)
