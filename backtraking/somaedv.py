def soma_recursiva(arr):
    """Função recursiva para calcular a soma dos elementos do vetor."""
    if len(arr) == 0:
        return 0  # Caso base: soma de um vetor vazio é zero
    else:
        return arr[0] + soma_recursiva(arr[1:])  # Soma o primeiro elemento e chama a função para o restante do vetor

# Exemplo de Teste
arr_exemplo = [1, 2, 3, 4, 5]
print(soma_recursiva(arr_exemplo))  # Saída: 15