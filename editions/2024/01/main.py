import csv

filename = 'editions/2024/01/input.txt'

list_a = []
list_b = []
with open('editions/2024/01/input.txt') as file:
    reader = csv.reader(file, delimiter=' ', skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        list_a.append(row[0])
        list_b.append(row[1])

list_a.sort()
list_b.sort()

distance = 0
similarity = 0
for i in range(len(list_a)):
    distance += abs(list_a[i] - list_b[i])
    number_a_count_in_list_b = list_b.count(list_a[i])
    similarity += list_a[i] * number_a_count_in_list_b

print(f"Part 1: {distance}")
print(f"Part 2: {similarity}")
