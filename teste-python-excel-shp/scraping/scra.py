import requests
from bs4 import BeautifulSoup

url = 'http://doc.brazilia.jor.br/Centro/Setor-Bancario-Sul-quadra-201.shtml'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)


# Extrair dados da página usando BeautifulSoup
# ...

