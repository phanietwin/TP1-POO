
from math import sqrt, cos, sin
from Class2 import*
from Class3 import*

#Classe couleur prenant en argument trois entiers pour les couleurs r, b,v
class Couleur(object):
    def __init__(self, r, b, v):
        self.r = r
        self.b = b
        self.v = v
        
#Classe objet 3D, prenant comme attribut un vecteur centre, une couleur (de classe Couleur) et une liste de triangles
class Objet3D(object):
    def __init__(self, centre, couleur):
        self.centre = centre
        self.couleur = couleur
        self.triangle = []
#fonction pour ajouter des triangles à la liste, prenant en argument un triangle de type Triangle
    def Ajouter_triangle(self, triangle):
        self.triangle.append(triangle)
        
#fonction pour déplacer l'Objet 3d le long d'un vecteur de référence
    def déplacer(self, vectref):
        self.centre = self.centre.additionner(vectref)
        for triangle in self.triangle :
            triangle.Deplacer(vectref)
            
#Fonction pour afficher ses points :
    def Afficher(self):

        print("points de l'objet 3D:")
        print("")
        for triangle in self.triangle :
            print("")
            print("triangle :")
            print("")
            triangle.afficher()
