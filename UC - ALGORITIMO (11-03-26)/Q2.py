distancia = 450
consumo = 8
preco = 5.50          

Consumidos = distancia / consumo

total = Consumidos * preco

print(f"Distância percorrida: {distancia} km")
print(f"Consumo do veículo: {consumo} km/l")
print(f"Preço da gasolina: R$ {preco:.2f}")
print(f"Total de litros usados: {Consumidos:.2f} L")
print(f"Custo total do dia: R$ {total:.2f}")