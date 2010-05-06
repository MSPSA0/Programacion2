def printMatrix(matrix) -> None:
    for i in range(len(matrix)):
        print(matrix[i])

filas: int = 6
columnas: int = 6
matriz: list = []
producto: int = 0

for i in range(columnas):
    matriz.append([0] * filas)
    for j in range(filas):
        matriz[i][j] = 1 + j + i * filas

printMatrix(matriz)

for i in range(min(columnas, filas)):
    print(matriz[i][filas - 1 - i], end='')
    producto *= matriz[i][filas - 1 - i]
    if (i < min(columnas, filas) - 1):
        print(' * ', end='')

print(' = ' + str(producto), end='')
