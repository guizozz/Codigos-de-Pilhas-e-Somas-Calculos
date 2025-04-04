from collections import deque

def exibir_menu():
    print("\n--- MENU BANCO ---")
    print("1. Adicionar um novo cliente na fila")
    print("2. Atender o próximo cliente")
    print("3. Verificar quem é o próximo na fila")
    print("4. Verificar se a fila está vazia")
    print("5. Sair")

def main():
    fila = deque()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            fila.append(nome)
            print(f"{nome} foi adicionado(a) à fila.")

        elif opcao == "2":
            if fila:
                atendido = fila.popleft()
                print(f"{atendido} foi atendido(a).")
            else:
                print("A fila está vazia. Ninguém para atender.")

        elif opcao == "3":
            if fila:
                print(f"O próximo cliente é: {fila[0]}")
            else:
                print("A fila está vazia.")

        elif opcao == "4":
            if not fila:
                print("A fila está vazia.")
            else:
                print("Ainda há clientes na fila.")

        elif opcao == "5":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
