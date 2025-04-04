materiais = {}

while True:
    print("\n1.Inserir\n2.Visualizar\n3.Média de preços\n4.Sair")
    op = input("Escolha: ")

    if op == "1":
        for _ in range(10 - len(materiais)):
            cod = int(input("Código: "))
            if cod not in materiais:
                materiais[cod] = float(input("Preço: "))
            else:
                print("Código já existe.")
        if len(materiais) == 10:
            print("Limite de 10 materiais atingido.")
    elif op == "2":
        if materiais:
            for c, p in materiais.items():
                print(f"Código: {c} | Preço: R${p:.2f}")
        else:
            print("Nenhum material cadastrado.")
    elif op == "3":
        if materiais:
            media = sum(materiais.values()) / len(materiais)
            print(f"Média de preços: R${media:.2f}")
        else:
            print("Nenhum material para calcular a média.")
    elif op == "4":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
