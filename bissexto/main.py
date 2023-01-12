# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Ano bissexto



ano = int(input())

if (ano % 4) == 0:
    print(f"{ano} é bissexto")

elif (ano % 400) == 0 and (ano % 100) != 0:
    print(f"{ano} não é bissexto")

else:
    print(f"{ano} não é bissexto")
