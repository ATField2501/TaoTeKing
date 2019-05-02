#!/usr/bin/python3
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com>
# Oracle

from CaglioConstantes import *
import random


def artefact(i,presentation):
    if i == 0:
        presentation.append('   le Ciel')
        for e in ciel:
            presentation.append(' '+e)
    if i == 1:
        presentation.append(' la Terre')
        for e in terre:
            presentation.append(' '+e)
    if i == 2:
        presentation.append('   le Feu')
        for e in feu:
            presentation.append(' '+e)
    if i == 3:
        presentation.append(' le Tonerre')
        for e in tonnerre:
            presentation.append(' '+e)
    if i == 4:
        presentation.append('la Montagne')
        for e in montagne:
            presentation.append(' '+e)
    if i == 5:
        presentation.append('le Vent/le Bois')
        for e in ventBois:
            presentation.append(' '+e)
    if i == 6:
        presentation.append('les Maraicages')
        for e in maraicage:
            presentation.append(' '+e)
    if i == 7:
        presentation.append('  l Eau')
        for e in eau:
            presentation.append(' '+e)



class Cagliostro():
    """
    Pour le Plaisiiir!.....
    """
    def __init__(self):
        # Remplissage du dico
        nb=1
        for i in hexagramme:
            tao[str(nb)] = i
            nb += 1

    def aide(self):
        """
        Prompt d'aide
        """
        print("Caglio-Oracle -l (lister 64 hexagrammes)")
        print("Caglio-Oracle -o (oracle) * (verbeux)")
        print("Caglio-Oracle -t (lister 8 trigrammes)")
        print("Caglio-Oracle -H 12 (Afficher hexagramme n°12)")
        print("Caglio-Oracle -r (Rivière du Tao)")

    def liste(self):
        """
        Affiche le Tao
        """
        for e,i in taOnumerik.items():
            print(e,i[1])

    def hexa(self, indice):
        try:
            print(tao[indice])
        except KeyError:
            print("Il existe 64 hexagrammes, spécifiez un nombre cohérent")

    def tri(self):
        """
        Methode qui affiche les trigrammes
        """
        affichage=[]
        for cle, valeur in trigramme.items():
            affichage.append(cle+ ':')
            for e in valeur:
                 affichage.append(e)
        print('   '+affichage[0]+'   '+affichage[4]+'   '+affichage[8]+'  '+ affichage[12])
        print(affichage[1]+'  '+affichage[5]+'   '+affichage[9]+'  '+ affichage[13])
        print(affichage[2]+'  '+affichage[6]+'   '+affichage[10]+'  '+ affichage[14])
        print(affichage[3]+'  '+affichage[7]+'   '+affichage[11]+'  '+ affichage[15])

        print('   '+affichage[16]+'  '+affichage[20]+'   '+affichage[24]+'  '+ affichage[28])
        print(affichage[17]+'  '+affichage[21]+'   '+affichage[25]+'  '+ affichage[29])
        print(affichage[18]+'  '+affichage[22]+'   '+affichage[26]+'  '+ affichage[30])
        print(affichage[19]+'  '+affichage[23]+'   '+affichage[27]+'  '+ affichage[31])

    def hasard(self):
        """
        Methode qui tire un hexagramme au hasard
        """
        target = random.randint(0,63)
        print("{} {}".format(target,tao[str(target)]))

    def riviere(self):
        """
        Rivière du Tao
        """
        nb1 = 0
        while nb1 < 8:
            ligne=[]
            nb =0
            while nb < 8:
                target = random.randint(1,64)

                ligne.append(tao[str(target)])
                nb += 1
            instant=""
            for e in ligne:
                instant += ' '+e+' ' 
            print(instant+ "\n")
            nb1 += 1

    def oracle(self, aleph):
        """
        Methode qui doit tirer au hasard deux trigrames pour construire un hexagramme en tenant compte des traies muables
        """
        ## Création d'un conteneur pour resultat de l'opération
        tirage= []
        transform= []
        ## tirage
        jet=0
        while jet < 6:
            target = random.randint(1,4)
            if target == 1:
                tirage.append(1)
                print('      '+str(jet+1)+trai1+' 1')
            if target == 2:
                tirage.append(2)
                print('      '+str(jet+1)+trai2+' 2')
            if target == 3:
                tirage.append(3)
                transformation = True
                print('      '+str(jet+1)+trai3+' 3')
            if target == 4:
                tirage.append(4)
                transformation = True
                print('      '+str(jet+1)+trai4+' 4')
            jet += 1
        # premier jet
        tirage1= list(tirage)
        for i,e in enumerate(tirage):
            if e == 3:
                tirage1[i]= 2
            if e == 4:
                tirage1[i]= 1
        # deuxieme jet
        tirage2= list(tirage)    
        for i,e in enumerate(tirage):
            if e == 3:
                tirage2[i]= 1
            if e == 4:
                tirage2[i]= 2
        # Découpage des deux trigrammes
        sub1= tirage1[:3]
        sub2= tirage1[3:]
        sub3= tirage2[:3]
        sub4= tirage2[3:]
        # Affichage uniquement en mode verbeux
        if aleph == True:
            print(tirage)   
            print(tirage1)
            print(tirage2)
            print(sub1,sub2)
            print(sub3,sub4)
        #####################################################################
        print("\n         ETAT INITIAL ")
        # On créer une liste conteneur pour afficher selon un ordre horizontale
        presentation= []
        presentation.append("    En Haut ")
        presentation.append("    ------- ")
        for i,element in enumerate(numerik):
            if element == sub1:
                artefact(i, presentation)

        presentation.append("    En Bas") 
        presentation.append("    ------")
        for i,element in enumerate(numerik):
            if element == sub2:
                artefact(i, presentation)

        # affichage
        print(presentation[0]+'     '+presentation[6])
        print(presentation[1]+'     '+presentation[7])
        print(presentation[2]+'      '+presentation[8])
        print(presentation[3]+'       '+presentation[9])
        print(presentation[4]+'       '+presentation[10])
        print(presentation[5]+'       '+presentation[11])

        # Recherche equivalence du tirage1 dans les valeurs du dico taOnumerik
        for e,i in taOnumerik.items():
            if i[0] == tirage1:
                print("\n      "+e)
                print('              '+i[1]+"\n")
                memoire= i[1]
        # Recherche de la position
        for index,e in enumerate(hexagramme):
            if e == memoire:
                print("              "+str(index+1))
                print(yinyang+ ' ' +oracle[index+1])
        #####################################################################
        if transformation == True:
            print("\n        TRANSFORMATION ")
            # je vide la liste pour la re-remplire
            presentation= []
            presentation.append("    En Haut ")
            presentation.append("    ------- ")
            for i,element in enumerate(numerik):
                if element == sub3:
                    artefact(i, presentation)
            presentation.append("    En Bas" )
            presentation.append("    ------")
            for i,element in enumerate(numerik):
                if element == sub4:
                    artefact(i, presentation)
            # Affichage
            print(presentation[0]+'     '+presentation[6])
            print(presentation[1]+'     '+presentation[7])
            print(presentation[2]+'       '+presentation[8])
            print(presentation[3]+'       '+presentation[9])
            print(presentation[4]+'       '+presentation[10])
            print(presentation[5]+'       '+presentation[11])


            # Recherche equivalence du tirage1 dans les valeurs du dico taOnumerik
            for e,i in taOnumerik.items():
                if i[0] == tirage2:
                    print("\n      "+e)
                    print('              '+i[1]+"\n")
                    memoire= i[1]
            # Recherche de la position
            for index,e in enumerate(hexagramme):
                if e == memoire:
                    print("              "+str(index+1))
                    print(yinyang+ ' ' +oracle[index+1])
        if transformation == False:
             print('Situation Stable\n Aucune Transformation')

