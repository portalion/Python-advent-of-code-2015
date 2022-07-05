import functools

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

    values = sorted(values)

    result += 2 * values[0] + 2 * values[1]
    result += functools.reduce(lambda a,b : a*b, values)
print(result)