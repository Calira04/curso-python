"""
Arquivo: ex025.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Procurando uma string dentro de outra
"""

nome = str(input("Digite um nome: ")).strip().title().split()

bool = "Silva" in nome

print(f"O nome contém 'Silva'? {bool}")
