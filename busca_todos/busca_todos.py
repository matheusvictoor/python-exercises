



def  busca_matriz(m, e):

    linha = len(m)
    coluna = len(m[0])
    lista = []

    for l in range(linha):
        for c in range(coluna):
            if m[l][c] == e:
                lista.append(c)
    print(lista)
matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [1, 2, 3, 2, 1],
]


busca_matriz(matriz, 3)

#assert busca_matriz(matriz, 4) == []
#assert set(busca_matriz(matriz, 3)) == set( [(0,1), (0,3), (1,0), (2,2)] )
