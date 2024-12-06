import re

filename = 'editions/2024/03/input.txt'

file_contents = None
with open(filename) as file:
    file_contents = file.read()

mul_regex = r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))'
mul_string = re.findall(mul_regex, file_contents)

mul_sum = 0
mul_enabled = True
for mul in mul_string:
    if mul == 'do()':
        mul_enabled = True
        continue
    if mul == 'don\'t()':
        mul_enabled = False
        continue

    if not mul_enabled:
        continue

    mul = mul[4:-1]
    a, b = map(int, mul.split(','))
    mul_sum += a * b

print(mul_sum)
