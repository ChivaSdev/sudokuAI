import numpy as np
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


from AideMiniBouton import AideMiniBouton

class UiAideCase(QtWidgets.QWidget):

    def __init__(self, possibleValues,constraint, selected, x, y, label):
        super().__init__()

        # Contraintes d'analyses importées du back-end

        # Box Mettant en place la grid
        self.x = x
        self.y = y
        self.selected = selected

        self.container = QtWidgets.QWidget(self)

        
        self.labelLayout = QtWidgets.QGridLayout(self)
        self.labelLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.labelLayout.setHorizontalSpacing(-5)
        self.labelLayout.setVerticalSpacing(-5)
        self.labelLayout.setContentsMargins(0, 0, 0, 0)


        self.container.setStyleSheet("border-style: none;font-size: 15px; margin-top: 16px;padding-top:5px; padding-bottom:76px; padding-right:60px;   background: white; color: #4A0C46;")

        self.constraint = constraint
        print(possibleValues)
        self.possibleSetValues = np.where(np.array(possibleValues) == 1)[0]
        for i in range(0,len(self.possibleSetValues)):
            self.possibleSetValues[i] += 1
        print(self.possibleSetValues)
        # Rempli le minilabel avec un chiffre si c'est une solution possible , sinon le laisse vide
        cpt = 1
        for i in range(0, 3):
            for j in range(0, 3):

                if self.constraint == None:
                    
                    if cpt in self.possibleSetValues:
                        self.minibutton = AideMiniBouton(str(cpt), self.x, self.y, True, label)
                        self.labelLayout.addWidget(self.minibutton, i, j)
                    else :
                        self.minibutton = AideMiniBouton(str(""), self.x, self.y, False, label)
                        self.labelLayout.addWidget(self.minibutton, i, j)
                    cpt += 1
                else:
                    self.minibutton = AideMiniBouton(str(self.constraint), self.x, self.y, False, label)
                    self.labelLayout.addWidget(self.minibutton, i, j)
                    


        self.labelLayout.addWidget(self.container)

    def getX(self):
        return self.x

    def getY(self):
        return self.y
