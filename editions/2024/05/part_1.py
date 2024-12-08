filename = 'editions/2024/05/input.txt'

file_contents = None
with open(filename) as file:
    file_contents = file.read()

rules = []
lists = []
for line in file_contents.split('\n'):
    if "|" in line:
        rules.append([*map(int,line.split("|"))])
    if "," in line:
        lists.append([*map(int,line.split(","))])

middle_sun = 0
for list in lists:
    is_rule_broken = False
    for rule in rules:
        before_index = list.index(rule[0]) if rule[0] in list else -1
        after_index = list.index(rule[1]) if rule[1] in list else -1

        if before_index != -1 and after_index != -1 and before_index > after_index:
            is_rule_broken = True
            break

    if not is_rule_broken:
        middle_sun += list[len(list) // 2]

print(middle_sun)
