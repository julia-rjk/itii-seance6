import numpy as np
import math

# COPYRIGHT ROJKOVSKA Julia
# paypal.me/juliarojkovska
# 1 euro la copie 

# Exercice 1 : méthode des rectangles

def integrale(f, a, b, n):
    # paypal.me/juliarojkovska
    integrale = 0
    k=a;
    while(k < b):
        largeur = (b-a)/n
        hauteur = f(a + k*(b-a)/n)
        aire = largeur * hauteur
        integrale += aire
        k+=n
 
    return integrale

# paypal.me/juliarojkovska
# Quelle valeur de n faut-il choisir pour être précis à 10^{-4} près ? Ecrire la fonction qui permette de calculer cette valeur.
# ......................

# paypal.me/juliarojkovska
#Tester avec la fonction sur l'interval 0,10 avec un pas de 0.001
f = lambda x : 3*x**3 + 2*x - 1
print(integrale(f,0,10,0.001)) # renvoie 7.50+22 ( à vérifier )

g = lambda x : math.cos(1/x)
print(integrale(g,0,10,0.001)) # ZeroDivisionError: float division by zero

# Exercice 2 : Méthode des trapèzes
# paypal.me/juliarojkovska
def trapez(f,a,b,n):
    # à toi de jouer