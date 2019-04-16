#!/usr/bin/python3
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com>
# Oracle

from CaglioConstantes import *
import random


def artefact(i):
    if i == 0:
        print('    le Ciel')
        for e in ciel:
            print(' '+e)
    if i == 1:
        print('    la Terre')
        for e in terre:
            print(' '+e)
    if i == 2:
        print('    le Feu')
        for e in feu:
            print(' '+e)
    if i == 3:
        print('   le Tonerre')
        for e in tonnerre:
            print(' '+e)
    if i == 4:
        print('   la Montagne')
        for e in montagne:
            print(' '+e)
    if i == 5:
        print(' le Vent, le Bois')
        for e in ventBois:
            print(' '+e) 
    if i == 6:
        print(' les Maraicages')
        for e in maraicage:
            print(' '+e)
    if i == 7:
        print('    l Eau')
        for e in eau:
            print(' '+e)

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
        print("Caglio-Oracle -o (oracle)")
        print("Caglio-Oracle -t (lister 8 trigrammes)")
        print("Caglio-Oracle -H 12 (Afficher hexagramme n°12)")
        print("Caglio-Oracle -r (Rivière du Tao)")

    def liste(self):
        """
        Affiche le Tao
        """
        for e,i in tao.items():
            print(e, i,end='')


    def hexa(self, indice):
        print(tao[indice])

    def tri(self):
        """
        Methode qui affiche les trigrammes
        """
        for cle, valeur in trigramme.items():
            print(cle+ ':')
            for e in valeur:
                print(e)

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
                target = random.randint(0,63)
                ligne.append(tao[str(target)])
                nb += 1
            instant=""
            for e in ligne:
                instant += ' '+e+' ' 
            print(instant+ "\n")
            nb1 += 1

    def oracle(self):
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
                print(str(jet+1)+trai1+' 1')
            if target == 2:
                tirage.append(2)
                print(str(jet+1)+trai2+' 2')
            if target == 3:
                tirage.append(3)
                transformation = True
                print(str(jet+1)+trai3+' 3')
            if target == 4:
                tirage.append(4)
                transformation = True
                print(str(jet+1)+trai4+' 4')
            jet += 1
        print(tirage)   
        # premier jet
        tirage1= list(tirage)
        for i,e in enumerate(tirage):
            if e == 3:
                tirage1[i]= 2
            if e == 4:
                tirage1[i]= 1
        print(tirage1)
        # deuxieme jet
        tirage2= list(tirage)    
        for i,e in enumerate(tirage):
            if e == 3:
                tirage2[i]= 1
            if e == 4:
                tirage2[i]= 2
        print(tirage2)
        # Découpage des deux trigrammes
        sub1= tirage1[:3]
        sub2= tirage1[3:]
        sub3= tirage2[:3]
        sub4= tirage2[3:]
        print(sub1,sub2)
        print(sub3,sub4)
        print("    En Haut \n    -------")
        for i,element in enumerate(numerik):
            if element == sub1:
                artefact(i)
        print("    En Bas \n    ------" )
        for i,element in enumerate(numerik):
            if element == sub2:
                artefact(i)
        if transformation == True:
            print('  transformation')
            print("    En Haut \n    -------")
            for i,element in enumerate(numerik):
                if element == sub3:
                    artefact(i)
            print("    En Bas \n    ------" )
            for i,element in enumerate(numerik):
                if element == sub4:
                    artefact(i)
        else:
            print('Aucune Transformation')
