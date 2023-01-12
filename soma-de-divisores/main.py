




while True:

    soma_divisores = 0
    conta_divisores = 0

    entrada = int(input())

    if entrada == -1:
        break

    for i in range(entrada):
        if entrada % 5 == 0:
            soma_divisores += entrada
            conta_divisores += 1

    print(soma_divisores)
    print(conta_divisores)




