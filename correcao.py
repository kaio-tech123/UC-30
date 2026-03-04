numero = int(input("Digite um valor: "))

if numero % 2 == 0:
    resultado = numero ** 2
else:
    resultado =  numero ** 3

print("Resultado ", resultado)


#pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if (usuario == "procopio" and senha == "12345") or (usuario == "paiva" and senha == "54321"): 
    print("Seja bem vindo!")

else: print("Usuário ou senha não confere")

#pppppppppppppppppppppppppppppppppppppppppppppppppppppppppp

nome = input("Digite seu nome: ")
senhaCorreta = "123456"

tentativa = 3

while tentativa > 0:
    senha = input("Digite sua senha: ")


    if senha == senhaCorreta:
        print(f"Olá {nome}! Seja bem vindo!")
        break

    else: 
        tentativa -= 1

        if tentativa == 2:
           print("Senha incorreta! Você tem 2 tentativas")
        elif tentativa == 1:
            print("Senha incorreta! Você tem 1 tentativas")
        elif: 
            print("Senha bloqueada!")