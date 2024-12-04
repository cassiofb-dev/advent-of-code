import csv

filename = 'editions/2024/01/input.txt'

list_a = []
list_b = []
with open(filename) as file:
    reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
    for row in reader:
        list_a.append(int(row[0]))
        list_b.append(int(row[1]))

similarity = 0
for i in range(len(list_a)):
    number_a_count_in_list_b = list_b.count(list_a[i])
    similarity += list_a[i] * number_a_count_in_list_b

print(similarity)
