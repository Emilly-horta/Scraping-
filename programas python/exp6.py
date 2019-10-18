import re

# "[]" = Qualquer Caractere dos listados individualmente
padrao = "[Eeé]" # No findall encontra 3 ocorrências de "Esta" e "Espero"
texto = "Esta é uma aula de Python.\n Nesta aula vamos falar sobre expressões regulares.\n Espero que goste."
resultado = re.findall(padrao, texto)
print(resultado)

