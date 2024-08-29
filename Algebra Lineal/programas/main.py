from funcionesMatrices.printing import printMatrix
from funcionesMatrices.reemplazar import reemplazarFila, alternarFilas
from funcionesMatrices.matrixFunctions import *
from enum import Enum

class Operacion(Enum):
    restar = False
    sumar = True

def main():
    
    matrix=[[ 4 ,0 ,4 ,2,3 ],
            [ 0 ,1 ,1 ,2,3 ],
            [ 0 ,4,0 ,7 ,6],
            [3,6,2,5,7]]
    printMatrix(matrix)
    try:
        pivoteoMax(matrix)

        print("##############################")
        print("resultados:")

        printMatrix(matrix)

        for x in range(len(matrix)):
            print(f"x{x+1} = {matrix[x][3]}")
    except:
        print("La matriz es indefinida")


      

def pivoteoMax(matrix):
    row:int = 0
    for column in range(len(matrix[0])- 1):
        
        if matrix[row][column] != 1:
            print("###################################")
            matrix[row] = multiplyRow(matrix[row],(1/matrix[row][column])) 
            printMatrix(matrix)

        # if matrix[row + 1][column] != 0:
        #     pass

        for fila in range(row + 1, len(matrix)):
            
            if matrix[fila][column] == 0: continue
            
            operation = False
            if matrix[fila][column] < 0: operation = True
            
            matrix[fila] = OperateRows(matrix[fila], multiplyRow(matrix[row][:],abs(matrix[fila][column])), operation ) 
            printMatrix(matrix)

        for filaArriba in range(row, 0, -1):
            # if row == 0: break
            
            operation = False
            if matrix[filaArriba - 1][column] < 0: operation = True

            matrix[filaArriba -1] = OperateRows(matrix[filaArriba -1],multiplyRow(matrix[row][:], abs(matrix[filaArriba -1][column])), operation)
            
            printMatrix(matrix)
            

        row += 1

main()