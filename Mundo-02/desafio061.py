print ('CALCULO DE PA')
print ('-='*20)
primeiro = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print (f'{termo} - ', end='')
    termo += razão
    cont += 1
print ('FIM')