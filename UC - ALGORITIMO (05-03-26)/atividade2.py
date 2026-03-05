import random


numeros = [91, 34, 67, 15, 82]
print("A lista original: ", numeros)

numeros.sort()
print("Após sort(): ", numeros)

numeros.sort(reverse=True)
print("Após sort(): ", numeros)

numeros2 = [80, 7, 10, 9, 10]
random.shuffle(numeros2)
print("Embaralhar: ", numeros2)

numeros3 = [45, 67, 12, 23, 92, 2]
print("A lista original: ", numeros3)

numeros3.sort()
print("Após sort(): ", numeros3)

numeros3.sort(reverse=True)
print("Após sort(): ", numeros3)

random.shuffle(numeros3)
print("Embaralhar: ", numeros3)