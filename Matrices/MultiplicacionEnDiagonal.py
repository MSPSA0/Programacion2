def printMatrix(matrix) -> None:
    for i in range(len(matrix)):
        print(matrix[i])

filas: int = 6
columnas: int = 6
matriz: list = []
producto: int = 1

for i in range(filas):
    matriz.append([0] * columnas)
    for j in range(columnas):
        matriz[i][j] = 1 + j + i * columnas

printMatrix(matriz)

for i in range(min(columnas, filas)):
    print(matriz[i][columnas - 1 - i], end='')
    producto *= matriz[i][columnas - 1 - i]
    if (i < min(filas, columnas) - 1):
        print(' * ', end='')

print(' = ' + str(producto), end='')
