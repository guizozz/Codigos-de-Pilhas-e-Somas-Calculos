alunos = {}

while True:
    print("\n1. Adicionar aluno\n2. Remover aluno\n3. Listar alunos\n4. Buscar por matrícula\n5. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        alunos[matricula] = nome
        print("Aluno adicionado.")
    elif opcao == "2":
        matricula = input("Matrícula do aluno a remover: ")
        print("Aluno removido." if alunos.pop(matricula, None) else "Aluno não encontrado.")
    elif opcao == "3":
        if alunos:
            print("\nAlunos matriculados:")
            for m, n in alunos.items():
                print(f"{m}: {n}")
        else:
            print("Nenhum aluno matriculado.")
    elif opcao == "4":
        matricula = input("Matrícula para buscar: ")
        print(f"Aluno: {alunos.get(matricula, 'Não encontrado.')}")
    elif opcao == "5":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida.")
