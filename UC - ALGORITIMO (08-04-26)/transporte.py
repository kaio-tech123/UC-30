def calcular_gasto_transporte(passagem, dias_letivos):
   
    custo_diario = passagem * 2
    custo_total = custo_diario * dias_letivos
    
    print(f"Valor da passagem: R$ {passagem:.2f}")
    print(f"Dias letivos:      {dias_letivos}")
    print(f"Gasto diário:      R$ {custo_diario:.2f}")
    print(f"O gasto total de Maria esse mês foi de: R$ {custo_total:.2f}")

passagem_atual = 4.50
dias_no_mes = 22

calcular_gasto_transporte(passagem_atual, dias_no_mes)