import sys 
from copy import deepcopy
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Delegate import *
from Grille import *
from Domaine import *
from Filtrage import *
from UiAideCase import UiAideCase

class Fenetre(QWidget):

    def __init__(self, grille, filtrage, parent=None):
        super(Fenetre, self).__init__(parent)

        self.position = QGridLayout(self)

        self.filtrage = filtrage
        self.grille = grille 
        height = 800
        width = 1024

        #Grile Sudo        
        self.table = QTableWidget(self)
        self.nbLigne, self.nbColonne = 9,9
        self.table.setRowCount(self.nbLigne)
        self.table.setColumnCount(self.nbColonne)
        
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()

        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        for row in range(0, self.nbLigne):
            self.table.setRowHeight(row, 58)
            for col in range(0, self.nbColonne):
                self.table.setColumnWidth(col, 76)

        # Chaque case devient un TableWidgetItem
        for row in range(0, self.nbLigne):
            for col in range(0, self.nbColonne):
                item = QTableWidgetItem()
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.table.setItem(row, col, item)
        

        #Widget / boutons

        self.switchView= QCheckBox("Activer la vue domaine ")
        self.switchView.stateChanged.connect(self.viewChange)
        

        font = QFont()
        font.setPointSize(16)

        self.l2 = QLabel()
        self.l2.setText("")
        self.l2.setFont(font)
        self.l2.setStyleSheet(" font-size: 15px; margin-top: 13px;padding-top:5px; padding-bottom:76px;  border-style:solid; border-width:1px;  background: white; color: #4A0C46;")
        

       
        
        #self.Baide = QPushButton("Informations")
        #self.Baide.clicked.connect(self.infoLog)
        #self.Baide.setStyleSheet(" font-size: 15px;  padding: 6px 50px 6px 50px;")

        self.BmaJ = QPushButton("Mise à jour")
        self.BmaJ.clicked.connect(self.maJ)
        self.BmaJ.setStyleSheet(" font-size: 15px;  padding: 6px 50px 6px 50px;")

        ### Ajout des widgets au Layout

        self.position.addWidget(self.table, 0,0,5,5)
        self.position.addWidget(self.BmaJ, 0,5,2,2)
        self.position.addWidget(self.switchView, 0,5, 1,1) 
        self.position.addWidget(self.l2,5,0,2,5)
        
        self.setFixedSize(width, height)

        

        self.initiale = grille

        # Délimitation des bordures de cases
        self.delegate = Delegate(self.table)
        self.table.setItemDelegate(self.delegate)

        self.setWindowTitle("MASK")
        

        self.delegate.grille_init(self.initiale)

        self.g = deepcopy(self.initiale)

        self.affiche(self.g, self.initiale)

        
        self.setLayout(self.position)

        self.show()

    def viewChange(self, state):
        if Qt.Checked == state:
            self.toDomaine()
        else:
            print("On est dedans")
            self.position.removeWidget(self.interfaceGroupBox)
            self.interfaceGroupBox.deleteLater()
            self.interfaceGroupBox = None
            #self.affiche(self.g)

    def toDomaine(self):

                #Grille Domaine
        self.interfaceGroupBox = QGroupBox(self)
        self.interfaceGroupBox_layout = QGridLayout(self)

        self.interfaceGroupBox.setLayout(self.interfaceGroupBox_layout)
        self.interfaceGroupBox.setStyleSheet("border-style:solid; background:#DCDCDC; border-width:1px; border-color:black;")
                # Boucle d'attribution des widgets aux cases ?
        for row in range(0, self.nbLigne):
            for col in range(0, self.nbColonne):

                if self.grille[row][col] == "-":
                    item = UiAideCase(self.filtrage.domaine.domaine[row][col],None,[],row,col, self.l2)## <--- a modif
                    item.setStyleSheet("border-style:none;")
                    self.interfaceGroupBox_layout.addWidget(item,row,col)

                else:
                    item = UiAideCase(self.grille[row][col],self.grille[row][col],[],row,col, self.l2) ### <--- a modif
                    item.setStyleSheet("border-style:none;")
                    self.interfaceGroupBox_layout.addWidget(item,row,col)
        self.position.addWidget(self.interfaceGroupBox, 0,0,5,5)
                    

    def infoLog(self):
        self.l2.setText("Les nombres présents dans les cases blanches \n représentent les valeurs possibles pour une case.")
 


    def affiche(self, g, gInit):

        for row in range(0, len(g[0])):
            for col in range(0, len(g)):
                if g[row][col] == "-" or g[row][col] != gInit[row][col]:

                    if self.table.item(row, col).text() == None:
                        self.table.item(row, col).setText("")
                        
                    self.table.item(row, col).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
                    
                else:
                    self.table.item(row, col).setText(str(g[row][col]))
                    self.table.item(row, col).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)


    def maJ(self):

        print(self.g)

        print("Picsou was here")
        self.g[0][0] = str(self.table.item(0,0).text())
        self.affiche(self.g, self.initiale)
                
        print(self.g)
        
    




