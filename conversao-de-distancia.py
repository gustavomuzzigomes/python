print("Conversor de Kilômetro para Milhas")

# Converter de Kilômetros para milhas
kilometros= float(input("\nDigite uma distância em Kilômetros: "))
# 1 Kilômetro equivale a 0.261371 milhas
fator_de_conversao= 0.6213712
milhas= kilometros * fator_de_conversao

print(f"{kilometros} Kilômetros é equivalente a {milhas} milhas")
