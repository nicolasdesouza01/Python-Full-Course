from utilidadescev.moeda import metade, dobro, aumento, moeda
Preço = float(input('Digite o preço: R$ '))
m =  metade(Preço)
print (f'A metade de {moeda(Preço)} é {moeda(m)}')
d = dobro(Preço)
print (f'O dobro de {moeda(Preço)} é {moeda(d)}')
a = aumento(Preço)
print (f'Aumentando 10%, temos {moeda(a)}')