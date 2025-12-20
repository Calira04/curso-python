"""
Arquivo: ex036.py
Autor: Carlos Lira
Data: 20/12/2025
Descrição: Aprovando emprestimo
"""

casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário do comprador: R$ "))
anos = int(input("Digite em quantos anos o empréstimo será pago: "))

prestacao = casa / (anos * 12)
minimo = salario * 0.3

print(f"Para pagar uma casa de R$ {casa:.2f} em {anos} anos")
print(f"A prestação mensal será de R$ {prestacao:.2f}")
if prestacao <= minimo:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")
