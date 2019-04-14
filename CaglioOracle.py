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



## Instance de l'objet Caglio 
Caglio= Cagliostro()

try:
   ####### Prompt d'aide
   if action == '-h':
       Caglio.aide()
   else:
       pass
   ####### Liste hexagramme  
   if action == '-l':
       Caglio.liste()  
   else:
       pass
   ####### hexagramme  
   if action == '-H':
      ## Appel de la methode hexa à laquelle on passe l'argument indice
      Caglio.hexa(indice) 
   else:
       pass
   ####### Trigramme  
   if action == '-t':
       Caglio.tri()
   else:
       pass
   ###### Oracle
   if action == '-o':
       Caglio.oracle()
   else:
       pass 
except:
   pass
