"""
Arquivo: ex051.py
Autor: Carlos Lira
Data: 24/12/2025
Descrição: PA - Progressão Aritmética
"""

termo1 = int(input("Digite o primeiro termo da PA: "))
razo = int(input("Digite a razão da PA: "))
termos = int(input("Digite quantos termos você quer mostrar: "))

for i in range(0, termos):
    print(termo1 + i * razo, end=' → ')
print("FIM")
