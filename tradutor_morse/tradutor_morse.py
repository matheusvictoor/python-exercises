# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# Questão: Tradudor Morse


def tradutor_morse(lista):
    letras = ['a','b' ,'c','d' ,'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u','v', 'w', 'x', 'y', 'z']
    codigo = ['.-', '-...' , '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    
    palavra = ''
    for i in range(len(lista)):
        for j in range(len(codigo)):
            if lista[i] == codigo[j]:
                palavra = palavra + letras[j]
    return palavra

tradutor_morse(['.--.', '-.--', '-', '....', '---', '-.'])
assert tradutor_morse(['.--.', '-.--', '-', '....', '---', '-.']) == 'python'



