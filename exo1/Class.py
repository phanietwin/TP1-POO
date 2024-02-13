
#Classe Algèbre prenant en attribut et argument un entier n
class Algebre(object):
    def __init__(self,n):
        self.n = n
#fonction pour sommer tous les entiers jusqu'à n
    def somme(self,somme):
        for i in range (self.n+1):
            somme = i + somme
        print("la somme de nombre est : ",somme)
        return self.somme
        
    #Fonction pour calculer la factorielle d'un nombre    
    def factorielle(self):
        fact = 1
        for i in range (self.n+1):
            if(i>1):
                fact = fact *i
            print("factorielle de ",i, "est :",fact)
        print("la factorielle totale est :" , fact)
