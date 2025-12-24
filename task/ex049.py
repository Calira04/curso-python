"""
Arquivo: ex049.py
Autor: Carlos Lira
Data: 23/12/2025
Descrição: Tabuada de um número digitado pelo usuário.
"""

from time import sleep

num = int(input("Digite um número inteiro: "))

print(f"Tabuada de {num}:")

for i in range(0, 11):
    print(f"{num:02} x {i:02} = {num * i:02}")
    sleep(0.3)
print("Fim da tabuada.")
