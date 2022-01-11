import numpy as np
from Grille import *
from Domaine import *


class Filtrage:

    def __init__(self, grille, domaine):
        self.grille = grille
        self.domaine = domaine
        self.modif = False

    def lire_Grille(self, nom_fichier):
        """
        Lis une grille de sudoku à partir d'un fichier .txt puis affecte les valeurs correspondantes à la grille et au domaine
        """
        f = open(nom_fichier, 'r', encoding='utf-8')
        sudoku_texte = f.read()
        matrice_sudoku = np.reshape(sudoku_texte.split(), (9, 9))
        for i in range(0, len(self.grille.grille)):
            for j in range(0, len(self.grille.grille)):
                self.affecter_case(i, j, matrice_sudoku[i][j])

    def affecter_case(self, index_ligne, index_colonne, nombre):
        """
        Affecte les valeurs des cases à la grille du sudoku et initialise en conséquence le domaine
        """
        if nombre == "-":
            self.grille.modValue(index_ligne, index_colonne, -1)
            for i in range(0, self.domaine.getDimLigne()):
                self.domaine.modValue(index_ligne, index_colonne, i, 1)
        else:
            self.grille.modValue(index_ligne, index_colonne, int(nombre)-1)

    def propager_case(self, i0, j0, valeur):
        """
        Vérifie que la valeur donnée n'apparait qu'une fois sur la ligne et la colonne
        """
        for j in range(0, self.domaine.getDimLigne()):
            if j != j0:
                self.domaine.modValue(i0, j, valeur, 0)
        for i in range(0, self.domaine.getDimLigne()):
            if i != i0:
                self.domaine.modValue(i, j0, valeur, 0)

    def nombre_valeurs(self, index_ligne, index_colonne):
        """ Calcul le nombre de valeurs possible pour une case """
        nb = 0
        for i in range(0, len(self.domaine.domaine[0][0])):
            if self.domaine.domaine[index_ligne][index_colonne][i] == 1:
                nb += 1
        return nb

    def chercher_valeur(self, index_ligne, index_colonne):
        """
        Trouve la valeur manquant à une case de la grille grâce au domaine
        """
        i = 0
        while self.domaine.domaine[index_ligne][index_colonne][i] == 0:
            i += 1
        return i

    def maj_grille(self):
        """
        Mets à jour les valeurs de la grille en fonction du domaine
        """
        for i in range(0, len(self.grille.grille)):
            for j in range(0, len(self.grille.grille[i])):
                if self.grille.grille[i][j] == -1 and self.nombre_valeurs(i, j) == 1:
                    self.grille.grille[i][j] = self.chercher_valeur(i, j)
                    print("La grille a été modifiée")
                    self.modif = True
        

    def propager_une_fois(self):
        """
        Boucle parcourant une fois toute la grille du sudoku pour vérifiant que la valeur n'apparait qu'une fois dans sa ligne et colonne
        """
        for i in range(0, len(self.grille.grille)):
            for j in range(0, len(self.grille.grille[i])):
                if self.grille.grille[i][j] != -1:
                    self.propager_case(i, j, int(self.grille.grille[i][j]))
        self.maj_grille()


    def propager_tout(self):
        """
        Methode principale executant toutes les méthodes nécessaires pour filtrer les résultats possibles pour le sudoku
        """
        self.modif = False
        self.propager_une_fois()
        for i in range(0, self.grille.get_ligne() * self.grille.get_colonne()):
            self.propager_une_fois()
        for i in range(0,len(self.grille.grille)):
            for j in range(0, len(self.grille.grille[i])):
                self.grille.grille[i][j] += 1 

    def toString(self):
        print("###Affichage Domaine ###")
        self.domaine.printDomaine()
        print("###Affichage Grille ###")
        self.grille.printGrille()

    def suggest(self):
        """
        Affiche seulement les cases ayant au moins une possibilité
        """
        for i in range(0,len(self.domaine.domaine)):
            print("Valeurs possible pour la ligne : ", i+1)
            for j in range(0, len(self.domaine.domaine[i])):
                if 1 in self.domaine.domaine[i][j] :
                    print("Case numéro : ", j+1, " ",self.domaine.domaine[i][j])

    def suggestOneCase(self, i,j):
        if  i < 0 or i >8 or j <0 or j>8 :
            return print(" La case : [", i,"," ,j, "] n'existe pas")
        print(self.grille.grille[i][j])
        if self.grille.grille[i][j] == 0 or self.grille.grille[i][j] == -1:
            print(self.domaine.domaine[i][j])
            print(self.domaine.domaine[i][j].index(1))
            print(np.where(np.array(self.domaine.domaine[i][j]) == 1)[0])
        else:
            print("La case est déjà complétée.")
