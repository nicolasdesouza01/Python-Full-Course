sexo = str(input('Informe seu sexo: (M/F)')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = (str(input('Dados inválidos por favor informe seu sexo:')))
print (f'Sexo {sexo} registrado com sucesso!')