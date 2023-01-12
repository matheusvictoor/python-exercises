# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# Questão: Conta Alertas do Açude                


def conta_alertas_acude(medicoes):
    cont_alertas = 0
    for i in range(len(medicoes)-1):
        if (abs(medicoes[i] - medicoes[i+1]) < 10) and medicoes[i] <= 17:
            cont_alertas += 1
    return cont_alertas



medicoes = [50, 50, 50, 23, 21, 17, 15, 60, 65, 15, 15]
assert conta_alertas_acude(medicoes) == 2

