import pandas as pd

# Seu DataFrame (vou usar um exemplo simplificado)
data = {'Local': ['SAIN', 'SH BOA VISTA - IMPÉRIO DOS NOBRES', 'SMAS', ...]}  # Adicione todas as suas linhas aqui

df = pd.DataFrame(data)

# Dicionário de traduções (adicione todas as suas traduções aqui)
traducoes = {
    'SAIN': 'Translation_SAIN',
    'SH BOA VISTA - IMPÉRIO DOS NOBRES': 'Translation_SH_BOA_VISTA',
    'SMAS': 'Translation_SMAS',
    # Adicione outras traduções conforme necessário
}

# Criar nova coluna de tradução
df['Traducao'] = df['Local'].map(traducoes)

# Exibir DataFrame resultante
print(df)
