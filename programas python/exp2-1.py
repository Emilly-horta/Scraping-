import re

padrao = "."
texto = "\nEsta é uma aula de Python.\n Nesta aula vamos falar sobre expressões regulares.\n Espero que goste.\n"

# Com DOTALL
resultado = re.search(padrao, texto, re.DOTALL)

print(f"*{resultado.group()}*")
# Resultado (encontrou o enter, \n):
#*
#*