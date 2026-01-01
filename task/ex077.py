"""
Arquivo: ex077.py
Autor: Carlos Lira
Data: 31/12/2025
Descrição: Programa que exibe as vogais de cada palavra em uma tupla.
"""

palavras  = ('bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard',
             'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree',
             'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raticate')
for p in palavras: # laço para cada palavra na tupla
    print(f'\nNa palavra {p.upper()} temos ', end='') # exibe a palavra em maiúsculas
    for letra in p: # laço para cada letra na palavra
        if letra.lower() in 'aeiou': # verifica se a letra é uma vogal
            print(letra, end=' ') # exibe a vogal encontrada