from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self. favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)


    def ficha(self):
        conteudo = f"[blue]Nome Real:[/] [black on blue] {self.nome} [/]"
        conteudo += f"\n[blue]Jogos favoritos:[/]"
        for num, game in enumerate(self.favoritos):
            conteudo+= f"\n:video_game: [white]{game}[/]"
        painel = Panel(conteudo, title=f"Jogador: {self.nick}", width=40, style="white")
        print(painel)


j1 = Gamer("Nicolas",  "PEN1TENT3")
j1.add_favoritos("GTA V")
j1.add_favoritos("Twisted")
j1.ficha()

j2 = Gamer("Laura", "L4UR4")
j2.add_favoritos("Minecraft")
j2.add_favoritos("The Sims")
j2.ficha()