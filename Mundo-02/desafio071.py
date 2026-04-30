 # Simulador de caixa eletrônico feito para o Desafio 071! Obrigado por conferir! #PartiuMundo3
print ('='*36)
print (f'{'BANCO WEATHER':^36}')
print ('='*36)
valor = int(input("Qual o valor que você deseja sacar? R$ "))
total = valor
totced = 0
ced = 200
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else: 
        if totced > 0:
            print (f'Total de {totced} cédulas de R$ {ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
           break
print ('='*36)
print ('Volte sempre ao BANCO WEATHER, obrigado por escolher nossos serviços!')
print ('='*36)