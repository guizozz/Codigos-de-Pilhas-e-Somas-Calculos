def calcular_volume():
    try:
        base = float(input("Digite a base da viga (m): "))
        altura = float(input("Digite a altura da viga (m): "))
        comprimento = float(input("Digite o comprimento da viga (m): "))
        volume = base * altura * comprimento
        print(f"Volume da viga: {volume:.2f} m³")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        
while True:
    print("\nMenu:")
    print("1. Calcular o volume de uma viga retangular")
    print("2. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        calcular_volume()
    elif opcao == '2':
        print("Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")
