# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
# Questão: Mais Velhos Primeiro




def idosos_inicio(fila):
    index = 0
    for i in range(len(fila)-1):
        if fila[i] >= 60:
            fila[index], fila[i] = fila[i], fila[index]
            index += 1


fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]
