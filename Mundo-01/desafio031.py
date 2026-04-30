dis = float(input('Qual a distância da sua viagem? '))
print (f'Você está prestes a começar uma viagem de {dis:.2f}Km.')
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print (f'E o preço da sua passagem será de {preço:.2f}')