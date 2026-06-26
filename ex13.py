def pares_matriz(matriz):
    return [n for linha in matriz for n in linha if n % 2 == 0]

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(pares_matriz(matriz))