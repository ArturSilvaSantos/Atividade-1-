def letras_das_palavras(lista):
    return [letra for palavra in lista for letra in palavra]

lista = ["python", "java", "c"]

print(letras_das_palavras(lista))