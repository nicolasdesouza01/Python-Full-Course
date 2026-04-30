menor = 0
maior = 0
for pess in range (1, 6):
    peso = float(input(f'Qual peso da {pess} pessoa: (Kg)'))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print (f'O maior peso lido foi de {maior}Kg')
print (f'O menor peso lido foi de {menor}Kg')
