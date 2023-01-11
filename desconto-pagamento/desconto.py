# Universidade Federal de Campina grande - UFCG
# Ciência da Computação - Programação I
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Questão: Desconto no pagamento



opcao_pagamento = int(input())
valor = float(input())

if opcao_pagamento == 1:
    valor_final = valor - (valor * 0.15)
    print(f"Valor final: R$ {valor_final:0.2f}")

if opcao_pagamento == 2:
    valor_final = valor - (valor * 0.05)
    print(f"Valor final: R$ {valor_final:0.2f}")

if opcao_pagamento == 3:
    valor_final = valor
    print(f"Valor final: R$ {valor_final:0.2f}")

if opcao_pagamento == 4:
    valor_final = valor + (valor * 0.10)
    print(f"Valor final: R$ {valor_final:0.2f}")


