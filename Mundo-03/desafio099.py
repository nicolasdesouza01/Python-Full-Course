from time import sleep
def maior(*num):
    cont = maior = 0
    print ('='*35)
    print('analisando os valores passados')
    for valor in num:
        print(f'{valor}',end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print (f'\nForam informados {cont} valores ao todo')
    print (f'O maior valor informado foi {maior}')

maior (0, 7, 6)
maior (8,7,5)
maior(0)
maior (0,33,44,8,6)