estruturas = {}

while True:
    print("\n1. Registrar  2. Visualizar  3. Média  4. Em risco  5. Sair")
    op = input("Opção: ")

    if op == "1":
        while len(estruturas) < 10:
            i = int(input("ID: "))
            if i in estruturas: print("ID já existe."); continue
            estruturas[i] = (float(input("Carga: ")), int(input("Estado (1-3): ")))
        print("10 estruturas registradas.")
    elif op == "2":
        print(*[f"ID:{i} Carga:{c} Estado:{e}" for i, (c, e) in estruturas.items()], sep="\n") if estruturas else print("Nenhuma estrutura.")
    elif op == "3":
        print(f"Média: {sum(c for c, _ in estruturas.values()) / len(estruturas):.2f}" if estruturas else "Sem dados.")
    elif op == "4":
        print(f"Em risco: {sum(e==3 for _, e in estruturas.values())}" if estruturas else "Sem dados.")
    elif op == "5":
        print("Até a próxima!"); break
    else:
        print("Inválido.")
