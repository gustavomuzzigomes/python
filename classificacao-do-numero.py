print("Classificação de um número")

print("\nNegativo | Zero | Positivo")

numero= float(input("\nDigite um número: "))

# Condicional para analisar o número
if numero > 0:
    print("Número positivo")
elif numero == 0:
    print("Zero")
else:
    print("Número negativo")