"""
Arquivo: ex074.py
Autor: Carlos Lira
Data: 31/12/2025
Descrição: Programa que gera cinco números aleatórios e mostra o maior e o menor valor sorteado.
"""

from random import randint

num = (randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60))

print('Os números sorteados foram: ', end='')

for n in sorted(num):
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
