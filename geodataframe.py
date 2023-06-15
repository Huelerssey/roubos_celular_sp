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
    return Point(row['LONGITUDE'], row['LATITUDE'])

# aplica a função para criar a coluna
tabela['GEOMETRY'] = tabela.apply(create_point, axis=1)

#cria o  geo dataframe 
tabela_gdf = gpd.GeoDataFrame(tabela, geometry='GEOMETRY')

# Carrega os dados de geolocalização
data = gpd.read_file(r'C:\dev\roubos_celular_sp\geo\SP_Municipios_2022.shp')

# Plota um gráfico com todos os municipios de sp
# data.plot(figsize=(10, 9), facecolor='white', edgecolor='black')
# plt.show()

# filtra apenas a geometria da captal de sp
gdf_sp = data[data['NM_MUN'] == 'São Paulo']

# Plota um gráfico da geometria filtrada
# gdf_sp.plot(figsize=(10, 9), facecolor='white', edgecolor='black')
# plt.show()

# Salva um arquivo geojson com os dados da geometria da captal de sao paulo
# filename = r'C:\dev\roubos_celular_sp\geo\capital_sao_paulo.json'
# gdf_sp.to_file(filename, driver='GeoJSON')

# Carrega os dados geojson da geometria da captal de sao paulo
filename = r'C:\dev\roubos_celular_sp\geo\capital_sao_paulo.json'
gdf_capital_sp = gpd.read_file(filename, driver='GeoJSON')

# Plota um gráfico exibindo os arquivos GeoJSON
# gdf_capital_sp.plot()
# plt.show()

# correlacionar a tabela com o geodataframe
# fig, ax = plt.subplots(figsize=(8,8))

# tabela.plot(ax=ax)
# gdf_capital_sp.plot(ax=ax, facecolor='None', edgecolor='black')
# plt.show()

# Mostrar apenas os dados de interseção das ocorrencias dentro da captal de sp
polygon_sp = gdf_capital_sp.iloc[0].geometry

# mostra os pontos que dão match entre as ocorrencias e o mapa da captal de sp
# print(tabela_gdf.intersects(polygon_sp))

# plota um gráfico com todos os pontos dentro da interseção
gdf_roubos_capital = tabela_gdf[tabela_gdf.intersects(polygon_sp)]
# fig, ax = plt.subplots(figsize=(8,8))

# gdf_roubos_capital.plot(ax=ax)
# gdf_capital_sp.plot(ax=ax, facecolor='None', edgecolor='black')
# plt.show()

# Salva um arquivo geojson com os dados dentro da interseção de roubos na captal de são paulo
filename1 = r'C:\dev\roubos_celular_sp\geo\roubos_celular_capital.json'
gdf_roubos_capital.to_file(filename1, driver='GeoJSON')