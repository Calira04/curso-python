"""
Arquivo: ex040.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Media de nota
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f"Média: {media:.1f} - REPROVADO")
elif 5.0 <= media < 7.0:
    print(f"Média: {media:.1f} - RECUPERAÇÃO")
else:
    print(f"Média: {media:.1f} - APROVADO")
