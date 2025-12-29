"""
Arquivo: ex063.py
Autor: Carlos Lira
Data: 29/12/2025
Descrição: Programa que exibe os n primeiros termos da Sequência de Fibonacci.
"""

ts = int(input("Digite um um numero: "))

f = 0
f1 = 0
f2 = 0

c = 0

while c <= ts:
    if c == 0:
        f = 0
        f1 = 0
        f2 = 0
    elif c == 1:
        f = 0
        f1 = 0
        f2 = 0
    elif c == 2:
        f = 1
        f1 = 1
        f2 = 0
    else:
        f = f1 + f2
        f2 = f1
        f1 = f
    if c != 0:
        print("{} ".format(f), end='')
    c += 1
print("FIM")