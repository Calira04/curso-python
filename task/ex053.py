"""
Arquivo: ex053.py
Autor: Carlos Lira
Data: 28/12/2025
Descrição: 
"""

frase = str(input("Digite uma frase: ")).strip().upper()

frase = frase.replace(" ", "") #Remoção dos espaços em branco
inverso = frase[::-1] #Inversão da string usando slicing

print(f"O inverso de '{frase}' é '{inverso}'")

if frase == inverso:
    print("A frase é um PALÍNDROMO.")
else:
    print("A frase NÃO é um PALÍNDROMO.")
