while True:

    figura = input("\nÁrea de Figuras Geométricas Planas"
               "\n\nOpções:"
               "\n1. Triângulo"
               "\n2. Quadrado"
               "\n3. Retângulo"
               "\n4. Trapézio"
               "\n5. Losango"
               "\n6. Círculo"
               "\n\nDigite o número da figura plana que deseja calcular a sua área: "
               )

    if figura == '1':
        base = float(input("\nDigite o tamanho da base: "))
        altura = float(input("Digite o tamanho da altura: "))
        area = base*altura/2
        figura = 'triangulo'
        print("\nO valor da área do %s é %.1f" %(figura,area))

    elif figura == '2':
        lado = float(input("\nDigite o tamanho do lado: "))
        area = lado*lado
        figura = 'quadrado'
        print("\nO valor da área do %s é %.1f" %(figura,area))

    elif figura =='3':
        comprimento = float(input("\nDigite o tamanho do comprimento: "))
        largura = float(input("Digite o tamanho da largura: "))
        area = comprimento*largura
        figura = 'retângulo'
        print("\nO valor da área do %s é %.1f" %(figura,area))

    elif figura == '4':
        base_maior = float(input("\nDigite o tamanho da base maior: "))
        base_menor = float(input("Digite o tamanho da base menor: "))
        altura = float(input("Digite o tamanho da altura: "))
        area = (base_maior+base_menor)*altura/2
        figura = 'trapézio'
        print("\nO valor da área do %s é %.1f" %(figura,area))
        
    elif figura == '5':
        diagonal_maior = float(input("\nDigite o tamanho da diagonal maior: "))
        diagonal_menor = float(input("Digite o tamanho da diagonal menor: "))
        area = diagonal_maior*diagonal_menor/2
        figura ='losango'
        print("\nO valor da área do %s é %.1f" %(figura,area))

    elif figura == '6':
        raio = float(input("\nDigite o tamanho do raio: "))
        area = 3.14*raio**2
        figura = 'círculo'
        print("\nO valor da área do %s é %.1f" %(figura,area))    

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


  


