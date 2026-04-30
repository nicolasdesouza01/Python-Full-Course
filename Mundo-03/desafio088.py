from random import randint
from time import sleep
megasena = []
print('MEGA SENA'.center(40, '-'))
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, quantidade):
    megasena.append([])
    while len(megasena[i]) < 6:
        numero = randint(1, 60)
        if numero not in megasena[i]:
            megasena[i].append(numero)
    megasena[i].sort()
print(f'SORTEANDO {quantidade} JOGOS'.center(40, '-'))
for i in range(0, quantidade):
    print(f'Jogo {i + 1}: {megasena[i]}')
    sleep(1)
print('BOA SORTE'.center(40, '-'))