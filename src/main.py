from Grille import *
from Domaine import *
from Filtrage import *
from Fenetre import *


grille = Grille(3)
grille.genGrille()

domaine = Domaine(3)
domaine.genDomaine()
         

filtrage = Filtrage(grille, domaine)
grille = filtrage.lire_Grille("../ressources/5.txt")
filtrage.propager_tout()


app = QApplication(sys.argv)
fen = Fenetre(grille, filtrage)
sys.exit(app.exec_())
