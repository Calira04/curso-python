"""
Arquivo: ex055.py
Autor: Carlos Lira
Data: 28/12/2025
Descrição: Maior e menor peso lidos.
"""

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa (kg): '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi {maior} kg.')
print(f'O menor peso lido foi {menor} kg.')
