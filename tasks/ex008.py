"""
Arquivo: ex008.py
Autor: Carlos Lira
Data: 16/12/2025
Descrição: Conversor de medidas
"""

var = float(input("Digite um valor em metros: "))

km = var / 1000
hm = var / 100
dam = var / 10
dm = var * 10
cm = var * 100
mm = var * 1000

print(f"O valor em quilômetros é: {km} km")
print(f"O valor em hectômetros é: {hm} hm")
print(f"O valor em decâmetros é: {dam} dam")
print(f"O valor em decímetros é: {dm} dm")
print(f"O valor em centímetros é: {cm} cm")
print(f"O valor em milímetros é: {mm} mm")  
