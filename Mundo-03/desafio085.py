princ = [[], []]
valor = 0
for n in range(1, 8):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        princ[0].append(valor)
    else:        
        princ[1].append(valor)
print (f'Os números pares digitados foram {sorted(princ[0])}')
print (f'Os números ímpares digitados foram {sorted(princ[1])}')