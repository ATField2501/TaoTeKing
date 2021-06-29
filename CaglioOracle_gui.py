#!/usr/bin/python3
#-*- coding: utf8

import tkinter as tk
from CaglioOracleClass import *


class Application(tk.Frame):
    visu=" :(;,,;):"
    ### Affichage de l'ecran
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.creation_canvas()

    def visuel(self, *args):
        print(args)
        Application.visu= args
        
    def create_widgets(self):
        ##### Commande Oracle
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Oracle"
        self.hi_there["command"] = self.say_hi
        self.hi_there["fg"] = "green"
        self.hi_there.grid (column = 0, row = 0)

        # Rivière de Tao
        self.riviere = tk.Button(self)
        self.riviere["text"] = "Rivière de Tao"
        self.riviere["command"] = self.appel_tao
        self.riviere["fg"] = "blue" 
        self.riviere.grid (column = 1, row = 0)
        
        ##### Commande Aide
        self.hi = tk.Button(self)
        self.hi["text"] = "Aide"
        self.hi["command"] = self.appel_aide 
        self.hi.grid (column = 2, row = 0)

        ##### Commande Quitter
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid (column = 3, row = 0)

    # Création du canvas
    def creation_canvas(self):
        cnv=tk.Canvas(root, width=300, height=400, bg="black")
        cnv.pack(padx=50, pady=50)
#        font = cnv.Font(family='Liberation Serif', size=12)
        cnv.create_text(10 , 25 ,text=Application.visu,fill="red" )
    
    # action des commandes
    def say_hi(self):
        print("Au secour!!")

    def appel_aide(self):
        self.retour = Caglio.aide()
        Application.visuel(self.retour)
    def appel_tao(self):
        self.retour = Caglio.riviere()
        Application.visuel(self.retour)


Caglio= Cagliostro()

root = tk.Tk()
root.title(' - TaoTéKing -')
app = Application(master=root)
app.mainloop()
