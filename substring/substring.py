# Universidade Federal de Campina Grande - UFCG
# Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
#
# Questão: Verificando se uma String é Substring de Outra String



def is_substring(str1, str2):
    lista = []
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                lista.append(j)

    if len(lista) == len(str2):
        return True
    return False



#is_substring('boiada','oi')

assert is_substring('boiada','oi')
assert not is_substring('casorio', 'casa')

