alunos = {}
print('-=' * 20)
alunos['nome'] = input('Nome: ')
alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['média'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
print('-=' * 20)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')