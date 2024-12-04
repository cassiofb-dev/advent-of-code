import csv

filename = 'editions/2024/02/input.txt'

report = []
safe_reports = 0
with open(filename) as file:
    reader = csv.reader(file, delimiter=' ', skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        level_deltas = []
        for level in range(len(row) - 1):
            level_delta = row[level + 1] - row[level]
            level_deltas.append(level_delta)

        if 0 in level_deltas:
            continue

        min_delta = min(level_deltas)
        max_delta = max(level_deltas)

        if abs(min_delta) > 3 or abs(max_delta) > 3:
            continue

        delta_signal = min_delta * max_delta
        if delta_signal < 0:
            continue

        safe_reports += 1

print(safe_reports)
