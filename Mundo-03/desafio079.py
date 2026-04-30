num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
    else:
        print ('esse número já está na lista, por favor digite novamente...')
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if cont in 'N':
        break

num.sort()
print (f'Os valores digitados foram {num}')
