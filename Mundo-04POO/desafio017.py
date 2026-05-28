from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def __rich__(self):
        return f"[blue]{self.nome} custa R${self.preco:,.2f}[/blue]"
    

    def etiqueta(self):
        conteudo = f"[green]{self.nome.center(30, ' ')}[/green]"
        conteudo += f"[yellow]{'-'*30}[/yellow]"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"[yellow]{precof.center(30, '-')}[/yellow]"
        etiqueta = Panel(conteudo, title="[red]Produto[/red]", width=34)
        print (etiqueta)

p1 = Produto("iPhone 17 Pro Max", 25_000.85)
print (p1)
p1.etiqueta()

p2 = Produto("Notebook Gamer", 8_000)
print (p2)
p2.etiqueta()