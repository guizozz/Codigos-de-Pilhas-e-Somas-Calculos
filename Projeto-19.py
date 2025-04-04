pilha = []

while True:
    print("\n1.Inserir número\n2.Calcular fatorial\n3.Ver topo\n4.Sair")
    op = input("Escolha: ")

    if op == "1":
        try:
            num = int(input("Número inteiro positivo: "))
            if num >= 0:
                pilha.append(num)
            else:
                print("Digite um número não negativo.")
        except:
            print("Entrada inválida.")
    elif op == "2":
        if not pilha:
            print("Pilha vazia.")
            continue
        n = pilha[-1]
        fat = 1
        for i in range(2, n + 1):
            fat *= i
        print(f"Fatorial de {n}: {fat}")
    elif op == "3":
        print("Topo:", pilha[-1] if pilha else "Pilha vazia.")
    elif op == "4":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
