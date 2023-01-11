# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
# Questão: Diff índices


def idiff(seq1, seq2):
    
    limite = 0
    lista = []
    lista2 = []

    if len(seq1) > len(seq2):
        limite = len(seq1)
        lista = seq1
        lista2 = seq2

    else:
        limite = len(seq2)
        lista = seq2
        lista2 = seq1

    for i in range(limite):
        if lista2[i] == lista[i]:
            print("ok")

seq1 = [10, 20, 30, 40, 50, 60, 70]
seq2 = [10, 20, 20, 40, 80]
idiff(seq1, seq2)
#assert idiff(seq1, seq2) == [2, 4, 5, 6]

