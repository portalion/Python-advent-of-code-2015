import hashlib

# filename = 'test.in'
filename = 'data.in'

data = open(filename, 'r')


def getNumberWithNZeros(line, n):
    i = 0
    done = True
    while done:
        tohash = line[0:-1] + str(i)
        hashed = hashlib.md5(tohash.encode())
        for j in range(n):
            if hashed.hexdigest()[j] != '0':
                done = False
        if done:
            return i
        i += 1
        done = True
    return i


for line in data:
    print('First part:', getNumberWithNZeros(line, 5))  # 117946
    print('Second part:', getNumberWithNZeros(line, 6))
