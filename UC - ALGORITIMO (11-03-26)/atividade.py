aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno["nota1"] = float(input("Digite a nota da primeira prova: "))
aluno["nota2"] = float(input("Digite a nota da segunda prova: "))

media = (aluno["nota1"] + aluno["nota2"]) / 2
aluno['media'] = media

if aluno["media"] >= 7:
    situacao = "Aprovado"
elif 5 <= aluno["media"] < 7:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Dados do Aluno: {aluno["nome"]}")
print(f"Nota 1: {aluno["nota1"]}")
print(f"Nota 2: {aluno["nota2"]}")
print(f"Média Final: {aluno["media"]:.1f}")
print(f"Situação: {situacao}")
