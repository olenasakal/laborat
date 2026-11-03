def swap(matrix):
    size = len(matrix)
    n = size // 2 
    
    new_matrix = [row[:] for row in matrix]
    
    for i in range(n):
        for j in range(n):
            new_matrix[i][j], new_matrix[i + n][j + n] = matrix[i + n][j + n], matrix[i][j]
            new_matrix[i][j + n], new_matrix[i + n][j] = matrix[i + n][j], matrix[i][j + n]
            
    return new_matrix

matrix_4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Початкова матриця:")
for row in matrix_4x4:
    print(row)

result = swap(matrix_4x4)

print("\nРезультат (блоки переставлені навхрест):")
for row in result:
    print(row)
