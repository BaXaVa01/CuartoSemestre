def multiplyRow(row:list, multiply):

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
    