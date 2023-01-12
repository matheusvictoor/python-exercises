
def formata_texto(lista):
    saida = ""
    for i in range(len(lista)):
        l = lista[i]
        saida += f"{l}  "
    
    return saida


frase = input()
int1 = int(input())
int2 = int(input())
imprime = []

for i in range(int1, int2):
    if frase[i] == " ":
        imprime.append(",")
    else:
        imprime.append(frase[i])

print(f"{formata_texto(imprime)}")



    
