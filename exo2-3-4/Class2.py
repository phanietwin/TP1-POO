
from math import sqrt, cos, sin

#Classe vecteur qui prend comme arguments ses coordonnées, x,y, z
class Vecteur(object):
    def __init__(self,x,y,z):
        self.x= x
        self.y = y
        self.z =z
#fonction pour donner un vecteur 000
    def zero(self):
        
        vector = Vecteur(0,0,0)
       
        return vector

    #additionner deux vecteurs
    def additionner(self,vecteur):
        new_vecteur = Vecteur(self.x+vecteur.x,self.y+vecteur.y,self.z+vecteur.z)
        
        return new_vecteur
    #calculer la norme
    def CalculerNorme(self):
        Norme = sqrt(self.x**2+ self.y **2+ self.z**2)
        print('La norme de ce vecteur est', Norme)
        return Norme
    #calculer le produit scalaire avec un autre vecteur donné en attribut
    def CalculerProduitScalaire(self,vecteur):
        Scalaire = self.x*vecteur.x+self.y*vecteur.y+self.z*vecteur.z
        print('le proDuit scalaire des deux vecteur v1 et v2 est :', Scalaire)
        return Scalaire
        
    #rotation du vecteur autour d'un angle alpha
    def Tourner(self, alpha):
        vecteur = Vecteur(self.x*cos(alpha) +self.y*sin(alpha), self.y*cos(alpha)-self.x*sin(alpha), self.z)
        return vecteur
    #afficher le vecteur et ses attributs
    def afficher(self):
    
        print( self.x,',',self.y,',',self.z)
