temperaturas =  [25, 27.9, 36, 29, 32]

total = 0

for temp in temperaturas:
    total += temp

dias =  len(temperaturas)
media = total / dias

print(f"Temperaturas registradas {temperaturas}")
print(f"A média delas na semana foi: {media:.1f}")