"""
Arquivo: ex063.py
Autor: Carlos Lira
Data: 29/12/2025
Descrição: Programa que exibe os n primeiros termos da Sequência de Fibonacci.
"""

termos = int(input("Digite um um numero: "))

fator = 0 # Fator de controle para a sequência
fator_anterior = 0 # Fator anterior na sequência
fator_anterior2 = 1 # Fator anterior ao anterior na sequência

contagem = 0 # Contador de termos exibidos

while contagem <= termos: # Loop para exibir os termos da sequência de Fibonacci
    if contagem == 0: # Primeiro termo da sequência
        fator = 0 # Fator inicial
        fator_anterior = 0 # Fator anterior inicial
        fator_anterior2 = 0 # Fator anterior ao anterior inicial
    elif contagem == 1: # Segundo termo da sequência
        fator = 0 # Fator inicial
        fator_anterior = 0 # Fator anterior inicial
        fator_anterior2 = 0 # Fator anterior ao anterior inicial
    elif contagem == 2: # Terceiro termo da sequência
        fator = 1 # Fator inicial
        fator_anterior = 1 # Fator anterior inicial
        fator_anterior2 = 0 # Fator anterior ao anterior inicial
    else: # Demais termos da sequência
        fator = fator_anterior + fator_anterior2 # Calcula o próximo termo da sequência
        fator_anterior2 = fator_anterior # Atualiza o fator anterior ao anterior
        fator_anterior = fator # Atualiza o fator anterior
    if contagem != 0 and contagem != termos: # Exibe o termo com formatação adequada
        print("{} -> ".format(fator), end='') # Exibe o termo atual com seta
    elif contagem == termos: # Último termo da sequência
        print("{}".format(fator), end='') # Exibe o último termo sem seta
    contagem += 1 # Incrementa o contador de termos exibidos
print(" FIM") # Indica o fim da sequência exibida
