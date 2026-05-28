from rich import print
from rich.console import Console
console = Console()
class Caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
                console.print(f":warning: [yellow]Cor inválida, a caneta será criada com a cor [white]branca[/][/yellow]")
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            console.print(f":warning: [yellow]A {self.cor}caneta[/] está tampada, destampe para escrever.[/yellow]")
        else:
            console.print(F"{self.cor}{msg}[/]",end='')

    def quebrar_linha(self, qtd = 1):        
        console.print("\n" * qtd, end="")

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")
c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, Mundo!")
c2.escrever("Funciona!")
c2.quebrar_linha(3)
c3.escrever("Deu Certo!")

#c1.tampar()
c1.escrever("Não vai aparecer")