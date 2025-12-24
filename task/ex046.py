"""
Arquivo: ex046.py
Autor: Carlos Lira
Data: 23/12/2025
Descrição: Contagem Regressiva para o Ano Novo
Este script realiza uma contagem regressiva de 10 segundos para o Ano Novo,
imprimindo cada número com uma pausa de um segundo entre eles.
Uso: Execute o script para ver a contagem regressiva.
"""

from time import sleep

print('Contaegm regressiva para o estouro de fogos:')
for i in range(10, 0, -1):
    print(f'{i}...')
    sleep(1)
print('Feliz Ano Novo! 🎉🎆')