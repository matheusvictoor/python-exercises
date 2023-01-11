# Computação - UFCG
# Wilkerson
# Matheus Victor Pereira - 120111309
#
# Calcula o salário



salario_bruto = float(input())
horas_de_trabalho = int(input())

hora_bruta = salario_bruto / horas_de_trabalho
ir = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - ir - inss - sindicato 
hora_liquida = salario_liquido / horas_de_trabalho

print(f"Salário Bruto{salario_bruto: .2f}")
print(f"Hora Bruta{hora_bruta: .2f}")
print(f"Desconto IR{ir: .2f}")
print(f"Desconto INSS{inss: .2f}")
print(f"Desconto Sindicato{sindicato: .2f}")
print(f"Salário Líquido{salario_liquido: .2f}")
print(f"Hora Líquida{hora_liquida: .2f}")

