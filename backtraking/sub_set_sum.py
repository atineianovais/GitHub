# Imprimir todos os subconjuntos se existir pelo menos um subconjunto de _set[] 
# cuja soma seja igual à soma alvo fornecida
flag = False

def calculador_subconjunto_soma(i, n, _conjunto, soma_alvo, subconjunto):
    global flag # Utiliza a variável global 'flag' para manter o estado de existência de um subconjunto válido
    # Se soma_alvo é zero, então existe um subconjunto válido
    if soma_alvo == 0:
        # Imprime o subconjunto válido
        flag = True # flag é atualizado para True e a função retorna, interrompendo a recursão
        print("[", end=" ")
        for elemento in subconjunto:
            print(elemento, end=" ")
        print("]", end=" ")
        return

    if i == n:
        # Se i atingir n, isso significa que todos os elementos foram considerados. A função retorna sem fazer nada.
        return

    # Não considerando o elemento atual
    calculador_subconjunto_soma(i + 1, n, _conjunto, soma_alvo, subconjunto)

    # Considerar o elemento atual se ele for menor ou igual à soma_alvo
    if _conjunto[i] <= soma_alvo:
        # Adiciona o elemento atual ao subconjunto
        subconjunto.append(_conjunto[i])

        # Chamada recursiva considerando o elemento atual
        calculador_subconjunto_soma(i + 1, n, _conjunto, soma_alvo - _conjunto[i], subconjunto)

        # Remove o último elemento após a chamada recursiva para restaurar a configuração original do subconjunto
        subconjunto.pop()

# Código principal
if __name__ == "__main__":
    # Caso de teste 1
    conjunto_1 = [1, 2, 1]
    soma_1 = 3
    n_1 = len(conjunto_1)
    subconjunto_1 = []
    print("Saída 1:")
    calculador_subconjunto_soma(0, n_1, conjunto_1, soma_1, subconjunto_1)
    print()
    flag = False

    # Caso de teste 2
    conjunto_2 = [3, 34, 4, 12, 5, 2]
    soma_2 = 39
    n_2 = len(conjunto_2)
    subconjunto_2 = []
    print("Saída 2:")
    calculador_subconjunto_soma(0, n_2, conjunto_2, soma_2, subconjunto_2)
    print()
    flag = False
    
    # Caso de teste 3
    conjunto_3 = [3, 34, 4, 12, 5, 2]
    soma_3 = 100
    n_3 = len(conjunto_3)
    subconjunto_3 = []
    print("Saída 3:")
    calculador_subconjunto_soma(0, n_3, conjunto_3, soma_3, subconjunto_3)

    if not flag:
        print("Não existe tal subconjunto")
