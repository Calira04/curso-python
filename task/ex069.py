"""
Arquivo: ex069.py
Autor: Carlos Lira
Data: 30/12/2025
Descrição: Programa que lê a idade e o sexo de várias pessoas, calculando e mostrando:
"""

opcao = 'S'
maior, homens, mulheres = 0, 0, 0

while opcao == 'S':
    idade = int(input("Digite a idade do pessoal: "))
    sexo = str(input("Digite o sexo [M/F]: ")).upper().strip()
    opcao = str(input("Deseja continuar? [S/N]: ")).upper().strip()

    if idade >= 18:
        maior = maior + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulheres = mulheres + 1

print("Total de pessoas com mais de 18 anos: {}".format(maior))
print("Total de homens cadastrados: {}".format(homens))
print("Total de mulheres com menos de 20 anos: {}".format(mulheres))

