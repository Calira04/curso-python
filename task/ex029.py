"""
Arquivo: ex029.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Radar Eletronico
"""

velocidade = float(input("Digite a velocidade atual do carro (km/h): "))

limite = float(input("Digite o limite de velocidade da via (km/h): "))
valor = float(input("Digite o valor da multa por km acima do limite (R$): "))

if velocidade > limite:
    multa = (velocidade - limite) * valor
    print(f"Você foi multado! O valor da multa é R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade. Boa viagem!")
