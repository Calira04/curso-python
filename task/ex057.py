"""
Arquivo: ex057.py
Autor: Carlos Lira
Data: 29/12/2025
Descrição: Programa que solicita ao usuário que informe seu sexo (M/F).
O programa deve aceitar apenas as entradas 'M' ou 'F', ignorando maiúsculas e minúsculas.
Se o usuário inserir um valor inválido, o programa deve continuar solicitando até que uma entrada válida seja fornecida.
"""

sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()

while sexo != 'M' and sexo != 'F':
    print("Dados inválidos. Por favor, digite novamente.")
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()

print("Sexo {} registrado com sucesso.".format(sexo))
