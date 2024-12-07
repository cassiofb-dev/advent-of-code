import re

filename = 'editions/2024/04/input.txt'

file_contents = None
with open(filename) as file:
    file_contents = file.read()

matrix = []
for line in file_contents.split('\n'):
    matrix.append(list(line))

horizontal_lines = []
for line in matrix:
    horizontal_lines.append(''.join(line))

vertical_lines = []
for i in range(len(matrix[0])):
    vertical_lines.append(''.join([line[i] for line in matrix]))

diagonal_lines = []
for i in range(-len(matrix[0]) + 1, len(matrix)):
    diagonal_line = []
    for j in range(max(len(matrix), len(matrix[0]))):
        if 0 <= i + j < len(matrix) and 0 <= j < len(matrix[0]):
            diagonal_line.append(matrix[i + j][j])
    diagonal_lines.append(''.join(diagonal_line))

    diagonal_line = []
    for j in range(max(len(matrix), len(matrix[0]))):
        if 0 <= i + j < len(matrix) and 0 <= j < len(matrix[0]):
            diagonal_line.append(matrix[i + j][len(matrix[0]) - j - 1])
    diagonal_lines.append(''.join(diagonal_line))

matrix_lines = horizontal_lines + vertical_lines + diagonal_lines

xmas_count = 0
xmas_regex = r'XMAS'
xmas_backward_regex = r'SAMX'
for line in matrix_lines:
    xmas_founds = re.findall(xmas_regex, line)
    xmas_founds += re.findall(xmas_backward_regex, line)
    xmas_count += len(xmas_founds)

print(xmas_count)
