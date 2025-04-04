def verificar_ponte():
    try:
        peso = float(input("Digite o peso total dos veículos na ponte (em toneladas): "))
        if peso > 5000:
            print("Atenção! A ponte está sobrecarregada.")
        else:
            print("A ponte está segura.")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

while True:
    print("\nMenu:")
    print("1. Verificar segurança da ponte")
    print("2. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        verificar_ponte()
    elif opcao == '2':
        print("Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")
