import math
import numpy

class AdjacencyMatrix:

    def __init__(self, n):
        # Global variables
        # number of rows and columns in adjacency matrix
        self.n = n
        self.n_squared = int(n) * int(n)
        # numver of rows and columns of each submatrix
        self.k = math.sqrt(int(n))
        # number of submatrices
        self.broj_podmatrica_sudokua = 0
        # create an empty matrix n_squared x n_squared
        self.mainAdjacencyMatrix = [[0]*int(self.n_squared) for i in range(int(self.n_squared))]
    
    # Fill Adjacency matrix with "ones" where it is required (where row and column cannot be the same colour)
    def getAdjacencyMatrix(self):
        sudokuMatrix = self.generate_sudoku_matrix(int(self.n))
        redak = 0
        # for every row in sudoku matrix
        for red in sudokuMatrix:
            stupac = 0
            redMatrice = red
            # for every field in sudoku matrix
            for polje in red:
                brojac = 0
                # first field of every submatrix
                if(int(redak)%self.k == 0 and polje%self.k == 0):
                    self.broj_podmatrica_sudokua += 1
                    subMatrix = self.get_subMatrix(sudokuMatrix, redak, stupac)
                    self.connect_subMatrix(subMatrix)
                    # print("\nPodmatrica ", self.broj_podmatrica_sudokua, "\n", subMatrix)
                    
                stupacMatrix = self.dohvatiStupac(sudokuMatrix, stupac)
                # get every field in the same row
                for vrh in redMatrice:
                    # if the field has greater index than currently selected vertex put one in adjacency matrix
                    if(polje < vrh):
                        #print(polje-1, vrh-1)
                        self.mainAdjacencyMatrix[polje][vrh] = 1
                        self.mainAdjacencyMatrix[vrh][polje] = 1
                    # if the field has greater index than current column put one in adjacency matrix
                    if(polje < stupacMatrix[brojac]):
                        #print(polje-1, [stupacMatrix[brojac]])
                        self.mainAdjacencyMatrix[polje][stupacMatrix[brojac]] = 1
                        self.mainAdjacencyMatrix[stupacMatrix[brojac]][polje] = 1
                    brojac += 1
                stupac += 1
            redak += 1
        return self.mainAdjacencyMatrix
    
    
    # Return submatrix which starts in wanted row and column
    def get_subMatrix(self, sudokuMatrix, rowNumber, columnNumber):
        #print(rowNumber, columnNumber)
        #print(sudokuMatrix[rowNumber][columnNumber])
        subMatrix = []
        for row in range(int(self.k)):
            for field in range(int(self.k)):
                subMatrix.append(sudokuMatrix[rowNumber + row][columnNumber + field])
        #print("Submatrix: ", subMatrix)
        return subMatrix

    # Connect submatrix in adjacency matrix 
    def connect_subMatrix(self, subMatrix):
        for number1 in subMatrix:
            for number2 in subMatrix:
                if(number1 != number2):
                    self.mainAdjacencyMatrix[number1][number2] = 1
                    self.mainAdjacencyMatrix[number2][number1] = 1
    

    # Return wanted column from matrix
    def dohvatiStupac(self, matrix, column):
        return [row[column] for row in matrix]

    # Generate vertices of sudoku matrix and label them with numbers
    def generate_sudoku_matrix(self, n):
        mainMatrix = []
        vertexNumber = 0
        for red in range(0, n):
            subMatrix = []
            for polje in range(0, n):
                subMatrix.append(vertexNumber)
                vertexNumber += 1
            mainMatrix.append(subMatrix)
        return mainMatrix
            
    def save_matrix_to_csv(self, matrix):
        matrix_csv = open("matrica_susjedstva.csv", "w") #Adjacency Matrix folder
        for red in matrix:
            brojac = 0
            for polje in red:
                if(brojac < self.n_squared-1):
                    matrix_csv.write(str(polje) + ";")
                else:
                    matrix_csv.write(str(polje))
                brojac += 1
            matrix_csv.write("\n")
        matrix_csv.close()
            
    def printMatrix(self, tekst, matrix):
        print("\n", tekst)
        for red in matrix:
            print(red)

    def printDetails(self):
        if(int(self.n) < 25):
            self.printMatrix("\nAdjacencyMatrix:\n", self.mainAdjacencyMatrix)            
        else:
            print("\nMatrix is too large to print!")
        print("\nCreated sudoku contains", self.n_squared, " fields \n\nNumber of rows and columns: ", self.n, " \n\nNumber of submatrixes: ", self.broj_podmatrica_sudokua)


