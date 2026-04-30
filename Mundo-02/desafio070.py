print ('-='*38)
print (f'{"LOJAS WEATHER":^76}')
print ('-='*38)
maiorp = menor = total = gasto = caro =0
barato = ''
while True:
    print ('-'*38)
    nome = str(input('Digite o nome do produto: '))
    num = float(input('Qual o preço do produto? R$ '))
    if num == 0:
        break
    total += 1
    if total == 1:
        maiorp = menor = num
    else:
        if num > maiorp:
            maiorp = num
        if num < menor:
            menor = num
            barato = nome
    gasto += num
    if num > 1000:
        caro += 1
    continuar = str(input('Deseja Continuar [Ss/Nn] ')).strip()[0].upper()
    if continuar not in 'SsNn':
        print ('Resposta inválida, tente novamente!')
        continue
    if continuar in 'Nn':
        break
print ('-='*38)
print (f'O total gasto foi R$ {gasto:.2f}')
print (f'Temos {caro} produtos custando mais de R$ 1000,00')
print (f'O nome do produto mais barato é {barato} e custa R$ {menor:.2f}')
print ('Fim do programa, obrigado por participar!')
print ('-='*38)