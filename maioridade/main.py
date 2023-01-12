# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: 0Maioridade Penal


nomes = input().split(" ")
idade = input().split(" ")

for i in range(len(idade)):
    if int(idade[i]) >= 18:
        print(nomes[i])
