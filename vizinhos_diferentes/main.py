# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Vizinhos diferentes


qnt_numeros = int(input())
lista = []
saida = ""

for i in range(qnt_numeros):

    num = int(input())
    lista.append(num)

for j in range(qnt_numeros-1,-1,-1):

    if lista[j] == lista[j - 1]:
        lista[j - 1] = lista[j - 1] + 1

for k in range(len(lista)):
    saida = saida + str(lista[k]) + " "

print(saida)

