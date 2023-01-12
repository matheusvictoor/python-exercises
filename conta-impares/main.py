# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Conta ímpares e Imprime Último Ímpar



cont_impar = 0

qnt_numeros = int(input())

for i in range(qnt_numeros):
    numero = int(input())
    if numero % 2 == 1:
        cont_impar += 1

porcentagem = (cont_impar / qnt_numeros) * 100
print(f"{cont_impar} ({porcentagem:.1f}%)")


