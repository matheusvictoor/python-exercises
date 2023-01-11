def meu_join(delimitador, sequencia_de_string):
    concatenado = ""

    for i in range(len(sequencia_de_string)):
        if i  == len(sequencia) - 1:
            concatenado += sequencia_de_string[i]
        else:
            concatenado += sequencia_de_string[i] + delimitador

    return concatenado


sequencia = input()

for i in range(len(sequencia))






funcao = meu_join(deli, sequencia)

print(funcao)
    
