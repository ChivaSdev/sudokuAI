import numpy as np
import Grille
import Domaine


class Filtrage:

    def __init__(self, grille, domaine):
        self.grille = grille
        self.domaine = domaine
        self.modif = False

    def print_grille(self):
        for i in range(0, len(self.grille)):
            print(self.grille[i])

    def print_domaine(self):
        for i in range(0, len(self.domaine)):
            print(f"Valeurs possivles pour la ligne : {i + 1}")
            for j in range(0, len(self.domaine[i])):
                print(f"Case numéro : {j + 1} {self.domaine[i][j]}")

    def lire_grille(self, nom_fichier):
        f = open(nom_fichier, 'r', encoding='utf-8')
        sudoku_texte = f.read()
        matrice_sudoku = np.reshape(sudoku_texte.split(), (9, 9))
        for i in range(0, len(self.grille[0])):
            for j in range(0, len(self.grille[0])):
                self.affecter_case(i, j, sudoku_texte[i][j])

    def affecter_case(self, index_ligne, index_colonne, nombre):
        if nombre == "-":
            self.grille[index_ligne][index_colonne] = -1
            for i in range(0, len(self.domaine[index_ligne][index_colonne])):
                self.domaine[index_ligne][index_colonne][i] = 1
        else:
            self.grille[index_ligne][index_colonne] = int(nombre) - 1

    def propager_case(self, i0, j0, valeur):
        for j in range(0, len(self.domaine[0])):
            if j != j0:
                self.domaine[i0][j][valeur] = 0
        for i in range(0, len(self.domaine[0])):
            if i != i0:
                self.domaine[i][j0][valeur] = 0

    def nombre_valeurs(self, index_ligne, index_colonne):
        """ Calcul le nombre de valeurs possible pour une case """
        nb = 0
        for i in range(0, len(self.domaine[0][0])):
            if self.domaine[index_ligne][index_colonne][i] == 1:
                nb += 1
        return nb

    def chercher_valeur(self, index_ligne, index_colonne):
        i = 0
        while self.domaine[index_ligne][index_colonne][i] == 0:
            i += 1
        return i

    def maj_grille(self):
        for i in range(0, len(self.grille)):
            for j in range(0, len(self.grille[i])):
                if self.grille[i][j] == -1 and self.nombre_valeurs(i, j) == 1:
                    self.grille[i][j] = self.chercher_valeur(i, j)
                    print("La grille a été modifiée")
                    self.modif = True

    def propager_une_fois(self):
        for i in range(0, len(self.grille)):
            for j in range(0, len(self.grille[i])):
                if self.grille[i][j] != -1:
                    self.propager_case(i, j, int(self.grille[i][j]))
        self.maj_grille()

    def propager_tout(self):
        self.modif = False
        self.propager_une_fois()
        self.print_grille()
        for i in range(0, self.grille.get_ligne() * self.grille.get_colonne()):
            self.propager_une_fois()
