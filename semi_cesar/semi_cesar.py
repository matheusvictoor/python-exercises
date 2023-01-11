# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# Data: 14/10/2021      miniteste: 9
# Questão: Semi César


def cesar(msg, d):
    letras = ['a','b' ,'c','d' ,'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u','v', 'w', 'x', 'y', 'z']
    palavra = ''
    for i in range(len(msg)):
        char = msg[i]
        if char not in letras:
            palavra += char
        else:
            if(char.isupper()):
                palavra += chr((ord(char) + d - 65) % 26 + 65)
            else:
                palavra += chr((ord(char) + d - 97) % 26 + 97)
    return palavra

assert cesar("exemplo", 4) == "ibiqtps"
assert cesar("Exemplo 2!", 4) == "Ebiqtps 2!"
