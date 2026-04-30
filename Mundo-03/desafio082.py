lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
    pares = []
    impares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Você digitou os números {lista}')
print(f'Os números pares digitados foram {pares}')
print(f'Os números ímpares digitados foram {impares}')