lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    parar = str(input('Deseja parar? [S/N]')).strip().upper()[0]
    if parar in 'S':
        break
print (f'Foram digitados {len(lista)} números, a ordem decrescente dos números é {sorted(lista,reverse=True)}')
if 5 in lista:
    print ('O valor 5 está na lista')
else:
    print ('O valor 5 não está na lista')