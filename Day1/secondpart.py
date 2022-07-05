#filename = "test.in"
filename = "data.in"

data = open(filename, 'r')

for line in data:
    result, position = 0, 1
    for char in line:
        if char == '(':
            result += 1
        else:
            result -= 1
        if result == -1:
            print(position)
            break
        position += 1
