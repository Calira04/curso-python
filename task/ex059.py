"""
Arquivo: ex059.py
Autor: Carlos Lira
Data: 29/12/2025
Descrição: Programa que lê dois números e apresenta um menu de opções para o usuário.
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

opcao = 0

while opcao != 5:
    print("""
    [1] Soma
    [2] Multiplicação
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    """)
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é {}.".format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print("O produto entre {} e {} é {}.".format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {}, o maior é {}.".format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif opcao == 5:
        print("Finalizando o programa...")
    else:
        print("Opção inválida. Tente novamente.")