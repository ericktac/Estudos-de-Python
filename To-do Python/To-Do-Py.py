###     To-do list em python com painel rich     ###
#   Esse script implementa uma lista de tarefas (to-do list) em Python utilizando a biblioteca Rich para exibir um painel interativo no terminal.
#
#   Esse script foi desenvolvido para estudar CRUD de dados simples e manipulação de arquivos JSON em Python.
#   Autor: Erick Tavares
# ###


import json,os # Biblioteca para manipulação de JSON e operações do sistema
from rich.console import Console # Biblioteca Rich para exibir painéis bonitos no terminal
from rich.table import Table # Biblioteca Rich para criar tabelas no terminal
from rich.panel import Panel    # Biblioteca Rich para criar painéis no terminal

BASE_DIR = os.path.dirname(os.path.abspath(__file__)); # Diretório base do script
JSON_PATH = os.path.join(BASE_DIR, "ToDo.json"); # Caminho do arquivo JSON para armazenar a lista de tarefas

class Lista: # Classe para gerenciar a lista de tarefas
    def __init__(self):
        if JSON_PATH: # Verifica se o arquivo JSON existe
            with open(JSON_PATH, "r") as f:
                self.list = json.load(f); # Carrega a lista de tarefas do arquivo JSON caso exista
        else:
            self.list = {}; # Inicializa uma lista vazia se o arquivo JSON não existir

    def add(self, nome, text): # Função para adicionar uma nova tarefa
        self.list[nome] = [text, bool(False)];
        self._salvar__();   # Salva a lista atualizada no arquivo JSON

    def remove(self, nome): # Função para remover uma tarefa
        if nome in ["all","tudo","todas","clear","delete","*"]: # Verifica se o usuário quer remover todas as tarefas
            self.list.clear(); # Limpa toda a lista de tarefas
            self._salvar__(); # Salva a lista vazia no arquivo JSON
        elif nome in self.list: # Verifica se a tarefa existe na lista
            del self.list[nome]; # Remove a tarefa da lista
            self._salvar__();# Salva a lista vazia no arquivo JSON
        else: # Se a tarefa não for encontrada
            print(f"Item '{nome}' não encontrado na lista.");
            raise KeyError(f"Item '{nome}' não encontrado na lista.");

    def show(self) -> list[str]:
        #   Função que retorna todo o conteúdo da lista
        return [f"{nome}: {text[0]} : {'Feito' if text[1] else 'A fazer'}" for nome, text in self.list.items()];

    def atualizar(self, nome): # Função para atualizar o status de uma tarefa
        if nome in self.list: # Verifica se a tarefa existe na lista
            self.list[nome][1] = not self.list[nome][1];
            self._salvar__();
        else: # Se a tarefa não for encontrada
            print(f"Item '{nome}' não encontrado na lista.");
            raise KeyError(f"Item '{nome}' não encontrado na lista.");

    def _salvar__(self):  # Função interna para salvar a lista de tarefas no arquivo JSON
        with open(JSON_PATH, "w") as f:
            json.dump(self.list, f);

def entrada(prompt: str):
    return input(prompt).strip().lower();

def mostrarLista(lista: Lista, console: Console): # Função para exibir a lista de tarefas em um painel Rich
    table = Table(title="Lista de Tarefas")
    table.add_column("Nome", style="cyan", no_wrap=True)
    table.add_column("Descrição", style="magenta")
    table.add_column("Status", style="green")

    for nome, (text, feito) in lista.list.items():
        status = "Feito" if feito else "A fazer"
        table.add_row(nome, text, status)

    console.print(table)

def criar(): # Função para criar uma nova tarefa
    console.print(Panel("[bold blue]Adicionar Nova Tarefa[/bold blue]"));

    nome = entrada("Nome da tarefa: ");
    text = entrada("Descrição da tarefa: ");

    lista.add(nome, text);
    console.print(f"[green]Tarefa '{nome}' adicionada com sucesso![/green]");

def remover(): # Função para remover uma tarefa
    console.print(Panel("[bold red]Remover Tarefa[/bold red]"));

    mostrar()

    nome = entrada("Nome da tarefa a remover (ou 'all', '*' para remover todas): ");

    try:
        lista.remove(nome);
        console.print(f"[green]Tarefa '{nome}' removida com sucesso![/green]");
    except KeyError as e:
        console.print(f"[red]{e}[/red]");

def atualizar():    # Função para atualizar o status de uma tarefa
    console.print(Panel("[bold yellow]Atualizar Status da Tarefa[/bold yellow]"));

    mostrar()

    nome = entrada("Nome da tarefa a atualizar: ");

    try:
        lista.atualizar(nome);
        console.print(f"[green]Status da tarefa '{nome}' atualizado com sucesso![/green]");
    except KeyError as e:
        console.print(f"[red]{e}[/red]");

def mostrar():  # Função para mostrar a lista de tarefas
    console.print(Panel("[bold magenta]Lista de Tarefas[/bold magenta]"));
    mostrarLista(lista, console);

def menu():  # Função para exibir o menu principal
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

