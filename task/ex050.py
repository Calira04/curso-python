"""
Arquivo: ex050.py
Autor: Carlos Lira
Data: 23/12/2025
Descrição: Soma dos números pares digitados pelo usuário.
"""

s = 0

for i in range(0, 6):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        s += num
print(f"A soma dos números pares digitados é {s}")
