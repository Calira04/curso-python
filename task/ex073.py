"""
Arquivo: ex073.py
Autor: Carlos Lira
Data: 31/12/2025
Descrição: Programa que exibe informações sobre os times do Campeonato Brasileiro de Futebol.
"""

serie_a = ('Flamengo', 'Palemiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 
           'Botafogo', 'Bahia', 'Sao Paulo', 'Gremio', 'Bragantino', 
           'Atletico-MG', 'Santos', 'Corinthians', 'Vasco', 'Vitoria', 
           'Internacional', 'Ceara', 'Fortaleza', 'Juventude', 'Sport')

print('Os 5 primeiros colocados são:')
for time in serie_a[0:5]:
    print(time)

print('\nOs 4 últimos colocados são:')
for time in serie_a[-4:]:
    print(time)

print('\nTimes em ordem alfabética:')
for time in sorted(serie_a):
    print(time)

print(f'\nO Sport está na {serie_a.index('Sport') + 1}ª posição.')
