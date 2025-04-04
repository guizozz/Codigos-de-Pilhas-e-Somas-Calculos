pilha = []

while True:
    print("\n1.Adicionar\n2.Somar\n3.Subtrair\n4.Multiplicar\n5.Dividir\n6.Topo\n7.Sair")
    op = input("Escolha: ")

    if op == "1":
        try: pilha.append(float(input("Número: ")))
        except: print("Inválido.")
    elif op in "2345":
        if len(pilha) < 2:
            print("Precisa de 2 números.")
            continue
        a, b = pilha.pop(), pilha.pop()
        try:
            res = {
                "2": a + b,
                "3": a - b,
                "4": a * b,
                "5": a / b
            }[op]
            pilha.append(res)
            print("Resultado:", res)
        except ZeroDivisionError:
            print("Erro: divisão por zero.")
            pilha.extend([b, a])
    elif op == "6":
        print("Topo:", pilha[-1] if pilha else "Pilha vazia.")
    elif op == "7":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
