from datetime import date
atual = date.today().year
nascimento = int(input('Qual sua data de nascimento(Apenas números): '))
idade = atual - nascimento
print (f'O atleta tem {idade} anos')
if idade <= 9:
    print ('Classificação: MIRIM')
elif idade <=14:
    print ('Classificação: INFANTIL')
elif idade <= 19:
    print ('Classificação: JUNIOR')
elif idade <= 25:
    print ('Classificação: SÊNIOR')
elif idade <=26:
    print ('Classificação: MASTER')