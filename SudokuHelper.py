import csv
import math
import networkx as nx
import matplotlib.pyplot as plt
from Vertex import Vertex
from Sudoku import Sudoku
from AdjacencyMatrix import AdjacencyMatrix

class SudokuHelper:

    @staticmethod
    def getSudokuFromCSV(file):
        sud = Sudoku()
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            index_i = 0
            for row in reader:
                subMatrix = []
                sud.addSubmatrix(subMatrix)
                index_j = 0
                for element in row:
                    m = int(element)
                    if (m == 0):
                        v = Vertex()
                        sud.addCell(v, index_i, index_j)
                    else:
                        v = Vertex(m)
                        sud.addCell(v, index_i, index_j)
                    index_j = index_j + 1
                index_i = index_i + 1
        sud.setDimension(index_i)
        subdim = int(math.sqrt(index_i))
        sud.setSubDimension(subdim)
        return sud

    def fillAdjacencyMatrix(sud):
        dim = sud.getDimension()
        am = AdjacencyMatrix(dim)
        fillAM = am.getAdjacencyMatrix()
        am.save_matrix_to_csv(fillAM)
        indexRow = 0
        indexColumn = 0
        counter_r = 0
        for row in fillAM:
            counter_c = 0
            indexRow = (counter_r) // dim
            indexColumn = (counter_r) % dim
            currentVertex = sud.getSudoku()[indexRow][indexColumn]
            for element in row:
                r = 0
                c = 0
                if (element == 1):
                    r = int((counter_c) / dim)
                    c = int((counter_c) % dim)
                    currentVertex.addNeighbour(sud.getSudoku()[r][c])
                counter_c = counter_c + 1
            counter_r = counter_r + 1
        return sud

    @staticmethod
    def createDict(dim):
        Y=100
        X=10
        pocetniX = 10
        pos = dict()
        key = 1
        for n in range(0,dim):
            Y= Y-10
            for j in range (0,dim):
                pos[key]= [X,Y]
                key = key + 1
                X = X + 10
            X = pocetniX
       
        return pos

    @staticmethod
    def drawGraph(sudoku, dim):
        pos = SudokuHelper.createDict(dim)
        #for i in pos:
            #print(pos[i])

        # read adjacency matrix and create network
        network = nx.Graph()
        fileName = "matrica_susjedstva.csv"
        with open(fileName, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for indexRow, row in enumerate(reader, start = 1):                
                for indexColumn, column in enumerate(row, start = 1):
                    if(indexColumn > indexRow and column == '1'):
                        startVertex = indexRow
                        endVertex = indexColumn
                        #print (startVertex, '-', endVertex)
                        network.add_edge(startVertex, endVertex)
        

        #DRAW
        colors = ["b","g","r","c","m","y","#b79aa4","w","#42f48f"]
        color_map = []
        labels = dict()
        
        k=1
        for row in sudoku:
            for item in row:
                labels[k]=item.getColor()
                k=k+1
        
        plt.figure(figsize=(16,16))
        
        nx.set_node_attributes(network, labels, 'labels')

        for i in network.nodes():
            color_map.append(colors[network.nodes[i]['labels']-1])
        
        nx.draw(network,pos,labels = labels, node_color = color_map, with_labels=True, font_size=10)
        
        nx.draw_networkx_edges(network, pos)
      
        plt.show()

