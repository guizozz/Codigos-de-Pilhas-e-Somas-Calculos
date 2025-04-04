soma = 0

while True:
    print("\n1.Inserir número\n2.Finalizar e mostrar soma")
    op = input("Escolha: ")

    if op == "1":
        try:
            n = int(input("Número positivo: "))
            if n >= 0:
                soma += n
            else:
                print("Número negativo! Não será somado.")
        except:
            print("Entrada inválida.")
    elif op == "2":
        print(f"Soma total: {soma}")
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
