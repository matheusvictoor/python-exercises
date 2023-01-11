# Universidade Federal de Campina Grande - UFCG
# Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
#
# Questão: Afinidade musical




def tem_afinidade(l1, l2):
    cont = 0
    for i in range(len(l2)):
        if l2[i] in l1:
            cont += 1
    if cont >= 3:
        return True
    return False




l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True
