# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import warnings
from Vertex import Vertex
from Sudoku import Sudoku
from AdjacencyMatrix import AdjacencyMatrix
from SudokuHelper import SudokuHelper
warnings.filterwarnings("ignore")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 40, 421, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.SudokuToSolve = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.SudokuToSolve.setContentsMargins(0, 0, 0, 0)
        self.SudokuToSolve.setObjectName("SudokuToSolve")

        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.SudokuToSolve.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.Dimension = QtWidgets.QGroupBox(self.centralwidget)
        self.Dimension.setGeometry(QtCore.QRect(20, 30, 191, 181))

        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(15)

        self.Dimension.setFont(font)
        self.Dimension.setObjectName("Dimension")
        self.Btn16x16 = QtWidgets.QRadioButton(self.Dimension)
        self.Btn16x16.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.Btn16x16.setFont(font)
        self.Btn16x16.setObjectName("Btn16x16")

        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.Btn16x16)
        self.Btn4x4 = QtWidgets.QRadioButton(self.Dimension)
        self.Btn4x4.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.Btn4x4.setFont(font)
        self.Btn4x4.setObjectName("Btn4x4")
        self.buttonGroup.addButton(self.Btn4x4)
        self.Btn9x9 = QtWidgets.QRadioButton(self.Dimension)
        self.Btn9x9.setGeometry(QtCore.QRect(20, 90, 91, 31))
        self.Btn9x9.setFont(font)
        self.Btn9x9.setObjectName("Btn9x9")

        self.buttonGroup.addButton(self.Btn9x9)
        self.Difficulty = QtWidgets.QGroupBox(self.centralwidget)
        self.Difficulty.setGeometry(QtCore.QRect(20, 240, 191, 181))
        self.Difficulty.setFont(font)
        self.Difficulty.setObjectName("Difficulty")
        self.BtnImpossible = QtWidgets.QRadioButton(self.Difficulty)
        self.BtnImpossible.setGeometry(QtCore.QRect(20, 130, 141, 31))
        self.BtnImpossible.setFont(font)
        self.BtnImpossible.setObjectName("BtnImpossible")
        self.BtnSimple = QtWidgets.QRadioButton(self.Difficulty)
        self.BtnSimple.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.BtnSimple.setFont(font)
        self.BtnSimple.setObjectName("BtnSimple")
        self.BtnHard = QtWidgets.QRadioButton(self.Difficulty)
        self.BtnHard.setGeometry(QtCore.QRect(20, 90, 91, 31))
        self.BtnHard.setFont(font)
        self.BtnHard.setObjectName("BtnHard")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(660, 40, 421, 381))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.SudokuSolved = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.SudokuSolved.setContentsMargins(0, 0, 0, 0)
        self.SudokuSolved.setObjectName("SudokuSolved")

        self.tableWidget_2 = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)

        self.SudokuSolved.addWidget(self.tableWidget_2, 0, 0, 1, 1)
        self.OutputText = QtWidgets.QTextEdit(self.centralwidget)
        self.OutputText.setGeometry(QtCore.QRect(20, 510, 1061, 181))
        self.OutputText.setObjectName("OutputText")
        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(20, 490, 81, 21))
        self.OutputLabel.setFont(font)
        self.OutputLabel.setObjectName("OutputLabel")
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setGeometry(QtCore.QRect(20, 440, 151, 31))

        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setObjectName("StatusLabel")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(660, 440, 421, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.StatusText = QtWidgets.QLabel(self.centralwidget)
        self.StatusText.setGeometry(QtCore.QRect(230, 440, 171, 31))
        self.StatusText.setFont(font)
        self.StatusText.setObjectName("StatusText")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdd_file = QtWidgets.QMenu(self.menubar)
        self.menuAdd_file.setObjectName("menuAdd_file")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.openGUIFile = QtWidgets.QAction(MainWindow)
        self.openGUIFile.setObjectName("openGUIFile")
        self.openAdjacencyMatrix = QtWidgets.QAction(MainWindow)
        self.openAdjacencyMatrix.setObjectName("openAdjacencyMatrix")
        self.openSudokuHelper = QtWidgets.QAction(MainWindow)
        self.openSudokuHelper.setObjectName("openSudokuHelper")
        self.openVertex = QtWidgets.QAction(MainWindow)
        self.openVertex.setObjectName("openVertex")
        self.openSudoku = QtWidgets.QAction(MainWindow)
        self.openSudoku.setObjectName("openSudoku")
        self.openDriver = QtWidgets.QAction(MainWindow)
        self.openDriver.setObjectName("openDriver")
        self.menuAdd_file.addAction(self.openGUIFile)
        self.menuAdd_file.addSeparator()
        self.menuAdd_file.addAction(self.openAdjacencyMatrix)
        self.menuAdd_file.addAction(self.openSudokuHelper)
        self.menuAdd_file.addAction(self.openVertex)
        self.menuAdd_file.addAction(self.openSudoku)
        self.menuAdd_file.addAction(self.openDriver)
        self.menubar.addAction(self.menuAdd_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Listeners

        self.Btn4x4.clicked.connect(self.dimensionOrDifficultyChanged)
        self.Btn9x9.clicked.connect(self.dimensionOrDifficultyChanged)
        self.Btn16x16.clicked.connect(self.dimensionOrDifficultyChanged)

        self.BtnSimple.clicked.connect(self.dimensionOrDifficultyChanged)
        self.BtnHard.clicked.connect(self.dimensionOrDifficultyChanged)
        self.BtnImpossible.clicked.connect(self.dimensionOrDifficultyChanged)

    # User input functions

    def getDimensionFolder(self, dimension):
        if(dimension == "1" or dimension == "4x4"):
            dimensionFolder = "4x4"
        elif (dimension == "2" or dimension == "9x9"):
            dimensionFolder = "9x9"
        else:
            dimensionFolder = "16x16"
        return dimensionFolder

    def getFileName(self, weight):
        if(weight == "1" or weight == "Easy"):
            fileName = "Easy"
        elif (weight == "2" or weight == "Hard"):
            fileName = "Hard"
        else:
            fileName = "Impossible"
        return fileName
        

    # Solving Sudoku

    def solveSudoku(self, dimension, weight):
        self.filePath = ("Sudoku/" + self.getDimensionFolder(dimension) + "/" + self.getFileName(weight) + ".csv")

        # Instanciramo prazni sudoku i citamo ga iz .CSV datoteke
        self.sud = SudokuHelper.getSudokuFromCSV(self.filePath)

        self.sud.printSudoku(self.SudokuToSolve)

        # Popunjavamo matricu susjedstva sudokua
        self.sudFill = SudokuHelper.fillAdjacencyMatrix(self.sud)

        # Rjesavamo sudoku i ispisujemo ga
        self.sudFill.solveByLogic(self.OutputText, self.SudokuSolved)

        #dohvaćam riješeni sudoku
        self.sudSolved = self.sudFill.getSudoku()
        self.dim = self.sudFill.getDimension()
   
        #crtanje grafa za sudoku
        if(self.dim <= 9):
            SudokuHelper.drawGraph(self.sudSolved, self.dim)
        else:
            print("\nGraph for sudoku 16x16 is too large for visual representation!\n")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Dimension.setTitle(_translate("MainWindow", "Dimension:"))
        self.Btn16x16.setText(_translate("MainWindow", "16x16"))
        self.Btn4x4.setText(_translate("MainWindow", "4x4"))
        self.Btn9x9.setText(_translate("MainWindow", "9x9"))
        self.Difficulty.setTitle(_translate("MainWindow", "Difficulty:"))
        self.BtnImpossible.setText(_translate("MainWindow", "Impossible"))
        self.BtnSimple.setText(_translate("MainWindow", "Simple"))
        self.BtnHard.setText(_translate("MainWindow", "Hard"))
        self.OutputLabel.setText(_translate("MainWindow", "Output"))
        self.StatusLabel.setText(_translate("MainWindow", "Current Status: "))
        self.StatusText.setText(_translate("MainWindow", "SOLVED!"))
        self.menuAdd_file.setTitle(_translate("MainWindow", "Open File"))
        self.openGUIFile.setText(_translate("MainWindow", "GUI File"))
        self.openAdjacencyMatrix.setText(_translate("MainWindow", "Adjacency Matrix"))
        self.openSudokuHelper.setText(_translate("MainWindow", "SudokuHelper"))
        self.openVertex.setText(_translate("MainWindow", "Vertex"))
        self.openSudoku.setText(_translate("MainWindow", "Sudoku"))
        self.openDriver.setText(_translate("MainWindow", "Driver"))

    def checkDifficultyAndDimension(self):
        if((self.Btn4x4.isChecked() == True or self.Btn9x9.isChecked() == True or self.Btn16x16.isChecked() == True)
        and (self.BtnSimple.isChecked() == True or self.BtnHard.isChecked() == True or self.BtnImpossible.isChecked() == True)):
            return True
        return False


    def dimensionOrDifficultyChanged(self):
        if(self.checkDifficultyAndDimension()):
            dimension = self.getCheckedDimension()
            difficulty = self.getCheckedDifficulty()
            self.solveSudoku(dimension, difficulty)

    def getCheckedDimension(self):
        if(self.Btn4x4.isChecked() == True):
            return "4x4"
        elif(self.Btn9x9.isChecked() == True):
            return "9x9"
        elif(self.Btn16x16.isChecked() == True):
            return "16x16" 
        else:
            return "None"
    
    def getCheckedDifficulty(self):
        if(self.BtnSimple.isChecked() == True):
            return "Easy"
        elif(self.BtnHard.isChecked() == True):
            return "Hard"
        elif(self.BtnImpossible.isChecked() == True):
            return "Impossible" 
        else:
            return "None"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
