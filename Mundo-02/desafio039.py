from datetime import date
atual = date.today().year
nas = int(input('Que ano você nasceu(Apenas números): '))
resu = atual - nas
resu1 = resu - 18
if resu == 18:
    print ('Você deve se alistar esse ano! BUCHA KAKAKAKAK')
elif resu < 18:
    print(f'Ainda falta {str(resu1)[1:]} ano(s) para você se alistar!')
elif resu > 18:
    print(f'Você já se alistou ou está {str(resu1)} ano(s) atrasado.')
