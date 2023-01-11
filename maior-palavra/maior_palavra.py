# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Frase com Maior Palavra




cont = 1
posicao_da_frase = 0
maior_frase = ""

while True:
    frase = input().split(" ")
    if frase[0] == "fim":
        break
    maior_palavra = frase[0]

    for palavra in frase:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    if len(maior_palavra) > len(maior_frase):
        maior_frase = maior_palavra
        posicao_da_frase = cont
    cont += 1

print(f"Frase {posicao_da_frase}: {maior_frase}")

