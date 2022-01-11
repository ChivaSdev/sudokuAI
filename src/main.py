from Grille import *
from Domaine import *
from Filtrage import *

print("###Génération de la grille ###")            
g1 = Grille(3)
g1.genGrille()
print("###Affichage de la grille vide ###")
g1.printGrille()

d1 = Domaine(3)
print("### Generation du domaine###")
d1.genDomaine()
print("### Affichage du domaine vide ###")
#d1.printDomaine()

print("### Le filtrage ###")
f1 = Filtrage(g1, d1)
f1.lire_Grille("../ressources/5.txt")
f1.propager_tout()
f1.toString()
print("###Suggest ###")
f1.suggest()
print("### Help for case ###")
f1.suggestOneCase(0,0)
f1.suggestOneCase(0,1)
f1.suggestOneCase(0,9)
