# Matheus Victor Pereira - 120111309
# Multiplica Dígitos Ímpares


lista = []
sequencia = input()

for i in range(len(sequencia)):
    if sequencia[i] in "13579":
        lista.append(int(sequencia[i]))

cont = 1
if len(lista) > 0:
    for j in range(len(lista)):
        cont = cont * lista[j]

    print(cont)

else:
    print("1")
