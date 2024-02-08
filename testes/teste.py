import pandas as pd

# Se não houver erros ao importar, a biblioteca está disponível

# Caminho para o arquivo Excel (.xls) local
caminho_excel = '/home/david/autom'

# Ler dados do Excel para um DataFrame do pandas
dados_excel = pd.read_excel('/home/david/autom/excel_final_v2.xls')
print(dados_excel)
# Realizar manipulações ou padronizações nos dados, se necessário
# Exemplo: converter todas as letras para maiúsculas na coluna 'Nome'
# dados_excel['Nome'] = dados_excel['Nome'].str.upper()

# Conectar-se ao banco de dados SQLite local (ou criar um novo se não existir)
#caminho_db_local = 'caminho/para/seu/arquivo_local.db'
#conexao_db_local = sqlite3.connect(caminho_db_local)

# Salvar o DataFrame no banco de dados SQLite local
# dados_excel.to_sql('tabela_nome', conexao_db_local, index=False, if_exists='replace')

# Fechar a conexão
#conexao_db_local.close()
