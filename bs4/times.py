#programa utilizando a lib bs4 para buscar links que conste os nomes de um dos 6 primeiros times do brasileirão 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re #lib de expressoes regulares

paginas = set()
paginas_invalidas = set()
nova_pagina = ""

def abrir_pagina(url_da_pagina):
    global paginas
    try:
        if url_da_pagina not in paginas_invalidas:
            html = urlopen(url_da_pagina)
            bsObj = BeautifulSoup(html, "html.parser")
            serie_a_g6_2017 = ('.corinthians.|.botafogo.|.vasco.|.palmeiras.|.flamengo.|.cruzeiro.')

            for link in bsObj.findAll("a", href=re.compile(serie_a_g6_2017)):
                if "href" in link.attrs:
                    if link.attrs['href'] not in paginas and link.attrs['href'] not in paginas_invalidas:
                        nova_pagina = link.attrs['href']
                        print(nova_pagina)
                        paginas.add(nova_pagina)
                        abrir_pagina(nova_pagina)
    except:
        paginas_invalidas.add(nova_pagina)

abrir_pagina("http://globoesporte.globo.com")
