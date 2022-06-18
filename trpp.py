# faire un script calculator 
# importer les modules néacaissaires 
from pystyle import Write, Colors, Box 
import math 
import os

# clear le system 
os.system('cls')

# installer les modules nécaissaires 
print("INSTALLATION DES MODULES [*]")
os.system('pip install pystyle')
print("INSTALLATION DU MODULE TERMINER [*]")

# clear le system 
os.system('cls')

# definir les couleurs 
green = Colors.green
latence = interval = 0.04

# creer la banière 
banner = """
 ██████╗███╗   ███╗ █████╗ ████████╗██╗  ██╗
██╔════╝████╗ ████║██╔══██╗╚══██╔══╝██║  ██║ 
██║     ██╔████╔██║███████║   ██║   ███████║
██║     ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
╚██████╗██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
 ╚═════╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝

Coded by pryvox                                         
"""
print(green, banner)

# creation des choix de calcul 
print(Box.DoubleCube("[1] Carré \n[2] Rectangle\n[3] Triangle\n[4] Racine carré\n[5] Cylindre\n[6] pavé droit\n[7] Cone"))

def main():
    
    b = Write.Input("Quel figure voulez vous choisir ->", green, latence)

    if b == '1':
        print(green, ("\n-1 Air\n-2 Perimètre"))
        c = Write.Input("Que voulez-vous calculer ->", green, latence)

        # calculer l'air d'un carré 
        if c == '1':
            x = float(Write.Input("\nsaisissez la longueur des cotés :", green, latence))
            # faire le calcul 
            resl = x * x
            # afficher le calcul 
            print(green, "\nl'air du carré est égale a", resl, "m²")

        # calculer le perimetre d'un carré 
        elif c == '2':
            x = float(Write.Input("\nsaisissez la longueur :", green, latence))
            y = float(Write.Input("\nsaisissez la largeur :", green, latence))

            # faire le calcul 
            resl = x * y

            # afficher le calcul 
            print(green, "\nl'air du carré est égale a", resl, "m")

    if b == '2':
        print(green, ("\n-1 Air\n-2 Perimètre"))
        c = Write.Input("\nQue voulez vous calculer ->", green, latence)

        #calculer l'air d'un rectangle
        if c == '1':
            x = float(Write.Input("\nsaisissez la longueur :", green, latence))
            y = float(Write.Input("saisissez la largeur :", green, latence))
            # faire le calcul 
            result = x * y
            # afficher le résultat
            print(green, "l'air du rectangle est égale a", result,"m²")

        # calculer le perimetre d'un rectangle
        elif c == '2':
            x = float(Write.Input("\nsaisissez la longueur :", green, latence))
            y = float(Write.Input("\nsaisissez la largueur :", green, latence))
            # faire le calcul 
            resl = x + y * 2
            # afficher le calcul 
            print(green, "le perimetre du rectangle est égale a", resl, "m")

    if b == '3':
        print(green, ("\n-1 Air\n-2 Perimètre"))
        c = Write.Input("Que voulez-vous calculer ->", green, latence)
        if c == '1':
            x = float(Write.Input("Saisissez la hauteur ->", green, latence))
            y = float(Write.Input("Saisissez le coté ->", green, latence))
            # faire le calcul
            resultat = y * x / 2
            # afficher le resultat
            print(green, "l'air du triangle est égale a", resultat, "m²") 
        
        # calculer le perimetre du triangle
        elif c == '2':
            x = float(Write.Input("saisit la longueur d'un coté"))
            y = float(Write.Input("saisit la longueur d'un coté"))
            n = float(Write.Input("saisit la longueur d'un coté"))
            # faire le calcul 
            p = x + y + n
            # afficher le resultat
            print(green, "le perimetre du triangle est égale a", p, "m") 

    elif b == '4':
        x = float(Write.Input("Saisissez un nombre ->", green, latence))
        # bien verifier si le nombre ou le chiffre choisit est bon 
        if x >= 0:
            # faire le calcul 
            y = float(math.sqrt(x))
            # afficher le calcul 
            print(green, "La racin carré de", x, "est égale a", y)

    elif b == '5':
        # afficher les choix 
        print(green,"\n-1 Air\n-2 Volume")
        l = Write.Input("Que voulez vous calculer ->", green, latence)
        if l == '1':
            r = float(Write.Input("Saisissez le rayon ->", green, latence))
            h = float(Write.Input("Saisissez la hauteur ->", green, latence))

            # faire le calcule 
            res = 2 * math.pi * r * h

            # afficher le resultat 
            print(green, "l'air du cylindre est égal a ", res)

        if l == '2':
            r = float(Write.Input("Saisissez le rayon :", green, latence))
            h = float(Write.Input("Saisissez la hauteur :", green, latence))

            # calculer la surface 
            a = math.pi * r * r

            # calculer le volume 
            v = a * h

            # afficher le resultat du cylindre 
            print(green, "Le volume du cylinre est égale a", v,"m3")

    elif b == '6':
        # afficher les choix 
        print(green, "\n-1 Volume\n-2 Périmètre\n-3 Air")

        s = Write.Input("\nQue voulez vous calculer ->", green, latence)

        if s == '1':
            # demander les dimensions a l'utilisateur 
            l = float(Write.Input("\nSaisissez la largeur :", green, latence))
            x = float(Write.Input("Saisissez la longueur :", green, latence))
            h = float(Write.Input("Saisissez la hauteur :", green, latence))

            # faire le calcul 
            v = l * x * h

            # afficher le resulatt du calcul 
            print(green, "\nle volume du pavé droit est égale a", v,"m3")

        if s == '2':
            # demander les dimensensions a l'utilisateur 
            l = float(Write.Input("\nSaisissez la largeur :", green, latence))
            b = float(Write.Input("Saisissez la longueur :", green, latence))

            # faire le calcule
            p = 2 * l + 2 * b

            # afficher le resultat du calcule 
            print(green, "\nle périmetre de la base du pavé droit est égale a :", p,"m")
        
        if s == '3':
            # demander les dimensions a l'utilisateur 
            l = float(Write.Input("\nSaisissez la largeur :", green, latence))
            lo = float(Write.Input("Saisissez la longueur :", green, latence))
            h = float(Write.Input("Saisissez la hauteur :", green, latence))

            # faire le calcule
            r = 2 * l * lo + l * h + l * h

            # afficher le résultat 
            print(green, "\nl'Air du périmetre de la base est égale a", r,"m2")
            
    elif b == '7':
        # demander a l'utilisateur 
        Write.Print("\n-1 Volume\n-2 Air", green, latence)

        s = Write.Input("\n\nQue voulez vous calculer ->", green, latence)

        # premier choix 
        if s == '1':
            # demander les dimensions a l'utilisateur 
            r = float(Write.Input("\nSaisissez le rayon R :", green, latence))
            h = float(Write.Input("Saisissez la hauteur du cône :", green, latence))

            # faire le calcule 
            v = math.pi * r * r * h / 3

            # afficher le résultat 
            print(green, "\nLe volume du cône est égale a :", v,"m3")

        # deuxième choix
        elif s == '2':
            # demander les dimensions a l'utilsateur
            r = float(Write.Input("\nSaisissez le rayon R du cône :", green, latence))

            # faire le calcul 
            a = math.pi * r * r 

            # afficher le resultat 
            print(green, "\nL'air du cône est égale a", a, "m²")

    # afficher une erreur si le l'utilisateur a mal chosisit les options 
    else:
        print("ERREUR : Veuillez saisir le bon chiffre")

            
if __name__=='__main__':
    main()      
