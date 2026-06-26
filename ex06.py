def contar_vogais(texto):
    vogais = "aeiou"
    return sum(1 for letra in texto if letra in vogais)

lista = ["python"]

print(contar_vogais(lista))