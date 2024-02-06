import pandas as pd
import re

# Dicionário de Traduções
traducoes = {'SAIN': 'teste-teste ', 'SH': 'teste-sh-sh', 'SETOR': 'traducao-teste-3'}
padrao_tamanho_minimo = 4

# Caminho para o arquivo Excel
caminho_excel = '/home/david/autom/teste-excel.xlsx'

# Ler o arquivo Excel
df = pd.read_excel(caminho_excel)

# Função para identificar e traduzir palavras com base no tamanho
def identificar_e_traduzir(texto):
    palavras = re.findall(r'\b\w+\b', str(texto))
    palavras_traduzidas = [traducoes[p] if len(p) > padrao_tamanho_minimo and p in traducoes else p for p in palavras]
    return ' '.join(palavras_traduzidas)

# Aplicar a função a todas as células do DataFrame
for coluna in df.columns:
    df[coluna] = df[coluna].apply(identificar_e_traduzir)

# Exibir o DataFrame resultante
print(df)