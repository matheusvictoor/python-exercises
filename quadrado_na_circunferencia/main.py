# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Quadrado na Circunferência



import math

raio = float(input())

area_nao_comum = (math.pi * (raio ** 2)) - (raio * (2 * raio))

print(f"Área não comum: {area_nao_comum:.5f}")
