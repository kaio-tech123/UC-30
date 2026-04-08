def financas(mesada, gastos):

    total_gastos = sum(gastos)
    saldo = mesada - total_gastos
    
    print(f"--- Resumo Financeiro ---")
    print(f"Mesada: R$ {mesada:.2f}")
    print(f"Gastos: R$ {total_gastos:.2f}")
    
    if saldo > 0:
        print(f"João economizou R$ {saldo:.2f}! Mandou bem! 💰")
    elif saldo == 0:
        print("João gastou exatamente o que tinha. Cuidado para não ficar no zero! ⚖️")
    else:
        print(f"João excedeu o orçamento em R$ {(saldo):.2f}. Hora de cortar gastos! ⚠️")

mesada = 500.00
gastos = [120.50, 50.00, 85.00, 40.00]

financas(mesada, gastos)