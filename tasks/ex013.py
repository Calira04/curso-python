"""
Arquivo: ex013.py
Autor: Carlos Lira
Data: 18/12/2025
Descrição: Reajuste Salarial
"""

valor = float(input("Digite o valor do salário atual: R$ "))
reajuste = float(input("Digite a porcentagem de reajuste (%): "))

valor_reajuste = valor * (reajuste / 100)
salario_final = valor + valor_reajuste

print(f"O valor do reajuste é: R$ {valor_reajuste:.2f}")
print(f"O salário final após o reajuste é: R$ {salario_final:.2f}")
print("Cálculo de reajuste salarial concluído com sucesso!")
