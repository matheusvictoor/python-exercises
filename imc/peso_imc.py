# Computação - UFGC
# Wilkerson
#
# Calcular o imc


peso = float(input())
altura = float(input())

imc = peso / altura ** 2
total = (29.4 * peso) / imc
resultado = total - peso

print(f"IMC atual = {imc:.2f}")
print(f"Peso a ser ganho/perdido = {resultado:.2f}")

