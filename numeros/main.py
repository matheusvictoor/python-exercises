#Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Números ocilantes


def seleciona_perfeitos(lista):
    lista_perfeito = []
    for elemento in lista:
        soma = 0
        for i in range(1, elemento):
            if elemento % i == 0:
                soma += i
        if soma == elemento:
            lista_perfeito.append(elemento)
    return lista_perfeito

lista = [3, 6, 9, 12, 15, 18, 19, 21, 28]
assert seleciona_perfeitos(lista) == [6, 28]
assert lista == [3, 6, 9, 12, 15, 18, 19, 21, 28]
