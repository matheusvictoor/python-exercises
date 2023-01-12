# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# Questão: Divisor


def divisor(num, lista):
    for i in range(len(lista)):
        if lista[i] % num == 0:
            return i
    return -1


lista1 = [100,10,40,50]
lista2 = [3,15,50,23,5]
lista3 = [4,5,6,7,8,2,4,64,6,7]

assert divisor(10, lista1) == 0
assert divisor(5, lista2) == 1
assert divisor(7, lista3) == 3

