from random import shuffle
alunos = input('Diga o nome dos alunos separados por vírgula: ').split(',')
shuffle (alunos)
print (f'A ordem de alunos será {alunos}')