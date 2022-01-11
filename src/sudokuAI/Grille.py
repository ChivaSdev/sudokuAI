class Grille:

    def __init__(self, p):
        self.p = p
        self.n = p*p
        self.grille = []

    def genGrille(self):
        for i in range(0, self.n):
            tmp = []
            for j in range(0, self.n):
                tmp.append(0)
            self.grille.append(tmp)

    def printGrille(self):
        for i in range(0, len(self.grille)):
            print(self.grille[i])

    def modValue(self, positionLigne, positionColonne, valeur):
        self.grille[positionLigne][positionColonne] = valeur 

    def delValue(self, n, m):
        self.grille[n][m] = 0

    def resetGrille(self):
        for i in range(0, len(self.grille)):
            for j in range(0, len(self.grille[i])):
                self.grille[i][j] = 0

    def get_ligne(self):
        return self.p

    def get_colonne(self):
        return self.p


