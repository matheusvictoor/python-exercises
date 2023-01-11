# Universidade Federal de Campina Grande - UFCG
# Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
#
# Questão: Soma intervalo



def soma_intervalo(a, b):
    if b >= a:
        diferenca = b - a
        soma = 0
        x = a
        for u in range(diferenca + 1):
            soma += a
            a += 1
        return soma

assert soma_intervalo(5,15) == 110
assert soma_intervalo(10,10) == 10
