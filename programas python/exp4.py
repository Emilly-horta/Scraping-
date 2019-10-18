import re

# Definindo o padrão usando barra invertida
# "\" = Caractere de escape
#padrao = "." # Qualquer caracter, exceto quebra de linha
padrao = "\." # Localiza ocorrências do caractere ponto

texto = r"Esta é uma aula de Python.\n Nesta aula vamos falar sobre expressões regulares.\n Espero que goste.\n"

resultado = re.findall(padrao, texto)
print(resultado)