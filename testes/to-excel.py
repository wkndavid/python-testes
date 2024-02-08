import geopandas as gpd

# Caminho para o shapefile (.shp) local
caminho_shapefile = '/home/david/autom/setor'

# Ler o shapefile para um GeoDataFrame
gdf = gpd.read_file('/home/david/autom/setor/setor.shp')

# Caminho para salvar o arquivo Excel localmente (com a extensão .xlsx)
caminho_excel = '/home/david/autom/setor/teste.xlsx'

# Salvar o GeoDataFrame como um arquivo Excel
try:
    gdf.to_excel(caminho_excel, index=False, encoding='utf-8')
except UnicodeEncodeError:
    try:
        gdf.to_excel(caminho_excel, index=False, encoding='utf-16')
    except UnicodeEncodeError:
        gdf.to_excel(caminho_excel, index=False, encoding='latin-1')
