# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Ordena 3 Números




num1 = int(input())
num2 = int(input())
num3 = int(input())

if(num3 > num2):
    aux = num3
    num3 = num2
    num2 = aux

if(num2 > num1):
    aux = num2
    num2 = num1
    num1 = aux

if(num3 > num2):
    aux = num3
    num3 = num2
    num2 = aux

print(num3, num2, num1)
 
