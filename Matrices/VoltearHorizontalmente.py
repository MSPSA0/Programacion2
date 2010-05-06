def printMatrix(matrix) -> None:
    for i in range(len(matrix)):
        print(matrix[i])

filas: int = 6
columnas: int = 6
matriz: list = []

for i in range(columnas):
    matriz.append([0] * filas)
    for j in range(filas):
        matriz[i][j] = 1 + j + i * filas

printMatrix(matriz)

for i in range(columnas):
    for j in range(filas // 2):
        k = filas - j - 1
        v = matriz[i][j]
        matriz[i][j] = matriz[i][k]
        matriz[i][k] = v

print('\n')
printMatrix(matriz)
