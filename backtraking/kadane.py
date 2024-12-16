def kadane_algorithm(arr):
    # Inicializa as variáveis
    max_atual = max_global = arr[0]

    # Percorre o array a partir do segundo elemento
    for i in range(1, len(arr)):
        # Atualiza max_atual para o maior valor entre o elemento atual e a soma de max_atual com o elemento atual
        max_atual = max(arr[i], max_atual + arr[i])
        # Atualiza max_global se max_atual for maior
        if max_atual > max_global:
            max_global = max_atual

    return max_global

# Casos de teste
arr1 = [1, 2, 3, -2, 5]
print(f"A soma máxima do subarray em {arr1} é {kadane_algorithm(arr1)}")  # Esperado: 9
