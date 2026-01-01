"""
Arquivo: ex076.py
Autor: Carlos Lira
Data: 31/12/2025
Descrição: Programa que exibe uma lista de preços formatada.
"""

lista = ('Pikachu', 1.50,
         'Bulbasaur', 2.00,
         'Charmander', 2.50,
         'Squirtle', 2.00,
         'Jigglypuff', 1.00,
         'Meowth', 1.50,
         'Psyduck', 1.80,
         'Snorlax', 3.00)
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>5.2f}')
print('-' * 40)