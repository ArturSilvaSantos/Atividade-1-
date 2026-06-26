def achatar(lista):
    resultado = []

    for item in lista:
        if type(item) == list:
            resultado.extend(achatar(item))
        else:
            resultado.append(item)

    return resultado
def achatar(lista):
    return [
        item
        for sub in lista
        for item in (achatar(sub) if isinstance(sub, list) else [sub])
    ]
lista = [1, 2, [4, 2], 5, [2, [1, 7], [9, [3]]]]

print(achatar(lista))