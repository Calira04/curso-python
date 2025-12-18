"""
Arquivo: ex012.py
Autor: Carlos Lira
Data: 16/12/2025
Descrição: Calculando Desconto
"""

preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite a porcentagem de desconto (%): "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print(f"O valor do desconto é: R$ {valor_desconto:.2f}")
print(f"O preço final do produto após o desconto é: R$ {preco_final:.2f}")
print("Cálculo de desconto concluído com sucesso!")
