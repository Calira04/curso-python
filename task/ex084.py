"""
Arquivo: ex084.py
Autor: Carlos Lira
Data: 01/01/2026
Descrição: Classificao de IMC
"""

database = list()
dados = list()

continuar = 'S'

while True:
    if continuar in 'Ss':

        dados.append(str(input('Nome: ')))
        dados.append(float(input('Peso(kg): ')))
        dados.append(float(input('Altura(metros): ')))

        valor = round(dados[1]/(dados[2] ** 2))
        dados.append(valor)

        database.append(dados[:])
        dados.clear()

    else:
        break

    continuar = str(input('Deseja continuar?[S/N]: ')).upper().strip()

for i in database:
    if i[3] < 18.5:
        classificacao = 'Abaixo do peso'
        print(f'{i[0]} esta classificado como: {classificacao}')
    elif i[3] < 25:
        classificacao = 'Peso ideal'
        print(f'{i[0]} esta classificado como: {classificacao}')
    elif i[3] < 30:  
        classificacao = 'Sobrepeso'
        print(f'{i[0]} esta classificado como: {classificacao}')
    elif i[3] < 40:
        classificacao = 'Obesidade'
        print(f'{i[0]} esta classificado como: {classificacao}')
    else:
        classificacao = 'Obesidade mórbida'
        print(f'{i[0]} esta classificado como: {classificacao}')
