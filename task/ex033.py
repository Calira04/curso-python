"""
Arquivo: ex033.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Maior e Menor numero
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

menor = num1
if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print(f"O menor número digitado foi: {menor}")
print(f"O maior número digitado foi: {maior}")
