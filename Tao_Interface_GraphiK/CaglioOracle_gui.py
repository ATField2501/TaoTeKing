#!/usr/bin/python3
#-*- coding: utf8
# auteur: <atfield2501@gmail.com>
# Oracle graphique

import tkinter as tk
from CaglioOracleClass import *
import CaglioOracleMeth as Source
from tkinter.font import Font

class Application(tk.Frame):
    visu= "..:: (;,,;) ::.."
    indice= '44'
    zelote = False
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
#        self.pack()
        self.create_widgets()
        self.creation_canvas()
        self.creation_label1()
        self.creation_label2()
        
    def create_widgets(self):
        """ ya Cthulhu """

        # Création du cadre-conteneur pour les menus
        self.zoneMenu = tk.Frame(root, borderwidth=1, bg='ivory')
        self.zoneMenu.grid(row=1,column=0)

        # Création de l'onglet Fichier
        self.menuFichier = tk.Menubutton(self.zoneMenu,
                text='Executer', width='20', borderwidth=2, 
                bg='black', fg='chartreuse' ,
                activebackground='darkorange',
                relief = tk.RAISED)
        self.menuFichier.grid(row=1,column=0)

        # Création de l'onglet Edition
        self.menuEdit = tk.Menubutton(self.zoneMenu, text='Editer',
                width='20', borderwidth=2, bg='black', fg='chartreuse',
                activebackground='darkorange',relief = tk.RAISED)
        self.menuEdit.grid(row=1,column=1)

        # Création de l'onglet A Propos 
        self.menuFormat = tk.Menubutton(self.zoneMenu, text='A propos', 
                width='20', borderwidth=2, bg='black', fg='chartreuse',
                activebackground='darkorange',relief = tk.RAISED)
        self.menuFormat.grid(row=1,column=2)



        # Création du menu deroulant pour l'onglet Executer
        self.menuDeroulant1 = tk.Menu(self.menuFichier, tearoff = 0)
        self.menuDeroulant1.add_command(label='Oracle', 
                command = self.appel_oracle)
        self.menuDeroulant1.add_command(label="Tao", 
                command = self.appel_tao )
        self.menuDeroulant1.add_command(label="Trigrammes",
                command = self.appel_tri)
        self.menuDeroulant1.add_command(label="recherche Hexagramme",
                command = self.hexagrame)
        self.menuDeroulant1.add_command(label="Quitter",
                command = self.master.destroy)
        # Attribution du menu déroulant au menu Affichage
        self.menuFichier.configure(menu=self.menuDeroulant1)

        self.bTest = tk.IntVar()


        # Création du menu deroulant pour l'onglet Editer
        self.menuDeroulant2 = tk.Menu(self.menuEdit, tearoff = 0)
        self.menuDeroulant2.add_checkbutton(label='Verbeux', 
                variable=self.bTest, onvalue=1, offvalue=0)
        self.menuEdit.configure(menu=self.menuDeroulant2)
        

        # Création du menu deroulant pour l'onglet A Propos 
        self.menuDeroulant3 = tk.Menu(self.menuFormat, tearoff = 0)
        self.menuDeroulant3.add_command(label='Auteur', 
                command = self.appel_oracle)
        self.menuDeroulant3.add_command(label="Code Source", 
                command = self.appel_tao )
        self.menuFormat.configure(menu=self.menuDeroulant3)


    def creation_canvas(self):
        """ Label contenant le tirage """
        self.canvas_tirage = tk.Canvas(root, width=100, 
                height=130, bg='black')  
        # image
        self.fond = tk.PhotoImage(file="yinyang.png") 
        #image de fond 
        self.canvas_tirage.create_image(50, 65, image=self.fond)


#
#        self.canvas_tirage.create_oval(0,25,100,110,fill="chartreuse")
#        self.canvas_tirage.create_oval(20,25,80,70,fill="black")
#        self.canvas_tirage.create_oval(20,70,80,110,fill="ivory")
#        self.canvas_tirage.create_oval(44,45,52,53,fill="chartreuse")
#        self.canvas_tirage.create_oval(40,95,52,83,fill="black")

################# COORDONEE POUR TIRAGE
#        ### traçage du YIN
#        self.canvas_tirage.create_line(20,25,80,25, width=4, fill="chartreuse")
#        ### traçage du YANG
#        self.canvas_tirage.create_line(20,40,40,40, width=4, fill="chartreuse")
#        self.canvas_tirage.create_line(60,40,80,40, width=4, fill="chartreuse")
#        ### traçage du VIEUX YIN
#        self.canvas_tirage.create_line(20,55,80,55, width=4, fill="darkorange")        
#        ### traçage du VIEUX YANG
#        self.canvas_tirage.create_line(20,70,40,70, width=4, fill="darkorange")
#        self.canvas_tirage.create_line(60,70,80,70, width=4, fill="darkorange")
#
#
#        self.canvas_tirage.create_line(20,85,80,85, width=4, fill="chartreuse")
#
#        self.canvas_tirage.create_line(20,100,80,100, width=4, fill="chartreuse")
        self.canvas_tirage.grid(row=4, column=0)

    def creation_label1(self):
        """ Label contenant la traduction """
        self.tatatext1= tk.StringVar()
        self.tatatext1.set(" - TaoTéKing - \n"+yinyang)
        self.font = Font(family='Liberation Serif', size=32)
        self.font2 = Font(family='Liberation Serif', size=12)     
#        scrollbar = tk.Scrollbar(root)
#        scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
        self.label0 = tk.Label(root, textvariable=self.tatatext1 , 
                bg="black", fg='#00ff3e', relief="ridge" , 
                borderwidth=2 , font=self.font2)
        self.label0.grid(row=7, column=0)
    
    def creation_label2(self):
        """ Label l'entete """
        self.tatatext2= tk.StringVar()
        self.tatatext2.set(" - oba production - ")
        self.label = tk.Label(root, textvariable=self.tatatext2)
        self.label["fg"] = "yellow" 
        self.label['bg']='black'
        self.label.grid(row=3, column=0)



    ######################## action des commandes
    def appel_oracle(self):
        """ COMMANDE """
        Source.Appel_oracle(self, Caglio, Application)


    ## methode apppelé par les 64 boutons pour pouvoir renvoyer
    #  une valeur à la variable 'indice'
    def retourValeur(self,compteur):
        Application.indice = compteur

    def hexagrame(self):
        """ COMMANDE """
        Source.Hexagrame(self, Caglio, Application , tk , root)

    
    
    def appel_tao(self):
        """ COMMANDE """
        Source.Appel_tao(self, Caglio, Application)


    def appel_tri(self):
        """ COMMANDE """    
        Source.Appel_tri(self, Caglio, Application)


Caglio= Cagliostro()

root = tk.Tk()
root.title(' - TaoTéKing -')
root["bg"]="black"
root.geometry("800x600")

### Mode fullscreen (snippet)
root.attributes('-fullscreen', True)  
root.bind("<F11>",
                 lambda event: root.attributes("-fullscreen",
                            not root.attributes("-fullscreen")))
root.bind("<Escape>",
                 lambda event: root.attributes("-fullscreen",
                            False))
app = Application(master=root)
app.mainloop()

