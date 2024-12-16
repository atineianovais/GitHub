def encontrar_lideres(arr):
    n = len(arr)
    lideres = []
    max_atual = arr[-1]
    
    # O último elemento é sempre um líder
    lideres.append(max_atual)
    
    # Percorrer o array de trás para frente
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_atual:
            max_atual = arr[i]
            lideres.append(max_atual)
    
    # Reverter a lista para apresentar os líderes na ordem correta
    lideres.reverse()
    return lideres

# Casos de teste
arr1 = [16, 17, 4, 3, 5, 2]
print(f"Líderes em {arr1} são {encontrar_lideres(arr1)}")