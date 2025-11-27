import json,os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "ToDo.json")

class Lista:
    def __init__(self):
        if JSON_PATH:
            with open(JSON_PATH, "r") as f:
                self.list = json.load(f);
        else:
            self.list = {};

    def add(self, nome, text):
        self.list[nome] = [text, bool(False)];
        self._salvar__();

    def remove(self, nome):
        if nome in ["all","tudo","todas","clear","delete","*"]:
            self.list.clear();
            self._salvar__();
        elif nome in self.list:
            del self.list[nome];
            self._salvar__();
        else:
            print(f"Item '{nome}' não encontrado na lista.");
            raise KeyError(f"Item '{nome}' não encontrado na lista.");

    def show(self) -> list[str]:
        return [f"{nome}: {text[0]} : {'Feito' if text[1] else 'A fazer'}" for nome, text in self.list.items()];

    def atualizar(self, nome):
        if nome in self.list:
            self.list[nome][1] = not self.list[nome][1];
            self._salvar__();
        else:
            print(f"Item '{nome}' não encontrado na lista.");
            raise KeyError(f"Item '{nome}' não encontrado na lista.");

    def _salvar__(self):
        with open(JSON_PATH, "w") as f:
            json.dump(self.list, f);

def entrada(prompt: str):
    return input(prompt).strip().lower();

def mostrarLista(lista: Lista, console: Console):
    table = Table(title="Lista de Tarefas")
    table.add_column("Nome", style="cyan", no_wrap=True)
    table.add_column("Descrição", style="magenta")
    table.add_column("Status", style="green")

    for nome, (text, feito) in lista.list.items():
        status = "Feito" if feito else "A fazer"
        table.add_row(nome, text, status)

    console.print(table)

def criar():
    console.print(Panel("[bold blue]Adicionar Nova Tarefa[/bold blue]"));

    nome = entrada("Nome da tarefa: ");
    text = entrada("Descrição da tarefa: ");

    lista.add(nome, text);
    console.print(f"[green]Tarefa '{nome}' adicionada com sucesso![/green]");

def remover():
    console.print(Panel("[bold red]Remover Tarefa[/bold red]"));

    mostrar()

    nome = entrada("Nome da tarefa a remover (ou 'all', '*' para remover todas): ");

    try:
        lista.remove(nome);
        console.print(f"[green]Tarefa '{nome}' removida com sucesso![/green]");
    except KeyError as e:
        console.print(f"[red]{e}[/red]");

def atualizar():
    console.print(Panel("[bold yellow]Atualizar Status da Tarefa[/bold yellow]"));

    mostrar()

    nome = entrada("Nome da tarefa a atualizar: ");

    try:
        lista.atualizar(nome);
        console.print(f"[green]Status da tarefa '{nome}' atualizado com sucesso![/green]");
    except KeyError as e:
        console.print(f"[red]{e}[/red]");

def mostrar():
    console.print(Panel("[bold magenta]Lista de Tarefas[/bold magenta]"));
    mostrarLista(lista, console);

def menu():
    while True:
        console.print(Panel("""
[bold cyan]MENU TO-DO[/bold cyan]
1. Adicionar Tarefa
2. Remover Tarefa
3. Atualizar Status da Tarefa
4. Mostrar Tarefas
0. Sair
"""))

        escolha = entrada("Escolha uma opção (1-5): ");

        if escolha == "1":
            criar();
        elif escolha == "2":
            remover();
        elif escolha == "3":
            atualizar();
        elif escolha == "4":
            mostrar();
        elif escolha == "0":
            console.print("[bold green]Saindo...[/bold green]");
            break;
        else:
            console.print(Panel("""




"""))


if __name__ == "__main__":
    console = Console();
    lista = Lista();
    menu();

