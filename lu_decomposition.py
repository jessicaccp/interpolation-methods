from decimal import Decimal, Context, setcontext, DivisionByZero, Underflow, Overflow


def lu_decomposition(A, b):
    """TODO
    
    Arguments:
        A {[type]} -- [description]
        b {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """

    setcontext(Context(traps=[DivisionByZero, Underflow, Overflow]))
    # Número de linhas e colunas da matriz A
    n = len(A)

    # Cria uma matriz L de tamanho nxn e uma matriz U que recebe o conteúdo da matriz A
    L = [[Decimal(0.0) for _ in range(n)] for _ in range(n)]
    U = list(map(list, A))

    # Faz a fatoração, alterando os valores de L e U
    for pivot in range(n):
        L[pivot][pivot] = Decimal(1.0)
        for row in range(pivot + 1, n):
            L[row][pivot] = U[row][pivot] / U[pivot][pivot]
            for column in range(pivot, n):
                U[row][column] -= L[row][pivot] * U[pivot][column]

    x = [Decimal(0.0) for i in range(n)]
    y = [Decimal(0.0) for i in range(n)]

    # Resolve L . y = b
    for row in range(n):
        for column in range(n):
            if row == column:
                y[row] += b[row]
                break
            y[row] -= L[row][column] * y[column]

    # Resolve U . x = y
    for row in range(n - 1, -1, -1):
        for column in range(n - 1, -1, -1):
            if row == column:
                x[row] += y[row]
                x[row] /= U[row][column]
                break
            x[row] -= U[row][column] * x[column]

    # print()
    # print([[float(A[i][j]) for j in range(n)] for i in range(n)])
    # print([[float(L[i][j]) for j in range(n)] for i in range(n)])
    # print([[float(U[i][j]) for j in range(n)] for i in range(n)])
    # print([float(a) for a in y])
    # print([float(a) for a in x])

    return x
