from decimal import Decimal, Context, setcontext, DivisionByZero, Underflow, Overflow

setcontext(Context(traps=[DivisionByZero, Underflow, Overflow]))


def check_convergence(A):
    """Verifica convergêcia da matriz A
    
    Arguments:
        A {list(list)} -- Matriz
    
    Returns:
        Boolean -- True se o método converge, False senão
    """

    # Número de linhas do vetor A
    n = len(A)
    # Inicializa A_modified e B
    A_modified = list(map(list, A))
    B = [Decimal(0.0) for _ in range(n)]

    # Coloca em B os valores beta calculados para o teste de convergência
    for row in range(n):
        for column in range(n):
            if row != column:
                B[row] += abs(A_modified[row][column])
        if A_modified[row][row] != 0:
            B[row] /= abs(A_modified[row][row])
        for rows in range(row + 1, n):
            A_modified[rows][row] *= B[row]

    return max(B) < 1


def sassenfeld(A, _b):
    """Modifica a matriz de entrada para uma possível convergência do método
    
    Arguments:
        A {list(list)} -- Matriz
    
    Returns:
        list(list), None -- Retorna a matriz moficada se foi possível fazer a convergêcia, senão retorna None
    """

    # Número de linhas do vetor A
    n = len(A)

    # Testa se a matriz original A já converge
    if check_convergence(A):
        return A, _b

    # Faz o teste de convergência trocando as linhas
    for a in range(n - 1):
        for b in range(a + 1, n):
            A[a], A[b] = A[b], A[a]
            _b[a], _b[b] = _b[b], _b[a]
            if check_convergence(A):
                return A, _b

            # Para cada linha trocada, troca todas as colunas e então aplica o teste de convergência
            for c in range(n - 1):
                for d in range(c + 1, n):
                    for line in A:
                        line[c], line[d] = line[d], line[c]
                    if check_convergence(A):
                        return A, _b
                    for line in A:
                        line[c], line[d] = line[d], line[c]

            A[a], A[b] = A[b], A[a]
            _b[a], _b[b] = _b[b], _b[a]

    return None, None
