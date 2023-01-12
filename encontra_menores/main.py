# Universidade Federal de Campina Grande - UFCG
# Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
#
# Questão: Encontra menores



def encontra_menores(num, sequencia):
    for i in sequencia:
        if i < num:
            return i 
    return -1


lista1 = [100,200,300,400]
lista2 = [15, 12, 4, 9, 10]
lista3 = [600,15,16,-45, -60]
assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4
assert encontra_menores(15, lista3) == -45
