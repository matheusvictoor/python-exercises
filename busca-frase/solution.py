# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Busca na frase


nome1 = input()
nome2 = input()

cont = 1
lista =[]

for i in range(len(nome2)):
    for j in range(len(nome1)):
        if nome2[i] == nome1[j]:
            cont += 1
    print(cont)

