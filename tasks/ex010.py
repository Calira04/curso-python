"""
Arquivo: ex010.py
Autor: Carlos Lira
Data: 16/12/2025
Descrição: Conversor de moedas - Converte um valor em reais para dólares, euros, yens.
"""

var = float(input("Digite o valor em reais (R$): "))

dolar = var / 5.25
euro = var / 5.90
yen = var / 0.038

print(f"Valor em dólares: U$ {dolar:.2f}")
print(f"Valor em euros: € {euro:.2f}")
print(f"Valor em yens: ¥ {yen:.2f}")
print("Conversão concluída com sucesso!")
