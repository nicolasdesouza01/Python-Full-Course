numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {numero[n]}')
        continu = str(input('Deseja Continuar [S/N] ')).strip()[0].upper()
        if continu in 'SsNn':
            if continu in 'Nn':
                break
print('Fim do programa, obrigado por participar!')