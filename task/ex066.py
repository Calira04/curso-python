"""
Arquivo: ex066.py
Autor: Carlos Lira
Data: 30/12/2025
Descrição: 
"""

num = 0
soma = 0

while num != 999:
    num = int(input('Digite um número: '))
    
    if num == 999:
        break

    soma += num
print(f'A soma dos valores foi {soma}.')
