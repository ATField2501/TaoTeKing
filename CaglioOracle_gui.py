#!/usr/bin/python3
#-*- coding: utf8

import tkinter as tk
from CaglioOracleClass import *
from tkinter.font import Font

class Application(tk.Frame):
    visu= "..:: (;,,;) ::.."

    ### Affichage de l'ecran
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
#        self.creation_canvas()
        self.creation_label1()
        self.creation_label2()
        

    def visuel(self, retour):
        print(retour)
        Application.visu= retour 
        
    def create_widgets(self):
        ##### Commande Oracle
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Oracle"
        self.hi_there["command"] = self.oracle
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
        
        ##### Commande Aide
        self.hi = tk.Button(self)
        self.hi["text"] = "Aide"
        self.hi["command"] = self.appel_aide 
        self.hi.grid (column = 3, row = 0)
        self.hi["fg"] = "green"
        self.hi['bg']='black'

        ##### Commande Quitter
        self.quit = tk.Button(self, text="QUIT", fg="green",
                              command=self.master.destroy)
        self.quit.grid (column = 4, row = 0)
        self.quit['bg']='black'

    # Création du canvas
    def creation_canvas(self):
        self.cnv=tk.Canvas(root, width=300, height=400, bg="black")
        self.cnv.pack(padx=50, pady=50)
        self.font = Font(family='Liberation Serif', size=32)
        textCaglio = tk.StringVar() 
        textCaglio.set("TaoTéKing")
        self.cnv.create_text(150 , 105 ,font=self.font,
                                        text=textCaglio,
                                        fill="red" )
    def creation_label1(self):
        self.tatatext1= tk.StringVar()
        self.tatatext1.set(" - TaoTéKing - ")
        self.font = Font(family='Liberation Serif', size=32)
        self.label = tk.Label(root, textvariable=self.tatatext1 , 
                bg="black", fg='#00ff3e', font=self.font)

        self.label.pack(pady=55)
    

    def creation_label2(self):
        self.tatatext2= tk.StringVar()
        self.tatatext2.set(" - oba production - ")
        self.label = tk.Label(root, textvariable=self.tatatext2)
        self.label["fg"] = "yellow" 
        self.label['bg']='black'

        self.label.pack(pady=5)
    
    # action des commandes
    def oracle(self):
        Caglio.oracle(aleph = True)
        ff=open("tmp.tmp","r")
        retour=ff.read()
        self.tatatext1.set(retour)
        # Création fenetre anexe
        superFenetre = tk.Toplevel(root)
        self.label=tk.Label(superFenetre, text="TEST!!!!",bg="black", fg="chartreuse")
        self.label.pack()
        self.tatatext2.set(".: Oracle :.")        
        ff.close()
    def appel_aide(self):
        Caglio.aide()
        self.tatatext2.set(".: Aide :.")        
        caglioFichier1= open("tmp.tmp","r")
        retour=caglioFichier1.read()
        self.tatatext1.set(retour)


#        Application.visuel(retour)
    
    def appel_tao(self):
        Caglio.riviere()
        ff=open("tmp.tmp","r")
        retour=ff.read()
        print(retour)
        self.tatatext1.set(retour)
#        font = Font(family='Liberation Serif', size=30)
#        self.cnv.create_text(65 , 230 ,font=font,text=retour,fill="green" )
        ff.close()
#        textCaglio.set(retour)
        self.tatatext2.set(".: Rivière de Tao :.")        
#        Application.visuel(self.retour)
        self.after(250,self.appel_tao)


    
    def appel_tri(self):
        self.retour=Caglio.tri()
        self.tatatext2.set(".: Liste des Trigrames :.")        



Caglio= Cagliostro()

root = tk.Tk()
root.title(' - TaoTéKing -')
root["bg"]="black"
app = Application(master=root)
app.mainloop()
