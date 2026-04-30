from time import sleep
n1 = int (input ('Digite um valor: '))
n2 = int (input ('Digite um valor: '))
opçao = 0
fim = 0
while fim != 5:
    opçao = int(input('''Escolha uma opção
[1] somar os números
[2] multiplicar os números
[3] qual o maior entre eles
[4] adicionar NOVOS números
[5] encerrar programa '''))
    if opçao == 1:
        soma = n1 + n2
        print (f'O resultado da soma de {n1} + {n2} é {soma}')
    elif opçao == 2:
        mul = n1 * n2
        print (f'A multiplicação de {n1} x {n2} é {mul}')
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print (f'O maior número entre eles é {maior}')
    elif opçao == 4:
        n1 = int(input ('Digite um valor: '))
        n2 = int(input ('Digite um valor: '))
    elif opçao == 5:
        fim = 5
    else:
        print ('Tente novamente')
    sleep (1)
    print ('=-' * 20)
print ('Programa encerrado.')