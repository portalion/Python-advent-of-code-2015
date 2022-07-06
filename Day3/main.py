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

def firstPart(line):
    actual = (0, 0)
    values = set()
    values.add(actual)

    for char in line:
        actual = getNewPosition(actual, char)
        values.add(actual)

    return len(values)

def secondPart(line):
    santa = (0, 0)
    bot = (0, 0)
    values = set()
    values.add(santa)

    i = 0

    for char in line:
        if i % 2:
            santa = getNewPosition(santa, char)
            values.add(santa)
        else:
            bot = getNewPosition(bot, char)
            values.add(bot)
        i += 1
    return len(values)

#filename = 'test.in'
filename = 'data.in'

data = open(filename, 'r')

for line in data:
    print('First part: ', firstPart(line))
    print('Second part: ', secondPart(line))

