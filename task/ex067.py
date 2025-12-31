"""
Arquivo: ex067.py
Autor: Carlos Lira
Data: 30/12/2025
Descrição: 
"""

num = 0

while num >= 0:
    num = int(input('Digite um numero para ver a tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
print('Programa encerrado. Volte sempre!')
