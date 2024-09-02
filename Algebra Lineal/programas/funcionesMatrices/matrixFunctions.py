from funcionesMatrices.printing import printMatrix
from funcionesMatrices.reemplazar import alternarFilas

def multiplyRow(row:list, multiply):
    """Esta funcion lo que hace es muiltiplicar una fila: {row} por el segundo parametro {multiply}"""

    for index in range(len(row)):
        row[index] *= multiply

    return row

def OperateRows(rowFrom:list , rowAuxiliar:list, operation:bool) -> list:
    """
    \n operation:bool -> true: sumar , false: restar
    \nNOTE: AMBAS FILAS TIENEN QUE TENER EL MISMO TAMANIO
    """

    if len(rowFrom) != len(rowAuxiliar):
        print("No se pudo realizar la operacion debido a que ambas filas no son del mismo tamanio")
        return rowFrom
    
    auxRow:list = rowAuxiliar[:]

    if not operation:
        auxRow =  (multiplyRow(rowAuxiliar[:], -1))
        

    for index in range(len(rowFrom)):
        
        rowFrom[index] = rowFrom[index] + auxRow[index]

    
    return rowFrom

def hacer_uno_el_pivote(matrix, row, column):  
    #COMPROBAR SI EL PIVOTE 1 ES 0:

    if matrix[row][column] == 0:
         
         for fila in range(row + 1, len(matrix)):
              if matrix[fila][column] != 0: 
                  alternarFilas(matrix, fila, row)
                  printMatrix(matrix)
                  break


    if matrix[row][column] != 1 and matrix[row][column] != 0:
            #Aqui lo unico qeu hace es imprimir la operacion que hace: en caso de la primera iteracion imprimiria:
            #F[0+1] => [1/matriz[0][0]] * F[0+1]
            print(f"F{row+1} => {1/matrix[row][column]}*F{row+1}")
            print("###################################") 
            # Aqui solo multiplica la fila por una fraccion para que el pivote sea 1 siempre :D
            matrix[row] = multiplyRow(matrix[row],(1/matrix[row][column])) 
            printMatrix(matrix) 
            
