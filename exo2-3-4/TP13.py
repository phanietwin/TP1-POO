from Class4 import*
from Class2 import*
from math import sqrt,cos, sin,pi


#On implémente la classe triangle avec les vecteurs

triangle = Triangle(Vecteur(1,1,1),Vecteur(2,2,2),Vecteur(-1,-1,1))

#afficher les trois vecteurs
print("")
print("Le triangle comprend trois points :")
print("")
triangle.afficher()

#On tourne le triangle d'un angle pi
alpha = 0
triangle2 = Triangle(Vecteur(1,1,1),Vecteur(2,2,2),Vecteur(-1,-1,1))
triangle2.Tourner(alpha)


#On translate du vecteur 1,1,1
vecret = Vecteur(1,1,1)
triangle2.Deplacer(vecret)

#Afficher à nouveau les points du triangle retourner et déplacer
print("")
print("Voici le nouveau triangle : ")
print("")
triangle2.afficher()
print("")
