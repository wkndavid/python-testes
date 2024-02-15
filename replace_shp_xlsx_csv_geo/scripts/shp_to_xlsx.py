import geopandas as gpd

# Caminho para o shapefile (.shp) local
#
# Execute em algum => Terminal / Linha de comando / Shell => o comando 'pwd' =>
# (Exemplo de retorno => '/home/david/autom/replace_shp_xlsx_csv_geo/excel_example_file.xlsx' ou 'C:\\Users\\Documents\\arquivo.shp') => para achar o caminho do arquivo existente na estrutura de pastas =>
caminho_shapefile = '/home/david/autom/replace_shp_xlsx_cvs_geo/files/'

# Lê o shapefile para um GeoDataFrame
gdf = gpd.read_file('/home/david/autom/replace_shp_xlsx_csv_geo/files/quadras.shp')

# Caminho para salvar o arquivo Excel localmente (com a extensão .xlsx) =>
caminho_excel = '/home/david/autom/replace_shp_xlsx_csv_geo/files/123.xlsx'

# Salva o GeoDataFrame como um arquivo Excel =>
gdf.to_excel(caminho_excel, index=False, engine='openpyxl')
