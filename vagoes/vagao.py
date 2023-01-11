# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Vagões



k = int(input())
vagao = input().split()
cont = 0

for i in range(len(vagao)-1):
    teste = int(vagao[i]) - int(vagao[i+1])
    if k < abs(teste):
        cont += 1
print(cont)

