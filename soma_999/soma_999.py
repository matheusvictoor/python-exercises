# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Soma 999




soma = 0
numeros = []

while True:

    num = int(input())
    soma += num
    numeros.append(num)

    if soma >= 999: 
        break

print(soma)

contador = 0
media = soma / len(numeros)

print(f'{media:.2f}')

for i in numeros:
    if i > media:
        contador += 1

print(contador)

