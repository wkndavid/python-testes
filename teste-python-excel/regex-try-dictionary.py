import pandas as pd
import re

# Caminho para o arquivo Excel
caminho_excel = '/caminho/para/seu/arquivo_excel.xlsx'

# Ler o arquivo Excel
df = pd.read_excel(caminho_excel)

# Nome da coluna que contém as palavras
coluna_palavras = 'Palavras'

# Função para aplicar regras específicas e traduzir
def processar_palavra(palavra):
    # Aqui você pode adicionar suas próprias regras ou lógica de processamento
    # No exemplo, vamos apenas traduzir 'AB' para 'Traducao_AB'
    if palavra == 'AB':
        return 'Traducao_AB'
    else:
        return palavra

# Aplicar a função a todas as células da coluna
df[coluna_palavras] = df[coluna_palavras].apply(lambda x: ' '.join([processar_palavra(p) for p in re.findall(r'\b\w+\b', str(x))]))

# Exibir o DataFrame resultante
print(df)
