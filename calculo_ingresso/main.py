# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Calculo do Ingresso



idade = int(input("Idade: "))



if idade < 12:

    print("===")
    print("Nome: anônimo")
    print(f"Idade: {idade}")
    print("Documento: ")
    print("Preço: 10.00")

elif idade >= 12 and idade <=18:
    nome = input()
    numero_doc = int(input())

    print("===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Documento: {numero_doc}")
    print("Preço: 10.00")

elif idade > 18 and idade < 60:
    print("===")
    print("Nome: anônimo")
    print(f"Idade: {idade}")
    print("Documento: ")
    print("Preço: 20.00")

elif idade > 60:
    nome = input()
    numero_doc = int(input())

    print("===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Documento: {numero_doc}")
    print("Preço: 12.00")

