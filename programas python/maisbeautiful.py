from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://evaldowolkers.wordpress.com")

bsObj = BeautifulSoup(html.read(),"html.parser")

# .get_text() - Retorna todo o texto da página
print(bsObj.get_text())

# .tag - Retorna a primeira ocorrência da tag informada
print(bsObj.title)

# .tag.name - Retorna o nome da primeira ocorrência da tag informada
print(bsObj.title.name)

# Alterando o nome da tag título
bsObj.title.name = "titulo"

#Visualizando o nome da tag titulo (que era title)
print(bsObj.titulo.name)

# .tag.string - Retorna o texto da primeira ocorrência da tag informada
print(bsObj.title.string)

# .tag.parent - Retorna a tag externa à tag atual (tag pai/mãe)
print(bsObj.title.parent)

# .tag.parent.name - Retorna o nome da tag externa à tag atual (tag pai/mãe)
print(bsObj.title.parent.name)

# .tag['atributo'] - retorna todos os valores do atributo informado
print(bsObj.body['class'])
print(bsObj.button['aria-controls'])

# .find(id="descricao") - retorna a tag que possua o id informado
print(bsObj.find(id="menu-item-147"))

# .attrs retorna um dicionário com os atributos
print(bsObj.meta.attrs)

print("*********")
print(bsObj.name)