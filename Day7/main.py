from numpy import ushort


class Gates:
    # Static variable which is dictionary of all 'Gates'
    variables = dict()

    def __init__(self, name, inputs):
        self.operation = ''
        self.inputs = []
        self.value = None
        variables[name] = self

        if 'NOT' in inputs:
            self.operation = 'NOT'
            self.inputs.append(inputs[1])
        elif inputs[1] == '->':
            self.operation = 'ASSIGN'
            self.inputs.append(inputs[0])
        else:
            self.inputs.append(inputs[0])
            self.inputs.append(inputs[2])
            self.operation = inputs[1]

    def __repr__(self):
        return '{ ' + self.operation + ' inputs: ' + str(self.inputs) + ' }'

    @staticmethod
    def getValueOfInput(value):
        if value.isdigit():
            return ushort(value)
        else:
            return variables[value].getValue()

    def getValue(self):
        if self.value is not None:
            return self.value

        match self.operation:
            case 'ASSIGN':
                self.value = self.getValueOfInput(self.inputs[0])
            case 'NOT':
                self.value = ~ self.getValueOfInput(self.inputs[0])
            case 'AND':
                self.value = self.getValueOfInput(self.inputs[0]) & self.getValueOfInput(self.inputs[1])
            case 'OR':
                self.value = self.getValueOfInput(self.inputs[0]) | self.getValueOfInput(self.inputs[1])
            case 'LSHIFT':
                self.value = self.getValueOfInput(self.inputs[0]) << self.getValueOfInput(self.inputs[1])
            case 'RSHIFT':
                self.value = self.getValueOfInput(self.inputs[0]) >> self.getValueOfInput(self.inputs[1])
            case _:
                raise Exception('There is no operation named: ' + self.operation)
        return self.value


def getData():
    # filename = 'test.in'
    filename = 'data.in'
    return open(filename, 'r')


data = getData()
variables = Gates.variables

for line in data:
    line = line.strip()
    filtered = line.split(' ')
    Gates(filtered[-1], filtered)

valueOfA = variables['a'].getValue()

print('First part:', valueOfA)

for variable in variables:
    variables[variable].value = None

variables['b'].value = valueOfA
print('Second part:', variables['a'].getValue())
