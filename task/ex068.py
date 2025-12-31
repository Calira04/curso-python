"""
Arquivo: ex068.py
Autor: Carlos Lira
Data: 30/12/2025
Descrição: Programa que permite ao usuário jogar "Par ou Ímpar" contra o computador, contabilizando o número de vitórias consecutivas até a primeira derrota.
"""

from random import randint

cpu = qtde = 0
resultado = 'Vitoria'
jogador = -1

while resultado == 'Vitoria':
    jogador = int(input('Digite um valor entre 0 e 10: '))
    cpu = randint(0, 10)
    total = jogador + cpu
    tipo = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()
    if total % 2 == 0:
        resultado = 'Vitoria' if tipo == 'P' else 'Derrota'
    else:
        resultado = 'Vitoria' if tipo == 'I' else 'Derrota'
    if resultado == 'Vitoria':
        qtde += 1
        print(f'Você jogou {jogador} e o computador {cpu}. Total de {total} DEU PAR')
        print('Você VENCEU! Vamos jogar novamente...')
    else:
        print(f'Você jogou {jogador} e o computador {cpu}. Total de {total} DEU ÍMPAR')
        print('Você PERDEU!')
print(f'GAME OVER! Você venceu {qtde} vezes.')