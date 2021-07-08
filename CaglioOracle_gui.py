#!/usr/bin/python3
#-*- coding: utf8
# auteur: <atfield2501@gmail.com>
# Oracle graphique

import tkinter as tk
from CaglioOracleClass import *
from tkinter.font import Font

class Application(tk.Frame):
    visu= "..:: (;,,;) ::.."
    indice= '44'
    ### Affichage de l'ecran
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.creation_label1()
        self.creation_label2()
        
        
    def create_widgets(self):
        """ ya Cthulhu """
        ##### Commande Oracle
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Oracle"
        self.hi_there["command"] = self.appel_oracle
        self.hi_there["fg"] = "green"
        self.hi_there['bg']='black'
        self.hi_there.grid (column = 0, row = 0)

        # Commande Rivière de Tao
        self.riviere = tk.Button(self)
        self.riviere["text"] = "Rivière de Tao"
        self.riviere["command"] = self.appel_tao
        self.riviere["fg"] = "green"
        self.riviere['bg']='black'
        self.riviere.grid (column = 1, row = 0)
        
        # Commande Affichage Trigrammes
        self.trigrame = tk.Button(self)
        self.trigrame["text"] = "Trigrames"
        self.trigrame["command"] = self.appel_tri
        self.trigrame["fg"] = "green" 
        self.trigrame['bg']='black'
        self.trigrame.grid (column = 2, row = 0)        
        
        ##### Commande Hexagrame
        self.hi = tk.Button(self)
        self.hi["text"] = "Hexagrame"
        self.hi["command"] = self.hexagrame
        self.hi.grid (column = 3, row = 0)
        self.hi["fg"] = "green"
        self.hi['bg']='black'

        ##### Commande Quitter
        self.quit = tk.Button(self, text="QUIT", fg="green",
                              command=self.master.destroy)
        self.quit.grid (column = 4, row = 0)
        self.quit['bg']='black'
    
    def creation_label1(self):
        """ ya Cthulhu """
        self.tatatext1= tk.StringVar()
        self.tatatext1.set(" - TaoTéKing - \n"+yinyang)
        self.font = Font(family='Liberation Serif', size=32)
        self.font2 = Font(family='Liberation Serif', size=12)        
        self.label0 = tk.Label(root, textvariable=self.tatatext1 , 
                bg="black", fg='#00ff3e', font=self.font2 )
        self.label0.pack(pady=55)
    

    def creation_label2(self):
        """ ya Cthulhu """
        self.tatatext2= tk.StringVar()
        self.tatatext2.set(" - oba production - ")
        self.label = tk.Label(root, textvariable=self.tatatext2)
        self.label["fg"] = "yellow" 
        self.label['bg']='black'
        self.label.pack(pady=5)


    ######################## action des commandes
    def appel_oracle(self):
        """
        Appel de la méthode Oracle de la classe Cagliostro
        et mise à jour des labels
        """
        Caglio.oracle(aleph = True)
        caglioListe=[]

        with open("tmp.tmp", 'r') as filin:
            # Affichage lent de l'hexagrame en train de se tirer
            for e in filin.readlines():
                caglioListe.append(e)
                print(e)
        
        affichage=""
        for e in caglioListe[:6]:
            affichage += e
            self.tatatext1.set(affichage)
            ## SUPER instruction à connaitre :/ 
            ## Mise à jour de l'affichage
            self.label.update_idletasks()
            self.after(500)

        with open("tmp2.tmp","r") as canin:
            retour= canin.read()       
            self.after(500)
            self.tatatext1.set(retour)

        # Création fenetre annexe pour basculer l'affichage
        # du tirage
        supra=""
        for e in caglioListe:
            supra += e
        superFenetre = tk.Toplevel(root, width=54, padx=2, pady=2)
        self.label=tk.Label(superFenetre, text=supra,
                bg="black", fg="chartreuse")
        self.label.pack()
        
        # mise à jour pied de page
        self.tatatext2.set(".: Oracle :.")        


    ## methode apppelé par les 64 boutons pour pouvoir renvoyer
    #  une valeur à la variable 'indice'
    def retourValeur(self,compteur):
        Application.indice = compteur

    def hexagrame(self):
#        self.chess2= tk.Button(superFenetre, 
#            text="Valider", fg='red',
#            anchor='nw',
#            ## utilisation d'une fonction lambda pour 
#            ## passer un parametre à la commande
#            command=lambda x=1:Application.retourValeur(self,
#                compteur))            
#
        indice = Application.indice 
        Caglio.hexa(indice)
        # mise à jour pied de page
        self.tatatext2.set(".: Hexagrame :.")        
        caglioFichier1= open("tmp.tmp","r")
        retour=caglioFichier1.read()
        self.tatatext1.set(retour)

#        Application.visuel(retour)
        caglioFichier1.close()
        # Création fenetre annexe
        superFenetre = tk.Toplevel(root,takefocus=True,)
        compteur=0
        while compteur <= 9:
            ##### Commande 64 boutons
            self.chess1= tk.Button(superFenetre, 
                    text=compteur, fg='green',
                    anchor='nw',
                    ## utilisation d'une fonction lambda pour 
                    ## passer un parametre à la commande
                    command=lambda x=1:Application.retourValeur(self,
                        compteur))
            self.chess1.pack(side='left', fill='both')
            compteur += 1 

    def appel_tao(self):
        Caglio.riviere()
        ff=open("tmp.tmp","r")
        retour=ff.read()
#        print(retour)
        self.tatatext1.set(retour)
        retour2 = tk.StringVar()
        retour2 = retour

        ff.close()
#        textCaglio.set(retour)
        self.tatatext2.set(".: Rivière de Tao :.")        
#        Application.visuel(self.retour)
#         self.after(250,self.appel_tao)

  
    def appel_tri(self):
        Caglio.tri()
        self.tatatext2.set(".: Liste des Trigrames :.")       
        caglioFichier1= open("tmp.tmp","r")
        retour= caglioFichier1.read()
        self.tatatext1.set(retour)
        caglioFichier1.close()


Caglio= Cagliostro()

root = tk.Tk()
root.title(' - TaoTéKing -')
root["bg"]="black"

app = Application(master=root)
app.mainloop()

