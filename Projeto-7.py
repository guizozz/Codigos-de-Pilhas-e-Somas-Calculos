# Inicializa a fila vazia
fila = []

# Leitura e armazenamento das informações de 5 clientes
for i in range(5):
    print(f"\nCadastro do {i+1}º cliente:")
    codigo = int(input("Código do cliente: "))
    idade = int(input("Idade do cliente: "))
    salario = float(input("Salário do cliente: "))
    fila.append({"codigo": codigo, "idade": idade, "salario": salario})

# Relatório contendo todos os dados dos clientes cadastrados
print("\nRelatório de clientes cadastrados:")
for cliente in fila:
    print(f"Código: {cliente['codigo']}, Idade: {cliente['idade']}, Salário: {cliente['salario']:.2f}")

# Mostrar o cliente que está na primeira posição da fila de atendimento
if fila:
    print("\nCliente na primeira posição da fila:")
    primeiro_cliente = fila[0]
    print(f"Código: {primeiro_cliente['codigo']}, Idade: {primeiro_cliente['idade']}, Salário: {primeiro_cliente['salario']:.2f}")

# Verificar se um cliente está cadastrado pelo código
codigo_consulta = int(input("\nDigite o código do cliente para consulta: "))
cliente_encontrado = None
for cliente in fila:
    if cliente["codigo"] == codigo_consulta:
        cliente_encontrado = cliente
        break

if cliente_encontrado:
    print("\nDados do cliente consultado:")
    print(f"Código: {cliente_encontrado['codigo']}, Idade: {cliente_encontrado['idade']}, Salário: {cliente_encontrado['salario']:.2f}")
else:
    print("\nCliente não cadastrado.")
