# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Sensor de Ruídos



detector = input()
horario = int(input())


if detector != ("") and (horario >= 22 and horario <= 6):
    print("Perturbação Detectada!")

elif detector == ("") and (horario < 22 and horario > 6):
    print("Condomínio em Paz.")


