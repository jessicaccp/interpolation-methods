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
            L[row][pivot] = round(U[row][pivot] / U[pivot][pivot], 5)
            for column in range(pivot, n):
                U[row][column] -= round(L[row][pivot] * U[pivot][column], 5)
    
    x = [0.0 for i in range(n)]
    y = [0.0 for i in range(n)]

    # Resolve L . y = b
    for row in range(n):
        for column in range(n):
            if row == column:
                y[row] += b[row]
                break
            y[row] -= L[row][column] * b[column]

    # Resolve U . x = y
    for row in range(n - 1, -1, -1):
        for column in range(n - 1, -1, -1):
            if row == column:
                x[row] += y[row]
                x[row] /= U[row][column]
                break
            x[row] -= U[row][column] * x[column]

    # print(x)

    print()
    print(A)
    print(L)
    print(U)
    print(y)
    print(x)

    return x