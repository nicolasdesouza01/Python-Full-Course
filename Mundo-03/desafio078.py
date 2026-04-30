valores = []
for c in range (1, 6):
    valores.append(int(input(f'Digite o valor de poçisão {c}: ')))
maior = max(valores)
menor = min(valores)
print (f'O maior número foi {maior} e está na posição: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}',end=' ')
print ()
print (f'O menor número foi {menor} e está na posição: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print (f'{i+1}',end=' ')