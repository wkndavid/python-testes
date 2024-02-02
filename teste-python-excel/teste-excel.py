import pandas as pd

# Definição do Dicionário de Mapeamento
mapeamento = {'AB': 'Traducao_AB', 'CD': 'Traducao_CD'}

# Caminho para o arquivo Excel
caminho_excel = '/home/david/autom/teste-python-excel/teste-dictionary.xlsx'

# Ler o arquivo Excel
df = pd.read_excel(caminho_excel)

# Alteração direta dos valores na coluna de chave
df['ColunaChave'] = df['ColunaChave'].replace(mapeamento)

# Exibir o DataFrame resultante
print(df)
