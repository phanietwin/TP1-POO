

from random import randint


class Joueur(object):
    def __init__(self, nom):
        self.nom = nom
        self.points = 0

    #Pour  afficher le nom du joueur et ses points 
    def afficher(self):
        print("\nLe joueur", self.nom, "a", self.points, "points\n")

    #Lancer les dés une première fois
    def Lancer(self):
        scores = []
        de = Dé()  
        for i in range(3):
            scores.append(de.lancer()) 
        self.afficher_des(scores) 
        return scores
    
    #Les afficher
    def afficher_des(self,scores):
        print("vos scores : ",scores[0], scores[1], scores[2]) 

    #Les relancer une seconde fois
    def relancer(self, scores):
        de = Dé()
        nb_des= int(input("Combient de dés voulez vous relancer ?"))

        #cas de 3 dés
        if nb_des == 3 :
            for i in range (3) :
                scores[i] = de.lancer()
        
        #cas d'un dé
        if nb_des == 1:
            res = 'q'
            i=0
            while i<3 and res != 'o':
                res ='q'
                #pour vérifier que oui ou non est donné 
                while res!= 'n' and  res!= 'o' :
                    res = input("Voulez-vous relancer le dé {} ? (o pour oui, n pour non)".format(i+1))
                i=i+1
                

            print("on relance le dé", i)
            scores[i-1]=de.lancer()

        #cas de deux dés
        if nb_des == 2 : 
            res = 'q'
            compt = 0
            i =0
            while i<2  :
                res = "q"
                #pour vérifier que oui ou non est donné 
                while res!= 'n' and  res!= 'o' :
                    res = input("Voulez-vous relancer le dé {} ? (o pour oui, n pour non) ".format(i+1))
                i=i+1
                if res == 'o':
                    scores[i-1]=de.lancer()
                   
                    compt = compt +1

            #Pour ne pas demander le dés 3
            if compt != 2 :
                scores[2]=de.lancer()

        self.afficher_des(scores)
        return scores

#Compter les scores en fonction des scores des dés
    def Compter_score(self, scores):
        scores.sort()
        if scores == [1, 2, 4]:
            self.points += 10
        elif scores[0] == scores[1] == 1:
            self.points += scores[2]
        elif scores[0] == scores[1] + 1 and scores[1] == scores[2] + 1:
            self.points += 2


#CLasse dé pour lancer un dé       
class Dé(object):
    def __init__(self):
        self.score = 0
    def lancer(self):
        self.score = randint(1,6)
        return self.score

          
#Classe jeu pour regler le déroulement de la partie
class Jeu(object):
    def __init__(self):
        self.joueurs = []  

#AJouter des joueurs
    def Ajouter_joueur(self, Joueur):
        self.joueurs.append(Joueur)  

#initialiser une nouvelle partie
    def nouvelle_partie(self):
        for joueur in self.joueurs:  
            joueur.points = 0 
            joueur.afficher() 

#Démarrer une partie
    def Tour(self):
        for joueur in self.joueurs:  
            print("c'est au tour de ", joueur.nom)
            scores = joueur.Lancer()  
            scores2 = joueur.relancer(scores)  
            joueur.Compter_score(scores2)
            joueur.afficher()  

            print("\n************************************************************************ \n")
#Calculer les points de chaque joueur 
    def final(self):
        scores = {}  
        for joueur in self.joueurs:
            joueur.afficher()
            scores[joueur.nom] = joueur.points  
        print("Le joueur gagnant est :", max(scores, key=scores.get))
        print("Avec un score de :", scores[max(scores,key =scores.get)])


            
            
            
        
    
           

