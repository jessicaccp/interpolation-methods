def lagrange(x, y):
    n = len(x)
    midpoint = x[0] + ((x[n-1] - x[0]) / 2)
    
    diference = 10000
    for i in range(1, n-1):
        if abs(midpoint - x[i]) < diference:
            if midpoint - x[i] < 0:
                i0, i1 = i, i-1
            else:
                i0, i1 = i, i+1
            
            diference = abs(midpoint - x[i])
    
    factor1 = y[i0]*((midpoint - x[i1]) / (x[i0] - x[i1]))
    factor2 = y[i1]*((midpoint - x[i0]) / (x[i1] - x[i0]))

    p = factor1 + factor2

    return p