"""
Arquivo: ex017.py
Autor: Carlos Lira
Data: 19/12/2025
Descrição: Catetos e Hipotenusas
"""

from math import hypot

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")
