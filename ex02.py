def descendentes(a):
    if a[1] == []:
        return []
    else:
        return [nm for nm, _ in a[1]] + \
               [nm for f in a[1] for nm in descendentes(f)]

def descendentes_compreensao(arvore):
    return [
        pessoa
        for filho in arvore[1]
        for pessoa in [filho[0]] + descendentes(filho)
    ]

arvore = (
    "João",
    [
        ("Maria", [
            ("Pedro", []),
            ("Ana", [])
        ]),
        ("Carlos", [
            ("Lucas", [])
        ])
    ]
)

print(descendentes_compreensao(arvore))