"""
Arquivo: ex024.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Verificando as primeiras letras do nome
"""

nome = str(input("Digite seu nome completo: ")).strip().title().split()
bool = nome[0] == "Santo"

print(f"Seu nome começa com 'Santo'? {bool}")
