"""
Arquivo: ex075.py
Autor: Carlos Lira
Data: 31/12/2025
Descrição: Programa que lê quatro valores inteiros e mostra:
- Quantas vezes o valor 9 foi digitado.
- Em que posição foi digitado o primeiro valor 3.
- Quais foram os números pares digitados.
"""

num = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in num:   
    if n % 2 == 0:
        print(n, end=' ')
