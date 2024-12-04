import csv

filename = 'editions/2024/01/input.txt'

list_a = []
list_b = []
with open(filename) as file:
    reader = csv.reader(file, delimiter=' ', skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        list_a.append(row[0])
        list_b.append(row[1])

list_a.sort()
list_b.sort()

distance = 0
for i in range(len(list_a)):
    distance += abs(list_a[i] - list_b[i])

print(distance)
