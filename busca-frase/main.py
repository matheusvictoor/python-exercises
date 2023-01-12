frase1 = input()
frase2 = input()

cont = 0
lista = []

for i in range(len(frase2)):
    for j in range(len(frase1)):
        if frase2[i] == frase1[j]:
            cont += 1
        else:
            break
    lista.append(cont)

print(lista)

