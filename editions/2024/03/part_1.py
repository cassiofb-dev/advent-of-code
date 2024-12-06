import re

filename = 'editions/2024/03/input.txt'

file_contents = None
with open(filename) as file:
    file_contents = file.read()

mul_regex = r'mul\(\d+,\d+\)'
mul_string = re.findall(mul_regex, file_contents)

mul_sum = 0
for mul in mul_string:
    mul = mul[4:-1]
    a, b = map(int, mul.split(','))
    mul_sum += a * b

print(mul_sum)
