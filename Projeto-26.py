produtos, quantidades = [], []

while True:
    print("\n1.Adicionar\n2.Atualizar\n3.Consultar\n4.Listar\n5.Sair")
    op = input("Escolha: ")

    if op == "1":
        cod = input("Código: ")
        if cod in produtos:
            print("Já existe.")
        else:
            produtos.append(cod)
            quantidades.append(int(input("Quantidade: ")))
    elif op == "2":
        cod = input("Código: ")
        if cod in produtos:
            quantidades[produtos.index(cod)] = int(input("Nova quantidade: "))
        else:
            print("Não encontrado.")
    elif op == "3":
        cod = input("Código: ")
        print(f"Quantidade: {quantidades[produtos.index(cod)]}" if cod in produtos else "Não encontrado.")
    elif op == "4":
        [print(f"{c}: {q}") for c, q in zip(produtos, quantidades)]
    elif op == "5":
        print("Até a próxima!")
        break
    else:
        print("Inválido.")
