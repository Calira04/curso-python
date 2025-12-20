"""
Arquivo: ex028.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Jogo de Adivinhacao v1.0
"""

import random
import time


print("Bem-vindo ao jogo de adivinhação!")

time.sleep(2)

tentativa = int(input("Tente adivinhar o número entre 1 e 10: "))
numero_secreto = random.randint(1,10)

print("Processando...")
time.sleep(2)

if tentativa == numero_secreto:
    print("Parabéns! Você adivinhou o número secreto!")
else:
    print(f"Que pena! O número secreto era {numero_secreto}. Tente novamente!")
