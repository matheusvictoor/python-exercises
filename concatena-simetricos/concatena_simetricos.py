# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Concatena Simétricos




def concatena_simetricos(valor):
    lista = []
    if len(valor) % 2 == 0:

      for i in range(0, len(valor)-1):
        um = valor[i]
        dois = valor[-i-1]

        palavra = valor[i] + valor[-i-1]

        if um > dois:
          lista.append(valor[-i-1] + valor[i])

        elif um < dois:
          lista.append(valor[i] + valor[-i-1])

        else:
          lista.append(valor[i] + valor[-i-1])

      lista.pop(-1)
      return lista
    
    else:
        contador = -1

        cond = (( len(valor) - 1 ) / 2)

    for i in range(0, len(valor)-1):
      contador += 1

      if contador != cond:

        um = valor[i]
        dois = valor[-i-1]

        palavra = valor[i] + valor[-i-1]

        if um > dois:
          lista.append(valor[-i-1] + valor[i])

        elif um < dois:
          lista.append(valor[i] + valor[-i-1])

        else:
          lista.append(valor[i] + valor[-i-1])

        lista.append(palavra)

      else:
        lista.append(valor[i])
        break

    lista.pop(-1)


    return lista


x = ["bola", "tv", "zebra", "arara"]
y = ["ab", "cd", "ef", "gh", "ij"]
u = ["cd", "gh", "ck"]

print(concatena_simetricos(u))


