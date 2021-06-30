#!/usr/bin/python3
#-*- coding: utf8

import tkinter as tk
from CaglioOracleClass import *
from tkinter.font import Font

class Application(tk.Frame):
    visu= "..... test (;,,;)"
    ### Affichage de l'ecran
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.creation_canvas()

    def visuel(self, retour):
        print(retour)
        Application.visu= retour 
        
    def create_widgets(self):
        ##### Commande Oracle
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Oracle"
        self.hi_there["command"] = self.oracle
        self.hi_there["fg"] = "green"
        self.hi_there.grid (column = 0, row = 0)

        # Commande Rivière de Tao
        self.riviere = tk.Button(self)
        self.riviere["text"] = "Rivière de Tao"
        self.riviere["command"] = self.appel_tao
        self.riviere["fg"] = "blue" 
        self.riviere.grid (column = 1, row = 0)
        
        # Commande Affichage Trigrammes
        self.trigrame = tk.Button(self)
        self.trigrame["text"] = "Trigrames"
        self.trigrame["command"] = self.appel_tri
        self.trigrame["fg"] = "cyan" 
        self.trigrame.grid (column = 2, row = 0)        
        
        ##### Commande Aide
        self.hi = tk.Button(self)
        self.hi["text"] = "Aide"
        self.hi["command"] = self.appel_aide 
        self.hi.grid (column = 3, row = 0)

        ##### Commande Quitter
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid (column = 4, row = 0)

    # Création du canvas
    def creation_canvas(self):
        self.cnv=tk.Canvas(root, width=300, height=400, bg="black")
        self.cnv.pack(padx=50, pady=50)
        font = Font(family='Liberation Serif', size=32)
        self.cnv.create_text(150 , 105 ,font=font, text="TaoTéKing",fill="red" )
    
    # action des commandes
    def oracle(self):
        print("Au secour!!")
        Caglio.oracle(aleph = True)
    
    def appel_aide(self):
        Caglio.aide()


#        Application.visuel(retour)
    
    def appel_tao(self):
        Caglio.riviere()
        ff=open("tmp.tmp","r")
        retour=ff.read()
        print(retour)
        font = Font(family='Liberation Serif', size=30)
        self.cnv.create_text(65 , 230 ,font=font,text=retour,fill="green" )
        ff.close()
#        Application.visuel(self.retour)


    
    def appel_tri(self):
        self.retour=Caglio.tri()

Caglio= Cagliostro()

root = tk.Tk()
root.title(' - TaoTéKing -')
app = Application(master=root)
app.mainloop()
