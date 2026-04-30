numero = (int(input('Digite um número: ')), int(input('Digite outro número: ')), 
          int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print (f'Você digitou os números: {numero}')
print (f'O número 9 apareceu {numero.count(9)} vezes!')
if 3 in numero:
    print (f'O número 3 apareceu {numero.index(3)+1} vezes!')
else:
    print ('O número 3 não foi digitado!')
print ('Os números pares digitados foram: ', end=' ')
for n in numero:
    if n % 2 == 0:
        print (n, end=' ')