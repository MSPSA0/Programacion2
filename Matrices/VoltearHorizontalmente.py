def printMatrix(matrix) -> None:
    for i in range(len(matrix)):
        print(matrix[i])

filas: int = 6
columnas: int = 6
matriz: list = []

for i in range(filas):
    matriz.append([0] * columnas)
    for j in range(columnas):
        matriz[i][j] = 1 + j + i * columnas

printMatrix(matriz)

for i in range(filas):
    for j in range(columnas // 2):
        k = columnas - j - 1
        v = matriz[i][j]
        matriz[i][j] = matriz[i][k]
        matriz[i][k] = v

print('\n')
printMatrix(matriz)
