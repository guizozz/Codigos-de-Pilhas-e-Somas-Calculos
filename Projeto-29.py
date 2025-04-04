N = 5
comp = [0.0] * N
larg = [0.0] * N
forca = [0.0] * N
pressao = [None] * N  # Usamos None para verificar se foi calculada

while True:
    print("\nMenu:")
    print("1. Inserir dimensões")
    print("2. Inserir força")
    print("3. Calcular pressão")
    print("4. Exibir dados")
    print("5. Sair")
    op = input("Opção: ")

    if op == '1':
        for i in range(N):
            comp[i] = float(input(f"Fundação {i+1} - Comprimento: "))
            larg[i] = float(input(f"Fundação {i+1} - Largura: "))
    elif op == '2':
        for i in range(N):
            forca[i] = float(input(f"Força fundação {i+1}: "))
    elif op == '3':
        for i in range(N):
            area = comp[i] * larg[i]
            if area > 0:
                pressao[i] = forca[i] / area
            else:
                pressao[i] = None
        print("Pressão calculada com sucesso!")
    elif op == '4':
        for i in range(N):
            print(f"\nFundação {i+1}:")
            print(f"  Comprimento: {comp[i]}")
            print(f"  Largura: {larg[i]}")
            print(f"  Força: {forca[i]}")
            if pressao[i] is not None:
                print(f"  Pressão de contato: {pressao[i]:.2f}")
            else:
                print("  Pressão de contato: ainda não calculada.")
    elif op == '5':
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
