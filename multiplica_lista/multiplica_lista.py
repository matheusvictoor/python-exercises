# Universidade Federal de Campina Grande - UFCG
# Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
#
# Questão: Multiplica lista



def multiplica_lista(n,lista):
    l = []
    for k in range(n):
        for i in range(len(lista)):
            l.append(lista[i])
    return l

l = ['joao', 'pedro']
assert multiplica_lista(2,l) == ['joao', 'pedro', 'joao', 'pedro']



