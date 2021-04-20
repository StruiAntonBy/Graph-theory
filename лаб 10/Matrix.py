class Matrix:

    def __init__(self):
        self.Array = []
        self.line = 0
        self.column = 0

    def initializeMatrix(self, line, column):
        self.column = column
        self.line = line
        for i in range(0, line):
            tmp = [0 for x in range(0, column)]
            self.Array.append(tmp)

    def copyMatrix(self):
        CopyMatrix = Matrix()
        CopyMatrix.initializeMatrix(self.line, self.column)
        for i in range(0, self.line):
            for j in range(0, self.column):
                CopyMatrix.Array[i][j] = self.Array[i][j]
        return CopyMatrix

    def setMatrixFile(self, FileName):
        file = open(FileName, 'r')
        for string in file:
            string = [x for x in string]
            buffer = ''
            line = []
            for element in string:
                if element == ' ' or element == '\n':
                    if buffer != '':
                        line.append(int(buffer))
                        buffer = ''
                elif element == '$':
                    line.append(element)
                else:
                    buffer = buffer + element
            if buffer != '':
                line.append(int(buffer))
            self.Array.append(line)
        self.line = len(self.Array)
        self.column = len(self.Array[0])

    def show_matrix(self):
        for line in self.Array:
            for x in line:
                print(x, end=' ')
            print()