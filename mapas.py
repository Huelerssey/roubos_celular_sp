import geopandas as gpd
import folium
from folium.plugins import FastMarkerCluster, HeatMap

# Função para criar um mapa de cluster
def criar_mapa_cluster(dataframe):
    fmap = folium.Map(location=[-23.550520, -46.633308], zoom_start=12, tiles='cartodbpositron')
    mc = FastMarkerCluster(dataframe[['LATITUDE', 'LONGITUDE']])
    fmap.add_child(mc)
    return fmap

# Função para criar um mapa de heatmap
def criar_mapa_heatmap(dataframe):
    fmap = folium.Map(location=[-23.550520, -46.633308], zoom_start=12, tiles='cartodbpositron')
    heat_map = HeatMap(gdf_roubos_capital[['LATITUDE', 'LONGITUDE']])
    fmap.add_child(heat_map)
    return fmap

# Carrega os dados da geometria da capital
gdf_geometria_sp = gpd.read_file(r'C:\dev\roubos_celular_sp\geo\capital_sao_paulo.json', driver='GeoJSON')

# Carrega os dados de roubos de celular
gdf_roubos_capital = gpd.read_file(r'C:\dev\roubos_celular_sp\geo\roubos_celular_capital.json', driver='GeoJSON')

# Cria o mapa de cluster
mapa_cluster = criar_mapa_cluster(gdf_roubos_capital)

# Cria o mapa de heatmap
mapa_heatmap = criar_mapa_heatmap(gdf_roubos_capital)

# Adiciona a geometria da capital aos mapas
folium.GeoJson(gdf_geometria_sp).add_to(mapa_cluster)
folium.GeoJson(gdf_geometria_sp).add_to(mapa_heatmap)

# Salva os mapas como arquivos HTML
mapa_cluster.save(r'C:\dev\roubos_celular_sp\mapas_capital\mapa_cluster.html')
mapa_heatmap.save(r'C:\dev\roubos_celular_sp\mapas_capital\mapa_heatmap.html')
