# Importar biblioteca calendário
import calendar
print("Calendário")

ano= int(input("\nDigite o ano: "))
mes= int(input("Digite o mês: "))

calendario= calendar.month (ano, mes)

print(calendario)