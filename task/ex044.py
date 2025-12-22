"""
Arquivo: ex044.py
Autor: Carlos Lira
Data: 22/12/2025
Descrição: Gerenciador de Pagamentos
Este script calcula o valor total de uma compra com base na forma de pagamento escolhida pelo usuário.
As opções de pagamento são:
1 - À vista dinheiro/cheque: 10% de desconto
2 - À vista cartão: 5% de desconto
3 - 2x no cartão: preço normal
4 - 3x ou mais no cartão: 20% de juros
Uso: Execute o script, insira o preço das compras e escolha a forma de pagamento.
Exemplo de entrada:
Digite o preço das compras: R$ 100.00
Escolha a opção de pagamento: 1
Exemplo de saída:
Pagamento à vista no dinheiro/cheque. Total com 10% de desconto: R$ 90.00
"""

preco = float(input('Digite o preço das compras: R$ '))

print('''Formas de pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Escolha a opção de pagamento: '))

match opcao:
    case 1:
        total = preco * 0.90
        print(f'Pagamento à vista no dinheiro/cheque. Total com 10% de desconto: R$ {total:.2f}')
    case 2:
        total = preco * 0.95
        print(f'Pagamento à vista no cartão. Total com 5% de desconto: R$ {total:.2f}')
    case 3:
        total = preco
        parcela = total / 2
        print(f'Pagamento em 2x no cartão. Total: R$ {total:.2f} em 2 parcelas de R$ {parcela:.2f}')
    case 4:
        parcelas = int(input('Número de parcelas: '))
        total = preco * 1.20
        parcela = total / parcelas
        print(f'Pagamento em {parcelas}x no cartão. Total com 20% de juros: R$ {total:.2f} em {parcelas} parcelas de R$ {parcela:.2f}')
    case _:
        print('Opção inválida de pagamento.')
