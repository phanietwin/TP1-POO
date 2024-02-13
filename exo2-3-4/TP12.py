from Class2 import*
from math import sqrt,cos, sin,pi



x = int(input('donnez moi x : '))
y= int(input('donnez moi y : '))
z =int(input('donnez moi z :'))

v1 = Vecteur(x,y,z)
v2 = Vecteur(x+2,y+3,z+4)

#additionner deux vecteurs
addition = v1.additionner(v2)
print('la somme de v1 et v2 donne :')
addition.afficher()

#la norme
v1.CalculerNorme()

#tourner d'un angle alpha
alpha = pi/2
rot= v1.Tourner(alpha)
print('le nouveau vecteur avec une rotation de',alpha,'radians est ' )
rot.afficher()


#calcul du produit scalaire entre v1 et v2
v1.CalculerProduitScalaire(v2)

# création d'un vecteur zero

v3 = v1.zero()


