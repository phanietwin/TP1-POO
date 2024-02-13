from Class4 import*
from Class2 import*
from Class3 import*


#On implémente l'objet 3D par 3 triangles, une couleur bleu et un centre de gravité de 0
tri1 = Triangle(Vecteur(1,1,1),Vecteur(2,2,2),Vecteur(1,1,-1))
tri2 = Triangle(Vecteur(2,4,1),Vecteur(3,2,3),Vecteur(-2,1,-1))
tri3 = Triangle(Vecteur(2,5,1),Vecteur(8,2,3),Vecteur(-4,5,-8))


objet_color = Couleur(0, 255, 0) 
objet_center = Vecteur(0, 0, 0)

objet = Objet3D(objet_center, objet_color)

#On ajoute les trois triangles


objet.Ajouter_triangle(tri1)
objet.Ajouter_triangle(tri2)
objet.Ajouter_triangle(tri3)

#Afficher les coordonnées de cet objet
objet.Afficher()

#Translater l'objet
vectref = Vecteur(1, 1, 1)
objet.déplacer(vectref)

#afficher le nouvelle objet
objet.Afficher()