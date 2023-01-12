# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Limpeza

servico = int(input())

if servico == 1:
    tamanho_fossa = int(input())
    total = tamanho_fossa * 80
    print(f"R$ {total:.2f}")
    
    if total >= 200:
        print("Brinde !")

elif servico == 2:
    tamanho_caixa = int(input())
    total = tamanho_caixa * 50
    print(f"R$ {total:.2f}")

    if total >= 200:
        print("Brinde !")

elif servico == 3:
    print ("R$ 50,00")
