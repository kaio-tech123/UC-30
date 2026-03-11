
atleta = input("Digite o nome do atleta: ")
idade = int(input(f"Digite a idade de {atleta}: "))

if idade < 12:
    categoria = "Infatil"
elif 12 <= idade < 18:
    categoria = "Juvenil"
elif 18 <= idade < 60:
    categoria = "Adulto"
else:
    categoria = "Sênior"


print(f"BEM-VINDO(A) À COMPETIÇÃO, {atleta.upper()}!")
print(f"Com {idade} anos, sua categoria é: {categoria}")
