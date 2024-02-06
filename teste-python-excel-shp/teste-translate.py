import geopandas as gpd
import os
import re

# Caminho para o arquivo shapefile
shapefile_path = 'caminho/para/seu/arquivo.shp'

# Carregar o shapefile como GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# Dicionário de substituição para cada coluna
dicionario = {
    'NomeDaColuna1': {'ValorAntigo1': 'NovoValor1', 'ValorAntigo2': 'NovoValor2'},
    'NomeDaColuna2': {'OutroValorAntigo1': 'OutroNovoValor1', 'OutroValorAntigo2': 'OutroNovoValor2'},
    # Adicione mais colunas conforme necessário
}

# Iterar sobre as colunas do GeoDataFrame
for coluna in gdf.columns:
    # Verificar se a coluna está no dicionário
    if coluna in dicionario:
        # Aplicar regex ou substituição conforme necessário
        for valor_antigo, novo_valor in dicionario[coluna].items():
            gdf[coluna] = gdf[coluna].replace({valor_antigo: novo_valor}, regex=True)#

# Mostrar o GeoDataFrame após a manipulação
print("GeoDataFrame após a manipulação:")
print(gdf)

# Salvar o GeoDataFrame de volta para um novo arquivo shapefile
novo_shapefile_path = 'caminho/para/seu/novo_arquivo.shp'
gdf.to_file(novo_shapefile_path, driver='ESRI Shapefile')
