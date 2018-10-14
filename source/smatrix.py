import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QInputDialog,
QPushButton, QLabel, QGridLayout, QDialog)

class Appl(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.startUI()
        self.linesArray = []
    def startUI(self):

        self.grid = QGridLayout()

        label = QLabel()
        label.setText('ordine di M: ')

        self.qle = QLineEdit()
      
        okBtn = QPushButton('Ok')
        okBtn.clicked.connect(lambda: self.showInputGrid())

        cancBtn= QPushButton('Cancel') 
        cancBtn.clicked.connect(lambda: self.qle.setText(('')))

        self.grid.setSpacing(10)

        self.grid.addWidget(label, 1,0)
        self.grid.addWidget(self.qle, 1,1)
        self.grid.addWidget(okBtn, 2,1)
        self.grid.addWidget(cancBtn, 2,0)

        self.setLayout(self.grid)
  
        self.setGeometry(300,300,100,200)
        self.setWindowTitle("Ordine(M)")
        
        self.show()

    def showInputGrid(self):

        self.d = QDialog(self)
    
        self.linesArray = []

        if self.qle.text() == '':
            self.grid.addWidget(QLabel('Inserisci un valore'), 3,0)
        else:

            self.n = int(self.qle.text())
        
            
            self.grid2 = QGridLayout()
            self.grid2.setSpacing(10)

            for i in range(self.n):
                for j in range(self.n):
                    l = QLineEdit()
                    l.resize(20,20)
                    self.grid2.addWidget(l, i, j)
                    self.linesArray.append(l)
            
            sucButton = QPushButton('Continua')
            delButton = QPushButton('Cancella')
            fillButton = QPushButton('Riempi')
            uniButton = QPushButton('Unitaria')

            fillButton.setToolTip('Riempi le caselle vuote con 0')
            uniButton.setToolTip('Matrice Unitaria di ordine {}'.format(self.n))

            sucButton.clicked.connect(lambda: self.matrixCalc())
            delButton.clicked.connect(lambda: self.delTab())
            fillButton.clicked.connect(lambda: self.completeTab())
            uniButton.clicked.connect(lambda: self.unitTab())

            self.grid2.addWidget(fillButton,self.n, 0)
            self.grid2.addWidget(sucButton,self.n, 1)
            self.grid2.addWidget(delButton, self.n, 2)        
            self.grid2.addWidget(uniButton,self.n, 3)            

            self.d.setLayout(self.grid2)
            self.d.setGeometry(200,200,self.n*100,self.n*100)
            self.d.show()

    def delTab(self):

        self.d.setWindowTitle('Matrice M')

        for k in range(len(self.linesArray)):
            self.linesArray[k].setText('')
        
    def completeTab(self):
        for k in range(len(self.linesArray)):
            if self.linesArray[k].text() == '':
                self.linesArray[k].setText('0')
    
    def unitTab(self):
        for k in range(0,len(self.linesArray), self.n+1):
            self.linesArray[k].setText('1') 
        

        #print(self.n)

    def matrixCalc(self):
            
            
            self.completeTab()

            
            matrix = np.zeros((self.n,self.n))

            for i in range(self.n):
                for j in range(self.n):
                    matrix[i][j] = float(self.linesArray[self.n * i + j].text())



            rank = np.linalg.matrix_rank(matrix)

            d1 = QDialog(self)
            
            grid3 = QGridLayout(self)

            grid3.setSpacing(10)

            grid3.addWidget(QLabel('det(M) = {}'.format(np.linalg.det(matrix))), 1, 1)

            grid3.addWidget(QLabel('rango(M) = {}'.format(rank)), 3,1)

          
            self.d.setWindowTitle('Aggiunta di M, M*')


            if np.linalg.det(matrix) == 0.0:
                grid3.addWidget(QLabel("M non e' invertibile"),2,1)
                for i in range(self.n):
                    for j in range(self.n):
                        self.linesArray[i*self.n + j].setText('NaN')
            else:
                inv = np.linalg.inv(matrix)
                adj = inv * np.linalg.det(matrix)
                for i in range(self.n):
                    for j in range(self.n):
                        self.linesArray[i*self.n +j].setText(str(round(adj[i][j],2)))
                        
            d1.setLayout(grid3)
            d1.setGeometry(100,100,300,300)
            d1.setWindowTitle('Det(M)')
            d1.show()
            print(matrix)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    ex = Appl()

    sys.exit(app.exec_())
