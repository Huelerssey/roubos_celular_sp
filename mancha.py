import os
import sqlalchemy
import pandas as pd
import geopandas as gpd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from shapely.geometry import Point


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv('.env')

# Obtém as variáveis de ambiente necessárias
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Conexão com o banco de dados PostgreSQL
engine = sqlalchemy.create_engine(
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

# Consulta SQL
query = 'SELECT "LATITUDE", "LONGITUDE" FROM roubos'

# Executa a consulta e carrega os resultados em um DataFrame
tabela = pd.read_sql_query(query, engine)

# Função para criar um objeto do tipo Point
def create_point(row):
    return Point(row['LATITUDE'], row['LONGITUDE'])

# aplica a função para criar a coluna
tabela['GEOMETRY'] = tabela.apply(create_point, axis=1)

#cria o  geo dataframe 
tabela = gpd.GeoDataFrame(tabela, geometry='GEOMETRY')
