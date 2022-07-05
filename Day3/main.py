#filename = 'test.in'
filename = 'data.in'

data = open(filename, 'r')


def getNewPosition(actual, move):
    first, second = actual
    match move:
        case '^':
            first -= 1
        case 'v':
            first += 1
        case '>':
            second += 1
        case '<':
            second -= 1
    return first, second


for line in data:
    actual = (0, 0)
    values = set()
    values.add(actual)

    for char in line:
        actual = getNewPosition(actual, char)
        if actual not in values:
            values.add(actual)
    print(len(values))
