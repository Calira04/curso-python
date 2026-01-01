"""
Arquivo: ex070.py
Autor: Carlos Lira
Data: 01/01/2026
Descrição: Programa que lê vários números inteiros do usuário e armazena em uma lista,
mas só adiciona valores que não estejam duplicados. No final, mostra os valores únicos em ordem crescente.
"""

lista = [] # lista para armazenar os valores únicos
continuar = 'S' # variável para controlar o loop
num = 0 # variável para armazenar o número digitado

while continuar == 'S': # loop para continuar adicionando números
    num = int(input('Digite um valor: ')) # lê o número do usuário

    if num in lista: # verifica se o número já está na lista
        print('Valor duplicado! Não vou adicionar...') # mensagem de aviso
    else: # se o número não estiver na lista
        lista.append(num) # adiciona o número à lista
        print('Valor adicionado com sucesso...') # mensagem de sucesso
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip() # pergunta se o usuário quer continuar

lista.sort() # ordena a lista em ordem crescente
print(f'Você digitou os valores {lista}') # mostra os valores únicos em ordem crescente
