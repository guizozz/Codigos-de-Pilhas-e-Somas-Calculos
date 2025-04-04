vetor = []

while True:
    print("\n1.Inserir número\n2.Verificar número\n3.Ver vetor\n4.Sair")
    op = input("Escolha: ")

    if op == "1":
        try:
            vetor.append(int(input("Número: ")))
        except:
            print("Entrada inválida.")
    elif op == "2":
        try:
            num = int(input("Número a verificar: "))
            print("Número encontrado!" if num in vetor else "Número não está no vetor.")
        except:
            print("Entrada inválida.")
    elif op == "3":
        print("Vetor:", vetor if vetor else "Vazio.")
    elif op == "4":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
