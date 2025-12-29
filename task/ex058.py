"""
Arquivo: ex058.py
Autor: Carlos Lira
Data: 29/12/2025
Descrição: Programa que gera um número aleatório entre 0 e 10 e desafia o usuário a adivinhar qual é esse número.
"""

from random import randint # Importa a função randint para gerar números aleatórios

num = randint(0, 10) # Gera um número aleatório entre 0 e 10
tentativas = 0 # Contador de tentativas
acertou = False # Flag para indicar se o usuário acertou o número

print("Tente adivinhar o número que estou pensando entre 0 e 10.") # Instrução inicial para o usuário

while not acertou:
    palpite = int(input("Digite seu palpite: ")) # Solicita o palpite do usuário
    tentativas += 1 # Incrementa o contador de tentativas

    if palpite == num: # Verifica se o palpite está correto
        acertou = True # Atualiza a flag para indicar que o usuário acertou
    else:
        if palpite < num:
            print("Mais... Tente novamente.") # Dica para o usuário
        else:
            print("Menos... Tente novamente.") # Dica para o usuário
