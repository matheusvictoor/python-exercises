# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Calcula o valor a ser pago na moldura.




comprimento = float(input()) 
largura = float(input())

valor_a_pagar = ((comprimento / 100) * 2 + ((largura / 100) * 2)) * 120

print(f"R$ {valor_a_pagar:.1f}")
