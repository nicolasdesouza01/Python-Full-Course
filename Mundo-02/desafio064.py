num = conta = soma = 0
num = int(input('Digite um número para somar: [digite 999 para parar] '))
while num != 999:
    soma += num
    conta += 1
    num = int(input('Digite um número para somar: [Digite 999 para parar]'))
print (f'Você digitou {conta} números, e a soma total deles foi {soma}')