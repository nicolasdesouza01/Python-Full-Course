frase = str(input('Escreva uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A letra A aparece pela primeira vez em {frase.find('A')+1}')
print(f'A letra A aparece pela última vez em {frase.rfind('A')+1}')