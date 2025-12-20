"""
Arquivo: ex038.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Comparando dois números inteiros
"""

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else:
    print("Os dois números são iguais.")
