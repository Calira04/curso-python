"""
Arquivo: ex004.py
Autor: Carlos Lira
Data: 15/12/2025
Descrição: Dissecando uma variavel
"""

a = input("Digite algo: ")

print(f"O tipo primitivo de {a} é {type(a)}")
print(f"Só tem espaços? {a.isspace()}")
print(f"É um número? {a.isnumeric()}")
print(f"É alfabético? {a.isalpha()}")
print(f"É alfanumérico? {a.isalnum()}")
print(f"Está em maiúsculas? {a.isupper()}")
print(f"Está em minúsculas? {a.islower()}")
print(f"Está capitalizada? {a.istitle()}")
print(f"É imprimível? {a.isprintable()}")
