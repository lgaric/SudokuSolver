# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import warnings
import os
from pathlib import Path
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
        self.SolvingGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.SolvingGrid.setContentsMargins(0, 0, 0, 0)
        self.SolvingGrid.setObjectName("SolvingGrid")

        self.SudokuToSolve = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.SudokuToSolve.setObjectName("SudokuToSolve")
        self.SudokuToSolve.setColumnCount(9)
        self.SudokuToSolve.setRowCount(9)
        self.SolvingGrid.addWidget(self.SudokuToSolve, 0, 0, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(660, 40, 421, 381))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.SolvedGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.SolvedGrid.setContentsMargins(0, 0, 0, 0)
        self.SolvedGrid.setObjectName("SolvedGrid")

        self.SudokuSolved = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.SudokuSolved.setObjectName("tableWidget_2")
        self.SudokuSolved.setColumnCount(9)
        self.SudokuSolved.setRowCount(9)
        self.SolvedGrid.addWidget(self.SudokuSolved, 0, 0, 1, 1)

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

    def printSudoku(self):
        row = 1
        for arr in self.sud.cells:
            self.SudokuToSolve.insertRow(row)
            column = 1
            for v in arr:
                print(f"Boja: %s %s %s" % (row, column, v.getColor()))
                self.SudokuToSolve.setItem(row, column, QtWidgets.QTableWidgetItem(v.getColor()))
                column += 1
            row += 1
        

    # Solving Sudoku

    def solveSudoku(self, dimension, weight):
        
        current_older = Path(__file__).parent.absolute()
        path = ("Sudoku/" + self.getDimensionFolder(dimension) + "/" + self.getFileName(weight) + ".csv")
        self.filePath = os.path.join(current_older, path)

        # Read sudoku from .CSV file
        self.sud = SudokuHelper.getSudokuFromCSV(self.filePath)

        self.printSudoku()

        # Fill adjacency matrix
        self.sudFill = SudokuHelper.fillAdjacencyMatrix(self.sud)

<<<<<<< HEAD
        # Rjesavamo sudoku i ispisujemo ga
        self.sudFill.solveByLogic(self.OutputText)

        # dohvaćam riješeni sudoku
        self.sudSolved = self.sudFill.getSudoku()
        self.dim = self.sudFill.getDimension()
   
        # crtanje grafa za sudoku
=======
        # Solve sudoku by logic -> if not possible switch to backtracking algorithm
        self.sudFill.solveByLogic(self.OutputText, self.SudokuSolved)

        # Get solved sudoku
        self.sudSolved = self.sudFill.getSudoku()
        self.dim = self.sudFill.getDimension()
   
        # If sudoku dimensions are 4x4 or 9x9 draw graphical representation of sudoku
>>>>>>> fe9f273ef588d771ff9bb7b99256beb86cbea9fa
        if(self.dim <= 9):
            SudokuHelper.drawGraph(self.sudSolved, self.dim)
        else:
            self.OutputText.append("\nGraph for sudoku 16x16 is too large for visual representation!\n")

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
        if((self.Btn4x4.isChecked() or self.Btn9x9.isChecked() or self.Btn16x16.isChecked())
        and (self.BtnSimple.isChecked() or self.BtnHard.isChecked() or self.BtnImpossible.isChecked())):
            return True
        return False


    def dimensionOrDifficultyChanged(self):
        if self.checkDifficultyAndDimension():
            dimension = self.getCheckedDimension()
            difficulty = self.getCheckedDifficulty()
            self.solveSudoku(dimension, difficulty)

    def getCheckedDimension(self):
        if self.Btn4x4.isChecked():
            return "4x4"
        elif self.Btn9x9.isChecked():
            return "9x9"
        elif self.Btn16x16.isChecked():
            return "16x16" 
        else:
            return "None"
    
    def getCheckedDifficulty(self):
        if self.BtnSimple.isChecked():
            return "Easy"
        elif self.BtnHard.isChecked():
            return "Hard"
        elif self.BtnImpossible.isChecked():
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
