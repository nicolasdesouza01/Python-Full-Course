kmh = float(input('Qual sua velocidade do carro? '))
if kmh > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80Km/h.')
    multa= (kmh-80)*7
    print(f'Você deverá pagar uma multa de {multa:.2f}R$')
print ('Tenha um bom dia! Dirija com segurança!')