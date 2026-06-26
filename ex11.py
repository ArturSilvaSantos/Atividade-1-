def notas_maiores_que5(n):
    return [x for x in n if int(x) > 5]

notas = ["2", "5", "6", "8", "3", "10", "7"]

print(notas_maiores_que5(notas))
