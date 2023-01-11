# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
#Questão: Calculo do IMC


peso = float(input())
altura = float(input())

imc = peso / altura ** 2

if imc < 18.5:
    classificacao = "Magreza"

elif imc >= 18.5 and imc < 25:
    classificacao = "Saudável"

elif imc >= 25 and imc < 30:
    classificacao = "Sobrepeso"

elif imc >= 30:
    classificacao = "Obesidade"

print(f"IMC = {imc:.1f}")
print(f"Classificação = {classificacao}")

