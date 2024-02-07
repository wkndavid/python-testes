import re

# Função para traduzir siglas
def traduzir_sigla(sigla):
    # Adapte essa função conforme necessário
    traducao = {
        "ADE": "Área de Desenvolvimento Econômico",
        "AE": "Área Especial",
        "AeB": "Aeroporto de Brasília",
        # Adicione mais traduções conforme necessário
    }

    return traducao.get(sigla, sigla)  # Retorna a tradução se existir, senão, retorna a sigla original

# Função para identificar e traduzir siglas no texto
def identificar_e_traduzir(texto):
    padrao_sigla = re.compile(r'\b[A-Za-z]{2}\b')  # Padrão de duas letras isoladas

    # Encontrar todas as siglas no texto
    siglas_encontradas = padrao_sigla.findall(texto)

    # Traduzir as siglas
    traducoes = [traduzir_sigla(sigla) for sigla in siglas_encontradas]

    return siglas_encontradas, traducoes

# Exemplo de uso
texto_exemplo = """
ADE: Área de Desenvolvimento Econômico
AE: Área Especial
AeB: Aeroporto de Brasília
Alguma outra coisa AE que não é uma sigla
"""

# Identificar e traduzir siglas no texto de exemplo
siglas, traducoes = identificar_e_traduzir(texto_exemplo)

# Exibir resultados
for sigla, traducao in zip(siglas, traducoes):
    print(f"Sigla: {sigla}, Tradução: {traducao}")
