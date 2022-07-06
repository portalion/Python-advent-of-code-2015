import re

def getData():
    # filename = 'test.in'
    filename = 'data.in'

    return open(filename, 'r')

def doFirstAction(line, light):
    if 'turn on' in line:
        return True
    elif 'turn off' in line:
        return False
    else:
        return not light

def doSecondAction(line, light):
    if 'turn on' in line:
        return light + 1
    elif 'turn off' in line:
        return 0 if light == 0 else light - 1
    else:
        return light + 2

def getAllLights(data, lights, doAction):
    result = 0

    for line in data:
        numbers = re.findall('[\d]+', line)
        numbers = [int(number) for number in numbers]
        for i in range(numbers[0], numbers[2] + 1):
            for j in range(numbers[1], numbers[3] + 1):
                lights[i][j] = doAction(line, lights[i][j])

    for row in lights:
        for light in row:
            result += int(light)
    return result

def firstPart():
    data = getData()
    SIZE = 1000
    lights = [ [False for i in range(SIZE)] for i in range(SIZE)]

    return getAllLights(data, lights, doFirstAction)


def secondPart():
    data = getData()
    SIZE = 1000
    lights = [ [0 for i in range(SIZE)] for i in range(SIZE)]

    return getAllLights(data, lights, doSecondAction)

print('First part:', firstPart())
print('Second part:', secondPart())
