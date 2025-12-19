"""
Arquivo: ex018.py
Autor: Carlos Lira
Data: 19/12/2025
Descrição: Seno, cosseno e tangente
"""

from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo que você deseja: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O seno de {angulo} é igual a {seno:.2f}")
print(f"O cosseno de {angulo} é igual a {cosseno:.2f}")
print(f"A tangente de {angulo} é igual a {tangente:.2f}")
