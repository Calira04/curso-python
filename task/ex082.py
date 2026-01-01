"""
Arquivo: ex082.py
Autor: Carlos Lira
Data: 01/01/2026
Descrição: Dividindo valores em listas
"""

lista_princial = []
lista_par = []
lista_impar = []

while True:
    numero = int(input('Digite um número (ou -1 para parar): '))
    if numero == -1:
        break
    lista_princial.append(numero)
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

lista_princial.sort()
lista_par.sort()
lista_impar.sort()

print(f'\nLista completa: {lista_princial}')
print(f'Lista de números pares: {lista_par}')
print(f'Lista de números ímpares: {lista_impar}')
