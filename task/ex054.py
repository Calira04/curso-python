"""
Arquivo: ex054.py
Autor: Carlos Lira
Data: 28/12/2025
Descrição: Grupo de maioridade.
"""

from datetime import date

atual = date.today().year

for i in range(1, 8):
    nasc = int(input("Ano de nascimento: "))
    idade = atual - nasc
    print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")
    if idade < 21:
        print("Ainda não atingiu a maioridade.")
    elif idade == 21:
        print("Atingiu a maioridade este ano!")
    else:
        print("Já atingiu a maioridade.")
