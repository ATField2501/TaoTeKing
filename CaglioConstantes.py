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
ciel=["     ***","     ***","     ***"]
terre=["     * *","     * *","     * *"]
feu=["     ***","     * *","     ***"]
tonnerre=["     * *","     * *","     ***"]
montagne=["     ***","     * *","     * *"]
ventBois=["     ***","     ***","     * *"]
maraicage=["     * *","     ***","     ***"]
eau=["     * *","     ***","     * *"]
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
# Chaines de charactères representant les traies yin, yang, yin/yang, yang/yin
trai1 = "  ___________"
trai2 = "  ____   ____"
trai3 = "  ____ O ____"
trai4 = "  _____X_____"
# codes numériques des trigrammes
c=[1,1,1]
t=[2,2,2]
f=[1,2,1]
to=[2,2,1]
mo=[1,2,2]
v=[1,1,2]
ma=[2,1,1]
e=[2,1,2]
# Liste des codes numériques
numerik= [c,t,f,to,mo,v,ma,e]
# Les 64 Hexagrammes representés par un dictionnaire contenant en valeure la suite numérique (haut + bas) des deux trigrammes et en cle le nom de celui-ci
taOnumerik={}
taOnumerik["K\'IEN - Le Yang"]= c + c 
taOnumerik["K\'OUEN - Le Yin"]= t + t 
taOnumerik["TCHOUEN - La Difficulté Initiale"]= e + to
taOnumerik["MONG - La Folie Juvénile"]= mo + e
taOnumerik["SU - L'Attente"]= e + c
taOnumerik["SOUNG - Le Conflit"]= c + e
taOnumerik["SZE - L\'Armée"]= t + e
taOnumerik["PI - L'Union"]= e + t
taOnumerik["SIAO TCH\'OU - Le Pouvoir D'Apprivoisement du Petit"]= v + c
taOnumerik["LIU - La Marche"]= c + ma
taOnumerik["T\'AI - La Paix"]= t + c
taOnumerik["P\'I - La Stagnation"]= c + t
taOnumerik["T\'ONG JEN - La Societé"]= c + f
taOnumerik["TA YEOU - La Richesse"]= f + c
taOnumerik["K\'IEN - L'Humilité"]= t + mo
taOnumerik["YU - L'Enthousiasme"]= to + t
taOnumerik["SOUEI - La Suite"]= ma + to
taOnumerik["KOU - La Réparation"]= mo + v
taOnumerik["LIN - L'Approche"]= t + ma
taOnumerik["KOUAN - La Contemplation"]= v + t
taOnumerik["CHE HO - Mordre au Travers"]= f + to
taOnumerik["PII - La Beauté"]= mo + f
taOnumerik["Po - L'Eclatement"]= mo + t
taOnumerik["FOU - Le Retour"]= t + to
taOnumerik["WOU WANG - La Simplicité"]= c + to
taOnumerik["TA TCH\'OU - Le Pouvoir D'Apprivoisement du Grand"]= mo + c
taOnumerik["YE - La Nourriture"]= mo + to
taOnumerik["TA KOUO - La Prépondérance du Grand"]= ma + v
taOnumerik["K\'AN - L'Insondable"]= e + e
taOnumerik["LI - Le Feu"]= f + f
taOnumerik["HIEN - L'Inflence"]= ma + mo
taOnumerik["HONG - La Durée"]= to + v
taOnumerik["TOUEN - La Retraite"]= c + mo
taOnumerik["TA TCHOUANG - La Puissance du Grand"]= to + c 
taOnumerik["TSIN - Le Progrès"]= c + t
taOnumerik["Ming Yi - L\'Obscurcissement de la Lumière"]= t + f
taOnumerik["KIA JEN - La Famille"]= v + f
taOnumerik["K\'OUEI - La Neutralité"]= f + ma
taOnumerik["KI - L\'Obstacle"]= e + mo
taOnumerik["HIAI - La Libération"]= to + e
taOnumerik["SOUEN - La Récession"]= mo + ma
taOnumerik["YI - L\'Expansion"]= v + to
taOnumerik["KOUAI - LA Percée"]= ma + c
taOnumerik["KEOU - La Tentation"]= c + v
taOnumerik["TS\'OUEI - L\'Accord"]= ma + t
taOnumerik["CHENG - La Poussée vers le Haut"]= t + v     
taOnumerik["K\'OUENII - L'Accablement"]= ma + e
taOnumerik["TSING - Le Puit"]= e + v
taOnumerik["KO - La Révolution"]= ma + f
taOnumerik["TING - Le Chaudron"]= f + v
taOnumerik["TCHEN - Le Tonerre"]= to + to
taOnumerik["KEN - L\'Immobilité"]= mo + mo
taOnumerik["TSIEN - Le Developpement"]= v + mo
taOnumerik["KOUEI MEI - La Jeune Mariée"]= to + ma
taOnumerik["FONG - L\'Abondance"]= to + f
taOnumerik["LU - Le Voyageur"]= f + mo
taOnumerik["SOUEN - La Peetration du Vent"]= v + v 
taOnumerik["TOUEI - La Joie"]= ma + ma 
taOnumerik["HOUAN - La Dissolution"]= v + e
taOnumerik["TSIE - La Limitation"]= e + ma 
taOnumerik["TCHOUNG FOU - La Connaissance"]= v + ma 
taOnumerik["SIAO KOUO - La Prépondérance du Petit"]= to + mo 
taOnumerik["KI TSI - L\'Accomplissement"]= e + f 
taOnumerik["WEI TSI - Avant L\'Accomplissement"]= f + e                       
