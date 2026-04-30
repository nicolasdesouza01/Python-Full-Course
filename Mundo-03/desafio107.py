from utilidadescev.moeda import metade, dobro, aumento
Preço = float(input('Digite o preço: R$ '))
m =  metade(Preço)
print (f'A metade de R${Preço} é {m}')
d = dobro(Preço)
print (f'O dobro de {Preço} é {d}')
a = aumento(Preço)
print (f'Aumentando 10%, temos {a}')