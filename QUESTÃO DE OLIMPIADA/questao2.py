inicial = int(input("Diga o número de pessoas infectadas no dia 0: "))
reprodução = int(input("Diga o fator reprodutivo: "))
alvo = int(input("Diga o número alvo de pessoas infectadas: "))

infectados = inicial

novos_infectados = inicial
dias_passados = 0

while infectados < alvo:
    dias_passados += 1
    
    novos = novos_infectados * reprodução
    
    total_infectados += novos
    
    novos_infectados_ontem = novos

print(f"\nSerão necessários {dias_passados} dias para atingir o alvo.")