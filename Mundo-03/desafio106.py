

def ajuda (com):
    help(com)

comando = ''
while True:
    comando = str(input("Função o Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)