from time import sleep
from random import randint
dici = {}
for c in range(0, 5):
    dici[f'jogador{c+1}'] = randint(1, 6)
for k, v in dici.items():
    print(f'O {k} tirou {v} no dado.')
    sleep (0.5)
sleep (1)
rank = sorted(dici.items(), key=lambda item: item[1], reverse=True)
print ('-='* 20)
print(f'{"== RANKING DOS JOGADORES ==":=^40}')
for i, v in enumerate(rank):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep (0.5)