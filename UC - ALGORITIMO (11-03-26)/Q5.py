aluno = input("Digite seu nome completo: ")

matricula_str = input("Digite o número da matrícula: ")
matricula = int(matricula_str)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = nota1 + nota2 / 2 

print(" HISTÓRICO ESCOLAR OFICIAL")
print(f"ALUNO: {aluno.upper()}")
print(f"MATRÍCULA: {matricula}")
print(f"NOTA 1: {nota1:>6.1f}")
print(f"NOTA 2: {nota2:>6.1f}")
print(f"MÉDIA FINAL: {media:>4.1f}")

