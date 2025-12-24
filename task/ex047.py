"""
Arquivo: ex047.py
Autor: Carlos Lira
Data: 23/12/2025
Descrição: Mostrar na tela todos os números pares que estão no intervalo entre 0 e um número digitado pelo usuário.
"""

from time import sleep

num = int(input("Digite um número inteiro:  "))

sleep(0.5)

print(f"Os números pares de 0 até {num} são:")

if num % 2 == 0:
    for i in range(0, num + 1, 2):
        sleep(0.3)
        print(i)
else:
    for i in range(0, num, 2):
        sleep(0.3)
        print(i)

