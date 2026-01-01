"""
Arquivo: ex070.py
Autor: Carlos Lira
Data: 01/01/2026
Descrição: 
"""

lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        if n > lista[-1]:
            lista.append(n)
        elif n < lista[0]:
            lista.insert(0, n)
        else:
            for i in range(0, len(lista)):
                if n <= lista[i]:
                    lista.insert(i, n)
                    break
        print('Valor adicionado na posição correta da lista.')
print(lista)
