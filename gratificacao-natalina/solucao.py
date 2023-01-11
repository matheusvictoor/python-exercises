# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Gratificação Natalina



codigo = int(input()) 

if  codigo == 1:
    print("Deverá receber em dezembro R$ 25000.00.")

elif codigo == 2:
    print("Deverá receber em dezembro R$ 15000.00")

elif codigo == 3:
    dias_faltados  = int(input())
    if dias_faltados == 0:
        G = 500
    else:
        G = (235 - dias_faltados) * 2

    print(f"Valor da gratificação R$ {G:.2f}")
    print(f"Deverá receber em dezembro R$ {8000.00 + G:.2f}")

elif codigo == 4:
    dias_faltados  = int(input())
    if dias_faltados == 0:
        G = 300
    else:
        G = (235 - dias_faltados)

    print(f"Valor da gratificação R$ {G:.2f}")
    print(f"Deverá receber em dezembro R$ {5000.00 + G:.2f}")

elif codigo == 5:
    dias_faltados  = int(input())
    if dias_faltados == 0:
        G = 200
    else:
        G = (235 - dias_faltados) * 0.7
        
    print(f"Valor da gratificação R$ {G:.2f}")
    print(f"Deverá receber em dezembro R$ {2500.00 + G:.2f}")


