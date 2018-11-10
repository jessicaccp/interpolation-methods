def lagrange(x, y):
    """
    lagrange Interpolação de lagrange
    
    [description] TODO
    
    Args:
        x (list): Os valores de x
        y (list): Os valores de p(x)
    
    Returns:
        [Decimal]: [description] TODO
    """
    n = len(x)
    midpoint = x[0] + ((x[n-1] - x[0]) * 0.5)
    
    difference = 10000
    i0, i1 = (None, None)
    for i in range(1, n-1):
        if abs(midpoint - x[i]) < difference:
            if midpoint - x[i] < 0:
                i0, i1 = i, i-1
            else:
                i0, i1 = i, i+1
            
            difference = abs(midpoint - x[i])
    factor1 = factor2 = None
    try:
        factor1 = y[i0]*((midpoint - x[i1]) / (x[i0] - x[i1]))
        factor2 = y[i1]*((midpoint - x[i0]) / (x[i1] - x[i0]))
    except ZeroDivisionError:
        print('Check the interpolation, catch division by Zero')

    p = factor1 + factor2

    return p