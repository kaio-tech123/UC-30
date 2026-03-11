contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
    "@joao": "João"
}

print("Chaves: ")
for insta in contato.keys():
    print(insta)

print("\n Valores: ")
for nome in contato.values():
    print(nome)

print("\n Pares: ")
for insta, nome in contato.items:
    print(f"{insta} --> {nome}")

contato = {
    "@camila": 1.66,
    "@paola": 1.50,
    "@sheron": 1.80,
    "@bruna": 1.60,
    "@joao": 1.70
}



print("Ordenar por chave: ")
for insta in sorted(contato.keys()):
    print(f"{insta} --> {contato[insta]:.2f}m")

from operator import itemgetter
print("\n Ordenado por valor (altura): ")
for insta, estatura in sorted(contato.items(), key=itemgetter(1)):
    print(f"{insta} --> {estatura:.2f}m")
    