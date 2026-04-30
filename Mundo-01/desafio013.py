sal = float(input('Qual é o sálario do funcionário? R$ '))
por = float(input('Qual a porcentagem (%) a adicionar: '))
novo = sal + (sal * por / 100)
print (f'Um funcionário que ganhava R${sal:.2f}, com aumento de {por}%, ele vai ganhar R${novo:.2f} ')