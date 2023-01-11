# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
# Questão: Precede Ímpares


def precede_impares(numeros):

    lista = [0]
    for i in range(len(numeros)-1):
        if numeros[i] % 2 == 0:
            if numeros[i + 1] % 2 != 0:
                cont = True
                for k in lista:
                    if numeros[i] == k:
                        cont = False
                        break
                if cont:
                    lista.append(numeros[i])
    lista.pop(0)
    return lista


assert precede_impares([15, 2, 4, 3, 8, 7, 6]) == [4, 8]
assert precede_impares([4, 3, 2, 2, 4, 5]) == [4]
assert precede_impares([1, 5, 4, 3, 8, 7]) == [4, 8]


