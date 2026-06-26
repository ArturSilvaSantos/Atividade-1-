def palavras_maiores_5_letras(lista):
    return [palavra for palavra in lista if len(palavra) > 5]

lista = ["python", "java", "javascript", "c", "programacao", "go"]

print(palavras_maiores_5_letras(lista))