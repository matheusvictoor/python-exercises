# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# Data: 14/10/2021     minitest: 9                 
# Questão: Primos até limite                   


def eh_primo(num):

    raiz = int(num ** (0.5))
    for i in range(2, raiz + 1):
        if num % i == 0:
            return False
    return True

def primos_ate(limite):
    lista = []
    for i in range(limite):
        if i > 1:
            if eh_primo(i):
                lista.append(i)
    return lista

assert primos_ate(10) == [2, 3, 5, 7]
assert primos_ate(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

