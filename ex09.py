def primos(n):
    return [x for x in n if eh_primo(int(x)) == True]

def eh_primo(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

lista = ["2", "3", "4", "5", "6", "7", "8", "11", "13", "15", "17"]

print(primos(lista))

