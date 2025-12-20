"""
Arquivo: ex035.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Analisando Triangulo
"""

lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os lados formam um triângulo.")
    if lado1 == lado2 == lado3:
        print("Tipo do triângulo: Equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Tipo do triângulo: Isósceles")
    else:
        print("Tipo do triângulo: Escaleno")
else:
    print("Os lados não formam um triângulo.")
