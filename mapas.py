import geopandas as gpd
import folium
from folium.plugins import FastMarkerCluster, HeatMap

# Função para criar um mapa de cluster
def criar_mapa_cluster(dataframe):
    media_latitude = dataframe['LATITUDE'].mean()
    media_longitude = dataframe['LONGITUDE'].mean()
    fmap = folium.Map(location=[media_latitude, media_longitude], zoom_start=8, tiles='cartodbpositron')
    mapa_cluster = FastMarkerCluster(dataframe[['LATITUDE', 'LONGITUDE']])
    fmap.add_child(mapa_cluster)
    return fmap

# Função para criar um mapa de heatmap
def criar_mapa_heatmap(dataframe):
    media_latitude = dataframe['LATITUDE'].mean()
    media_longitude = dataframe['LONGITUDE'].mean()
    fmap = folium.Map(location=[media_latitude, media_longitude], zoom_start=8, tiles='cartodbpositron')
    heat_map = HeatMap(dataframe[['LATITUDE', 'LONGITUDE']])
    fmap.add_child(heat_map)
    return fmap

# Carrega os dados da geometria da capital
gdf_geometria_sp = gpd.read_file(r'C:\dev\roubos_celular_sp\geo\capital_sao_paulo.json', driver='GeoJSON')

# Carrega os dados de roubos de celular da capital
gdf_roubos_capital = gpd.read_file(r'C:\dev\roubos_celular_sp\geo\roubos_celular_capital.json', driver='GeoJSON')

# carrega os dados da geometria do estado de sao paulo
gdf_geometria_estado_sp = gpd.read_file(r'C:\dev\roubos_celular_sp\geo\geometria_estado_de_sao_paulo.json', driver='GeoJSON')

# Carrega os dados de roubos de celular do estado de sao paulo
gdf_roubos_estado_sp = gpd.read_file(r'C:\dev\roubos_celular_sp\geo\roubos_estado_de_sao_paulo.json', driver='GeoJSON')

# Cria o mapa de cluster
mapa_cluster1 = criar_mapa_cluster(gdf_roubos_capital)
mapa_cluster2 = criar_mapa_cluster(gdf_roubos_estado_sp)

# Cria o mapa de heatmap
mapa_heatmap1 = criar_mapa_heatmap(gdf_roubos_capital)
mapa_heatmap2 = criar_mapa_heatmap(gdf_roubos_estado_sp)

# Adiciona a geometria da capital aos mapas
folium.GeoJson(gdf_geometria_sp).add_to(mapa_cluster1)
folium.GeoJson(gdf_geometria_sp).add_to(mapa_heatmap1)
folium.GeoJson(gdf_geometria_estado_sp).add_to(mapa_cluster2)
folium.GeoJson(gdf_geometria_estado_sp).add_to(mapa_heatmap2)

# Salva os mapas como arquivos HTML
mapa_cluster1.save(r'C:\dev\roubos_celular_sp\mapas_capital\mapa_cluster_capital.html')
mapa_heatmap1.save(r'C:\dev\roubos_celular_sp\mapas_capital\mapa_heatmap_capital.html')
mapa_cluster2.save(r'C:\dev\roubos_celular_sp\mapas_estado\mapa_cluster_estado.html')
mapa_heatmap2.save(r'C:\dev\roubos_celular_sp\mapas_estado\mapa_heatmap_estado.html')
# implementar o zoom_start=7 para o mapa do estado e 9 para a capital.