from datetime import date
print(f'{"CADASTRO DO TRABALHADOR":=^50}')
dados = {'nome': '', 'ano de nascimento': 0, 'carteira de trabalho': 0}
dados['nome'] = str(input('Nome: ')).strip()
dados['ano de nascimento'] = int(input('Ano de Nascimento: '))
dados['carteira de trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['carteira de trabalho'] != 0:
    dados['ano de contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['idade'] = date.today().year - dados['ano de nascimento']
    dados['aposentadoria'] = dados['idade'] + ((dados['ano de contratação'] + 35) - date.today().year)
print('=-' * 25)
for k, v in dados.items():
  if isinstance(v, float):
    print(f'{k}: R${v:.2f}')
  else:
    print(f'{k}: {v}')
print('=-' * 25)