# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Orçamento do nome.


nome  = str(input("Nome? "))
valor_da_letra = float(input("Valor da letra (R$)? "))

orcamento = len(nome) * valor_da_letra

print(f"Preço final: R$ {orcamento:.2f}")
