"""
Arquivo: ex071.py
Autor: Carlos Lira
Data: 30/12/2025
Descrição: Programa que simula o funcionamento de um caixa eletrônico,
"""

num = int(input('Digite um valor R$:'))
while num > 0:
    while num >= 50:
        ced50 = num // 50
        num = num - (ced50 * 50)
        print(f'Total de {ced50} cédulas de R$50')
    while num >= 20:
        ced20 = num // 20
        num = num - (ced20 * 20)
        print(f'Total de {ced20} cédulas de R$20')
    while num >= 10:
        ced10 = num // 10
        num = num - (ced10 * 10)
        print(f'Total de {ced10} cédulas de R$10')
    while num >= 1:
        ced1 = num // 1
        num = num - (ced1 * 1)
        print(f'Total de {ced1} cédulas de R$1')
