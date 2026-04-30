def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print ('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print ('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        
def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print ('\033[31mPor favor, digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print ('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        
n1 = LeiaInt('Digite um valor Inteiro: ')
n2 = LeiaFloat('Digite um valor Real: ')
print (f'O valor inteiro digitado foi {n1}, e o valor real digitado foi {n2}.')