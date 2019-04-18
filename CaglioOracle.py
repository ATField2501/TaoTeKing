#!/usr/bin/python3
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com>
# Oracle

from CaglioOracleClass import *

import sys



# Lecture des arguments
if len(sys.argv) < 2:
    print("-Veuillez spécifier un argument-")
if len(sys.argv) > 1:
   action = sys.argv[1]
if len(sys.argv) == 3:
   indice = sys.argv[2]
   aleph = True



## Instance de l'objet Caglio 
Caglio= Cagliostro()

try:
   ####### Prompt d'aide
   if action == '-h':
       Caglio.aide()
   ####### Liste hexagramme  
   if action == '-l':
       Caglio.liste()  
   ####### hexagramme  
   if action == '-H':
      if aleph == True:
          ## Appel de la methode hexa à laquelle on passe l'argument indice
          Caglio.hexa(indice)
      if aleph == False:
          Caglio.hasard() 
   ####### Trigramme  
   if action == '-t':
       Caglio.tri()
   ###### Oracle
   if action == '-o':
       Caglio.oracle()
   ###### Rivière
   if action == '-r':
       Caglio.riviere()
except:
   pass
