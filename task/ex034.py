"""
Arquivo: ex034.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Aumento multiplo
"""

salario = float(input("Digite o salário do funcionário: R$ "))

if salario <= 1250:
    novo_salario = salario * 1.15
else:
    novo_salario = salario * 1.10

print(f"O novo salário do funcionário é: R$ {novo_salario:.2f}")
