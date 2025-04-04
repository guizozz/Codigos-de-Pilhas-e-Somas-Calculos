def calcular_carga_distribuida():
    try:
        carga_total = float(input("Digite a carga total (em kN): "))
        comprimento = float(input("Digite o comprimento da viga (em metros): "))
        
        if comprimento <= 0:
            print("O comprimento deve ser maior que zero.")
            return
        
        carga_distribuida = carga_total / comprimento
        print(f"Carga distribuída: {carga_distribuida:.2f} kN/m")
    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos.")

while True:
    print("\nMenu:")
    print("1. Calcular carga distribuída")
    print("2. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        calcular_carga_distribuida()
    elif opcao == '2':
        print("Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")
