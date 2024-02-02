import pandas as pd
from geopandas import GeoDataFrame
# Caminho para o arquivo Excel (.xls) local
caminho_excel = '/home/david/autom/'

# Ler dados do Excel para um GeoDataFrame do geopandas
gdf = pd.read_excel('/home/david/autom/setor-teste-dictionary.xlsx')
print(gdf)

# Define a coluna de geometria
gdf = gdf.set_geometry('setor-teste-dictionary.xlsx')

# Caminho para salvar o shapefile localmente
caminho_shapefile = '/home/david/autom/arquivo_shapefile.shp'

# Salvar o GeoDataFrame como shapefile
gdf = GeoDataFrame(gdf)

gdf.to_file(caminho_shapefile, driver='ESRI Shapefile')
