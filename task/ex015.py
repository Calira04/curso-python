"""
Arquivo: ex015.py
Autor: Carlos Lira
Data: 18/12/2025
Descrição: Alugel de Carros
"""

dias = int(input("Digite o número de dias que o carro foi alugado: "))
km = float(input("Digite o número de quilômetros rodados: "))

custo_dias = float(input("Digite o custo por dia de aluguel: R$ "))
custo_km = float(input("Digite o custo por quilômetro rodado: R$ "))

total_dias = dias * custo_dias
total_km = km * custo_km
custo_total = total_dias + total_km 

print(f"O custo total do aluguel do carro é: R$ {custo_total:.2f}")
print("Cálculo do aluguel de carros concluído com sucesso!")
