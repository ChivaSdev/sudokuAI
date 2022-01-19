from Grille import *
from Filtrage import *
from Domaine import *


class SudokuGame:

    def __init__(self, grille, domaine, AImethode) -> None:
        self.grille = grille
        self.domaine = domaine
        self.AImethode = AImethode

    


if __name__ == '__main__':
    print("Création de la grille...")
    g1 = Grille(3)
    g1.genGrille()
    print("Affichage de la grille...")

    d1 = Domaine(3)
    d1.genDomaine()

    f1 = Filtrage(g1, d1)
    f1.lire_Grille("../ressources/5.txt")
    g1.printGrille()
    f1.propager_tout()
    g1.printGrille()

        
        

