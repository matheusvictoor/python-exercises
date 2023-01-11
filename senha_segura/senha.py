# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# Questão: Senha segura


def senha_segura(senha):
    cont = 0
    for i in range(len(senha)):
        if ((int(senha[i]) % 2 == 0) and (int(i)+1) % 2 == 0) or ((int(senha[i]) % 2 != 0) and (int(i)+1) % 2 != 0):
            cont += 1
        else:
            return "Senha insegura"
    return "Senha segura"


assert senha_segura("12346") == "Senha insegura"
assert senha_segura("125638") == "Senha segura"
assert senha_segura("123456789") == "Senha segura"




