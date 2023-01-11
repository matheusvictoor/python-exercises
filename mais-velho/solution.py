# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Mais velho entre duas pessoas

import datetime

nome1 = str(input())
dia1 = int(input())
mes1 = int(input())
ano1 = int(input())

nome2 = str(input())
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())

data1 = datetime.date(ano1, mes1, dia1)
data2 = datetime.date(ano2, mes2, dia2)

if data1 < data2:
    print(nome1)
elif data1 > data2:
    print(nome2)
else:
    print("nenhuma")
