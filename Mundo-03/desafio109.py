from utilidadescev.moeda import metade, dobro, aumento, moeda
Preço = float(input('Digite o preço: R$ '))
print (f'A metade de {moeda(Preço)} é {metade(Preço, True)}')
print (f'O dobro de {moeda(Preço)} é {dobro(Preço, True)}')
print (f'Aumentando 10%, temos {aumento(Preço, True)}')