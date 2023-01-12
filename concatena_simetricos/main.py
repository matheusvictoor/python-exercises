# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Concatena Simétricos


def concatena_simetricos(valor):
    lista = []
    if len(valor) % 2 == 0:
        for i in range(0, len(valor)-1):
            contador += 1

            if contador != cond:

                um = valor[i]
                dois = valor[-i-1]

                palavra = valor[i] + valor[-i-1]

            if um > dois:
                lista.append(valor[-i-1] + valor[i])

            elif um < dois:
                lista.append(valor[i] + valor[-i-1])

            else:
                lista.append(valor[i] + valor[-i-1])

                lista.append(palavra)

    else:
        
        cond = (( len(valor) - 1 ) / 2)
        lista.append(valor[int(cond)])

    return lista

y = ["ab", "cd", "ef", "gh", "ij"]
x = ["bola", "tv", "zebra", "arara"]

print(concatena_simetricos(x))

