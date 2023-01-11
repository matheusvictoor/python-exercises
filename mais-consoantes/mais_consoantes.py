# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Mais Consoantes




lista = []

while True:

    palavra= input()
    qnt_vogal = 0

    for elemento in palavra:
        if elemento in "aeiouAEIOU":
            qnt_vogal += 1

    consoantes = (len(palavra) - qnt_vogal)
    lista.append(consoantes)

    if consoantes > qnt_vogal:
        break

maior = 0

for i in range(len(lista)):
    if lista[i] > lista[maior]:
        maior = i

print(maior + 1)

