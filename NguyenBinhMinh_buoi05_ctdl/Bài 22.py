def get_diagonal(matrix):
    return tuple(matrix[i][i] for i in range(min(len(matrix), len(matrix[0]))))
input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)