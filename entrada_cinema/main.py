# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Entrada no Cinema


ano_atual = int(input("Ano atual? "))
ano_nascimento = int(input("Ano de nascimento? "))

idade = ano_atual - ano_nascimento

print(f"Idade calculada: {idade} anos")

if idade < 14 :
    print("Entrada proibida para menores de 14 anos")

elif idade >= 14 and idade < 16:
    pais = input("Com os pais? ")

    if pais == "s":
        print("Entrada permitida")
    elif pais == "n":
        print("Entrada proibida para menores de 16 anos sem os pais")

elif idade >= 16:
    print("Entrada permitida")
