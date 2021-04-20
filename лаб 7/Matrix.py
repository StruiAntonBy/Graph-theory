class Matrix:

    def __init__(self, FileName):
        file = open(FileName, 'r')
        self.Array = []
        for string in file:
            string = [x for x in string]
            buffer = ''
            line = []
            for element in string:
                if element == ' ' or element == '\n':
                    line.append(int(buffer))
                    buffer = ''
                else:
                    buffer = buffer+element
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