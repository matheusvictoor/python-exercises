# Universidade Federal de Campina Grande - UFCG
# Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
#
# Questão: Maioridade Penal Função



def maioridade_penal(nomes, idades):
    n = nomes.split(" ")
    i = idades.split(" ")
    l = ""
    for j in range(len(i)):
        if int(i[j]) >= 18:
            if len(idades) > 1:
                l = l + n[j] + " "
            else:
                l = l + n[j]
    return l.rstrip()

assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
