import re

file_contents = open('editions/2024/04/input.txt').read()

matrix = []
for line in file_contents.split('\n'):
    matrix.append(list(line))

def part_1():
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

    print(f"Part 1: {xmas_count}")

def part_2():
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

    print(f"Part 2: {xmas_count}")

part_1()
part_2()
