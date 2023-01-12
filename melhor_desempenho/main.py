# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Melhor desempenho


qnt_alunos = int(input())
lista = []
cont2 =0

for i in range(qnt_alunos):
    cont = 0
    resultado = input()
    
    for e in resultado:
        if e == ".":
            cont += 1
            cont2 += 1
    lista.append(cont)

if cont2 != 0:
    melhor = 0
    for i in range(len(lista)-1):
        if lista[i] <= lista[i+1]:
                melhor += 1 
    print(melhor)
else:
    print("-1")



