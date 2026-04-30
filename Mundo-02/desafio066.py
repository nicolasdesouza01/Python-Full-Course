soma = quant = 0
while True:
    num = int(input('Digite um número: [Digite 999 para Parar] '))
    if num == 999:
        break
    soma += num
    quant += 1
print (f'Foram digitados {quant}, e a soma entre eles é {soma}')
