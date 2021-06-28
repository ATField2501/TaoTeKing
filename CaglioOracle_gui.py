#!/usr/bin/python3
#-*- coding: utf8

import tkinter as tk
from CaglioOracleClass import *


class Application(tk.Frame):
    ### Affichage de l'ecran
    ecran = " ::(;,,;)::"
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.creation_canvas()

    def create_widgets(self):
        ##### Commande Oracle
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Oracle"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        ##### Commande Aide
        self.hi = tk.Button(self)
        self.hi["text"] = "Aide"
        self.hi["command"] = self.appel_aide 
        self.hi.pack(side="top")
        ##### Commande Quitter
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="top")


    # Création du canvas
    def creation_canvas(self):
        cnv=tk.Canvas(root, width=300, height=400, bg="black")
        cnv.pack(padx=50, pady=50)
#        font = cnv.Font(family='Liberation Serif', size=12)
        cnv.create_text(10 , 25 ,text=Application.ecran,fill="red" )

    def say_hi(self):
        print("hi there, everyone!")

    def appel_aide(self):
        retour1 = Caglio.aide()
        Application.ecran = retour1
        self.creation_canvas()

Caglio= Cagliostro()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
