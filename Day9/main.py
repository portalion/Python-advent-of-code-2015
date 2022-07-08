def getData():
    # filename = 'test.in'
    filename = 'data.in'
    return open(filename, 'r')


def generateGraph():
    data = getData()

    vertices = set()

    edges = dict()

    for line in data:
        line = line.strip()
        line = line.split(' ')
        line.remove('to')
        line.remove('=')

        vertices.add(line[0])
        vertices.add(line[1])

        if line[0] not in edges.keys(): edges[line[0]] = dict()
        if line[1] not in edges.keys(): edges[line[1]] = dict()

        edges[line[0]][line[1]] = int(line[2])
        edges[line[1]][line[0]] = int(line[2])

    return vertices, edges


def generateAllPaths(vertices):
    result = []
    if len(vertices) == 1:
        result.append(vertices.copy())
        return result

    for vertex in vertices:
        temp = generateAllPaths([x for x in vertices if x != vertex])
        for arr in temp:
            arr.append(vertex)
            result.append(arr)
    return result

def getPathLength(path, edges):
    result = 0
    actual = path[0]
    for i in range(1, len(path)):
        result += edges[actual][path[i]]
        actual = path[i]
    return result

def printPath(path, edges):
    pathName = ''
    for town in path:
        pathName += town + ' -> '
    print(pathName[:-4], getPathLength(path, edges))



vertices, edges = generateGraph()
result = (getPathLength(generateAllPaths(vertices)[0], edges), 0)
for path in generateAllPaths(vertices):
    result = (min(getPathLength(path, edges), result[0]), max(getPathLength(path, edges), result[1]))

print('First part:', result[0])
print('Second part:', result[1])
