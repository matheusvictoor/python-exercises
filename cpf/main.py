# Universidade Federal de Campina Grande
# Ciência da Computação
# Prof: Wilkerson, Jorge e Dalton
# Matheus Victor Pereira - 120111309
# 
# Questão: Dígitos de Verificação do CPF



def digito(cpf):
    x = 2
    soma = 0
    for i in range(len(cpf)-1,-1,-1):
        soma += int(cpf[i]) * x
        x += 1
    dig = ((soma * 10) % 11)
    if dig == 10: return str(0)

    return str(dig)


def calcula_digitos_verificacao(cpf):
    dig1 = digito(cpf)
    concatena = cpf + dig1
    dig2 = digito(concatena)
    return (dig1 + dig2)

assert calcula_digitos_verificacao('153245875') == '40'

