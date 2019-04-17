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
# Les 64 Hexagrammes representés par un dictionnaire contenant en valeure la suite numérique (haut + bas) des deux trigrammes plus l'element de la liste des code utf correspondants et en cle le nom de celui-ci
taOnumerik={}
taOnumerik["K\'IEN - Le Yang"]= c + c , hexagramme[0]
taOnumerik["K\'OUEN - Le Yin"]= t + t , hexagramme[1]
taOnumerik["TCHOUEN - La Difficulté Initiale"]= e + to , hexagramme[2]
taOnumerik["MONG - La Folie Juvénile"]= mo + e , hexagramme[3]
taOnumerik["SU - L'Attente"]= e + c , hexagramme[4]
taOnumerik["SOUNG - Le Conflit"]= c + e , hexagramme[5]
taOnumerik["SZE - L\'Armée"]= t + e , hexagramme[6]
taOnumerik["PI - L'Union"]= e + t , hexagramme[7]
taOnumerik["SIAO TCH\'OU - Le Pouvoir D'Apprivoisement du Petit"]= v + c , hexagramme[8]
taOnumerik["LIU - La Marche"]= c + ma , hexagramme[9]
taOnumerik["T\'AI - La Paix"]= t + c , hexagramme[10]
taOnumerik["P\'I - La Stagnation"]= f + t , hexagramme[11]
taOnumerik["T\'ONG JEN - La Societé"]= c + f , hexagramme[12]
taOnumerik["TA YEOU - La Richesse"]= f + c , hexagramme[13]
taOnumerik["K\'IEN - L'Humilité"]= t + mo , hexagramme[14]
taOnumerik["YU - L'Enthousiasme"]= to + t , hexagramme[15]
taOnumerik["SOUEI - La Suite"]= ma + to , hexagramme[16]
taOnumerik["KOU - La Réparation"]= mo + v , hexagramme[17]
taOnumerik["LIN - L'Approche"]= t + ma , hexagramme[18]
taOnumerik["KOUAN - La Contemplation"]= v + t , hexagramme[19]
taOnumerik["CHE HO - Mordre au Travers"]= f + to , hexagramme[20]
taOnumerik["PII - La Beauté"]= mo + f , hexagramme[21]
taOnumerik["Po - L'Eclatement"]= mo + t , hexagramme[22]
taOnumerik["FOU - Le Retour"]= t + to , hexagramme[23]
taOnumerik["WOU WANG - La Simplicité"]= c + to , hexagramme[24]
taOnumerik["TA TCH\'OU - Le Pouvoir D'Apprivoisement du Grand"]= mo + c , hexagramme[25]
taOnumerik["YE - La Nourriture"]= mo + to , hexagramme[26]
taOnumerik["TA KOUO - La Prépondérance du Grand"]= ma + v , hexagramme[27]
taOnumerik["K\'AN - L'Insondable"]= e + e , hexagramme[28]
taOnumerik["LI - Le Feu"]= f + f , hexagramme[29]
taOnumerik["HIEN - L'Inflence"]= ma + mo , hexagramme[30]
taOnumerik["HONG - La Durée"]= to + v , hexagramme[31]
taOnumerik["TOUEN - La Retraite"]= c + mo , hexagramme[32]
taOnumerik["TA TCHOUANG - La Puissance du Grand"]= to + c , hexagramme[33] 
taOnumerik["TSIN - Le Progrès"]= c + t , hexagramme[34]
taOnumerik["Ming Yi - L\'Obscurcissement de la Lumière"]= t + f , hexagramme[35]
taOnumerik["KIA JEN - La Famille"]= v + f , hexagramme[36]
taOnumerik["K\'OUEI - La Neutralité"]= f + ma , hexagramme[37]
taOnumerik["KI - L\'Obstacle"]= e + mo , hexagramme[38]
taOnumerik["HIAI - La Libération"]= to + e , hexagramme[39]
taOnumerik["SOUEN - La Récession"]= mo + ma , hexagramme[40]
taOnumerik["YI - L\'Expansion"]= v + to , hexagramme[41]
taOnumerik["KOUAI - LA Percée"]= ma + c , hexagramme[42]
taOnumerik["KEOU - La Tentation"]= c + v , hexagramme[43]
taOnumerik["TS\'OUEI - L\'Accord"]= ma + t , hexagramme[44]
taOnumerik["CHENG - La Poussée vers le Haut"]= t + v , hexagramme[45]    
taOnumerik["K\'OUENII - L'Accablement"]= ma + e , hexagramme[46]
taOnumerik["TSING - Le Puit"]= e + v , hexagramme[47]
taOnumerik["KO - La Révolution"]= ma + f , hexagramme[48]
taOnumerik["TING - Le Chaudron"]= f + v , hexagramme[49]
taOnumerik["TCHEN - Le Tonerre"]= to + to , hexagramme[50]
taOnumerik["KEN - L\'Immobilité"]= mo + mo , hexagramme[51]
taOnumerik["TSIEN - Le Developpement"]= v + mo , hexagramme[52]
taOnumerik["KOUEI MEI - La Jeune Mariée"]= to + ma , hexagramme[53]
taOnumerik["FONG - L\'Abondance"]= to + f , hexagramme[54]
taOnumerik["LU - Le Voyageur"]= f + mo , hexagramme[55]
taOnumerik["SOUEN - La Pénetration du Vent"]= v + v , hexagramme[56]
taOnumerik["TOUEI - La Joie"]= ma + ma , hexagramme[57]
taOnumerik["HOUAN - La Dissolution"]= v + e , hexagramme[58]
taOnumerik["TSIE - La Limitation"]= e + ma , hexagramme[59]
taOnumerik["TCHOUNG FOU - La Connaissance"]= v + ma , hexagramme[60]
taOnumerik["SIAO KOUO - La Prépondérance du Petit"]= to + mo , hexagramme[61]
taOnumerik["KI TSI - L\'Accomplissement"]= e + f , hexagramme[62]
taOnumerik["WEI TSI - Avant L\'Accomplissement"]= f + e , hexagramme[63]   
                  
