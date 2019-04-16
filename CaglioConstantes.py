""" Constantes du programme Caglio-Oracle """
aleph = False
transformation = False
# petit dico
tao={}
#Liste des charctère utf des hexagrammes
hexagramme = [u"\u4DC0",u"\u4DC1",u"\u4DC2",u"\u4DC3",u"\u4DC4",u"\u4DC5",u"\u4DC6",u"\u4DC7",u"\u4DC8",u"\u4DC9",u"\u4DCA",u"\u4DCB",u"\u4DCC",u"\u4DCD",u"\u4DCE",u"\u4DCF",
       u"\u4DD0",u"\u4DD1",u"\u4DD2",u"\u4DD3",u"\u4DD4",u"\u4DD5",u"\u4DD6",u"\u4DD7",u"\u4DD8",u"\u4DD9",u"\u4DDA",u"\u4DDB",u"\u4DDC",u"\u4DDD",u"\u4DDE",u"\u4DDF",
       u"\u4DE0",u"\u4DE1",u"\u4DE2",u"\u4DE3",u"\u4DE4",u"\u4DE5",u"\u4DE6",u"\u4DE7",u"\u4DE8",u"\u4DE9",u"\u4DEA",u"\u4DEB",u"\u4DEC",u"\u4DED",u"\u4DEE",u"\u4DEF",
       u"\u4DF0",u"\u4DF1",u"\u4DF2",u"\u4DF3",u"\u4DF4",u"\u4DF5",u"\u4DF6",u"\u4DF7",u"\u4DF8",u"\u4DF9",u"\u4DFA",u"\u4DFB",u"\u4DFC",u"\u4DFD",u"\u4DFE",u"\u4DFF"]
# trigramme representer par des listes
ciel=["***","***","***"]
terre=["* *","* *","* *"]
feu=["***","* *","***"]
tonnerre=["* *","* *","***"]
montagne=["***","* *","* *"]
ventBois=["***","***","* *"]
maraicage=["* *","***","***"]
eau=["* *","***","* *"]
# Dico des trigrammes avec en cle le nom de l'element et en valeur la liste du trigramme associé
trigramme= {}
trigramme['Ciel'] = ciel
trigramme['terre'] = terre
trigramme['feu'] = feu
trigramme['tonnerre'] = tonnerre
trigramme['montagne'] = montagne
trigramme['ventBois'] = ventBois
trigramme['maraicage'] = maraicage
trigramme['eau'] = eau
# Chaines de charactères representant les traies
trai1 = "  ___________"
trai2 = "  ____   ____"
trai3 = "  ____ O ____"
trai4 = "  _____X_____"
# code de trigrammes
c=[1,1,1]
t=[2,2,2]
f=[1,2,1]
to=[2,2,1]
mo=[1,2,2]
v=[1,1,2]
ma=[2,1,1]
e=[2,1,2]
numerik= [c,t,f,to,mo,v,ma,e]
