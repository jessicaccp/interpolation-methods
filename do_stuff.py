from gauss_seidel import gauss_seidel
from lagrange import lagrange
from lu_decomposition import lu_decomposition
from sort_results import sort_results
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
        print('\n\n' + '-'*20 + ' L.U. Decomposition ' + '-'*20 + '\n\n')
        n = int(input("Enter the square matrix A dimension(n x n):\n"))
        assert n > 0, 'Matrix A dimension must be more than 0 (n > 0)'
        print('\n\nEnter the matrix values:')
        print('For example, for a 3x3 matrix:')
        print('\n1 2 3\n4 5 6\n7 8 9\n\n')
        for i in range(n):
            A1.append(list(map(Decimal, input().split())))
            assert len(A1[i]) == n, 'This is a square matrix! Try again...'
        print('\nChecking dimensions of A...\n')
        progress_bar(30)
        print('\nOk, now enter the values of b vector of dimension ({} x 1):'.format(n))

        assert input() == '#', 'The input file format is wrong, see documentation'

        b1 = list(map(Decimal, input().split()))
        assert len(b1) == n, 'b first dimension must be ({} x 1), got {}'.format(
            n, len(b1))

        print('\nProcessing L.U. decomposition of A...\n')
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
        print('\n\n' + '-'*20 + ' Gauss-Seidel method ' + '-'*20 + '\n\n')
        for i in range(n):
            A2.append(list(map(Decimal, input().split())))
            assert len(A2[i]) == n, 'This is a square matrix! Try again...'
        print('\nChecking dimensions of A...\n')
        progress_bar(30)
        print('\nOk, now enter the values of b vector of dimension ({} x 1):'.format(n))

        assert input() == '#', 'The input file format is wrong, see documentation'

        b2 = list(map(Decimal, input().split()))
        assert len(b2) == n, 'b first dimension must be ({} x 1), got {}'.format(
            n, len(b2))
        assert input() == '##', 'The input file format is wrong, see documentation'
        print('\nOk, now enter the value of the error\n')
        error = Decimal(input())
        print('\nProcessing Gauss-Seidel...\n')
        progress_bar(20)
        X2 = gauss_seidel(A2, b2, error)

        print('\nGot it!\n\nLet\'s check!\n')
        for i in range(n):
            print('x{} ='.format(i), X2[i])

    @staticmethod
    def lagrange():
        print('\n\n' + '-'*20 + ' Lagrange interpolation method ' + '-'*20 + '\n\n')
        tuple_list = list(zip(X1, X2))

        sorted_tuple_list = list(zip(*sorted(tuple_list)))

        sorted_X1, sorted_X2 = sorted_tuple_list[0], sorted_tuple_list[1]

        print('Points with their calculated pollution')
        for x in zip(sorted_X1, sorted_X2):
            print('{}----->{}'.format(round(float(x[0]), 5), round(float(x[1]), 5)))

        print('\nProcessing the interpolation...\n')
        progress_bar(20)
        pollution, midpoint = lagrange(sorted_X1, sorted_X2)

        print('\nPoint of the city and its pollution')
        print('{}----->{}'.format(round(float(midpoint), 5), round(float(pollution), 5)))

