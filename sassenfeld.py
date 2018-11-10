from decimal import Decimal, Context, setcontext, DivisionByZero, Underflow, Overflow

setcontext(Context(traps=[DivisionByZero, Underflow, Overflow]))


def check_convergence(A):
    """Verifica convergêcia da matriz A
    
    Arguments:
        A {list(list)} -- Matriz
    
    Returns:
        Boolean -- True se o método converge, False senão
    """
    n = len(A)
    A_modified = list(map(list, A))
    B = [Decimal(0.0) for _ in range(n)]

    for row in range(n):
        for column in range(n):
            if row != column:
                B[row] += abs(A_modified[row][column])
        if A_modified[row][row] != 0:
            B[row] /= abs(A_modified[row][row])
        for rows in range(row + 1, n):
            A_modified[rows][row] *= B[row]

    return max(B) < 1


def sassenfeld(A):
    """Modifica a matriz de entrada para uma possível convergência do método
    
    Arguments:
        A {list(list)} -- Matriz
    
    Returns:
        list(list), None -- Retorna a matriz moficada se foi possível fazer a convergêcia, senão retorna None
    """
    n = len(A)

    if check_convergence(A):
        return A
    for a in range(n - 1):
        for b in range(a + 1, n):
            A[a], A[b] = A[b], A[a]
            if check_convergence(A):
                return A

            for c in range(n - 1):
                for d in range(c + 1, n):
                    for line in A:
                        line[c], line[d] = line[d], line[c]
                    if check_convergence(A):
                        return A
                    for line in A:
                        line[c], line[d] = line[d], line[c]

            A[a], A[b] = A[b], A[a]

    return None
