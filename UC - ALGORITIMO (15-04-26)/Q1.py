def calcular_media():
    soma_notas = 0
    try:
       
        for i in range(3):
            nota = float(input("Digite uma nota: "))
            soma_notas += nota
    
        media = soma_notas / 3
        print(f"Média final: {media:.2f}")

    except ValueError:
        print("As notas devem ser numéros.")

calcular_media()
