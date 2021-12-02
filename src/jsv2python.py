import numpy as np

# Les dimensions de la grille de sudoku
p = 3
n = p * p
global modif


def print_grille(grille):
    for i in range(0, len(grille)):
        print(grille[i])


def print_domaine(domaine):
    for i in range(0, len(domaine)):
        print(f"Valeurs possibles pour la ligne : {i + 1}")
        for j in range(0, len(domaine[i])):
            print(f"Case numéro : {j + 1} {domaine[i][j]}")


def lire_grille(nom_fichier, grille, domaine):
    # On lit le fichier donné
    f = open(nom_fichier, 'r', encoding='utf-8')
    sudoku = f.read()
    print("### CONTENU DU FICHIER ###")
    print(sudoku)
    matrice_sudo = np.reshape(sudoku.split(), (9, 9))
    print("### FICHIER TRANSFORMÉ EN MATRICE 9x9 ###")
    print(matrice_sudo)
    for i in range(0, len(grille[0])):
        for j in range(0, len(grille[0])):
            affecter_case(i, j, matrice_sudo[i][j], grille, domaine)


def affecter_case(i, j, nb, grille, domaine):
    if nb == "-":
        grille[i][j] = -1
        for k in range(0, len(domaine[i][j])):
            domaine[i][j][k] = 1
    else:
        grille[i][j] =
        nb - 1


def propager_case(i0, j0, val, domaine):
    for j in range(0, len(domaine[0])):
        if j != j0:
            domaine[i0][j][val] = 0

    for i in range(0, len(domaine[0])):
        if i != i0:
            domaine[i][j0][val] = 0


def nb_valeurs(i, j, domaine):
    nb = 0
    for k in range(0, len(domaine[0])):
        if domaine[i][j][k] == 1:
            nb += 1
    return nb


def valeur(i, j, domaine):
    k = 0
    while domaine[i][j][k] == 0:
        k += 1
    return k


def maj_grille(grille, domaine):
    for i in range(0, len(grille)):
        for j in range(0, len(grille[i])):
            if grille[i][j] == -1 and nb_valeurs(i, j, domaine) == 1:
                grille[i][j] = valeur(i, j, domaine)
                print("La grille a été modifiée")
                modif = True

def propager_une_fois(grille, domaine):
