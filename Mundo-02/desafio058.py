from random import randint
computador = randint(0,10)
print ('Sou seu computador, Acabei de pensar num número entre 0 e 10.')
print ('Será que você consegue adivinhar qual foi? ')
acertou = False
palp = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palp += 1
    if jogador == computador:
        acertou = True
    else: 
        if computador > jogador:
            print ('Um pouco mais!!')
        else:
            print ('Um Pouco menos!!')
print (f'Você acertou com {palp} tentativas!')