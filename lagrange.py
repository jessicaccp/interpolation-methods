from decimal import Decimal, Context, setcontext, DivisionByZero, Underflow, Overflow

setcontext(Context(prec=5, traps=[DivisionByZero, Underflow, Overflow]))


def lagrange(x, y):
    """
    lagrange Interpolação de lagrange

    [description] TODO

    Args:
        x (list): Os valores de x
        y (list): Os valores de f(x)

    Returns:
        [Decimal]: [description] TODO
    """

    # Número de linhas do vetor x
    n = len(x)
    # Ponto central do rio que representa a localização da cidade
    midpoint = x[0] + ((x[n-1] - x[0]) * Decimal(0.5))

    # Inicializa a diferença entre os pontos com um alto valor
    difference = Decimal(10000)
    # Inicializa os pontos do intervalo a ser encontrado como vazios
    i0, i1 = (None, None)

    # Encontra o menor intervalo de pontos do vetor x com a menor diferença para o ponto central
    for i in range(1, n-1):
        if abs(midpoint - x[i]) < difference:
            if midpoint - x[i] < Decimal(0.0):
                i0, i1 = i, i-1
            else:
                i0, i1 = i, i+1

            difference = abs(midpoint - x[i])
    
    # Inicializa os fatores para o calculo da interpolação como vazios
    factor1 = factor2 = None

    # Calcula os fatores 1 e 2 para a soma que compõe o resultado da interpolação
    factor1 = y[i0] * ((midpoint - x[i1]) / (x[i0] - x[i1]))
    factor2 = y[i1] * ((midpoint - x[i0]) / (x[i1] - x[i0]))
    p = factor1 + factor2


    return p, midpoint
