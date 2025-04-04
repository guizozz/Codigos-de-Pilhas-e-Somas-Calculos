from collections import deque

class Cliente:
    def __init__(self, codigo, idade, salario):
        self.codigo = codigo
        self.idade = idade
        self.salario = salario

# Inicializa pilha e fila
pilha, fila = [], deque()

# Funções para manipular a pilha e a fila
def empilhar(cliente): pilha.append(cliente)
def desempilhar(): return pilha.pop() if pilha else None
def enfileirar(cliente): fila.append(cliente)
def desenfileirar(): return fila.popleft() if fila else None
def procurar(codigo, estrutura): return next((c for c in estrutura if c.codigo == codigo), None)

# Função para imprimir dados de qualquer estrutura (pilha ou fila)
def imprimir(estrutura): 
    if estrutura:
        for c in estrutura:
            print(f"Código: {c.codigo}, Idade: {c.idade}, Salário: {c.salario}")
    else:
        print("Estrutura vazia.")

# Menu
def menu():
    while True:
        print("\nMenu:")
        print("1. Empilhar cliente na PILHA")
        print("2. Desempilhar cliente da PILHA")
        print("3. Imprimir todo o conteúdo da PILHA")
        print("4. Contar quantidade de elementos na PILHA")
        print("5. Procurar um código na PILHA")
        print("6. Enfileirar cliente na FILA")
        print("7. Desenfileirar cliente da FILA")
        print("8. Imprimir todo o conteúdo da FILA")
        print("9. Procurar um código na FILA")
        print("10. Sair")
        
        opcao = int(input("Escolha uma opção (1-10): "))
        
        if opcao == 1:
            c = Cliente(int(input("Código: ")), int(input("Idade: ")), float(input("Salário: ")))
            empilhar(c)
            print("Cliente empilhado.")
        elif opcao == 2:
            c = desempilhar()
            print(f"Cliente {c.codigo} desempilhado." if c else "Pilha vazia.")
        elif opcao == 3:
            imprimir(pilha)
        elif opcao == 4:
            print(f"Quantidade de clientes na pilha: {len(pilha)}")
        elif opcao == 5:
            c = procurar(int(input("Código: ")), pilha)
            print(f"Cliente encontrado: {c.codigo}, {c.idade}, {c.salario}" if c else "Cliente não encontrado.")
        elif opcao == 6:
            c = Cliente(int(input("Código: ")), int(input("Idade: ")), float(input("Salário: ")))
            enfileirar(c)
            print("Cliente enfileirado.")
        elif opcao == 7:
            c = desenfileirar()
            print(f"Cliente {c.codigo} desenfileirado." if c else "Fila vazia.")
        elif opcao == 8:
            imprimir(fila)
        elif opcao == 9:
            c = procurar(int(input("Código: ")), fila)
            print(f"Cliente encontrado: {c.codigo}, {c.idade}, {c.salario}" if c else "Cliente não encontrado.")
        elif opcao == 10:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Inicia o programa
menu()
