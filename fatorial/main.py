# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Fatorial



fat = 1
numero = int(input())

if numero == 0:
    print("1")
else:
    for i in range(2,numero + 1):
        fat  = fat * i
    print(fat)
    

