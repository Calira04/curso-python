"""
Arquivo: ex078.py
Autor: Carlos Lira
Data: 01/01/2026
Descrição: Programa que lê cinco números e informa o maior e o menor valor,
"""
valores = []
maior = menor = 0

for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores): # enumerate para obter o índice e o valor
    if v == maior:
        print(f'{i + 1}... ', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i + 1}... ', end='')
print()
