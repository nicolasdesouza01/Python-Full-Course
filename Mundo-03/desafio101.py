from datetime import date
def voto (ano_nascimento):
    data = date.today().year
    idade = data - ano_nascimento
    if 16 <= idade < 18 or idade >70:
        return f'voto é opcional.'
    elif 18 <= idade <= 70:
        return f'voto é obrogatório.'
    elif idade <16:
        return f'NÃO VOTA'
    

nasc = int(input('Quando você nasceu: '))
print (voto(nasc))

