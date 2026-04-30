from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print ('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print ('JO')
sleep (1)
print ('KEN')
sleep (1)
print ('PO!!!')
print ('-=' * 12)
print (f'Computador jogou {itens[computador]}')
print (f'Jogador Jogou {itens[jogador]}')
print ('-=' * 12)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print ('EMPATE!')
    elif jogador == 1:
        print ('JOGADOR VENCE!')
    elif jogador == 2:
        print ('COMPUTADOR VENCE!')
    else:
        print ('JOGADA INVÁLIDA!')
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print ('COMPUTADOR VENCE!')
    elif jogador == 1:
        print ('EMPATE!')
    elif jogador == 2:
        print ('JOGADOR VENCE!')
    else:
        print ('JOGADA INVÁLIDA!')
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print ('JOGADOR VENCEU!')
    elif jogador == 1:
        print ('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print ('EMPATE!')
    else:
        print ('JOGADA INVÁLIDA!')
