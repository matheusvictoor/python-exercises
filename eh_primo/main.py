# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
# Questão: É primo?

def eh_primo(num):

    raiz = int(num ** (0.5))
    for i in range(2, raiz + 1):
        if num % i == 0:
            return False
    return True

assert eh_primo(3) == True
assert eh_primo(5) == True
assert eh_primo(10) == False
assert eh_primo(11) == True
assert eh_primo(15) == False
