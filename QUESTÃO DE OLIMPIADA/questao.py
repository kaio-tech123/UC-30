pao = 1
doce = 2 
bolo = 3

pao = int (input(f"Quantos pães você vendeu? "))
doce = int (input(f"Quantos doces você vendeu? "))
bolo = int (input(f"Quantos bolos você vendeu? "))

pontuação = (pao * 1) + (doce * 2) + (bolo * 3)

if pontuação >= 150:
    print(f"Sua pontuação foi de {pontuação}, você ganhou um bolo")
elif pontuação >= 120:
    print(f"Sua pontuação foi de {pontuação}, você ganhou um doce")
elif pontuação >= 100:
    print(f"Sua pontuação foi de {pontuação}, você ganhou um pão")
else:
    print(f"Sua pontuação foi de {pontuação}, você não recebe prêmio")       
    