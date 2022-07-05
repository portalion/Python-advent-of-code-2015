#filename = "test.in"
filename = "data.in"

data = open(filename, 'r')

result = 0

for line in data:
    values = ['']
    for char in line:
        if char.isdigit():
            values[len(values) - 1] += char
        elif values[len(values) - 1] != '':
            values.append('')
    if values[len(values) - 1 ] == '':
        del values[len(values) - 1]

    for index, value in enumerate(values):
        values[index] = int(value)

    dimensions = [values[0] * values[1], values[0] * values[2], values[1] * values[2]]
    for value in dimensions:
        result += 2 * value
    result += min(dimensions)

print(result)