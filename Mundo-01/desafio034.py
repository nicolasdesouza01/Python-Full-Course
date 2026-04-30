sal = float(input('Qual o salário do funcionário? R$'))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print (f'Quem ganhava {sal:.2f}R$ passa a ganhar {novo:.2f}R$ agora.')