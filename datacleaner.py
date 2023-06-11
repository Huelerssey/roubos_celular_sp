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


# print(df_final.info())
# RangeIndex: 241240 entries, 0 to 241239
# Data columns (total 54 columns):
#  #   Column                    Non-Null Count   Dtype         
# ---  ------                    --------------   -----         
#  0   ANO_BO                    241240 non-null  int64         
#  1   NUM_BO                    241240 non-null  int64         
#  2   NUMERO_BOLETIM            241240 non-null  object        
#  3   BO_INICIADO               241240 non-null  datetime64[ns]
#  4   BO_EMITIDO                241240 non-null  datetime64[ns]
#  5   DATAOCORRENCIA            241240 non-null  object        
#  6   HORAOCORRENCIA            222803 non-null  object        
#  7   PERIDOOCORRENCIA          241240 non-null  object        
#  8   DATACOMUNICACAO           241240 non-null  datetime64[ns]
#  9   DATAELABORACAO            241240 non-null  datetime64[ns]
#  10  BO_AUTORIA                241240 non-null  object        
#  11  FLAGRANTE                 241240 non-null  object        
#  12  NUMERO_BOLETIM_PRINCIPAL  52374 non-null   object        
#  13  LOGRADOURO                228691 non-null  object        
#  14  NUMERO                    240726 non-null  float64       
#  15  BAIRRO                    237674 non-null  object        
#  16  CIDADE                    240726 non-null  object        
#  17  UF                        240726 non-null  object        
#  18  LATITUDE                  211428 non-null  float64       
#  19  LONGITUDE                 211428 non-null  float64       
#  20  DESCRICAOLOCAL            241240 non-null  object        
#  21  EXAME                     2158 non-null    object        
#  22  SOLUCAO                   241240 non-null  object        
#  23  DELEGACIA_NOME            241240 non-null  object        
#  24  DELEGACIA_CIRCUNSCRICAO   241240 non-null  object        
#  25  ESPECIE                   241240 non-null  object        
#  26  RUBRICA                   241240 non-null  object        
#  27  DESDOBRAMENTO             2603 non-null    object        
#  28  STATUS                    241240 non-null  object        
#  29  TIPOPESSOA                696 non-null     object        
#  30  VITIMAFATAL               696 non-null     object        
#  31  NATURALIDADE              73 non-null      object        
#  32  NACIONALIDADE             82 non-null      object        
#  33  SEXO                      696 non-null     object        
#  34  DATANASCIMENTO            634 non-null     datetime64[ns]
#  35  IDADE                     634 non-null     float64       
#  36  ESTADOCIVIL               399 non-null     object        
#  37  PROFISSAO                 308 non-null     object        
#  38  GRAUINSTRUCAO             237 non-null     object        
#  39  CORCUTIS                  25 non-null      object        
#  40  NATUREZAVINCULADA         696 non-null     object        
#  41  TIPOVINCULO               696 non-null     object        
#  42  RELACIONAMENTO            0 non-null       float64       
#  43  PARENTESCO                0 non-null       float64       
#  44  PLACA_VEICULO             48826 non-null   object        
#  45  UF_VEICULO                48700 non-null   object        
#  46  CIDADE_VEICULO            48696 non-null   object        
#  47  DESCR_COR_VEICULO         48776 non-null   object        
#  48  DESCR_MARCA_VEICULO       48833 non-null   object        
#  49  ANO_FABRICACAO            240135 non-null  float64       
#  50  ANO_MODELO                234967 non-null  float64       
#  51  DESCR_TIPO_VEICULO        48787 non-null   object        
#  52  QUANT_CELULAR             189058 non-null  float64       
#  53  MARCA_CELULAR             239617 non-null  object        
# dtypes: datetime64[ns](5), float64(9), int64(2), object(38)