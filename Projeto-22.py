pessoas = []

while True:
    print("\n1.Inserir\n2.IMC\n3.Dados\n4.Sair")
    op = input("Escolha: ")

    if op == "1":
        try:
            p = float(input("Peso (kg): "))
            a = float(input("Altura (m): "))
            if p > 0 and a > 0: pessoas.append((p, a))
            else: print("Valores devem ser positivos.")
        except: print("Inválido.")
    elif op == "2":
        if not pessoas:
            print("Sem dados.")
            continue
        for i, (p, a) in enumerate(pessoas, 1):
            imc = p / (a**2)
            if imc < 18.5: c = "Abaixo do peso"
            elif imc < 25: c = "Peso normal"
            elif imc < 30: c = "Sobrepeso"
            else: c = "Obesidade"
            print(f"{i} - IMC: {imc:.1f} ({c})")
    elif op == "3":
        if not pessoas: print("Sem dados.")
        else:
            for i, (p, a) in enumerate(pessoas, 1):
                print(f"{i} - Peso: {p}kg, Altura: {a}m")
    elif op == "4":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
