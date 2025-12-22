"""
Arquivo: ex045.py
Autor: Carlos Lira
Data: 22/12/2025
Descrição: Pedra, Papel e Tesoura
Este script simula o jogo Pedra, Papel e Tesoura entre o usuário e o computador. 
O usuário escolhe uma das opções,e o computador escolhe aleatoriamente. 
O resultado do jogo é então exibido.
Uso: Execute o script e insira sua escolha entre Pedra, Papel ou Tesoura.
Exemplo de entrada: Pedra
Exemplo de saída: Computador escolheu Tesoura. Você venceu!
"""
from random import choice

lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)

jogador = input('Escolha Pedra, Papel ou Tesoura: ').capitalize()

print(f'Computador escolheu: {computador}')
if jogador == computador:
    print('Empate!')
elif (jogador == 'Pedra' and computador == 'Tesoura') or \
     (jogador == 'Papel' and computador == 'Pedra') or \
     (jogador == 'Tesoura' and computador == 'Papel'):
    print('Você venceu!')
else:
    print('Computador venceu!')
