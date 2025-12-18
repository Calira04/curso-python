"""
Arquivo: ex016.py
Autor: Carlos Lira
Data: 18/12/2025
Descrição: Quebrando um numero
"""

num = float(input("Digite um número real: "))

parte_inteira = int(num)
parte_fracionaria = num - parte_inteira

print(f"Parte inteira: {parte_inteira}")
print(f"Parte fracionária: {parte_fracionaria:.6f}")
