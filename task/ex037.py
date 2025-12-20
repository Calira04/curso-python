"""
Arquivo: ex037.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Conversor de base numerica
"""

num = int(input("Digite um número inteiro: "))

print("Escolha a base para conversão:")
print("[1] Binário")
print("[2] Octal")
print("[3] Hexadecimal")

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"O número {num} em binário é {bin(num)[2:]}")
elif opcao == 2:
    print(f"O número {num} em octal é {oct(num)[2:]}")
elif opcao == 3:
    print(f"O número {num} em hexadecimal é {hex(num)[2:].upper()}")
else:
    print("Opção inválida! Escolha uma opção entre 1 e 3.")
