from tabulate import tabulate
from fractions import Fraction
# def printMatrix(matrix:list):
#     """
#     Esta funcion acepta solamente matrices como parametro

#     Busca imprimir la matriz de la mejor forma posible
#     """

#     print(tabulate(matrix, tablefmt="github"))
#     print("\n")

def printMatrix(matrix: list):
    """
    Esta función acepta solamente matrices como parámetro.
    
    Busca imprimir la matriz de la mejor forma posible. Si as_fraction es True,
    imprime los elementos de la matriz como fracciones.
    """
    matrix2 = matrix
    matrix2 = [[Fraction(element) for element in row] for row in matrix]

    print(tabulate(matrix2, tablefmt="github"))
    print("\n")    