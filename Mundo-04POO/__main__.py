import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from personagem_rpg import Guerreiro, Mago

console = Console()

while True:
    console.print(
        Panel.fit(
            " [bold cyan]:video_game: SIMULADOR DE BATALHA RPG AUTOMÁTICA :video_game:[/bold cyan] ", 
            style="bold blue", 
            subtitle="POO Avançada"
        )
    )
    console.print("\n" * 1)
    
    try:
        nome_p1 = console.input("[bold yellow]Digite o nome do seu Guerreiro: [/bold yellow]").strip()
        if not nome_p1:
            nome_p1 = "Guerreiro Misterioso"
            
        nome_p2 = console.input("[bold yellow]Digite o nome do seu Mago: [/bold yellow]").strip()
        if not nome_p2:
            nome_p2 = "Mago Obscuro"
    except Exception:
        console.print("\n[bold red]:cross_mark: Erro ao capturar nomes. Usando padrões da guilda...[/bold red]\n")
        nome_p1, nome_p2 = "Pikachu", "Gandalf"

    p1 = Guerreiro(nome_p1)
    p2 = Mago(nome_p2)

    console.print("\n" * 1)
    with Progress(
        SpinnerColumn(spinner_name="earth"), 
        TextColumn("[bold green]:hourglass_not_done: Renderizando a arena de batalha...[/bold green]"), 
        transient=True
    ) as progress:
        progress.add_task("loading", total=None)
        time.sleep(2)
    
    rodada = 1
    
    while p1.vivo and p2.vivo:
        console.print(f"\n[bold magenta]:crossed_swords: --- RODADA {rodada} --- :crossed_swords:[/bold magenta]")
        
        tabela = Table(show_header=True, header_style="bold cyan")
        tabela.add_column("Classe", style="white")
        tabela.add_column("Lutador", style="bold yellow")
        tabela.add_column("HP Atual", justify="center")
        
        cor_hp1 = "bold green" if p1.vida > p1.vida_maxima * 0.4 else "bold red"
        cor_hp2 = "bold green" if p2.vida > p2.vida_maxima * 0.4 else "bold red"
        
        tabela.add_row("Guerreiro", p1.nome, f"[{cor_hp1}]{p1.vida}/{p1.vida_maxima}[/{cor_hp1}]")
        tabela.add_row("Mago", p2.nome, f"[{cor_hp2}]{p2.vida}/{p2.vida_maxima}[/{cor_hp2}]")
        console.print(tabela)
        
        time.sleep(1.5)
        
        if p1.vida < p1.vida_maxima * 0.3 and random.random() < 0.6:
            p1.curar()
        else:
            p1.atacar(p2)
            
        time.sleep(1.5)
        
        if p2.vivo:
            if p2.vida < p2.vida_maxima * 0.4 and random.random() < 0.7:
                p2.curar()
            else:
                p2.atacar(p1)
                
        time.sleep(1.5)
        rodada += 1

    console.print("\n" * 1)
    with Progress(
        SpinnerColumn(spinner_name="dots"), 
        TextColumn("[bold blue]:hourglass_not_done: O combate acabou! Calculando o resultado...[/bold blue]"), 
        transient=True
    ) as progress:
        progress.add_task("loading", total=None)
        time.sleep(2)
        
    vencedor = p1.nome if p1.vivo else p2.nome
    
    console.print(
        Panel.fit(
            f" [bold yellow]:trophy: O GRANDE VENCEDOR FOI {vencedor.upper()}! :trophy:[/bold yellow] ", 
            style="bold green"
        )
    )
    
    console.print("\n" * 1)
    while True:
        try:
            resposta = console.input("[bold cyan]:question_mark: Deseja simular outra batalha? [S/N]: [/bold cyan]").strip().upper()
            if resposta in ("S", "N"):
                break
            console.print("\n[bold red]:exclamation: Comando inválido! Digite apenas 'S' para Sim ou 'N' para Não.[/bold red]\n")
        except Exception:
            console.print("\n[bold red]:cross_mark: Erro na entrada. O jogo será encerrado por segurança.[/bold red]\n")
            resposta = "N"
            break
            
    if resposta == "N":
        console.print("\n" * 1)
        with Progress(
            SpinnerColumn(spinner_name="dots"), 
            TextColumn("[bold red]:door: Fechando os servidores da arena...[/bold red]"), 
            transient=True
        ) as progress:
            progress.add_task("loading", total=None)
            time.sleep(1.5)
            
        console.print(
            Panel.fit(
                " [bold green]Sistema finalizado com sucesso! Até a próxima! :rocket:[/bold green] ", 
                style="bold white"
            )
        )
        break
    else:
        console.print("\n" * 1)
        with Progress(
            SpinnerColumn(spinner_name="dots"), 
            TextColumn("[bold blue]:arrows_counterclockwise: Limpando a arena e convocando novos lutadores...[/bold blue]"), 
            transient=True
        ) as progress:
            progress.add_task("loading", total=None)
            time.sleep(1.5)
        console.print("\n" * 2)