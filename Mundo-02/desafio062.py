print ('Calculo de PA')
print ('-='*20)
primeiro = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
mais = 10
cont = 1
total = 0
while mais !=0:
    total += mais
    while cont <= total:
        print (f'{termo} - ', end='')
        cont += 1
        termo += razão
    print ('PAUSA')
    mais = int(input('Quantos termos vocẽ quer a mais? (digite apenas 0 para finalizar!) '))
print (f'Progressão finalizada com {total} de termos mostrados.')
