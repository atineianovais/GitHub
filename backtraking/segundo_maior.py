def segundo_maior(arr):
    # Verifica se o array tem menos de 2 elementos
    if len(arr) < 2:
        return -1  # Se sim, retorna -1 pois não é possível encontrar o segundo maior
    
    # Inicializa as variáveis para armazenar o maior e o segundo maior elementos
    primeiro_maior = segundo_maior = float('-inf') ## 'float('-inf')' representa o menor valor possível em ponto flutuante, ou seja, menos infinito
    
    # Percorre cada elemento do array
    for i in range(len(arr)):
        # Se o elemento atual for maior que o maior elemento encontrado até agora
        if arr[i] > primeiro_maior:
            segundo_maior = primeiro_maior
            primeiro_maior = arr[i]
        # Se o elemento atual for maior que o segundo maior e diferente do maior
        elif arr[i] > segundo_maior and arr[i] != primeiro_maior:
            segundo_maior = arr[i]  # Atualiza o segundo maior elemento
    
    # Retorna o segundo maior elemento, ou -1 se não houver um segundo maior válido
    return segundo_maior if segundo_maior != float('-inf') else -1

# Casos de teste
arr1 = [12, 35, 1, 10, 34, 1]
print(f"O segundo maior elemento em {arr1} é {segundo_maior(arr1)}")  # Esperado: 34
