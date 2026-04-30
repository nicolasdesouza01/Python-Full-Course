nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print (f'Contando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f} ')
if media < 5.0:
    print(f'Sua média foi {media}, você não atingiu o limite mínimo e está reprovado.')
elif media >= 5.0 and media <7:
    print (f'Sua média foi {media} você ficou de recuperação!')
elif media > 6.9:
    print (f'Sua média foi de {media} você passou, Parabéns!')