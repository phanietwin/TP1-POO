
from math import sqrt, cos, sin
from Class2 import*

#classe triangle prenant en arguments des objet vecteur
class Triangle(object):
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
#Fonction pour tourner ce triangle selon un angle alpha
    def Tourner(self, alpha):
        self.v1 = self.v1.Tourner(alpha)
        self.v2 = self.v2.Tourner(alpha)
        self.v3 = self.v3.Tourner(alpha)
        return self
#Fonction pour afficher les coordonnées de ses vecteurs/points
    def afficher(self):
        self.v1.afficher()
        self.v2.afficher()
        self.v3.afficher()
        
#Fonction pour le déplacer par rapport à un vecteur
    def Deplacer(self, vectref):
        self.v1 = self.v1.additionner(vectref)
        self.v2 = self.v2.additionner(vectref)
        self.v3 = self.v3.additionner(vectref)

