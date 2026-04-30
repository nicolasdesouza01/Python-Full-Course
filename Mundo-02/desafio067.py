cont = 0
min = 0
max = 0
while True:
    cont = int(input('Digite um número para tabuada: [Digite um número negativo para Parar] '))
    if cont < 0:
        break
    min = int(input('Digite qual o número mínimo que deseja começar a multiplicação:'))
    max = int(input('Digite qual o número máximo que deseja terminar a multiplicação:'))
    if min > max:
        print (f'Número mínimo {min} é maior que o número máximo {max}, tente novamente!')
        continue
    print ('-='*35)  
    for c in range (min, max+1):
           print (f'{cont} x {c:2} = {cont*c}')
    print ('-='*35)
print ('Programa de tabuada encerrado. Volte sempre!')