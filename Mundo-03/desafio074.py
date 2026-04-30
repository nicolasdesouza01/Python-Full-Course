from random import randint
num = (randint(0, 10)),(randint(0, 10)),(randint(0, 10)),(randint(0, 10)),(randint(0, 10))
print ('Os números sorteados foram: ', end=' ')
for n in num:
    print (f' {n}', end=' ')
print (f'\nO maior número sorteado foi {max(num)}!')
print (f'O menor número sorteado foi {min(num)}!')