from rich import print
from rich import inspect
class Funcionario:
    empresa = "JS Prime"
    
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __rich__(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}"



c1 = Funcionario("Maria", "TI", "Gerente")
print (c1)

c2 = Funcionario("Nicolas", "TI", "Junior")
print (c2)

c3 = Funcionario("Ines", "Saúde", "TE Enf")
print (c3)