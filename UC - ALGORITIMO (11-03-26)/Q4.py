estoque = 100
receber = 50
vender = 30
devolver = 5

print(f"Estoque inicial: {estoque} unidades")
print(f"Recebe no mês: {receber} unidades")
print(f"Vende no mês: {vender} unidades ")
print(f"E devolve no mês: {devolver} unidades ")

print(f"Estoque final: {estoque + receber - vender - devolver} ")