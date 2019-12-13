from Vertex import Vertex

class Sudoku:

    def __init__(self):
        self.cells = []

    def setDimension(self, dim):
        self.dimension = dim

    def getDimension(self):
        return self.dimension

    def setSubDimension(self, dim):
        self.subdimension = dim

    def getSubDimension(self):
        return self.subdimension

    def addSubmatrix(self, subMatrix):
        self.cells.append(subMatrix)

    def getSudoku(self):
        return self.cells

    def addCell(self, v, x, y):
        self.cells[x].insert(y, v)

    def isSolved(self):
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[i])):
                if (self.cells[i][j].getColor() == 0):
                    return False
        return True

    def findUnassignedVertex(self):
        for x in range(0, self.dimension):
            for y in range(0, self.dimension):
                if self.cells[x][y].getColor() == 0:
                    v = self.cells[x][y]
                    return v
        return -1

    def isValid(self, v, c):
        for n in v.neighbours:
            if (n.getColor() == c):
                return False
        return True

    def solveByBacktracking(self):
        v = self.findUnassignedVertex()
        if v == -1:
            return True
        for c in range(1, self.dimension+1):
            if self.isValid(v, c):
                v.setColor(c)
                if self.solveByBacktracking():
                    return True
                v.setColor(0)
        return False

    def solveByLogic(self, OutputText):
        OutputText.append("\nSolving logically..")
        while not(self.isSolved()):
            colorFound = False
            for i in range(0, len(self.cells)):
                for j in range(0, len(self.cells[i])):
                    v = Vertex()
                    v = self.cells[i][j]
                    c = v.findColor(self.dimension)
                    if (c != 0 and v.isDone() == False):
                        v.setColor(c)
                        colorFound = True
            if (colorFound == False):
                OutputText.append("Cannot be solved by logic. Switching to backtracking recursion algorithm...")
                self.solveByBacktracking()
        
        OutputText.append("\nDone!")
        OutputText.append("---------------------")
        self.printSudoku()

    def printSudoku(self):
        row = 0
        for arr in self.cells:
            column = 0
            for v in arr:
                print(v.getColor(), end=" ")
            print(" ")
            #table.append(" ")

