"""
Arquivo: ex011.py
Autor: Carlos Lira
Data: 16/12/2025
Descrição: Pintando parede
"""

largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))   

area = largura * altura
tinta = area / 2

print(f"A área da parede é: {area:.2f} metros quadrados.")
print(f"A quantidade de tinta necessária para pintar a parede é: {tinta:.2f} litros.")
print("Cálculo concluído com sucesso!")
