
from math import sqrt, cos, sin


class Vecteur(object):
    def __init__(self,x,y,z):
        self.x= x
        self.y = y
        self.z =z

    def zero(self):
        
        vector = Vecteur(0,0,0)
       
        return vector


    def additionner(self,vecteur):
        new_vecteur = Vecteur(self.x+vecteur.x,self.y+vecteur.y,self.z+vecteur.z)
        
        return new_vecteur
    
    def CalculerNorme(self):
        Norme = sqrt(self.x**2+ self.y **2+ self.z**2)
        print('La norme de ce vecteur est', Norme)
        return Norme

    def CalculerProduitScalaire(self,vecteur):
        Scalaire = self.x*vecteur.x+self.y*vecteur.y+self.z*vecteur.z
        print('le proDuit scalaire des deux vecteur v1 et v2 est :', Scalaire)
        return Scalaire
    
    def Tourner(self, alpha):
        vecteur = Vecteur(self.x*cos(alpha) +self.y*sin(alpha), self.y*cos(alpha)-self.x*sin(alpha), self.z)
        return vecteur
    
    def afficher(self):
    
        print( self.x,',',self.y,',',self.z)
