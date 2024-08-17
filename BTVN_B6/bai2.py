def tranpose (matrix : list, a : int, b : int) -> list:
    for i in range(a):
        for j in range(b):
            print(matrix[j][i], end=' ')
        print()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)
m = len(matrix[0])
(tranpose(matrix, n, m))