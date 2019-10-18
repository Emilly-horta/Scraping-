import re

# Definindo o padrão usando circunflexo
# "^" = Início da string
padrao = "E" # No findall encontra 2 ocorrências de Esta e Espero
#padrao = "^E" # Forçando retornar somente se estiver no início da string

texto = "Esta é uma aula de Python.\n Nesta aula vamos falar sobre expressões regulares.\n Espero que goste.\n"

resultado = re.findall(padrao, texto)
print(resultado)