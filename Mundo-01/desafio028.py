from random import randint
from time import sleep
cim = randint(0,5)
print ('-=-'*20)
print ('Vou pensar em um número de 0 a 5, tente adivinhar...')
print ('-=-'*20)
jog = int(input('Que número eu pensei?')) 
print ('CARREGANDO...')
sleep (0.5)
if jog == cim:
    print('PARABÉNS, VOCÊ GANHOU!')
else:
    print(f'Você PERDEU, Eu pensei no {cim} e não no {jog}')