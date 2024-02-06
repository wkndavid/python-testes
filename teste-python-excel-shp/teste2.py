import pandas as pd

# Função para mapear padrões para traduções
def traduzir(valor):
    # Exemplo: mapear padrões para traduções
    mapeamento = {'AB': 'Traducao_AB', 'CD': 'Traducao_CD'}

    # Verificar se algum padrão está presente no valor
    for padrao, traducao in mapeamento.items():
        if padrao in valor:
            return traducao

    # Se nenhum padrão for encontrado, manter o valor original
    return valor

# Caminho para o arquivo Excel
caminho_excel = '/home/david/autom/arquivo_excel.xlsx'

# Ler o arquivo Excel
df = pd.read_excel(caminho_excel)

# df['Palavras'] = df['Palavras'].replace(palavra_original, traducao) ====>  

# Aplicar a função de tradução à coluna desejada
df['ColunaValor'] = df['ColunaChave'].apply(traduzir)

# Exibir o DataFrame resultante
print(df)
