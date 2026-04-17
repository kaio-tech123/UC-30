def calcular_imc():
    try:
        
        peso = float(input("Qual o seu peso? "))
        altura = float(input("Qual sua altura? "))

        imc = peso / (altura ** 2)

        print(f"\nSeu IMC é de: {imc:.2f}")

        if imc < 24.9:
            print("Você está magro")
        else:
            print("Você está gordo")

    except ValueError:
         print("Por favor digite apenas números")

calcular_imc()