#write a pp to reverse every kth row in a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 2
for i in range(0, len(matrix), k):
    matrix[i] = matrix[i][::-1]
print(matrix)