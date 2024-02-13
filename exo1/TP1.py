import sys
from Class import*

if __name__ == '__main__':

    from Class import*

    #petit1 & petit3
    #argc = len(sys.argv)
    #args = sys.argv
    #print("args : ",args)
    n = int(input('veuillez entrer un nombre :  '))
    somme = 0
    algebre = Algebre(n)
    algebre.somme(somme)
    #petit2
    algebre.factorielle()






