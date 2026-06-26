def pares(n):
    return [x for x in n if int(x) % 2 == 0]

lista = ["10", "3", "8", "15", "22", "7"]

print(pares(lista))
