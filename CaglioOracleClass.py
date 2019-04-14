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

    def liste(self):
        """
        Affiche le Tao
        """
        print(tao)

    def hexa(self, indice):
        print(tao[indice])

    def tri(self):
        for cle, valeur in trigramme.items():
            print(cle+ ':')
            for e in valeur:
                print(e)

    def oracle(self):
        target = random.randint(1,64)
        print("{} {}".format(target,tao[str(target)]))
  
