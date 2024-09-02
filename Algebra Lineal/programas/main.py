from funcionesMatrices.printing import printMatrix
from funcionesMatrices.reemplazar import reemplazarFila, alternarFilas
from funcionesMatrices.matrixFunctions import *
import tkinter as tk
from tkinter import simpledialog
from enum import Enum
from fractions import Fraction


def main():
    
    matrix=[[ 0 ,0 ,1, 4 ],
            [ -2 ,2 ,7 , 5],
            [3, 6 ,3 ,6 ]]
            
    # matrix = obtener_matriz_desde_input() 
    printMatrix(matrix)
    try:
        pivoteoMax(matrix)

        print("##############################")
        print("resultados:")

        printMatrix(matrix)

        y = len(matrix[0])
        
        for x in range(len(matrix)):

            print(f"x{x+ 1} = {matrix[x][y - 1]}")

        
    except:
        print("La matriz es inconsistente")


def obtener_matriz_desde_input():
    root = tk.Tk()
    root.withdraw()  # Esconder la ventana principal

    input_text = simpledialog.askstring("Entrada de Matriz", "Pega aquí la matriz copiada desde Excel:")
    if input_text:
        filas = input_text.strip().split("\n")
        matriz = [list(map(Fraction ,fila.split())) for fila in filas]
        return matriz
    return None

def pivoteoMax(matrix):
    row:int = 0
    for column in range(len(matrix[0])- 1):
        
        

        # hay que comprobar si alguna fila es libre o free:
        # Para entender la siguiente piezxa de codigo:

        # Tanto {row} como {column} tienen siempre el mismo valor. Cuando se empieza a ejeutar ambos tienen [0][0]
        # Entonces comprobamos que la posicion [0][0] en la matriz sea distinta a  1 y a 0, porque si es 1 no es necesario sacarlo
        # Y en caso que fuera 0 daria un error catastrofico al dividir 0 entre cualquier numero
        # NOTA: HACE FALTA IMPLEMENTAR LO DE CAMBIAR FILAS EN CASO QUE LA DIAGONAL TENGA UN 0


        #Aqui seria bueno implemenar de un solo la logica para buscar si el pivote inicial es 0.
        hacer_uno_el_pivote(matrix, row, column)

        
        
        for fila in range(row + 1, len(matrix)):
            
            if matrix[fila][column] == 0: continue
            
            operation = False
            operacionString = "-"
            if matrix[fila][column] < 0: operation = True

            if operation: operacionString = " + "

            print(f"F{fila + 1}=> F{fila + 1}{operacionString}{abs(matrix[fila][column])}*F{row + 1} \n") 

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