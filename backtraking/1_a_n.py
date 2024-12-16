def elemento_faltante(arr, n):
    soma_esperada = n * (n + 1) // 2
    soma_atual = sum(arr)
    return soma_esperada - soma_atual

# Casos de teste
arr1 = [1, 2, 3, 5]
n1 = 5
print(f"Elemento faltante em {arr1} é {elemento_faltante(arr1, n1)}")
