"""
Arquivo: ex056.py
Autor: Carlos Lira
Data: 28/12/2025
Descrição: Analise de dados de um grupo de pessoas.
"""

idade_total = 0
idade_media = 0
mulheres_menores_20 = 0


for i in range(1, 5):
    nome = input(f"Nome da {i}ª pessoa: ")
    idade = int(input(f"Idade da {i}ª pessoa: "))
    sexo = input(f"Sexo da {i}ª pessoa [M/F]: ").strip().upper()
    print("-" * 30)

    idade_total += idade

    if i == 1:
        maior_idade = idade
        nome_maior = nome
        menor_idade = idade
        nome_menor = nome
        if sexo == 'M':
            homens = 1
        else:
            mulheres_menores_20 = 1 if idade < 20 else 0 # Conta mulheres menores de 20 anos
    else:
        if idade > maior_idade:
            maior_idade = idade
            nome_maior = nome
        if idade < menor_idade:
            menor_idade = idade
            nome_menor = nome
        if sexo == 'M':
            homens += 1
        else:
            if idade < 20:
                mulheres_menores_20 += 1
idade_media = idade_total / 4

print(f"A média de idade do grupo é de {idade_media:.1f} anos.")
print(f"O homem mais velho é {nome_maior} com {maior_idade} anos.")
print(f"A mulher mais jovem é {nome_menor} com {menor_idade} anos.")
print(f"O grupo tem {homens} homens cadastrados.")
print(f"O grupo tem {mulheres_menores_20} mulheres com menos de 20 anos.")

