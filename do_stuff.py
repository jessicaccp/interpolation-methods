from gauss_seidel import gauss_seidel
from lagrange import lagrange
from lu_decomposition import lu_decomposition
from sort_results import sort_results
from gs_second_edition import gauss_seidel_se
from utils import progress_bar

from decimal import Decimal

class DoStuff:
    """Classe DoStuff de métodos estáticos
    
    Classe resposável por manipular a entrada de dados de acordo com cada método
    """
    
    @staticmethod
    def lu_decomposition():
        """
        lu_decomposition Método para manipular a entrada da decomposição L.U
        
        Este método recebe uma matrix quadrada do usuário e u vetor para fazer
        a decomposição L.U.
        """
        A1 = []
        b1 = []
        print('\n\n' + '-'*20 + ' L.U. Decomposition '  + '-'*20 + '\n\n')
        n = int(input("Enter the square matrix A dimension(n x n):\n"))
        assert n > 0, 'Matrix A dimension must be more than 0 (n > 0)'
        for i in range(n):
            A1.append(list(map(Decimal, input().split())))
            assert len(A1[i]) == n, 'This is a square matrix! Try again...'
        print('\nChecking dimensions of A...\n')
        progress_bar(30)
        print('\nOk, now enter the values of b vector of dimension ({} x 1):'.format(n))
        
        assert input() == '#', 'The input file format is wrong, see documentation'
        
        b1 = list(map(Decimal, input().split()))
        assert len(b1) == n, 'b first dimension must be ({} x 1), got {}'.format(n, len(b1))

        print('\nProcessing L.U. decomposition of A...\n')
        progress_bar(20)
        x1 = lu_decomposition(A1, b1)

        print('\nGot it!\n\nLet\'s check!\n')
        for i in range(n):
            print('x{} ='.format(i), x1[i])

    @staticmethod
    def lagrange():
        """
        lagrange Método para manipular a entrada do método Interpolador de Lagrange
        
        Este método recebe uma lista de x's e p(x)'s e calcula a interpolação
        """
        print('\n\n' + '-'*20 + ' Lagrange interpolation '  + '-'*20 + '\n\n')
        x = list(map(float, input("Enter the values of x:\n").split()))
        y = list(map(float, input("Enter the values of p(x):\n").split()))
        assert len(x) == len(y), 'Number of x\'s and p(x)\'s must match'

        print('\nProcessing Lagrange Interpolation...\n')
        progress_bar(20)
        ans = lagrange(x, y)
        print('\n\nans = {}\n\n'.format(ans))

    @staticmethod
    def gauss_seidel():
        """
        gauss_seidel Método para manipular a entrada do método Gauss-Seidel
        
        Este método recebe uma matrix quadrada do usuário e u vetor para aplicar
        o método de Gauss-Seidel
        """
        A1 = []
        b1 = []
        print('\n\n' + '-'*20 + ' Gauss-Seidel method '  + '-'*20 + '\n\n')
        n = int(input("Enter the square matrix A dimension(n x n):\n"))
        assert n > 0, 'Matrix A dimension must be more than 0 (n > 0)'
        for i in range(n):
            A1.append(list(map(Decimal, input().split())))
            assert len(A1[i]) == n, 'This is a square matrix! Try again...'
        print('\nChecking dimensions of A...\n')
        progress_bar(30)
        print('\nOk, now enter the values of b vector of dimension ({} x 1):'.format(n))
        
        assert input() == '#', 'The input file format is wrong, see documentation'
        
        b1 = list(map(Decimal, input().split()))
        assert len(b1) == n, 'b first dimension must be ({} x 1), got {}'.format(n, len(b1))

        print('\nProcessing Gauss-Seidel...\n')
        progress_bar(20)
        pass
        # X1 = GaussSeidel TODO

        print('\nGot it!\n\nLet\'s check!\n')
        # for i in range(n):
        #     print('x{} ='.format(i), x1[i])
