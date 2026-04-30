from random import randint
computador = randint(0, 10)
jogador = 0
cont = 0
total = 0
print ('Vamos jogar PAR ou ÍMPAR!')
while True:
    computador = randint(0, 10)   
    desc = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    jogador = int(input('Digite um valor de 0 a 10: '))
    total = computador + jogador
    if desc == 'P' and total % 2 == 0 or desc == 'I' and total % 2 == 1:
        print (f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} DEU {"PAR" if total % 2 == 0 else "ÍMPAR"}')
        print ('Você VENCEU!')
        cont += 1
        continue
    else:
        print (f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} DEU {"PAR" if total % 2 == 0 else "ÍMPAR"}')
        print ('Você PERDEU!')
        break
if cont == 1:
    print (f'GAME OVER! Você venceu {cont} vez')
else:  
    print (f'GAME OVER! Você venceu {cont} vezes')
     