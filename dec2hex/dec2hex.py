# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Conversão Decimal Hexadecimal




hexadecimal = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
numero = int(input())
lista = []
num_hexa = ""

if numero == 0:
    print("q = 0, r = 0")
    print("0")

while numero > 0:

    resto = numero % 16
    lista.append(hexadecimal[resto])
    numero = numero // 16
    print(f"q = {numero}, r = {resto}")

for i in range(len(lista)-1,-1,-1):
    num_hexa = num_hexa + str(lista[i])

print(num_hexa)


