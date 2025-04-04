notas = []

while True:
    print("\n1.Inserir nota\n2.Finalizar e exibir resultados")
    op = input("Escolha: ")

    if op == "1":
        try:
            n = float(input("Nota do aluno: "))
            if n >= 0:
                notas.append(n)
            else:
                print("Nota negativa! Não cadastrada.")
        except:
            print("Entrada inválida.")
    elif op == "2":
        if notas:
            media = sum(notas) / len(notas)
            print(f"Média: {media:.2f}")
            print(f"Alunos cadastrados: {len(notas)}")
        else:
            print("Nenhuma nota cadastrada.")
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
