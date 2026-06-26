def positivos(n):
    return [x for x in n if int(x) >= 0]
lista = ["2", "3", "4", "5", "6", "7", "8", "11", "13", "15", "17"]

print(positivos(lista))