from tabulate import tabulate
from fractions import Fraction
def printMatrix(matrix:list, bool =False):
    """
    Esta funcion acepta solamente matrices como parametro

    Busca imprimir la matriz de la mejor forma posible
    """

    print(tabulate(matrix, tablefmt="github"))
    print("\n")

    