def printMatrix(matrix) -> None:
    for i in range(len(matrix)):
        print(matrix[i])

filas: int = 6
columnas: int = 6
matriz: list = []
suma: int = 0

for i in range(filas):
    matriz.append([0] * columnas)
    for j in range(columnas):
        matriz[i][j] = 1 + j + i * columnas

printMatrix(matriz)

for i in range(min(filas, columnas)):
    print(matriz[i][i], end='')
    suma += matriz[i][i]
    if (i < min(columnas, filas) - 1):
        print(' + ', end='')

print(' = ' + str(suma), end='')
