class Vertex:

    def __init__(self, c = 0):
        if (c == 0):
            self.color = 0
            self.done = False
        else:
            self.color = c
            self.done = True
        self.neighbours = []
    
    def addNeighbour(self, v):
        self.neighbours.append(v)

    def isDone(self):
        return self.done

    def getColor(self):
        return self.color

    def setColor(self, c):
        self.color = c
        self.done = True

    def findColor(self, colors):
        self.options = []
        for i in range(1, colors + 1):
            self.options.append(i)

        for n in self.neighbours:
            if (n.getColor() in self.options):
                self.options.remove(n.getColor())

        if (len(self.options) == 1):
            return self.options[0]

        return 0
