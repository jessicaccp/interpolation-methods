def lu_decomposition(A, b):
    # Número de linhas e colunas da matriz A
    n = len(A)
    
    # Cria uma matriz L de tamanho nxn e uma matriz U que recebe o conteúdo da matriz A
    L = [[0.0] * n for i in range(n)]
    U = list(map(list, A))

    # Faz a fatoração, alterando os valores de L e U
    for pivot in range(n):
        L[pivot][pivot] = 1
        for row in range(pivot + 1, n):
            L[row][pivot] = U[row][pivot] / U[pivot][pivot]
            for column in range(pivot, n):
                U[row][column] -= L[row][pivot] * U[pivot][column]
            
    return