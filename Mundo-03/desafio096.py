def área(larg, comp):
    d = larg * comp
    print (f'a área de um terreno {larg}x{comp} é de {d}m².')

print ('Controle de Terrenos')
print ('-'*20)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
área(l, c)