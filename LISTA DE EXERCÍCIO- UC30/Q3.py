total = 0.0

print("Digite o valor de cada compra e digite 0 para finalizar:")

while True:
    valor = float(input("Valor do item: R$ "))
    
    if valor == 0:
        break 

    total += valor 

print(f"O valor total da compra é: R$ {total:.2f}")