def getData():
    # filename = 'test.in'
    filename = 'data.in'
    return open(filename, 'r')


def firstPart(data):
    result = 0
    for line in data:
        line = line.strip()
        result += len(line)
        evaluated = eval(line)
        result -= len(evaluated)
    return result


def secondPart(data):
    result = 0
    for line in data:
        line = line.strip()
        result -= len(line)
        encoded = str(line.encode())[1:].replace('"', '\\"')
        # print(len(line), len(encoded), encoded)
        result += len(encoded)
    return result



data = getData()
print('First part:', firstPart(data))
data = getData()
print('Second part:', secondPart(data))
