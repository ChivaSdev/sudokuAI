import sys 
from copy import deepcopy
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Delegate import *
from Grille import *
from Domaine import *
from Filtrage import *


class Fenetre(QWidget):

    def __init__(self, grille, parent=None):
        super(Fenetre, self).__init__(parent)

        # création de la grille 9x9 
        self.table = QTableWidget(self)
        self.nbLigne, self.nbColonne = 9,9
        self.table.setRowCount(self.nbLigne)
        self.table.setColumnCount(self.nbColonne)
        
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()

        for row in range(0, self.nbLigne):
            self.table.setRowHeight(row, 50)
            for col in range(0, self.nbColonne):
                self.table.setColumnWidth(col, 50)

        for row in range(0, self.nbLigne):
            for col in range(0, self.nbColonne):
                item = QTableWidgetItem()
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.table.setItem(row, col, item)

        font = QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(16)
        self.setFont(font)

        self.resize(55*9, 55*9)

        position = QGridLayout()
        position.addWidget(self.table, 0, 0)
        self.setLayout(position)

        self.g0 = grille

        self.delegate = Delegate(self.table)
        self.table.setItemDelegate(self.delegate)

        self.delegate.grille_init(self.g0)

        self.g = deepcopy(self.g0)

        self.affiche(self.g)

        self.table.setFocus()
        self.table.setCurrentCell(0,0)

    def affiche(self, g):

        for row in range(0, len(g[0])):
            for col in range(0, len(g)):
                if g[row][col] == "-":
                    self.table.item(row, col).setText("")
                    self.table.item(row, col).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)

                else:
                    self.table.item(row, col).setText(str(g[row][col]))
                    self.table.item(row, col).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

if __name__ == '__main__':

    grille = Grille(3)
    grille.genGrille()

    domaine = Domaine(3)
    domaine.genDomaine()
 

    filtrage = Filtrage(grille, domaine)
    grille = filtrage.lire_Grille("5.txt")
    filtrage.propager_tout()


    app = QApplication(sys.argv)
    fen = Fenetre(grille)
    fen.show()
    sys.exit(app.exec_())
