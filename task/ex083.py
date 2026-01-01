"""
Arquivo: ex083.py
Autor: Carlos Lira
Data: 01/01/2026
Descrição: Verificando expressões matemáticas
"""

lista = list(input('Digite a expressão: '))
if lista.count('(') != lista.count(')'):
    print('A expressão está errada!')
else:
    print('A expressão está correta!')
