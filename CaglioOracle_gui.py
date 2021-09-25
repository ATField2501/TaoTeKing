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
    zelote = True
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
        zelote=True
        self.riviere["command"] =self.appel_tao           
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
    
#    def creation_canvasl00(self):
#        """ Canvas contenant le tirage """
#        self.canvas_tirage = tk.Canvas(root, width=100, height=150, bg='green')   
#        self.canvas_tirage.create_oval(0, 0, 200, 200, outline="red", width=10)
#        self.canvas_tirage.create_line(0, 0, 200, 200, fill="black", width=10)
#        self.canvas_tirage.create_line(0, 200, 200, 0, fill="black", width=10)
#        self.canvas_tirage.pack()

    def creation_label1(self):
        """ Label contenant la traduction """
        self.tatatext1= tk.StringVar()
        self.tatatext1.set(" - TaoTéKing - \n"+yinyang)
        self.font = Font(family='Liberation Serif', size=32)
        self.font2 = Font(family='Liberation Serif', size=12)        
        self.label0 = tk.Label(root, textvariable=self.tatatext1 , 
                bg="black", fg='#00ff3e', font=self.font2 )
      
        self.label0.pack(pady=55, side='top')
    
    def creation_label2(self):
        """ Label contenant le pied de page """
        self.tatatext2= tk.StringVar()
        self.tatatext2.set(" - oba production - ")
        self.label = tk.Label(root, textvariable=self.tatatext2)
        self.label["fg"] = "yellow" 
        self.label['bg']='black'
        self.label.pack(pady=5, side='bottom')


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
            # Colorisation en fonction du traie tiré
            if e == "  ____      ____"+" \n":
                self.label0.config(fg='cyan')

            if e == "  ____________"+" \n" :
                self.label0.config(fg='blue')

            if e == "  ____  O  ____"+" \n" :
                self.label0.config(fg='pink')

            if e == "  ____  X  ____"+" \n" :
                self.label0.config(fg='yellow')



            self.tatatext1.set(affichage) 
            ## SUPER instruction à connaitre :/ 
            ## Mise à jour de l'affichage
            self.label.update_idletasks()
            self.after(500)
                
        self.label0.config(fg='chartreuse')

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

    def lanceurCommande(self):
        Application.zelote = False

    
    
    def appel_tao(self):
        Caglio.riviere()
        with open("tmp.tmp","r") as ff:
            retour=ff.read()
            self.label0.config(font=("Courier", 25)) 
            self.tatatext1.set(retour)
            self.tatatext2.set(".: Rivière de Tao :.")        
            if Application.zelote == True:
                self.after(250,self.appel_tao)
      
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
root.geometry("800x600")
app = Application(master=root)
app.mainloop()

