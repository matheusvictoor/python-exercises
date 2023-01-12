

# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
# Questão: Uma Variação do Método Noves Fora



def ordena(numero):
    
    seq = str(numero)
    lista = []

    for i in seq:
        lista.append(int(i))

    for final in range(len(lista), 0, -1):
        for atual in range(0, final-1):
            if lista[atual] < lista[atual + 1]:
                lista[atual], lista[atual + 1] = lista[atual + 1], lista[atual]
    
    return lista

numero = 751934
lista = ordena(numero)

def noves_fora(lista):
    
    soma = 0
    index = 0
    for i in range(len(lista)-1):

        soma = lista[i] + lista[i + 1]
        if soma >= 9:
            soma -= 9
        soma += soma

        print(soma)




noves_fora(lista)

