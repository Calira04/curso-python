"""
Arquivo: ex043.py
Autor: Carlos Lira
Data: 22/12/2025
Descrição: 
"""

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = 'Abaixo do peso'
elif imc < 25:
    classificacao = 'Peso ideal'
elif imc < 30:  
    classificacao = 'Sobrepeso'
elif imc < 40:
    classificacao = 'Obesidade'
else:
    classificacao = 'Obesidade mórbida'

print(f'Seu IMC é {imc:.2f}. Classificação: {classificacao}.')
