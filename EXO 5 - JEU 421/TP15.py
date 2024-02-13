
from Class5 import*
from random import randint
from random import random

j1 = Joueur("Moi")
j2 = Joueur("Toi")
j3 = Joueur("elle")
j4 = Joueur("lui")

#nombre de tours :
partie = 3


jeu = Jeu()
jeu.Ajouter_joueur(j1)
jeu.Ajouter_joueur(j2)
jeu.Ajouter_joueur(j3)
jeu.Ajouter_joueur(j4)

print ("Commencons une nouvelle partie de 421")
print("\n**************************************\n")

jeu.nouvelle_partie()
print("\n**************************************\n")
for i in range(partie):
   print("TOUR ", i+1,":\n")
   jeu.Tour()
jeu.final()


