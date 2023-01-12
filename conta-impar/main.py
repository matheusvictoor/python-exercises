# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Conta ímpares e Imprime Último Ímpar



cont1 = 0
cont2 = 0
ultimo = 0

numero = input()

for i in range(len(numero)):
    
    if int(numero[i]) % 2 == 0:
        cont1 += 1
    elif int(numero[i]) % 2 != 0 :
        cont2 += 1
        ultimo = numero[i]
if cont1 == 0:
    print('-')
else :
    print(cont2)
    print(ultimo)

