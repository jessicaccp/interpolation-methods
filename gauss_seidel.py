def gauss_seidel(n, A, b, eps, iter_max, ):
    # n é ordem da matriz
    x = []

    for i in range(1,n):
        r = 1/A[i][i]

        for j in range(1,n):
            if i != j:
                A[i][j] = A[i][j] * r

        b[i] = b[i] * r
        x[i] = b[i]      

    k = 0

    while True:
        k = k + 1
        
        for i in range (1,n):
            soma = 0

            for j in range(1,n):
                if i != j:
                    soma = soma + A[i][j] * x[j]

            v[i] = b[i] - soma
            x[i] = b[i] - soma 
        
        norma = calcula_norma(n,x,v)
        if norma <= eps or k >= iter_max:
            break

    return x

def calcula_norma(n, x, v):    
    