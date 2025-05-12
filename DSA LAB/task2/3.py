def rotate_matrix(matrix):
    N = len(matrix)
    
    for layer in range(N // 2):
        first = layer
        last = N - layer - 1
        
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)

for row in matrix:
    print(row)
