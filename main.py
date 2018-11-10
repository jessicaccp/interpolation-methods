from do_stuff import DoStuff
from decimal import Decimal

def main():
    DoStuff.lu_decomposition()
    assert input() == '##', 'The input file format is wrong, see documentation'
    DoStuff.gauss_seidel()
    assert input() == '##', 'The input file format is wrong, see documentation'
    DoStuff.lagrange()

if __name__ == '__main__':
    main()
