
# Questão: Morangos por Caixa


qnt_morangos = int(input())

qnt_caixas = qnt_morangos // 400

porcentagem = ((qnt_morangos % 400) * 100) / qnt_morangos

print(f"{qnt_caixas} caixa(s) completa(s) para embalar os morangos.")
print(f"{porcentagem:.1f}% dos morangos serão perdidos.")
