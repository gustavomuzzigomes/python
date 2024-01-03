# Definindo uma função de adição
def adicao(x, y):
    return x + y

# Definindo uma função de subtração
def subtracao(x, y):
    return x - y 

# Definindo uma função de multiplicação
def multiplicacao(x, y):
    return x * y

# Definindo uma função de divisão
def divisao(x, y):
    return x / y

print("Calculadora")

print("\nSelecione uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
    opcao= input("\nEscolhe uma opção(1/2/3/4): ")
    if opcao in ('1', '2', '3', '4'):
        try:
            numero1= float(input("Digite o primeiro número: "))
            numero2= float(input("Digite o segundo número: "))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if opcao == '1':
            print(numero1, "+", numero2, "=", adicao(numero1,numero2))
        elif opcao == '2':
            print(numero1, "-", numero2, "=", subtracao(numero1,numero2))
        elif opcao == '3':
            print(numero1, "*", numero2, "=", multiplicacao(numero1,numero2))
        elif opcao == '4':
            print(numero1, "/", numero2, "=", divisao(numero1,numero2))
        
        proximo_calculo= input("Deseja realizar mais um cálculo? (sim/não): ")
        if proximo_calculo == "não":
            break
    
    else:
        print("Opção Inválida!")

    
