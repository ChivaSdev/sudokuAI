import numpy as np


class Domaine:

    def __init__(self, p):
        self.n = p*p
        self.p = p
        self.domaine = []

    def genDomaine(self):
        """Génére le domaine est place toutes ses valeurs à 0"""
        for i in range(0,self.n):
            tmp = []
            for j in range(0,self.n):
                tmp1 = []
                for k in range(0, self.n):
                    tmp1.append(0)
                tmp.append(tmp1)
            self.domaine.append(tmp)

    def initDomaine(self, sudo):
        """Initialise le domaine à partir d'une grille contenant le sudoku à résoudre"""
        for i in range(0, len(sudo[0])):
            for j in range(0, len(sudo[0])):
                if sudo[i][j] == "-":
                    for k in range(0, len(sudo[0])):
                        self.modValue(i, j, k, 1)

    def printDomaine(self):
        """Affiche le domaine"""
        for i in range(0,len(self.domaine)):
            print("Valeurs possible pour la ligne : ", i)
            for j in range(0, len(self.domaine[i])):
                print("Case numéro : ", j, " ",self.domaine[i][j])
            
    def modValue(self, i, j, k, value):
        """
        Modifie une valeur spécifique du domaine
        """
        self.domaine[i][j][k] = value

    def delValue(self, i, j, k):
        """
        Remet à zéro une valeur spécifique du domaine
        """
        self.domaine[i][j][k] = 0

    def resetDomaine(self):
        """
        Remet à zéro les valeurs des cases du domaine
        """
        for i in range(0,len(self.domaine)):
            for j in range(0,len(self.domaine[i])):
                for k in range(0, len(self.domaine[i][j])):
                    self.delValue(i, j, k)
                    
    def getDimLigne(self):
        return len(self.domaine)
    def getDomaine(self):
        return self.domaine
    
    def miseAJour():
        # Pour la partie graphique
        pass

