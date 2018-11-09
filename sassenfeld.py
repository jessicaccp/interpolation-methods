from decimal import Decimal

def check_convergence(A):
    n = len(A)
    A_modified = list(map(list, A))
    B = [Decimal(0.0) for _ in range(n)]

    for row in range(n):
        for column in range(n):
            if row != column:
                B[row] += abs(A_modified[row][column])
        try:
            B[row] /= abs(A_modified[row][row])
        except:
            pass
        for rows in range(row + 1, n):
            A_modified[rows][row] *= B[row]

    if max(B) < 1:
        return True
    print(max(B))
    return False

def sassenfeld(A):
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

    return False