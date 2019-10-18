import re

padrao = "."

# Modificando o texto para ser uma raw string
texto = r"\nEsta é uma aula de Python.\n Nesta aula vamos falar sobre expressões regulares.\n Espero que goste.\n"

resultado = re.search(padrao, texto, re.DOTALL)

print(f"*{resultado.group()}*")
# Resultado (encontrou uma barra literalmente e não um caractere enter \n):
#*\*