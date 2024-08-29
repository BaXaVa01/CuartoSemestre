from funcionesMatrices.printing import printMatrix
from funcionesMatrices.reemplazar import reemplazarFila, alternarFilas
from funcionesMatrices.matrixFunctions import *
from enum import Enum

class Operacion(Enum):
    restar = False
    sumar = True



def main():
    
    matrix=[[ 4 ,3 ,4 ,2 ],
            [ 2 ,4 ,1 ,2 ],
            [ 4 ,2 ,5 ,7 ]]
    printMatrix(matrix)
    pivoteoMax(matrix)





def pivoteo(matrix):

    printMatrix(matrix)
    rowObjective = 0

    for fila in matrix:
        if fila[0] == 1: 
            rowObjective = fila[0]
            break

    if rowObjective != 0:
        alternarfilas(matrix, 0, rowObjective)

        for row in matrix:
            row = OperateRows(row, matrix[0], False)

    else:
        pass\
        
        #         printMatrix(matrix)
        # rowObjective = 0

        # for fila in matrix:
        #     if fila[0] == 1: 
        #         rowObjective = fila[0]
        #         break

        # if rowObjective != 0:
        #     alternarfilas(matrix, 0, rowObjective)
        #     printMatrix(matrix)

        #     for index in range(len(matrix)):
        #         if index == 0: continue
                
        #         operacion = Operacion.restar
        #         if matrix[index][0] < 0: operacion = Operacion.sumar
                
        #         matrix[index] = OperateRows(matrix[index], multiplyRow(matrix[0][:], matrix[index][0]), operacion.value )

        #         printMatrix(matrix)
        # else:
        # matrix[0] = multiplyRow(matrix[0], 1/(matrix[0][0]))     
        # printMatrix(matrix)

        
        # # pivoteo(matrix)
    
    printMatrix(matrix, True)

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
            
        
        row += 1

def pivote(matrix, ):
    pass
main()