"""
Arquivo: ex019.py
Autor: Carlos Lira
Data: 19/12/2025
Descrição: Sorteando um item da lista
"""

from random import choice

n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))

lista = [n1, n2, n3, n4]

sorteado = choice(lista)

print(f"O aluno sorteado foi: {sorteado}")
