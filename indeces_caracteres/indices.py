# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Índices de caracteres



sequencia = input()
busca = input()


for i in range(len(busca)):
    if busca[i] in sequencia:   
        lista = ""
        for j in range(len(sequencia)):
            if busca[i] == sequencia[j]:
                if j == 0:
                    lista = lista + str(j)

                elif j < len(sequencia):
                    lista = lista + str(j) + " "

                if j == len(sequencia):
                    lista = lista + str(j)
        print(lista)
    else:
        print("-1")
    
