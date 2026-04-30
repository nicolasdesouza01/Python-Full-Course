continuar = 'S'
soma = quant = maior = menor = media = 0
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    continuar = str(input('Deseja Continuar [Ss/Nn] ')).strip()[0].upper()
    quant += 1
    soma += num
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    media = soma / quant
print (f'O Maior número digitado foi {maior}, O menor número digitado foi {menor}')
print (f'E a média de todos os números citados foi {media:.2f}')