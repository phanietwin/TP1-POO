
from math import sqrt, cos, sin
from Class2 import*


class Triangle(object):
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def Tourner(self, alpha):
        self.v1 = self.v1.Tourner(alpha)
        self.v2 = self.v2.Tourner(alpha)
        self.v3 = self.v3.Tourner(alpha)
        return self

    def afficher(self):
        self.v1.afficher()
        self.v2.afficher()
        self.v3.afficher()

    def Deplacer(self, vectref):
        self.v1 = self.v1.additionner(vectref)
        self.v2 = self.v2.additionner(vectref)
        self.v3 = self.v3.additionner(vectref)

