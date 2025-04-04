# Inicializa a fila para armazenar os cursos
fila_cursos = []

# Leitura das informações de 5 cursos
for i in range(5):
    print(f"\nCadastro do {i+1}º curso:")
    codigo = int(input("Código do curso: "))
    vagas = int(input("Número de vagas: "))
    candidatos_masculino = int(input("Número de candidatos do sexo masculino: "))
    candidatos_feminino = int(input("Número de candidatos do sexo feminino: "))
    
    # Adiciona os dados do curso na fila
    fila_cursos.append({
        "codigo": codigo,
        "vagas": vagas,
        "candidatos_masculino": candidatos_masculino,
        "candidatos_feminino": candidatos_feminino
    })

# Calcula e imprime o número de candidatos por vaga para cada curso
print("\nRelatório: Número de candidatos por vaga por curso:")
for curso in fila_cursos:
    total_candidatos = curso["candidatos_masculino"] + curso["candidatos_feminino"]
    candidatos_por_vaga = total_candidatos / curso["vagas"] if curso["vagas"] > 0 else 0
    print(f"Código do curso: {curso['codigo']}, Candidatos por vaga: {candidatos_por_vaga:.2f}")

# Consultar um curso específico pelo código
codigo_consulta = int(input("\nDigite o código do curso para consulta: "))
curso_encontrado = None

# Busca pelo curso na fila
for curso in fila_cursos:
    if curso["codigo"] == codigo_consulta:
        curso_encontrado = curso
        break

# Exibe as informações do curso consultado ou mensagem de inexistência
if curso_encontrado:
    total_candidatos = curso_encontrado["candidatos_masculino"] + curso_encontrado["candidatos_feminino"]
    candidatos_por_vaga = total_candidatos / curso_encontrado["vagas"] if curso_encontrado["vagas"] > 0 else 0
    print(f"\nCurso encontrado!")
    print(f"Código do curso: {curso_encontrado['codigo']}")
    print(f"Vagas: {curso_encontrado['vagas']}")
    print(f"Candidatos por vaga: {candidatos_por_vaga:.2f}")
else:
    print("\nCURSO INEXISTENTE.")
