resp = input("Você vai passar de ano? s/N:")
resultado = bool(resp)

print("Resposta ", resp)
print("Resultado ", resultado)

resp = input("Você vai passar de ano? s/N: "). strip().lower()

resultado = resp in ("s", "sim", "Sim", "SIM")

print("Resultado ", resultado)
print(type(resultado))
