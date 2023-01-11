# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Quantidade de Inteiros Divisíveis por K




k = int(input())
qnt_numeros = int(input())
cont = 0

for i in range(qnt_numeros):
    numero = int(input())
    if numero % k == 0:
        cont += 1
porcentagem = (qnt_numeros / k) * 100
print(f"{cont} ({porcentagem:.1f}%)")
