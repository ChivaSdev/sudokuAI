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

        # On définit la taille de chaque cases
        for row in range(0, self.nbLigne):
            self.table.setRowHeight(row, 50)
            for col in range(0, self.nbColonne):
                self.table.setColumnWidth(col, 50)

        # Chaque case devient un TableWidgetItem
        for row in range(0, self.nbLigne):
            for col in range(0, self.nbColonne):
                item = QTableWidgetItem()
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.table.setItem(row, col, item)

        # Choix de la police
        font = QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(16)
        self.setFont(font)

        self.resize(55*9, 55*9)
        
        position = QGridLayout()
        position.addWidget(self.table, 0, 0)
        self.setLayout(position)

        self.g0 = grille

        # On délégue le fait de dessiner en gars les bordures d'une case (traditionnelle à une grille de sudoku)
        self.delegate = Delegate(self.table)
        self.table.setItemDelegate(self.delegate)

        self.delegate.grille_init(self.g0)

        self.g = deepcopy(self.g0)

        self.affiche(self.g)

        # La grille séléctionnée au lancement est la première (0, 0)
        self.table.setFocus()
        self.table.setCurrentCell(0,0)

    def affiche(self, g):
        """ Fonction qui permet l'affichage de la grille """
        for row in range(0, len(g[0])):
            for col in range(0, len(g)):
                if g[row][col] == "-":
                    # Si la grille importée ne contient aucun chiffre, alors on la rend séléctionnable et éditable
                    self.table.item(row, col).setText("")
                    self.table.item(row, col).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)

                else:
                    # Si la grille importée contien un chiffre, alors on la rend immmuable
                    self.table.item(row, col).setText(str(g[row][col]))
                    self.table.item(row, col).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

if __name__ == '__main__':

    grille = Grille(3)
    grille.genGrille()

    domaine = Domaine(3)
    domaine.genDomaine()
 

    filtrage = Filtrage(grille, domaine)
    grille = filtrage.lire_Grille("../ressources/5.txt")
    filtrage.propager_tout()


    app = QApplication(sys.argv)
    fen = Fenetre(grille)
    fen.show()
    sys.exit(app.exec_())
