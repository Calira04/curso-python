"""
Arquivo: ex032.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Ano Bissexto
"""


import datetime

Ano = int(input("Digite um ano qualquer (ou 0 para o ano atual): "))

if Ano == 0:
    Ano = datetime.datetime.now().year
if (Ano % 4 == 0 and Ano % 100 != 0) or (Ano % 400 == 0):
    print(f"O ano de {Ano} é Bissexto")
else:
    print(f"O ano de {Ano} não é Bissexto")
