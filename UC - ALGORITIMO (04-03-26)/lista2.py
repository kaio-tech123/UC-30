animal = ["Cachorro", "Gato"]
print("Lista inicial: ", animal)

animal.append("Pato")
print("Lista atualizada: ", animal)

animal.insert(1, "Coelho")
print("Lista atualizada: ", animal)

animal.extend(["macaco", "leão"])
print("Lista atualizada: ", animal)

animal.remove("macaco")
print(animal)

removido = animal.pop
print(f"Removido: {removido}")
print("Após pop()", animal)

removido2 = animal.pop(1)
print(f"Removido do índice 1 {removido2}")
print("Após pop(1): ", animal)

del animal[0]
print("Após del ", animal)

animal.clear()
print(animal)