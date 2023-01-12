# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Orçamento Nome


nome  = input()
preco_por_letra = float(input())

preco_final = len(nome) * preco_por_letra

print(f"Nome? Valor da letra (R$)? Preço final: R$ {preco_final:.2f}")
