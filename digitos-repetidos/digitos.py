# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Dígitos repetidos



qnt_palavras = int(input())

repete = []
nao_repete = []

for i in range(qnt_palavras):
    palavra = input()
    cont = 0
    for j in range(len(palavra)):
        if len(palavra) <2: break
        if palavra[j-1] == palavra[j]:
            cont += 1
    if cont != 0:
        repete.append(palavra)
    else:
        nao_repete.append(palavra)

print(repete)
print(nao_repete)

