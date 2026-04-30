# Programa de registro de pessoas.
cont = 0
mans = 0
jovensm = 0
while True:
    print ('-'*30)
    while True:
        dado = input('Digite sua idade: ')
        if dado.isnumeric():
            idade = int(dado)
            break
        else:
            print ('Idade inválida, tente novamente!')
    sexo = str(input('Qual seu sexo: [M/F] ')).upper().strip()[0]
    if sexo not in 'MmFf':
        print ('Sexo inválido, tente novamente!')    
        continue
    continuar = str(input('Deseja Continuar [S/N] ')).upper().strip()[0]
    if continuar not in 'SsNn':
        print ('Resposta inválida, tente novamente!')
        continue
    if idade > 18:
        cont += 1
    if sexo in 'Mm':
        mans += 1
    if sexo in "Ff" and idade < 20:
        jovensm += 1
    if continuar in 'Nn':
        break
print ('-='*30)
if jovensm == 1:    print (f'Temos {jovensm} mulher com menos de 20 anos cadastrada')
else:   print (f'Temos {jovensm} mulheres com menos de 20 anos cadastradas')
print ('-='*30)
if mans == 1:    print (f'Temos {mans} homem cadastrado')
else:   print (f'Temos {mans} homens cadastrados')
print ('-='*30)
print (f'Total de pessoas com mais de 18 anos: {cont}')
print ('Obrigado por participar!')