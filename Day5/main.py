import re

def haveTwoSameLetters(line):
    last = ''
    for char in line:
        if last == char:
            return True
        last = char
    return False


def haveVowel(line, number):
    VOWELS = [i for i in 'aeiou']
    sum = 0
    for char in line:
        if char in VOWELS:
            sum += 1
    return sum >= number


def containString(line):
    strings = ['ab', 'cd', 'pq', 'xy']
    for expression in strings:
        if expression in line:
            return True
    return False

def isNaughty(line):
    if not haveVowel(line, 3):
        return False
    elif not haveTwoSameLetters(line):
        return False
    elif containString(line):
        return False
    return True

def getData():
    # filename = 'test.in'
    filename = 'data.in'

    return open(filename, 'r')

def firstPart(data):
    result = 0
    for line in data:
        if isNaughty(line):
            result += 1
    return result

def withSpace(line):
    for char in line:
        expression = char + '.' + char
        if re.search(expression, line) is not None:
            return True
    return False

def twoTimes(line):
    last = ' '
    for char in line:
        expression = last + char + '.*' + last + char
        if re.search(expression, line) is not None:
            return True
        last = char
    return False

def secondPart(data):
    result = 0
    for line in data:
        if withSpace(line) and twoTimes(line):
            result += 1

    return result

print('first part:', firstPart(getData()))
print('second part:', secondPart(getData()))