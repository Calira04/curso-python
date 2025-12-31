"""
Arquivo: ex072.py
Autor: Carlos Lira
Data: 31/12/2025
Descrição: Programa que lê um número entre 0 e 20 e exibe esse número por extenso.
"""

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número entre 0 e 20: '))
if 0 <= num <= 20:
    print(f'Você digitou o número {numeros[num]}')
else:
    print('Número inválido! Tente novamente.')
