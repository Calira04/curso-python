"""
Arquivo: ex052.py
Autor: Carlos Lira
Data: 24/12/2025
Descrição: Verificador de número primo.
"""
c = 0
num = int(input("Digite um número inteiro: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(f"{i} é um divisor de {num}")
        c += 1
if c == 2:
    print(f"O número {num} foi divisível somente por 1 e por ele mesmo, Numero PRIMO.")
else:
    print(f"O número {num} foi divisível por {c} números, Numero NÃO PRIMO.")
