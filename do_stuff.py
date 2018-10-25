from gauss_seidel import gauss_seidel
from lagrange import lagrange
from lu_decomposition import lu_decomposition

def do():
    # Para ambos os sistemas, cria a matriz A, o vetor b e recebe os seus respectivos valores
    # Sistema 1
    A1 = []
    b1 = []
    samples = int(input("Enter number of samples: "))
    for i in range(samples):
        A1.append(input("Enter values of row %s in A1: " % str(i + 1)).split(" "))
    b1 = input("Enter values of b1: ").split(" ")

    # Sistema 2
    A2 = []
    b2 = []
    for i in range(samples):
        A2.append(input("Enter values of row %s in A2: " % str(i + 1)).split(" "))
    b2 = input("Enter values of b2: ").split(" ")

    # Recebe o valor da precisão
    eps = float(input("Enter precision: "))

    x1 = lu_decomposition(A1, b1)
    x2 = gauss_seidel(A2, b2, eps)
    f = lagrange(x1, x2)

    # to-do:
    #   calcular ponto central - onde se encontra a cidade
    #   calcular grau de poluição da cidade a partir do resultado de lagrange 