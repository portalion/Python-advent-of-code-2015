def getData():
    # filename = 'test.in'
    filename = 'data.in'
    return open(filename, 'r')


def getNextIteration(previous):
    result = []
    actual = previous[0]
    actualSum = 0
    for number in previous:
        if number == actual: actualSum += 1
        else:
            result.extend([actualSum, actual])
            actual = number
            actualSum = 1
    result.extend([actualSum, actual])
    return result


def getIteration(first, times):
    for i in range(times):
        first = getNextIteration(first)
    return first


data = getData()
for first in data:
    first = [int(x) for x in first]
    print('First part:',len(getIteration(first, 40)))
    print('Second part:',len(getIteration(first, 50)))