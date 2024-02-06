import pandas as pd

# Seu DataFrame (substitua isso pelo caminho do seu arquivo CSV)
caminho_arquivo = '/home/david/autom/teste-excel.xlsx'
df = pd.read_csv(caminho_arquivo)

# Dicionário de traduções (substitua isso pelo seu dicionário)
traducoes = {
    'SAIN': 'Translation_SAIN',
    'SH BOA VISTA - IMPÉRIO DOS NOBRES': 'Translation_SH_BOA_VISTA',
    'SMAS': 'Translation_SMAS',
    # Adicione outras traduções conforme necessário
}

# Substituir valores apenas nas células que têm palavras para traduzir
df['Local'] = df['Local'].replace(traducoes)

# Criar um novo arquivo CSV com o sufixo "_traduzido"
novo_caminho_arquivo = caminho_arquivo.replace('.csv', '_traduzido.csv')
df.to_csv(novo_caminho_arquivo, index=False)

# Exibir mensagem quando o processo estiver concluído
print(f"Tradução concluída. Novo arquivo salvo em: {novo_caminho_arquivo}")
