import pandas as pd
from geopandas import GeoDataFrame
# Caminho para o arquivo Excel (.xls) local
caminho_excel = '/home/david/autom/testes'

# Ler dados do Excel para um GeoDataFrame do geopandas
gdf = pd.read_excel('/home/david/autom/testes/setor-teste-dictionary.xlsx')
print(gdf)


# Caminho para salvar o shapefile localmente
caminho_shapefile = '/home/david/autom/testes/1arquivvo1_shapefile.shp'

# Salvar o GeoDataFrame como shapefile
gdf = GeoDataFrame(gdf)

gdf.to_file(caminho_shapefile, driver='ESRI Shapefile')
