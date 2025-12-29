"""
Arquivo: ex061.py
Autor: Carlos Lira
Data: 29/12/2025
Descrição: Programa que exibe os termos de uma Progressão Aritmética (PA).
"""

termo = int(input("Digite o primeiro termo da PA: ")) # Solicita ao usuário o primeiro termo da PA
razao = int(input("Digite a razão da PA: ")) # Solicita ao usuário a razão da PA

cont = 1 # Contador de termos exibidos
total = 0 # Total de termos exibidos
mais = 10 # Número inicial de termos a serem exibidos

while mais != 0:
    total += mais # Atualiza o total de termos a serem exibidos

    while cont <= total: # Loop para exibir os termos da PA
        print("{}".format(termo), end=' -> ') # Imprime o termo atual
        termo += razao # Calcula o próximo termo da PA
        cont += 1 # Incrementa o contador de termos exibidos

    print("PAUSA") # Indica uma pausa na exibição dos termos
    mais = int(input("Quantos termos você quer mostrar a mais? ")) # Solicita ao usuário quantos termos adicionais deseja ver

print("Progressão finalizada com {} termos exibidos.".format(total)) # Mensagem final com o total de termos exibidos
