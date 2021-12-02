class Grille:

    def __init__(self):
        self.ligne = 3
        self.colonne = 3
        self.grille = []

    def genGrille(self):
        for i in range(0, self.ligne):
            tmp = []
            for j in range(0, self.colonne):
                tmp.append(0)
            self.grille.append(tmp)

    def printGrille(self):
        for i in range(0, len(self.grille)):
            print(self.grille[i])

    def updateValue(self, valeur, positionLigne, positionColonne):
        self.grille[positionLigne][positionColonne] = valeur 

    def delValue(self, n, m):
        self.grille[n][m] = 0

    def resetGrille(self):
        for i in range(0, len(self.grille)):
            for j in range(0, len(self.grille[i])):
                self.grille[i][j] = 0

    def get_ligne(self):
        return self.ligne

    def get_colonne(self):
        return self.colonne


if __name__ == "__main__":
    g1 = Grille()
    g1.genGrille()
    g1.printGrille()
    g1.updateValue(3,0,2)
    print("###Ajout valeur ###")
    g1.printGrille()
    print("###Supp valeur ###")
    g1.delValue(0,2)
    g1.printGrille()
    print("###Ajout valeur ###")
    g1.updateValue(3,0,2)
    g1.printGrille()
    print("###Reset ###")
    g1.resetGrille()
    g1.printGrille()
