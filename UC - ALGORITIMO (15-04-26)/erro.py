def soma_segura(a, b):
    try:
        return a + b
    except TypeError:
        print("Entrada inválida")
        return 0