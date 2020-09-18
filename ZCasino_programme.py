import os

from random import randrange
from math import ceil

#Déclarer les variables de début de partie
argent = 1000
continuer_partie = True
print("Vous vous installez à la table à roulette avec", argent, "€.")
while continuer_partie: #tant qu'on doit continuer la partie on demande à l'utilisateur de saisir le nombre sur lequel il mise
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49):")

        #Convertion du nombre misé
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Ce nombre est négatif")
        if nombre_mise > 49:
            print("Ce nombre est supérieur à 49")
    
    #Selection de la somme à miser sur le nombre
    mise = 0
    while mise <=0 or mise > argent:
        mise = input("Tapez le montant de votre mise:")
        #Convertion de la mise
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0: 
            print("La mise est négative ou nulle")
        if mise > argent:
            print("Vous ne pouvez pas miser autant, vous n'avez que", argent, "€")

        
    #On fait tourner la roulette

    numero_gagnant = randrange(50)
    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

    #Etablir le gain
    if numero_gagnant == nombre_mise:
        print("Félicitations !! Vous obtenez", mise *3, "€!")
        argent += mise *3
    elif numero_gagnant %2 == nombre_mise % 2: #ils sont de la meme couleur
        mise = ceil(mise *0.5)
        print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "€")
        argent +=mise
    else:
        print("Désolé, ce n'est pas pour cette fois. Vous perdez votre mise.")
        argent +=mise

    #Interrompre la partie si le joueur est ruiné
    if argent <=0:
        print("Vous êtes ruiné...C'est la fin de cette partie.")
        continuer_partie = False
    else:
        #Afficher argent du joueur
        print("Vous avez à présent", argent, "€")
        quitter = input("Souhaitez-vous quitter le casino (O/n)?")
        if quitter =="O" or quitter == "o":
            print("Vous quitter le casino avec vos gains")
            continuer_partie = False

#On met en pause la partie
os.system("pause") 