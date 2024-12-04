import csv

filename = 'editions/2024/02/input.txt'

levels_matrix = []
with open(filename) as file:
    reader = csv.reader(
        file,
        delimiter=' ',
        skipinitialspace=True,
        quoting=csv.QUOTE_NONNUMERIC,
    )

    for row in reader:
        levels_matrix.append(row)

safe_reports = 0
for levels_row in levels_matrix:
    for attempt in range(-1, len(levels_row)):
        levels = levels_row.copy()

        if attempt != -1:
            levels.pop(attempt)

        level_deltas = []
        for level_index in range(len(levels) - 1):
            level_delta = levels[level_index + 1] - levels[level_index]
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
        break

print(safe_reports)
