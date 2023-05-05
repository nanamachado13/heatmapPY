import osmnx as ox
import geopandas as gpd
from pyproj import CRS
import pandas as pd
import folium
from folium import plugins

# place_name = "Ribeirão Preto, SP, Brazil"

# # Obtém o mapa de Ribeirão Preto
# G = ox.graph_from_place(place_name, network_type="drive")

# Lê os dados dos acidentes de bicicleta
df = pd.read_csv('acidentes_naofatais-utf8.csv', delimiter=';')
df['LAT_(GEO)'] = df['LAT_(GEO)'].str.replace(',', '.')
df['LONG_(GEO)'] = df['LONG_(GEO)'].str.replace(',', '.')
nova_tabela = df.loc[:, ['LAT_(GEO)', 'LONG_(GEO)', 'Bicicleta']]
# remove as linhas com valores nulos
nova_tabela = nova_tabela.dropna()
#cria novo data frame com a coluna bicicleta contem 1  
bicicleta = nova_tabela.loc[nova_tabela['Bicicleta'] == 1]



# Cria um mapa centrado em Ribeirão Preto
mapa = folium.Map(location=[-21.1775, -47.8103], zoom_start=12)

# # Adiciona o grafo de ruas de Ribeirão Preto ao mapa
# folium.GeoJson(ox.graph_to_gdfs(G)[1]).add_to(mapa)

# Adiciona marcadores para cada ponto de atropelamento
# for index, row in bicicleta.iterrows():
#     folium.Marker(location=[row['LAT_(GEO)'], row['LONG_(GEO)']]).add_to(mapa)

# Cria lista de coordenadas a partir do dataframe bicicleta
coordenadas = []
for index, row in bicicleta.iterrows():
    coordenadas.append([row['LAT_(GEO)'], row['LONG_(GEO)']])

# Cria um mapa de calor a partir da lista de coordenadas
# heatmap = folium.plugins.HeatMap(coordenadas, min_opacity=0.2, radius=15, blur=10)
heatmap = plugins.HeatMap(coordenadas, min_opacity=0.2, radius=15, blur=10)

# Adiciona o mapa de calor ao mapa existente
heatmap.add_to(mapa)

# Exibe o mapa com o mapa de calor
mapa