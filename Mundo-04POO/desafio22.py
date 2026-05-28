from rich import print
from rich.console import Console
console = Console()
from rich.panel import Panel
from time import sleep

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max: int = 5
    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado
    
    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1
    
    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f"[red]A TV está desligada[/]"
        else:
            conteudo = f"CANAL = "
            for canal in range(self.canal_min, self.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal}"

            conteudo += "\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on cyan] [/]"
                else:
                    conteudo += f"[black on white] [/]"

        tv = Panel(conteudo,title="[ TV ]", width=30, style="white")
        print(tv)

c = ControleRemoto()
while True:
    c.mostrar_tv()
    comando = str(console.input(f" < CH{c.canal_atual} >  - VOL{c.volume_atual} + "))
    match comando:
        
        case '0':
            console.print(f":stop_sign: [red]Encerrando o programa...[/]")
            for i in range(3, 0, -1):
                if i == 1:
                    console.print(f":hourglass_flowing_sand: [yellow]Encerrando em {i} segundo...[/]")
                else:
                    console.print(f":hourglass_flowing_sand: [yellow]Encerrando em {i} segundos...[/]")
                sleep(1)
            console.print("Volte sempre! :wave:")
            break
        
        case '@':
            c.liga_desliga()
        
        case '>':
            c.canal_mais()
        
        case '<':
            c.canal_menos()
        
        case '-':
            c.volume_menos()
        
        case '+':
            c.volume_mais()
    
    print ("\n" * 15)

    