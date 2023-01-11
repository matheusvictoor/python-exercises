# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Soma 5 menores que 20


cont = 0
soma = 0
linha = 0


while True:
    
    sequencia = int(input())
    if sequencia < 20:
        soma += sequencia
        cont += 1

    linha += 1

    if cont == 5: break

print(f"soma = {soma}")
print(f"{cont} menores que 20 até a linha {linha}")


