def recursive_sum(arr, n):
    """Função recursiva para calcular a soma dos elementos do vetor."""
    if n == 0:
        return 0  # Caso base: soma de zero elementos é zero
    else:
        return arr[n-1] + recursive_sum(arr, n-1)  # Soma o último elemento e chama a função para o restante

def recursive_average(arr):
    """Função para calcular a média dos elementos do vetor usando recursão."""
    n = len(arr)
    if n == 0:
        return 0  # Caso especial: média de um vetor vazio é zero
    total_sum = recursive_sum(arr, n)  # Calcula a soma total dos elementos usando a função recursiva
    return total_sum // n  # Retorna a média inteira dos elementos

# Exemplo
arr_example = [1, 2, 3, 4, 5]
print(recursive_average(arr_example))  # Saída: 3