# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Palavras com Letras Dobradas




def repete(nome):
    for i in range(len(nome)):
        if nome[i] == nome[i+1]:
            return 1
        else:
            return 0

palavras = []
repete_letras = []
nao_repete = []

qnt_palavras = int(input())

for i in range(qnt_palavras):
    palavra = input()
    palavras.append(palavra)
    repete(palavras[i])

    cont1 = 0
    cont2 = 0

    if repete == 1:
        cont1 += 1
        repete_letras.append(cont1)

    elif repete == 0:
        cont2 += 1
        nao_repete.append(cont2)

print(repete_letras)
print(nao_repete)


