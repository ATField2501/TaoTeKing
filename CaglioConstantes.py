""" Constantes du programme Caglio-Oracle """
aleph = False
transformation = False
memoire=0
yinyang=u"\u262F"
# petit dico
tao={}
#Liste des charctère utf des hexagrammes
hexagramme = [u"\u4DC0",u"\u4DC1",u"\u4DC2",u"\u4DC3",u"\u4DC4",u"\u4DC5",u"\u4DC6",u"\u4DC7",u"\u4DC8",u"\u4DC9",u"\u4DCA",u"\u4DCB",u"\u4DCC",u"\u4DCD",u"\u4DCE",u"\u4DCF",
       u"\u4DD0",u"\u4DD1",u"\u4DD2",u"\u4DD3",u"\u4DD4",u"\u4DD5",u"\u4DD6",u"\u4DD7",u"\u4DD8",u"\u4DD9",u"\u4DDA",u"\u4DDB",u"\u4DDC",u"\u4DDD",u"\u4DDE",u"\u4DDF",
       u"\u4DE0",u"\u4DE1",u"\u4DE2",u"\u4DE3",u"\u4DE4",u"\u4DE5",u"\u4DE6",u"\u4DE7",u"\u4DE8",u"\u4DE9",u"\u4DEA",u"\u4DEB",u"\u4DEC",u"\u4DED",u"\u4DEE",u"\u4DEF",
       u"\u4DF0",u"\u4DF1",u"\u4DF2",u"\u4DF3",u"\u4DF4",u"\u4DF5",u"\u4DF6",u"\u4DF7",u"\u4DF8",u"\u4DF9",u"\u4DFA",u"\u4DFB",u"\u4DFC",u"\u4DFD",u"\u4DFE",u"\u4DFF"]
# trigrammes représentés par leur code utf
utf_trigramme=[u"\u2630", u"\u2631",u"\u2632", u"\u2633",u"\u2634",u"\u2635",u"\u2636", u"\u2637" ]

