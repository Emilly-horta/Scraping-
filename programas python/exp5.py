import re

# Definindo o padrão usando cifrão
# "$" = Fim da string
padrao = "\." # No findall encontra 3 ocorrências de Esta e Espero
#padrao = "\.$" # Forçando retornar somente se estiver no fim da string

texto = "Esta é uma aula de Python.\n Nesta aula vamos falar sobre expressões regulares.\n Espero que goste."

resultado = re.findall(padrao, texto)
print(resultado)