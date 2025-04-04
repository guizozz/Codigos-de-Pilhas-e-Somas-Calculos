from collections import deque

fila = deque()

while True:
    print("\n1.Adicionar\n2.Remover início\n3.Remover final\n4.Listar frente → trás\n5.Listar trás → frente\n6.Sair")
    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome da pessoa: ")
        fila.append(nome)
    elif op == "2":
        if fila:
            print(f"{fila.popleft()} saiu da fila (início).")
        else:
            print("Fila vazia.")
    elif op == "3":
        if fila:
            print(f"{fila.pop()} saiu da fila (final).")
        else:
            print("Fila vazia.")
    elif op == "4":
        print("Fila (frente → trás):", list(fila) if fila else "Fila vazia.")
    elif op == "5":
        print("Fila (trás → frente):", list(reversed(fila)) if fila else "Fila vazia.")
    elif op == "6":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
