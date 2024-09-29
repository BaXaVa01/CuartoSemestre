def multiplicar_matrices(matriz_a, matriz_b):
    # Verificar que las matrices se puedan multiplicar
    filas_a = len(matriz_a)
    columnas_a = len(matriz_a[0])
    filas_b = len(matriz_b)
    columnas_b = len(matriz_b[0])

    if columnas_a != filas_b:
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

    # Crear una matriz resultado con el tamaño adecuado
    resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]

    # Realizar la multiplicación de matrices
    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_a):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado

# Ejemplo de uso
matriz_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_b = [
    [7, 8,2],
    [9, 10,2],
    [11, 12,2]
]

resultado = multiplicar_matrices(matriz_a, matriz_b)

# Mostrar el resultado
for fila in resultado:
    print(fila)
