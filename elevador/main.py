# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Elevador



capacidade_elevador = int(input())
peso_medio = int(input())


qnt_pessoas = capacidade_elevador // peso_medio

print(f"O elevador pode transportar {qnt_pessoas} pessoas com segurança.")
