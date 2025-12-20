"""
Arquivo: ex027.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Primeiro e Ultimo nome
"""

nome = str(input("Digite seu nome completo: ")).strip().title().split()

print(f"Primeiro nome: {nome[0]}")
print(f"Último nome: {nome[-1]}")
