import re


def getData():
    # filename = 'test.in'
    filename = 'data.in'
    return open(filename, 'r')


def haveTwos(line):

    return len(re.findall(r'(.)\1', line)) >= 2


def haveLetter(line, letters):
    for letter in letters:
        if letter in line: return True
    return False


def isGood(line, letters):
    if haveLetter(line, letters): return False
    if not haveTwos(line): return False

    for i in range(ord('a'), ord('y')):
        if (chr(i) + chr(i + 1) + chr(i + 2)) in line: return True

    return False


def getNextChar(char):
    if char == 'z':
        raise Exception('Last letter')
    return chr(ord(char) + 1)


def generateNext(line):
    arr = list(line)
    index = -1
    while True:
        try:
            arr[index] = getNextChar(arr[index])
            break
        except:
            arr[index] = 'a'
            index -= 1
    return ''.join(arr)

data = getData()

for line in data:
    line = line.strip()
    while not isGood(line, ['i', 'o', 'l']):
        line = generateNext(line)
    print('First part:', line)
    line = generateNext(line)
    while not isGood(line, ['i', 'o', 'l']):
        line = generateNext(line)
    print('Second part:', line)