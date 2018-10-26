from decimal import Decimal

def sassenfeld(A):
    n = len(A)
    A_modified = list(map(list, A))
    B = [Decimal(0.0) for _ in range(n)]

    for row in range(n):
        for column in range(n):
            if row != column:
                B[row] += abs(A_modified[row][column])
        B[row] /= abs(A_modified[row][row])
        for rows in range(row + 1, n):
            A_modified[rows][row] *= B[row]

    if max(B) < 1:
        return A
    
    print("Não converge")
    while max(B) >= 1:
        pass

    # print()
    # print([[float(A[i][j]) for j in range(n)] for i in range(n)])
    # print([[float(A_modified[i][j]) for j in range(n)] for i in range(n)])
    # print([float(a) for a in B])