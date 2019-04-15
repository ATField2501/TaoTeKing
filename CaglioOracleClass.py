#!/usr/bin/python3
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com>
# Oracle

from CaglioConstantes import *
import random

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
        print(tao)

    def hexa(self, indice):
        print(tao[indice])

    def tri(self):
        """
        Methode qui ffiche les trigrammes
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
        jet=0
        while jet < 7:
            target = random.randint(1,4)
            if target == 1:
                print(trai1)
            if target == 2:
                print(trai2)
            if target == 3:
                print(trai3)
            if target == 4:
                print(trai4)
            jet += 1
  
