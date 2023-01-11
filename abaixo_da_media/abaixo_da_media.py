
# Questão: Remove abaixo da média


def remove_abaixo_media(l1):

    soma = 0
    cont = 0
    lista = []

    for i in l1:
        soma += i

    media = soma/len(l1)

    for j in range(len(l1)):
        if l1[j] < media:
            lista.append(j)
    for k in lista:
        l1.pop(k - cont)
        cont += 1

    return l1
