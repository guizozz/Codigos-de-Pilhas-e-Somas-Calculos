# Inicializa a lista vazia
lista = []

# Insere números no início da lista
numeros = [5, 10, 15, 20, 25]  # Exemplos de números
for numero in numeros:
    lista.insert(0, numero)  # Insere no início da lista

# Operações solicitadas
# Imprime o primeiro elemento
print("Primeiro elemento da lista:", lista[0])

# Imprime o último elemento
print("Último elemento da lista:", lista[-1])

# Imprime a lista completa
print("Lista completa:", lista)

# Retorna a quantidade de números na lista
print("Quantidade de números na lista:", len(lista))
