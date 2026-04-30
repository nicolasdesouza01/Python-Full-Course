from random import choice
alunos = input('Escreva o nome dos alunos separados por vírgula: ').split(",")
print (f'O aluno escolhido foi:{choice(alunos)}')