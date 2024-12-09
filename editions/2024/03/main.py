import re

file_contents = open('editions/2024/03/input.txt').read()

mul_regex = r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))'
mul_string = re.findall(mul_regex, file_contents)

mul_enabled = True
mul_enabled_sum = 0
mul_disabled_sum = 0
for mul in mul_string:
    if mul == 'do()':
        mul_enabled = True
        continue
    if mul == 'don\'t()':
        mul_enabled = False
        continue

    mul = mul[4:-1]
    a, b = map(int, mul.split(','))
    if mul_enabled:
        mul_enabled_sum += a * b
    else:
        mul_disabled_sum += a * b

print(f"Part 1: {mul_enabled_sum + mul_disabled_sum}")
print(f"Part 2: {mul_enabled_sum}")
