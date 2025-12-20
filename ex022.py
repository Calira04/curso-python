"""
Arquivo: ex022.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Analisador de texto
"""

nome = str(input("Digite uma frase: ")).strip()

maiusculas = nome.upper()
minusculas = nome.lower()
tamanho = len(nome) - nome.count(" ")
primmeiro = nome.find(" ")
ultimo = nome.rfind(" ")

print(f"O nome em maiúsculas é: {maiusculas}")
print(f"O nome em minúsculas é: {minusculas}")
print(f"O número de letras no nome é: {tamanho}")
print(f"O primeiro nome tem {primmeiro} letras")
print(f"O último nome tem {len(nome) - ultimo -1} letras")
