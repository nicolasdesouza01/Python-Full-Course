print (f'{"LOJAS GUANABARA":=^40}')
preço = float(input('Preço das compras: R$'))
print (f'''FORMAS DE PAGAMENTO
[1] à vista/dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual a opção desejada de 1 a 4? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print (f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print (f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = preço
    print ('Opção invalida de pagamento, Tente novamente!')
print (f'Sua compra de {preço:.2f} vai custar {total:.2f} no final.')
