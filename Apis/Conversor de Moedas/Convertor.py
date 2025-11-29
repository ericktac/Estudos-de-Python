###     conversor de moedas usando uma API pública     ###
#   Esse script solicita ao usuário uma moeda base, uma moeda de destino e um valor a ser convertido.
#   Feito isso, ele utiliza a API "exchangerate-api.com" para obter as taxas de câmbio atuais e realiza a conversão,
#   exibindo o resultado formatado com duas casas decimais.
#
#   Esse script foi desenvolvido para estudar requisições HTTP e manipulação de APIs em Python de forma simples.
#   Autor: Erick Tavares
# ###

import requests # Biblioteca para fazer requisições HTTP

def getMoedas(base='BRL'): # Função para obter as taxas de câmbio
    url = f"https://api.exchangerate-api.com/v4/latest/{base.upper().strip()}"; # URL da API com a moeda base e formatada corretamente
    response = requests.get(url); # Faz a requisição GET para a API

    if response.status_code == 404: # Verifica se a resposta indica que a moeda base é inválida
        print("Moeda base inválida ou não encontrada."); # Mensagem de erro
        raise ValueError("Moeda Base Invalida"); # Levanta uma exceção de valor inválido

    data = response.json(); # Converte a resposta JSON em um dicionário Python
    return data['rates']; # Retorna o dicionário de taxas de câmbio

def conversor():    # Função principal do conversor de moedas
    moedaBase = str(input("Qual a base de conversao? (Ex: BRL, USD, EUR): ")).upper().strip();   # Solicita a moeda base ao usuário e formata a entrada
    moedaDestino = str(input("Qual a moeda de destino? (Ex: BRL, USD, EUR): ")).upper().strip();  # Solicita a moeda de destino ao usuário e formata a entrada
    valor = float(input(f"Qual o valor em {moedaBase} que deseja converter para {moedaDestino}?: ")); # Solicita o valor a ser convertido e converte para float
    taxas = getMoedas(moedaBase); # Obtém as taxas de câmbio para a moeda base fornecida

    if moedaDestino in taxas: # Verifica se a moeda de destino está nas taxas obtidas
        taxaConversão = taxas[moedaDestino]; # Obtém a taxa de conversão para a moeda de destino
        valorConvertido = valor * float(taxaConversão);     # Calcula o valor convertido
        print(f"{valor:.2f} {moedaBase} equivalem a {valorConvertido:.2f} {moedaDestino}."); # Exibe o resultado formatado com duas casas decimais
    else: # Se a moeda de destino não for encontrada nas taxas
        print(f"Moeda de destino '{moedaDestino}' não encontrada."); # Mensagem de erro
        raise ValueError("Moeda de Destino Invalida");  # Levanta uma exceção de valor inválido


if __name__ == "__main__":
    conversor(); # Executa a função principal se o script for executado diretamente