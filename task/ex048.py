"""
Arquivo: ex048.py
Autor: Carlos Lira
Data: 23/12/2025
Descrição: Soma de todos os números múltiplos de 3 que estão no intervalo entre 0 e um número digitado pelo usuário.
"""

from time import sleep

s = 0

num = int(input("Digite um número inteiro: "))

if num % 3 == 0:
    for i in range(0, num + 1, 3):
        n = i
        s += n
        sleep(0.3)
        print(n)
else:
    for i in range(0, num, 3):
        n = i
        s += n
        sleep(0.3)
        print(n)

print(f"A soma dos valores é {s}")
