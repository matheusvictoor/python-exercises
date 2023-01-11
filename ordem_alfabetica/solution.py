# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Fora de Ordem


frase = input()

lista = frase.split(" ")

aux = frase.split(" ")

#print(lista)

def ordena(lista):
    for final in range(len(lista), 0, -1):
        for atual in range(0, final-1):
            if lista[atual] > lista[atual + 1]:
                lista[atual], lista[atual + 1] = lista[atual + 1], lista[atual]
    return lista

lista_ordenada = ordena(lista)

p = 0

for i in range(len(lista)):
    if lista_ordenada[i] != aux[i]:
        p = i + 1

if p != 0:
    print(f"fora de ordem: {p}")
else:
    print("em ordem")

        
