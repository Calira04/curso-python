"""
Arquivo: ex026.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Primeira e ultima ocorrencia de uma string
"""

nome = str(input("Digite uma frase: ")).strip().lower()
letra = str(input("Digite uma letra para pesquisar: ")).strip().lower()

quantidade = nome.count(letra)
primeira = nome.find(letra) + 1
ultima = nome.rfind(letra) + 1

print(f"A letra 'a' aparece {quantidade} vezes na frase.")
print(f"A primeira ocorrência da letra 'a' é na posição {primeira}.")
print(f"A última ocorrência da letra 'a' é na posição {ultima}.")
