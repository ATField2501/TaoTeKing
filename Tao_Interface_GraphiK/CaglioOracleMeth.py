#!/usr/bin/python3
#-*- coding: utf8
# auteur: <atfield2501@gmail.com>
# Module complémentaire pour le programe CaglioOracle_Guy.py
# du Repository TaoTeKing      ^(;,,;)^


def Appel_tao(self, Caglio, Application):
    """
    Affichage d'une rivière d'hexagrames en transformation
    """
    Caglio.riviere()
    Application.zelote = True
    if Application.zelote == True:
        with open("tmp.tmp","r") as ff:
            retour=ff.read()
            self.label0.config(font=("Courier", 25)) 
            self.tatatext1.set(retour)
            self.tatatext2.set(".: Rivière de Tao :.")        
            self.after(250,self.appel_tao)

def Appel_tri(self, Caglio, Appication):
    """ Fonction d'appel de la liste des trigrames """    
#    Application.zelote = False        
    Caglio.tri()
    self.tatatext2.set(".: Liste des Trigrames :.")       
    caglioFichier1= open("tmp.tmp","r")
    retour= caglioFichier1.read()
    self.tatatext1.set(retour)
    caglioFichier1.close()


def Appel_oracle(self, Caglio, Application):
    """
    Appel de la méthode Oracle de la classe Cagliostro
    et mise à jour du canvas et des labels
    """
    Caglio.oracle(aleph = True)
    caglioListe=[]
    Application.zelote = False        

    with open("tmp.tmp", 'r') as filin:
        # Affichage lent de l'hexagrame en train de se tirer
        for e in filin.readlines():
            caglioListe.append(e)
            print(e)
    
    affichage=""
    for e in caglioListe[:6]:
        affichage += e
      
        self.canvas_tirage.grid(row=4, column=0)
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

    self.canvas_tirage2 = tk.Canvas(root, width=100, 
            height=130, bg='black')
    self.canvas_tirage2.grid(row=4, column=0)

    # Création fenetre annexe pour basculer l'affichage
    # du tirage
    supra=""
    compter=0
    for e in caglioListe[:6]:
        supra += e
        if e == "  ____      ____"+" \n" and compter==0:
            ### traçage du YANG
            self.canvas_tirage2 .create_line(20,25,40,40,
                    width=4, fill="chartreuse")
            self.canvas_tirage2 .create_line(60,40,80,40,
                    width=4, fill="chartreuse")        
        
        if e == "  ____      ____"+" \n" and compter==1:
            ### traçage du YANG
            self.canvas_tirage2 .create_line(20,40,40,40,
                    width=4, fill="chartreuse")
            self.canvas_tirage2 .create_line(60,40,80,40,
                    width=4, fill="chartreuse") 
        
        if e == "  ____      ____"+" \n" and compter==2:
            ### traçage du YANG
            self.canvas_tirage2.create_line(20,55,40,40,
                    width=4, fill="chartreuse")
            self.canvas_tirage2.create_line(60,40,80,40,
                    width=4, fill="chartreuse") 
        
        if e == "  ____      ____"+" \n" and compter==3:
            ### traçage du YANG
            self.canvas_tirage2.create_line(20,55,40,40,
                    width=4, fill="chartreuse")
            self.canvas_tirage2.create_line(60,40,80,40,
                    width=4, fill="chartreuse") 
        
        if e == "  ____      ____"+" \n" and compter==4:
            ### traçage du YANG
            self.canvas_tirage2.create_line(20,55,40,40,
                    width=4, fill="chartreuse")
            self.canvas_tirage2.create_line(60,40,80,40,
                    width=4, fill="chartreuse") 
        
        if e == "  ____      ____"+" \n" and compter==5:
            ### traçage du YANG
            self.canvas_tirage2.create_line(20,55,40,40,
                    width=4, fill="chartreuse")
            self.canvas_tirage2.create_line(60,40,80,40,
                    width=4, fill="chartreuse") 

        compter += 1
    self.canvas_tirage2.destroy()        
    
    self.test="Longue chaine de characteres"
    print(supra)
    if self.bTest.get() == 1: 
        self.label1=tk.Label(root, textvariable=":::",
                bg="black", fg="chartreuse" ,relief="ridge" ,
                borderwidth=2 , font=self.font2)
        self.label1.grid(row=5, column=0)
        self.label2=tk.Label(root, textvariable=self.test,
                bg="black", fg="chartreuse" ,relief="ridge" ,
                borderwidth=2 , font=self.font2)
        self.label2.grid(row=5, column=1)
        ## SUPER instruction à connaitre :/ 
        ## Mise à jour de l'affichage
    self.label1.update_idletasks()
    self.label2.update_idletasks()


#            self.after(500)        
    # mise à jour Entete 
    self.tatatext2.set(".: Oracle :.")        




def Hexagrame(self, Caglio , Application , tk , root):
#        self.chess2= tk.Button(superFenetre, 
#            text="Valider", fg='red',
#            anchor='nw',
#            ## utilisation d'une fonction lambda pour 
#            ## passer un parametre à la commande
#            command=lambda x=1:Application.retourValeur(self,
#                compteur))            
#
    Application.zelote = False        
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
