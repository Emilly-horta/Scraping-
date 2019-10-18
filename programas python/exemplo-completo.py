from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitulo(url):
    try:
        html = urlopen(url)
    except HTTPError as erro:
        print(f"Ocorreu um erro HTTP: {erro}")
        return None
    except URLError as erro:
        print(f"Ocorreu um erro de URL: {erro}")
        return None
    except:
        print(f"Ocorreu um erro ao acessar a página.")
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        titulo = bsObj.body.h1
    except AttributeError as erro:
        print(f"Ocorreu um erro ao acessar o atributo.")
        return None
    except:
        print(f"Ocorreu um erro ao acessar os atributos.")
        return None

    return titulo

titulo = getTitulo(input("Informe a URL: "))

if titulo is None:
    print("Título não encontrado.")
else:
    print(titulo)
