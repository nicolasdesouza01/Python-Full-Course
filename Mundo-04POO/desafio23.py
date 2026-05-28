import time
from abc import ABC, abstractmethod
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado * self.lado


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * 3.14159 * self.raio

    def area(self):
        return 3.14159 * (self.raio ** 2)


def executar_sistema():
    while True:
        console.clear()
        
        console.print(Panel(
            "[bold white]GEOMETRY ENGINE v2.0[/bold white]\n[cyan]Processamento de Polígonos e Formas Curvas[/cyan]",
            expand=False, 
            border_style="bright_blue",
            padding=(1, 2)
        ))

        try:
            console.print("\n[bold magenta]─── CONFIGURAÇÃO DE ENTRADA ───[/bold magenta]")
            
            raw_lado = console.input("[white]➤ Medida do Lado (Quadrado): [/white]").replace(',', '.')
            raw_raio = console.input("[white]➤ Medida do Raio (Círculo): [/white]").replace(',', '.')
            
            valor_lado = float(raw_lado)
            valor_raio = float(raw_raio)

            console.print("\n")
            
            with console.status("[bold yellow]Sincronizando modelos...", spinner="bouncingBall"):
                time.sleep(1.2)
                quadrado = Quadrado(valor_lado)
            
            with console.status("[bold green]Aplicando fórmulas matemáticas...", spinner="dots"):
                time.sleep(1.2)
                circulo = Circulo(valor_raio)

            tabela = Table(
                title="\n[bold underline yellow]RELATÓRIO DE CÁLCULO FINAL[/bold underline yellow]",
                header_style="bold cyan",
                border_style="white",
                show_lines=True
            )

            tabela.add_column("Forma", justify="center", style="bold magenta")
            tabela.add_column("Lados", justify="center")
            tabela.add_column("Medida Base", justify="center", style="green")
            tabela.add_column("Perímetro", justify="right", style="bold white")
            tabela.add_column("Área", justify="right", style="bold white")

            tabela.add_row(
                "Quadrado", 
                str(quadrado.qtd_lados), 
                f"{quadrado.lado}".replace('.', ','), 
                f"{quadrado.perimetro():.2f}".replace('.', ','), 
                f"{quadrado.area():.2f}".replace('.', ',')
            )

            tabela.add_row(
                "Círculo", 
                "N/A", 
                f"{circulo.raio}".replace('.', ','), 
                f"{circulo.perimetro():.2f}".replace('.', ','), 
                f"{circulo.area():.2f}".replace('.', ',')
            )

            console.print(tabela)

        except ValueError:
            console.print("\n[panel red][bold]ALERTA DE SISTEMA:[/bold]\nEntrada inválida. Use apenas números (ex: 12,5).[/panel red]")

        console.print("\n" + "─" * 40)
        opcao = console.input("[bold yellow]Deseja realizar nova análise? (S/N): [/bold yellow]").strip().lower()
        
        if opcao != 's':
            console.print("\n[bold green]Encerrando processos e limpando cache...![/bold green]")
            time.sleep(1.5)
            break

if __name__ == "__main__":
    executar_sistema()