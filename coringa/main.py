# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Números Mais Próximos do Coringa




def separa_numeros(entrada):
    tokens = entrada.split()
    numeros = []
    for i in tokens:
        numeros.append(int(i))
    return numeros

def menor (lista):
    posicao_do_menor = 0
    for i in range(len(lista)):
        if lista[i] < lista [posicao_do_menor]:
            posicao_do_menor = i
    return posicao_do_menor

numero_coringa = int(input())
lista = input()
numeros = separa_numeros(lista)
lista_diferenca = []


for i in range(len(numeros)):
    diferenca = abs(numero_coringa - numeros[i])
    lista_diferenca.append(diferenca)
    menor_diferenca = 0
    if menor(lista_diferenca) < 
        
