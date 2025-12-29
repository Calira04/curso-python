"""
Arquivo: ex060.py
Autor: Carlos Lira
Data: 29/12/2025
Descrição: Programa que calcula o fatorial de um número fornecido pelo usuário,
"""

from math import factorial # Importa a função factorial da biblioteca math

fatorial = int(input("Digite um número para calcular seu fatorial: ")) # Solicita ao usuário um número inteiro
resultado = factorial(fatorial) # Calcula o fatorial do número fornecido

c = fatorial # Inicia uma variável de controle para a contagem regressiva

while c in range(fatorial, 0, -1): # Loop para exibir o cálculo do fatorial
    print(c, end='') # Imprime o número atual sem pular linha
    if c > 1: # Verifica se não é o último número
        print(" x ", end='') # Imprime o símbolo de multiplicação
    else: # Se for o último número
        print(" = ", end='') # Imprime o símbolo de igual
    c -= 1 # Decrementa a variável de controle
print(resultado) # Imprime o resultado do fatorial
print("O fatorial de {} é {}.".format(fatorial, resultado)) # Mensagem final com o resultado
