"""
Arquivo: ex081.py
Autor: Carlos Lira
Data: 01/01/2026
Descrição: 
"""

continuar = 'S'
lista = []
tamanho = 0

while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        print('Número adicionado com sucesso...')
    else:
        print('Número duplicado! Não será adicionado...')
    continuar = input('Deseja continuar? [S/N] ').strip().upper()

valor = int(input('Digite um valor para buscar na lista: '))
tamanho = len(lista)
lista.sort(reverse = True)

print(f'\nA lista possui {tamanho} elementos.')
print(f'Lista em ordem decrescente: {lista}')
if valor in lista:
    print(f'O valor {valor} foi encontrado na lista.')
else:
    print(f'O valor {valor} não foi encontrado na lista.')
