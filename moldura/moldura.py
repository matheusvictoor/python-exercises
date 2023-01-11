# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Calcula Moldura



comprimento = float(input())
largura = float(input())

valor_a_pagar = ((comprimento / 100) * 2 + ((largura / 100) * 2)) * 120

print(f"R$ {valor_a_pagar:.1f}")
