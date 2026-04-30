times = ('Palmeiras', 'Fluminense', 'São Paulo', 'Flamengo', 'Bahia', 
    'Athletico-PR', 'Coritiba', 'Atlético-MG', 'Red Bull Bragantino', 'Vitória', 
    'Vasco', 'Botafogo', 'Grêmio', 'Internacional', 'Santos', 
    'Corinthians', 'Mirassol', 'Chapecoense', 'Remo', 'Cruzeiro')
print (40*'=-')
print (f'lista de times do Brasileirão: {times}')
print (40*'=-')
print (f'Os 5 primeiros são: {times[0:5]}')
print (40*'=-')
print (f'Os 4 últimos são: {times[-4:]}')
print (40*'=-')
print (f'Times em ordem alfabética: {sorted(times)}')
print (40*'=-')
time = str(input('Quer saber em qual posição o seu time está? Qual o nome dele? ')).strip()
if time in times:
    print (f'O {time} está na {times.index(time)+1}ª posição')
else:    print (f'O {time} não está na lista de times do Brasileirão')