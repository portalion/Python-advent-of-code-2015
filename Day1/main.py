filename = "test"
filename = "data"

data = open(filename, 'r')

for line in data:
    result = 0
    for char in line:
        if char == '(':
            result += 1
        else:
            result -= 1
    print(result)