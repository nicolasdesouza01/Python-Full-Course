from rich.console import Console
console = Console()
from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        console.print(f":open_book: [green]Você acabou de abrir o Livro [blue]'{self.titulo}'[/] que tem [yellow]{self.total_paginas} páginas[/] no total. Você agora está na [red]pagina {self.pagina_atual}[/][/green]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                console.print(f"Pág: {self.pagina_atual} :arrow_forward: ", end='')
                time.sleep(0.3)
                cont += 1
        print (f"[blue]Você avançou {cont} e agora está na [red]pagina {self.pagina_atual}[/][/blue]")
        if self.fim_do_livro():
            console.print(f":closed_book: [red]Você chegou ao final do Livro '{self.titulo}'[/]")

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False
 

l1 = Livro("CEV de Python", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)