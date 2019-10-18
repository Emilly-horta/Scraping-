from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

# Quero só os links do folha.uol do mês 11 de 2017, da categoria mercado
html = urlopen("https://www.folha.uol.com.br/")
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a", {"href":re.compile(".*\.folha\.uol\.com\.br/mercado/2017/11/.*\.shtml")})

for link in links:
    print(link["href"])

