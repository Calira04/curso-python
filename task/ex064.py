"""
Arquivo: ex064.py
Autor: Carlos Lira
Data: 29/12/2025
Descrição: Programa que lê vários números inteiros do usuário e calcula a soma desses números.
"""

num = 0
valor = 0
qtde = 0

while valor != 999:
    valor = int(input('Digite um número: '))
    if valor != 999:
        num += valor  
print(num)