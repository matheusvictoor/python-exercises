# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
# Questão: Palavras que Começam com Consoantes


cont = 0

while True:

    seq = input()

    if seq == "***": break

    if seq[0] not in "AaEeIiOoUu0123456789":
        cont += 1

print(f"Palavras: {cont}")
