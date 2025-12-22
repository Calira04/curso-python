"""
Arquivo: ex041.py
Autor: Carlos Lira
Data: 22/12/2025
Descrição: Classificando Atletas
Este script solicita a data de nascimento do usuário, calcula sua idade e classifica-o em uma
categoria de atleta com base na idade. As categorias são: Mirim (até 9 anos), Infantil (10 a 14 anos),
Junior (15 a 19 anos), Sênior (20 a 25 anos) e Master (acima de 25 anos).
Uso: Execute o script e insira a data de nascimento no formato dd/mm/aaaa.
Exemplo de entrada: 15/08/2010
Exemplo de saída: Você tem 15 anos e está na categoria Junior.
"""

from datetime import date

nascimento = input('Digite sua data de nascimento (dd/mm/aaaa): ').split('/')
nascimento = date(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

hoje = date.today()

if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
    idade = hoje.year - nascimento.year - 1
else:
    idade = hoje.year - nascimento.year

if idade < 9:
    categoria = 'Mirim'
elif idade < 15:
    categoria = 'Infantil'
elif idade < 20:
    categoria = 'Junior'
elif idade < 26:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print(f'Você tem {idade} anos e está na categoria {categoria}.')
