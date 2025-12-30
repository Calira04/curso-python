"""
Arquivo: ex065.py
Autor: Carlos Lira
Data: 30/12/2025
Descrição: Programa que lê vários números inteiros do usuário e, ao final, mostra a média, o maior e o menor valor digitado.
"""

num = 0
continuar = 'S'
media = 0
maior = 0
menor = 0
qtde = 0

while continuar == 'S':
    num = int((input("Digite um número: ")))
    qtde += 1
    media += num
    if qtde == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input("Deseja continuar? [S/N]: ")).upper().strip()

media = media / qtde
print("Você digitou {} números e a média foi {:.2f}.".format(qtde, media))
print("O maior valor foi {} e o menor foi {}.".format(maior, menor))
