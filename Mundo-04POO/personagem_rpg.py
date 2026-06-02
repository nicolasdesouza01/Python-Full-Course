import random
from abc import ABC, abstractmethod
from rich.console import Console

console = Console()

class Personagem(ABC):
    def __init__(self, nome, vida_maxima, ataque, defesa, critico, esquiva):
        self.nome = nome
        self.vida_maxima = vida_maxima
        self.vida = vida_maxima
        self.ataque = ataque
        self.defesa = defesa
        self.critico = critico
        self.esquiva = esquiva
        self.golpes = []
        self.vivo = True

    def atacar(self, alvo):
        if self.vivo and alvo.vivo:
            golpe = random.choice(self.golpes)
            dano_bruto = random.randint(self.ataque // 2, self.ataque)
            
            is_critico = random.random() < self.critico
            if is_critico:
                dano_bruto = int(dano_bruto * 1.5)
            
            dano_real, status = alvo.receber_dano(dano_bruto)
            
            if status == "esquivou":
                console.print(f"[bold cyan]:dash: {alvo.nome}[/bold cyan] previu o movimento e se esquivou do [bold yellow]{golpe}[/bold yellow] de [bold red]{self.nome}[/bold red]!")
            elif status == "bloqueou":
                console.print(f"[bold blue]:shield: {alvo.nome}[/bold blue] bloqueou totalmente o ataque [bold yellow]{golpe}[/bold yellow] de [bold red]{self.nome}[/bold red]!")
            else:
                if is_critico:
                    console.print(f"[bold yellow]:high_voltage: ACERTO CRÍTICO! :high_voltage:[/bold yellow] [bold red]{self.nome}[/bold red] usou [bold yellow]{golpe}[/bold yellow] e obliterou [bold cyan]{alvo.nome}[/bold cyan] com [bold white]{dano_real}[/bold white] de dano!")
                else:
                    console.print(f"[bold yellow]:crossed_swords: {self.nome}[/bold yellow] usou [bold cyan]{golpe}[/bold cyan] em [bold red]{alvo.nome}[/bold red] e causou [bold white]{dano_real}[/bold white] de dano!")
        else:
            console.print("[bold red]:skull: Ação inválida. Um dos lutadores já está caído![/bold red]")

    def receber_dano(self, dano_bruto):
        if random.random() < self.esquiva:
            return 0, "esquivou"
            
        dano_real = max(0, dano_bruto - random.randint(0, self.defesa))
        self.vida -= dano_real
        
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
            
        if dano_real == 0:
            return 0, "bloqueou"
            
        return dano_real, "normal"

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida_maxima=1200, ataque=150, defesa=80, critico=0.15, esquiva=0.10)
        self.golpes = ['Soco Pesado', 'Corte de Machado', 'Investida de Escudo']

    def curar(self):
        if self.vivo:
            cura = random.randint(50, 150)
            self.vida = min(self.vida_maxima, self.vida + cura)
            console.print(f"[bold green]:sparkles: {self.nome} usou Poção de Vida e recuperou {cura} de HP! (HP Atual: {self.vida}/{self.vida_maxima})[/bold green]")


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida_maxima=800, ataque=250, defesa=30, critico=0.25, esquiva=0.20)
        self.golpes = ['Bola de Fogo', 'Raio Congelante', 'Explosão Arcana']

    def curar(self):
        if self.vivo:
            cura = random.randint(100, 200)
            self.vida = min(self.vida_maxima, self.vida + cura)
            console.print(f"[bold green]:sparkles: {self.nome} conjurou Cura Arcana e recuperou {cura} de HP! (HP Atual: {self.vida}/{self.vida_maxima})[/bold green]")