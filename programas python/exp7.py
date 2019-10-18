import re

# "*" = Zero ou mais ocorrências da expressão anterior
padrao = "X*"
texto = "Esta é uma aula de Python.\n Nesta aula vamos falar sobre expressões regulares.\n Espero que goste."
resultado = re.search(padrao, texto)
# Encontrou 0 ocorrências de X, mas não retorna None
print(f"*{resultado.group()}*")

# "+" = Uma ou mais ocorrências da expressão anterior
padrao = "X+"
texto = "Esta é uma aula de Python.\n Nesta aula vamos falar sobre expressões regulares.\n Espero que goste."
resultado = re.search(padrao, texto)
# Não encontrou 1 ou mais ocorrências de X, retorna None
if resultado:
    print(f"*{resultado.group()}*")
else:
    print("Não encontrou")

