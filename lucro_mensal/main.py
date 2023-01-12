# Universidade Federal de Campina Grande - UFCG
# Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
#
# Questão: Lucro mensal



receitas = []
lista = []
meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]

j = 0

for i in range(12):
    entrada = input()
    receitas += entrada.split()
    saldo = float(receitas[j]) - float(receitas[j+1])
    lista.append(saldo)
    j += 2

for n in range(12):
    if lista[n] < 0:
        print(f"{meses[n]} {lista[n]:.1f}")
    else:
        print(f"{meses[n]}  {lista[n]:.1f}")
