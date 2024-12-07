filename = 'editions/2024/04/input.txt'

file_contents = None
with open(filename) as file:
    file_contents = file.read()

matrix = []
for line in file_contents.split('\n'):
    matrix.append(list(line))

xmas_count = 0
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        diagonal_a = matrix[i - 1][j - 1] + matrix[i][j] + matrix[i + 1][j + 1]
        diagonal_b = matrix[i - 1][j + 1] + matrix[i][j] + matrix[i + 1][j - 1]
        if diagonal_a != 'MAS' and diagonal_a != 'SAM':
            continue
        if diagonal_b != 'MAS' and diagonal_b != 'SAM':
            continue
        xmas_count += 1

print(xmas_count)
