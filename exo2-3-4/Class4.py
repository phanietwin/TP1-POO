
from math import sqrt, cos, sin
from Class2 import*
from Class3 import*


class Couleur(object):
    def __init__(self, r, b, v):
        self.r = r
        self.b = b
        self.v = v

class Objet3D(object):
    def __init__(self, centre, couleur):
        self.centre = centre
        self.couleur = couleur
        self.triangle = []

    def Ajouter_triangle(self, triangle):
        self.triangle.append(triangle)

    def déplacer(self, vectref):
        self.centre = self.centre.additionner(vectref)
        for triangle in self.triangle :
            triangle.Deplacer(vectref)

    def Afficher(self):

        print("points de l'objet 3D:")
        print("")
        for triangle in self.triangle :
            print("")
            print("triangle :")
            print("")
            triangle.afficher()
