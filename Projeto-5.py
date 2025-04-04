def menu():
    print("\nMenu de Operações:")
    print("1. Somar dois números")
    print("2. Subtrair dois números")
    print("3. Multiplicar dois números")
    print("4. Dividir dois números")
    print("5. Sair")

while True:
    # Exibe o menu
    menu()

    # Solicita a escolha do usuário
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 5:
        print("Saindo do programa. Até logo!")
        break  # Encerra o programa

    # Para as opções de 1 a 4, solicita dois números
    if opcao in [1, 2, 3, 4]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realiza a operação correspondente
        if opcao == 1:
            resultado = num1 + num2
            print(f"A soma de {num1} + {num2} é {resultado:.2f}")
        elif opcao == 2:
            resultado = num1 - num2
            print(f"A subtração de {num1} - {num2} é {resultado:.2f}")
        elif opcao == 3:
            resultado = num1 * num2
            print(f"A multiplicação de {num1} * {num2} é {resultado:.2f}")
        elif opcao == 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"A divisão de {num1} / {num2} é {resultado:.2f}")
            else:
                print("Erro: divisão por zero não é permitida!")
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")
