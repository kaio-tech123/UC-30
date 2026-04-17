vendas = [877, 354, 176, 643, 908, 333]

soma_pares = 0

for valor in vendas:

    if valor % 2 == 0:
        soma_pares += valor
        print(f"O valor par encontrado foi: R$ {valor}")

print(f"A soma das vendas pares é: R$ {soma_pares}")
