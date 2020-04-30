# Nicolas Andrade Perdomo 20172020097


cuadrada = int(input("numero de filas y columnas: "))
matriz = [None] * cuadrada
for i in range(cuadrada):
    matriz[i] = [None] * cuadrada

for i in range(cuadrada):
    for j in range(cuadrada):
        print("[", i, "][", j, "]", end=" ")
        matriz[i][j] = int(input())

print(matriz)
x = 0
y = cuadrada
for z in range(cuadrada * cuadrada):
    for i in range(x, y):
        print(matriz[x][i])
    for i in range(x + 1, y):
        print(matriz[i][y - 1])
    for i in range(y - 2, x - 1, -1):
        print(matriz[y - 1][i])
    for i in range(y - 2, x, -1):
        print(matriz[i][x])
    x = x + 1
    y = y - 1
