from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://evaldowolkers.wordpress.com")
bsobj = BeautifulSoup(html, "html.parser")

#Localizar qualquer tag que tenha a propriedade class igual a comments-link
teste = bsobj.findAll("", {"class":"comments-link"})
for a in teste:
    print(a)

python = bsobj.findAll(text="Python")
for a in python:
    print(a)