# trigrammes representés par des listes
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
# Dictionnaire contenant les interprétation des hexagrammes
oracle= {}
chaine_redondante="Activitées Créatrice.\n      Influence\n      Amélioration\n      Persévérez."
oracle[1]="Le ciel en mouvement. La puissance du dragon. L\'homme se rend plus fort et infatigable.\n\n  -->> "+chaine_redondante
oracle[2]="La terre contient et soutient,\n  elle a les qualités d'une jument. L'homme ne devrait pas prendre l'initiative:\n il devrait chercher des amis à l'ouest et au sud et se passer d'amis à l'est et au nord\n\n -->> "+chaine_redondante
oracle[3]="L\'abîme s\'ouvre au dessus du tonerre.\n L'homme règle sa vie avec le même besoin que le tisserand à son metier.\n\n  -->> Succès.\n       Persévérez.\n       N'agissez pas inconsidérément.\n       Cherchez de l'aide."   
oracle[4]="Au pied de la montagne jaillit une source.\n L'homme est résolu et fortifi son charatère.\n Ce n'est pas moi qui recherche le jeune fou.\n C'est lui qui me recherche. Je leur aporterais mon enseignement.\n Je ne demande que la sincérité. S'ils se défont de leurs habitudes ils se heurteront à de graves difficultés.\n\n -->> Succès.\n      Si vous persévérez"     
oracle[5]="Des nuages montent dans le ciel.\n L'homme mange et bois. Il est joyeux.\n\n -->> Grand Succès.\n      Fortune si vous persévérez.\n      Vous pouvez traverser les grandes eaux."   
oracle[6]="Les eaux se dirigent vers l'Est, bien loi du ciel.\n En cas de conflit, l'homme connait l'importance des premiers pas.\n bien qu'il soit sincère, il rencontrera des obstacles.\n\n -->> Fortune si vous etes prudent.\n      Echec si vous menez le conflit à son terme.\n      Parlez avec le grand homme.\n      Ne traversez pas les grandes eaux."
oracle[7]="LA terrre recouvre l'abîme.\n L'homme noble nourrit et éduque son peuple transformant la multitude en armée.\n\n -->> Fortune.\n      Pas de blâme si vous persévérez\n      guidé par l'age et par l'expèrience."       
oracle[8]="L'abîme recouvre la terre.\n Les anciens rois partageaient leur terre en fiefs\n et entretenaient des relations amicales avec leurs princes.\n\n -->> Fortune.\n      Consultez l'oracle encore une fois\n      pour savoir si votre esprit est ferme et persévérant.\n      Alors il n'y a pas de blâme."
oracle[9]="Les vents du ciel:\n les grands courants célestes portent le temps.\n Ils viennent de l'Ouest, apportant des nuages épais, mais pas de pluie.\n L'homme nobleaffirme la forme exterieure de son être,\n manifestation sensible de ses qualités.\n\n -->> Succès"
oracle[10]="En haut le ciel, en bas le lac.\n L'homme distingue le haut et le bas,\n et agit en harmonie avec la volonté du peuple.\n\n -->> Vous marchez sur la queu du tigre\n      Il ne vous mors pas.\n      Fortune."
oracle[11]="Le ciel descend. LA terre monte. Ils s'unissent.\n L'osmose du ciel et de la terre se fait à l'extèrieur de l'homme.\n Le sage apporte cette harmonie au peuple.\n\n  --> ***"
oracle[12]="Le ciel et la terre se séparent.\n Les hommes ne se comprennent plus.\n Le grand s'en va. Le petit s'en vient.\n L'homme noble dissimule ses vraies qualités et évite les désastres.\n Il refuse toute récompense.\n\n  -->> Difficultés...\n       Même si vous persévérez."
oracle[13]="Un feu au-dessous du ciel sans limites.\n L'homme noble sépare les choses selon leur nature.\n\n  -->> Succès si vous persévérez.\n      Vous pouvez traversez les grandes eaux"
oracle[14]="Le feu au-dessus du ciel.\n L'homme noble réprime le mal et favorise le bien.\n dans l'esprit des lois divines.\n\n  -->> Grand Succès."
oracle[15]="La montagne s'éloigne derrière l'horizon.\n L'humilité crée le succès.\n\n -->> Equilibrez vos impulsions,\n      pour acquérir un jugement objectif."
oracle[16]="Le tonerre est la musique de la terre.\n Ainsi les anciens rois jouaient de la musique pour honorez les hommes de mérite.\n et l'offaient à Dieu en invitant leurs ancêtres à la cérémonie.\n\n -->> Rassembrez votre énergie\n      et agissez. "
oracle[17]="Au sein du lac, le tonerre est assoupi.\n A la tombée de la nuit, l'homme noble rentre chez lui\n et trouve le repos.\n\n  -->> Grand Succès.\n       Pas de blâme si vous persévérez."
oracle[18]="Au pied de la montagne souffle le vent.\n L'homme noble aide les autres et fortifie son caractère.\n\n  -->> Succès si vous persévérez.\n       Traverséez les grandes eaux.\n       Mais trois jours avant d'agir,\n       examinez soigneseusement la situation\n       et trois jours après,\n       rééxaminez-la."
oracle[19]="Au sein de la terre, le lac.\n Sol fertile.\n L'homme noble dispose d'une nourriture inépuisable\n qu'il partage avec les autres.\n\n -->> Succès si vous persévérez.\n      Lorsque vient le huitième mis, danger."
oracle[20]="Le vent souffle sur la terre.\n Les anciens rois accordaient leur lois aux coutumes des différents régions.\n L'adorateur a procédé à l'ablution mais il n'a pas encore présenté son offrande.\n\n -->> Perséverez.\n      Votre conduite pleine de dignité\n      attirera le respect"
oracle[21]="Les dents de la foudre illuminent la majesté du tonerre.\n En accordant leurs châtiments aux crimes commis,\n les anciens rois affermissez leur lois.\n\n  -->> Succès.\n       Laissez s'exercez la justice."
oracle[22]="Un feu brûle au pied de la montagne.\n L'homme noble est un excellent administrateur,\ mais il n'ose pas tenir le rôle d'un juge.\n\n -->> Persévérez\n      mais ne vous laissez pas déborder."
oracle[23]="La montagne repose sur la terre. L'homme noble renforce ses appuis en vue de maintenir sa position.\n\n  -->> N'entreprenez aucune action"
oracle[24]="Le tonerre au milieu de la terre. Lors du solstice d'hiver,\n les anciens roisfermaient les frontières, et obligeaient les marchands à prendre du repos.\n L'homme va et viens librement; il est sans blâme.\n Au septième jour, il revient; ses amis le congratulent.\n\n -->> Amélioration générale."
oracle[25]="Sous le ciel se meut naturellement le tonerre.\n Les anciens rois, en harmonie avec la nature,\n tenaient compte du rythme des saisons lorsqu'ils réglaient les affaires du pays\n et nourrissaient tous les êtres.\n\n  -->> Succès, si vous suivez votre voie.\n       Echec, si vouv vous en écartez.\n       Agissez avec prudence."
oracle[26]="Le ciel au milieu de la montagne.\n L'homme noble tire la leçon\n des paroles et des actes de l\'Histoire afin de connaîte ce qui est juste.\n\n  -->> Persévérez.\n       Eloignez-vous des honneurs.\n       N\'oubliez pas votre dette envers la société.\n       Vous pouvez traversez les grandes eaux."
oracle[27]="Au coeur de la montagne, le tonerre jaillit du volcan.\n L'homme supérieur contrôle sa bouche;\n ce qui y entre et ce qui en sort.\n\n  -->> Fortune si vous persévérez.\n      Soyez attentif à vos paroles et à votre nourriture."
oracle[28]="Le lac s\'élève au-dessus des arbres.\n LA poutre est fragile; elle va rompre.\n Seul et sans craintes, l'homme noble fait face.\n Il se retire du monde sans regrets.\n\n  -->> Succès si vous agissez."
oracle[29]="L'insondable au coeur de l'insondable.\n L'homme noble est un maître; il pratique ce qu'il enseigne.\n En raison de sa sincérité, on dit que son esprit est pénétrant.\n\n  -->> Toutes actions est la bienvenue."
oracle[30]="Le feu sur le feu. L'homme noble cultive son intelligence;\n sa lumière éclaire les régions proches et lointaines\n\n  -->> Soyez ferme.\n       Succès facile.\n       Fortune si vous êtes docile."
oracle[31]="L'étang est bercé par la montagne.\n L'homme noble est calme et chevaleresque.\n\n  -->> Succès,\b      Si vous persévérez et restez compréhensif."
oracle[32]="Tonerre et vent: image de l'éternelle durée.\n L'homme noble conserve une attitude ferme et ne change pas de dirrection.\n\n  -->> Succès,\n       Pas de blâme si vous persévérez.\n       Toute action est avantageuse."
oracle[33]="La montagne sort de la terre mais reste en-dessous du ciel. L'homme noble tient le vulgaire \n à distance avec mesure et dignité.\n Il ne dévoile pas ses penssées.\n\n -->> Amélioration.\n      Dans les petites choses,\b      la persévérence est avantageuse."
oracle[34]="Le tonerre fait rage au-dessus du ciel. Les gestes de l(homme noble sont toujours justes.\n\n --> Amélioration si vous persévérez."
oracle[35]="Le soleil brille au-dessus de la terre.\n L'homme noble affirme sa lumière.\n Il assure la tranquilité en société,\n et il est gratifié de cheveaux en grand nombre.\n Il est reçu en audience trois fois par jour.\n\n  -->> Amélioration."
oracle[36]="Le soleil se couche derrière la terre.\n L'homme noble conduit les autres. Il montre son intelligence\n en conservant une attitude calme et détachée.\n\n  -->> Persévérez\n       Anticipez sur les difficultés."
oracle[37]="Le vent passe au-dessus du feu et réchauffe la famille.\n L'homme noble adopteune attitude franche et durable.\n LA femme persévère.\n\n  -->> Persévérez."
oracle[38]="Le feu au-dessus du lac.\n Quelles que soient les normes sociales,\n l'homme noble conserve son individualité.\n\n -->> Succès dans les petites choses."
oracle[39]="Au sein du volcan, le lac.\n L'homme noble regarde en lui-même et fortifie son charactère.\n\n -->> Restez en terrain connu\n      et evitez les hostilités.\n      Parlez avec le grand homme.\n      Fortune si vous persévérez."
oracle[40]="Le tonerre gronde, libérant des rafales de pluie.\n L'homme noble reste en terrain connu.\n Il pardonne les fautes et absout ceux qui lui ont fait du tort.\n\n -->> Il est avantageux d'agir rapidement\n      en cas de nécéssité.\n      Il est avantageux de rester tranquille\n      si l'action ne s'impose pas naturellemnt à vous."
oracle[41]="Au pied de la montagne, le lac.\n L'homme maîtrise sa colère et réfrène ses désirs.\n\n  -->> Grande Fortune.\n       Pas de blâme.\n       Agissez comme bon vous semble.\n       Persévérez.\n       Offrez deux paniers de grain\n       même si c'est tout ce que vous possédez."
oracle[42]="Le vent et le tonerre se soutiennent mutuellement.\n L'homme noble cultive ses qualités et non ses defauts.\n\n  -->> Amélioration générale.\n       Vous pouvez traversez les grandes eaux."
oracle[43]="Au-dessus du ciel, le lac.\n L'homme noble disperse ses richesses autour de lui\n et les utilise avec sagesse.\n\n  -->> Vous devez exposer la situation\n       au siège du gouvernement,\n       avec ardeur et sincérité.\n       Danger et difficultés.\n       Informez votre propre ville,\n       mais ne prenez pas les armes.\n       Amélioration générale."
oracle[44]="Le vent souffle sous le ciel.\n Le prince hurle ses ordres et les fait proclamer au quatre vents.\n\n  -->> Un femme forte et autoritaire;\n       gardez vous de tous rapport avec elle."
oracle[45]="Le lac au-dessus de la terre.\n L'homme noble prépare ses armes,\n et se tient prêt à toute éventualité.\n\n  -->> Parlez avec le grand homme.\n       Succès si vous persévérez.\n       Fortune tant que vous srez prêt à en payer le prix "
oracle[46]="Les arbres sortent de la terre.\n L'homme noble se concentre et tire avantage des petites choses\n pour en accomplire de grandes.\n Il avance en terrain familier.\n\n -->> Succès.\n      Vous pouvez voir le grand homme sans crainte."
oracle[47]="Le lac s'écoule dans l'abîme.\n L'homme supérieur consent au sacrifice suprême pour suivre sa volonté.\n\n -->> Succès.\n      Fortune si vous persévérez.\n      Pas de blâme.\n      Ne faites aucune promesse."
oracle[48]="L'abîme est retenu par le bois et transformé en puits.\n Le plan d'une ville peut changer, mais ses puits restent au même endroit.\n L'eau du puit ne disparaît ni ne déborde.\n Elle fut utilisée par ceux qui viendront après.\n L'homme noble encourage le peuple et exhorte à l'aide mutuelle.\n\n -->> Echec si la cruche se brise\n      avant que l'eau ne soit tirée."
oracle[49]="Au coeur du lac, le feu.\n L'homme noble consulte les étoiles et règle le rythme des saisons.\n\n -->> Lorsqe cela est accompli,\n      tout le monde y croit.\n      Succès.\n      Persévérez\n      et le remords disparaîtra."
oracle[50]="Les flammes lèchent le bois.\n L'homme noble surveille le feu et assure le succés du sacrifice.\n\n -->> Grande Fortune."
oracle[51]="Le tonerre suit le tonerre.\n L'homme supérieur, dans l'appréhension et la crainte,\n cultive ses qualités et examine ses défauts.\n\n  -->> Lorsque le tonnerre vient,\n       restez sur vos gardes,\n       mais souriez et parlez gaiement.\n       Lorsque le tonerre sème l'effroi\n       sur une distance de cent milles,\n       soyez comme le disciple sincère\n       qui ne laisse pas tomber une seule goutte\n       de vin sacrificiele."
oracle[52]="La montagne survole la montagne.\n L'homme noble se concentre sur ses activités immédiates.\n Son dos est immobilisé, si bien qu'il ne sent plus son corps.\n Il entre dans sa cour et ne voit plus ses hommes.\n\n  -->> Pas de blâme."
oracle[53]="Sur la montagne est un arbre.\n L'homme noble cultive ses qualités, et donne l'exemple aux autres.\n La jeune fille célèbre son mariage.\n\n  -->> Fortune.\n        Persévérez."
oracle[54]="Au dessus du lac est le tonerre.\n L'homme qui connait l'éternité de la fin\n connait les épreuves du commencement.\n\n  -->> Danger.\n       L'action conduit à l'échec."
oracle[55]="Au plus fort de l'orage, foudre et tonerre.\n L'homme dirige les procès et tranche équitablement.\n\n  -->> Lorsque les gouvernements atteignent la prospérité,\n       ils n'ont pas à craindre leur déclin.\n       Soyez comme le soleil de midi.\n       Amélioration."
oracle[56]="Au-dessus de la montagne est le feu.\n L'homme noble agit avec sagesse et prudence; il ne fait trainer aucun différend en longueur.\n\n -->> Légère amélioration.\n      Fortune si vous persévérez."
oracle[57]="Deux vents pénètrent dans tous les coins et recoins.\n L'homme noble réaffirme ses ordres et execute ses entreprises.\n\n  -->> Amélioration.\n       Surtout si vous restez fidèle\n       à votre voie.\n       Parlez avec le grand homme."
oracle[58]="La surface du lac est tanquille; mais ses profondeurs bouillonnent de vie.\n Auprès du lac, les amis s'assoient et discutent.\n Leur conversation semble superficielle, mais leur communion est profonde.\n\n  -->> Succès si vous persévérez."
oracle[59]="Le vent vagabonde au-dessus des eaux; les eaux s'évaporent.\n Les anciens rois étaient pieux et se consacraient au service de Dieu.\n Ils construisent le temple ou le roi actuel vient faire ses dévotions.\n\n  --> Succès.\n      Persévérez.\n      Vous pouvez traversez les grandes eaux."
oracle[60]="Au sein de l'abîme, le lac.\n L'homme noble recherche systématiquement la perfection.\n\n  -->> Amélioration;\n       même si les contraintes\n       sont sévères et difficiles,\n       elles ne dureront pas."
oracle[61]="Le vent souffle au-dessus du lac.\n L'homme noble examine avec soin tous les litiges,\n et retarde les executions.\n\n  --> Porcs et poissons.\n      Fortune.\n      Persévérez.\n      Vous pouvez traversez les grandes eaux."
oracle[62]="Le tonerre est sur la montagne.\n L'homme noble adopte une attitude pleine de sagesse;\n par les temps d'humilité, il se montre réservé; par les temps de deuil, il se montre triste;\n par les temps de disette, il se montre frugale.\n\n  -->> Amélioration. Persévérez.\n       Soyez modeste.\n       N'entreprenez aucune action importante.\n       Ecoutez l'alouette\n       dont le chant devient plus doux\n       alors qu'elle amorce sa descente.\n       Grande Fortune."
oracle[63]="Au-dessus du feu, l'eau.\n L'homme noble considère le mal et s'arme contre lui.\n\n  -->> Succès dans les petites choses.\n       Persévérez.\n       Un commencement heureux\n       peut conduir à la fortune."
oracle[64]="Au-dessus de l'eau, le feu.\n L'homme noble voit les choses telles qu'elles sont afin de les harmoniser.\n\n  -->> Le jeune renard croit\n       avoir traversé la rivière;\n       mais il a la queue mouillée.\n       Fortune.\n       Echec si vous agissez comme le renard."
