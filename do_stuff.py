from gauss_seidel import gauss_seidel
from lagrange import lagrange
from lu_decomposition import lu_decomposition
from utils import progress_bar

from decimal import Decimal, Context, setcontext, ROUND_UP

n = 0
X1, X2 = None, None


class DoStuff:
    """Classe DoStuff de métodos estáticos

    Classe resposável por manipular a entrada de dados de acordo com cada método
    """

    @staticmethod
    def lu_decomposition():
        global n, X1
        """
        lu_decomposition Método para manipular a entrada da decomposição L.U
        
        Este método recebe uma matrix quadrada do usuário e u vetor para fazer
        a decomposição L.U.
        """
        A1 = []
        b1 = []
        print('\n' + '-'*20 + ' L.U. Decomposition ' + '-'*20 + '\n')
        n = int(input())
        print("Reading the square matrix A1 ({} x {})...\n".format(n, n))
        assert n > 0, 'Matrix A dimension must be more than 0 (n > 0)'
        for i in range(n):
            A1.append(list(map(Decimal, input().split())))
            assert len(A1[i]) == n, 'This is a square matrix! Try again...'
        print('Checking dimensions of A1...\n')
        progress_bar(30)
        print('\nOk, now reading the values of b1 vector of dimension ({} x 1)...'.format(n))

        assert input() == '#', 'The input file format is wrong, see documentation'

        b1 = list(map(Decimal, input().split()))
        assert len(b1) == n, 'b1 first dimension must be ({} x 1), got {}'.format(
            n, len(b1))

        print('\nProcessing L.U. decomposition of A1...\n')
        progress_bar(20)
        X1 = lu_decomposition(A1, b1)

        print('\nGot it!\n\nLet\'s check!\n')
        for i in range(n):
            print('x{} ='.format(i), round(X1[i], 5))

    @staticmethod
    def gauss_seidel():
        global n, X2
        """
        gauss_seidel Método para manipular a entrada do método Gauss-Seidel
        
        Este método recebe uma matrix quadrada do usuário e u vetor para aplicar
        o método de Gauss-Seidel
        """
        A2 = []
        b2 = []
        print('\n' + '-'*20 + ' Gauss-Seidel method ' + '-'*20 + '\n')

        print("Reading the square matrix A2 ({} x {})...\n".format(n, n))

        for i in range(n):
            A2.append(list(map(Decimal, input().split())))
            assert len(A2[i]) == n, 'This is a square matrix! Try again...'
        print('Checking dimensions of A2...\n')
        progress_bar(30)
        print('\nOk, now reading the values of b2 vector of dimension ({} x 1)...'.format(n))

        assert input() == '#', 'The input file format is wrong, see documentation'

        b2 = list(map(Decimal, input().split()))
        assert len(b2) == n, 'b2 first dimension must be ({} x 1), got {}'.format(
            n, len(b2))
        assert input() == '##', 'The input file format is wrong, see documentation'
        print('\nOk, now reading the value of the epsilon...\n')
        eps = Decimal(input())
        print('Processing Gauss-Seidel...\n')
        progress_bar(20)
        X2 = gauss_seidel(A2, b2, eps)

        print('\nGot it!\n\nLet\'s check!\n')
        for i in range(n):
            print('x{} ='.format(i), round(X2[i], 5))

    @staticmethod
    def lagrange():
        print('\n' + '-'*20 + ' Lagrange interpolation method ' + '-'*20 + '\n')
        tuple_list = list(zip(X1, X2))

        sorted_tuple_list = list(zip(*sorted(tuple_list)))

        sorted_X1, sorted_X2 = sorted_tuple_list[0], sorted_tuple_list[1]

        print('Points with their calculated pollution:')
        for x in zip(sorted_X1, sorted_X2):
            print('{}\t-----> {}'.format(round(float(x[0]), 5), round(float(x[1]), 5)))

        print('\nProcessing the interpolation...\n')
        progress_bar(20)
        pollution, midpoint = lagrange(sorted_X1, sorted_X2)

        print('\nGot it!\n\nLet\'s check!\n')
        print('Point of the city and its pollution:')
        print('{}\t-----> {}\n'.format(round(float(midpoint), 5), round(float(pollution), 5)))

