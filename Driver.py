import warnings
from Vertex import Vertex
from Sudoku import Sudoku
from AdjacencyMatrix import AdjacencyMatrix
from SudokuHelper import SudokuHelper
warnings.filterwarnings("ignore")

def getDimensionFolder(dimension):
    if(dimension == "1" or dimension == "4x4"):
        dimensionFolder = "4x4"
    elif (dimension == "2" or dimension == "9x9"):
        dimensionFolder = "9x9"
    else:
        dimensionFolder = "16x16"
    return dimensionFolder

def getFileName(weight):
    if(weight == "1" or weight == "Easy"):
        fileName = "Easy"
    elif (weight == "2" or weight == "Hard"):
        fileName = "Hard"
    else:
        fileName = "Impossible"
    return fileName

def getFilePath(dimension, weight):
    filePath = ("Sudoku/" + getDimensionFolder(dimension) + "/" + getFileName(weight) + ".csv")
    return filePath
    

if __name__ == "__main__":
    listOfDimensions = ["4x4", "9x9", "16x16"]
    listOfWeights = ["Easy", "Hard", "Impossible"]
    possibleAnswers = ["1", "2", "3"]
    dimension = 1
    weight = 5
    while(dimension != "0" and weight != "0"):
        dimension = 1
        weight = 5
        print("\n(---------- Sudoku Solver ----------)\n\n")
        print("Type 0 to exit the program.\n\n")
        print("Select sudoku dimension:\n\n1) 4x4\n2) 9x9\n3) 16x16\n")
        dimension = input("-- Your choice: ")
        if (dimension == "0"):
            print("\nThanks for playing! :)")
            exit()
        elif (dimension in listOfDimensions or dimension in possibleAnswers):
            while(weight not in listOfWeights and weight not in possibleAnswers):
                print("\nSelected dimension: " + getDimensionFolder(dimension) + "\n")
                print("Select difficulty level:\n\n1) Easy\n2) Hard\n3) Impossible\n")
                weight = input("-- Your choice: ")
                if (weight == "0"):
                    print("\nThanks for playing! :)")
                    exit()
                elif(weight in listOfWeights or weight in possibleAnswers):
                    print("\nSelected sudoku:")
                    print("\nDimension: " + getDimensionFolder(dimension))
                    print("Difficulty: " + getFileName(weight) + "\n")
                    filePath = getFilePath(dimension, weight)
                    # Instanciramo prazni sudoku i citamo ga iz .CSV datoteke
                    sud = SudokuHelper.getSudokuFromCSV(filePath)

                    sud.printSudoku()

                    # Popunjavamo matricu susjedstva sudokua
                    sudFill = SudokuHelper.fillAdjacencyMatrix(sud)

                    # Rjesavamo sudoku i ispisujemo ga
                    sudFill.solveByLogic()

                    #dohvaćam riješeni sudoku
                    sudSolved = sudFill.getSudoku()
                    dim = sudFill.getDimension()
   
                    #crtanje grafa za sudoku
                    if(dim <= 9):
                        SudokuHelper.drawGraph(sudSolved, dim)
                    else:
                        print("\nGraph for sudoku 16x16 is too large for visual representation!\n")
                else:
                    print("\n→→→→→→→→→→ Error\n")
                    print("Input not recognized. Please input choice number or write full choice. (eg. 2 or Hard)\n")
                    print("→→→→→→→→→→ Error\n\n")
                    
        else:
            print("\n→→→→→→→→→→ Error\n")
            print("Input not recognized. Please input choice number or write full choice. (eg. 1 or 4x4)\n")
            print("→→→→→→→→→→ Error\n\n")
        if(weight == "0" or dimension == "0"):
            exit()
               
            
        
