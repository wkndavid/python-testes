import pandas as pd

# Seu DataFrame (substitua isso pelo caminho do seu arquivo CSV ou Excel)
caminho_arquivo = '/home/david/autom/teste-excel.xlsx'  # ou 'caminho/do/seu/arquivo.xlsx'
df = pd.read_csv(caminho_arquivo) if caminho_arquivo.endswith('.csv') else pd.read_excel(caminho_arquivo)

# Dicionário de traduções (substitua isso pelo seu dicionário)
traducoes = {
    'SAIN': 'Setor de Áreas Isoladas Norte',
    'SH BOA VISTA - IMPÉRIO DOS NOBRES': 'Setor Habitacional Boa Vista - Império dos Nobres',
    'SMAS': 'Setor de Múltiplas Atividades Sul',
    # Adicione outras traduções conforme necessário
}

# Substituir valores apenas nas células que têm palavras para traduzir e deixa todas em caixa alta
df['se_setor'] = df['se_setor'].replace(traducoes).str.upper()

# Criar um novo arquivo com sufixo "_traduzido"
novo_caminho_arquivo = caminho_arquivo.replace('.csv', 'teste-traduzido.csv') if caminho_arquivo.endswith('.csv') else caminho_arquivo.replace('.xlsx', '1teste-traduzido.xlsx')
df.to_csv(novo_caminho_arquivo, index=False) if caminho_arquivo.endswith('.csv') else df.to_excel(novo_caminho_arquivo, index=False)

# Exibir mensagem quando o processo estiver concluído
print(f"Tradução concluída. Novo arquivo salvo em: {novo_caminho_arquivo}")
print(novo_caminho_arquivo)