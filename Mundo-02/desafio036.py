casa = float(input('Qual o valor da casa desejada: '))
sala = float(input('Qual seu salário: '))
anos = int(input(' Quantos anos você deseja pagar a casa: '))
prestação = casa / (anos*12)
min = sala * 30 / 100
print (f'Para pagar uma casa de {casa:.2f} em {anos}, a prestação será de R${prestação:.2f}')
if prestação <= min:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
