while True:
    
        figura = input("\nPerímetro de Figuras Geométricas Planas"
               "\n\nOpções:"
               "\n1. Triângulo"
               "\n2. Quadrado"
               "\n3. Retângulo"
               "\n4. Trapézio"
               "\n5. Losango"
               "\n6. Círculo"
               "\n\nDigite o número da figura plana que deseja calcular o seu perímetro: "
               )

        if figura == '1':
            lado1 = float(input("\nDigite o tamanho do primeiro lado do triângulo: "))
            lado2 = float(input("Digite o tamanho do segundo lado do triângulo: "))
            lado3 = float(input("Digite o tamanho do terceiro lado do triângulo: "))
            perimetro = lado1 + lado2 + lado3 
            figura = 'triangulo'
            print("\nO valor do perímetro do %s é %.1f" %(figura,perimetro))

        elif figura == '2':
            lado = float(input("\nDigite o tamanho do lado do quadrado: "))
            perimetro = 4*lado
            figura = 'quadrado'
            print("\nO valor do perímetro do %s é %.1f" %(figura,perimetro))

        elif figura == '3':
            base = float(input("\nDigite o tamanho da base do retângulo: "))
            altura = float(input("Digite o tamanho da altura do retângulo: "))
            perimetro = 2*base + 2*altura
            figura = 'retângulo'
            print("\nO valor do perímetro do %s é %.1f" %(figura,perimetro))

        elif figura == '4':
            base_maior = float(input("\nDigite o tamanho da base maior do trapézio: "))
            base_menor = float(input("Digite o tamanho da base menor do trapézio: "))
            lado1 = float(input("Digite o tamanho de um lado do trapézio: "))
            lado2 = float(input("Digite o tamanho do outro lado do trapézio: "))
            perimetro = base_maior + base_menor + lado1 + lado2
            figura = 'trapézio'
            print("\nO valor do perímetro do %s é %.1f" %(figura,perimetro))

        elif figura == '5':
            lado1 = float(input("\nDigite o tamanho de um lado do losango:  "))
            lado2 = float(input("Digite o tamanho do outro lado do losango: "))
            perimetro = 2*lado1 + 2*lado2
            figura ='losango'
            print("\nO valor do perímetro do %s é %.1f" %(figura,perimetro))

        elif figura == '6':
            raio = float(input("\nDigite o tamanho do raio do círculo: "))
            perimetro = 2*3.14*raio
            figura = 'círculo'
            print("\nO valor do perímetro do %s é %.1f" %(figura,perimetro))

        else:
            print("\nOpção inválida!")
        
        while True:
            opcao = input('\nDeseja reiniciar (S/N)? ').lower() 
            if opcao not in ('s', 'n'):
                print('Opção inválida, deve ser S ou N')
            else: 
                break 
        if opcao == 'n': 
            break 
   

        

        
       






