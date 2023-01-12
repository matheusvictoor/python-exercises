# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Maior Diferença Absoluta


qnt_numeros = int(input())

lista = []
maior_diferenca = 0
a = 0
b = 0

for i in range(qnt_numeros):

    lista.append(float(input()))
    diferenca = abs(lista[i-1] - lista[i])

    if diferenca > maior_diferenca:
        maior_diferenca = diferenca
        a = lista[i-1]
        b = lista[i]

print(f"{a} e {b}")

