from sassenfeld import sassenfeld

from decimal import Decimal, Context, setcontext, DivisionByZero, Underflow, Overflow

n = 0


def gauss_seidel(A, b, eps):
    global n
    setcontext(Context(traps=[DivisionByZero, Underflow, Overflow]))
    # Verifica se a matriz converge

    A_modified = sassenfeld(A)

    if A_modified is None:
        print('Convergence test failed')
        exit(0)

    n = len(A_modified)

    # Número de iterações máximas
    iter_max = 10000
    # Vetor inicial de x
    x = []
    # Vetor para os novos valores de x
    v = []

    # Inicializa com zero os vetores de x inicial e x atualizado do mesmo tamanho do vetor b
    for i in range(n):
        x.append(Decimal(0.0))
        v.append(Decimal(0.0))

    # Percorre todas as linhas da matriz
    for i in range(n):
        r = Decimal(1.0) / A_modified[i][i]

        # percorre todas colunas da matriz
        for j in range(n):
            if i != j:
                # Divide o valor dos elementos que não fazem parte da diagonal da
                # matriz pelo o valor da diagonal correspondente aquela linha
                A_modified[i][j] = A_modified[i][j] * r

        # Divide o elemento do vetor resposta pelo valor da diagonal da matriz
        # correspondente aquela linha
        b[i] *= r

    # Quantidade de iterações
    k = 0

    while True:
        # Inicializa a váriavel que recebe o calculo do critério de parada
        d = 0
        # Incrementa o número de iterações
        k += 1

        # Percorre todas as linhas da matriz
        for i in range(n):
            # Inicializa a soma como 0
            soma = 0

            # Percorre todas as colunas da matriz
            for j in range(n):
                # Se não for um elemento da diagonal principal soma o valor
                # do elemento multiplicado ao valor de x daquela linha a variavel soma
                if i != j:
                    # Se for a primeira linha da matriz, x0
                    if i == 0:
                        soma += A_modified[i][j] * x[j]
                    # Caso contrário, utiliza os valores de x já calculado
                    else:
                        soma += A_modified[i][j] * v[j]

            # Calcula o valor de x mais atualizado com relação aquela linha
            # e o valor de y da linha
            v[i] = b[i] - soma

        # Recebe o valor do critério de parada
        d = teste_parada(x, v)

        # A_modifiedtualiza o vetor x para os valores de x calculados na iteração
        for i in range(0, n):
            x[i] = v[i]

        # Verifica se d é menor ou igual que o eps
        if d <= eps:
            return x
        # Verifica se k é maior que o número máximo de iterações
        elif k >= iter_max:
            break

# Calcula o critério de parada


def teste_parada(x, v):
    global n

    # Valor do maior valor de x achado
    max_x = 0
    # Valor do maior valor achado entre a subtração do x da iteração atual com a passada
    max_norma = 0

    # Percorre o vetor
    for i in range(n):

        # Calcula o valor de x mais atualizado menos o anterior
        aux = abs(v[i] - x[i])

        # Verifica se a norma do valor atual de x é o maior armazenado
        if max_x < abs(v[i]):
            max_x = abs(v[i])

        # Verifica se o valor atual da norma da subtração é a maior
        if max_norma < aux:
            max_norma = aux

    return abs(max_norma / max_x)
