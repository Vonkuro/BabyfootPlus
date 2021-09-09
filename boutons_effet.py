import Capteur
from Page_Choix import *
from Page_Jeu import *
import tkinter as Tk
import time

# ----- Changement des écrans

#les quatres modes de jeu

def versClassique(menu : Menu, classique: EnJeu, ecran: Tk):
    menu.cache()

    #Titre
    classique.Label_titre.configure(text= "Classique", font= "Arial, 50", bg= "#000000", fg="#ffffff")
    classique.Label_titre.place(x=810 , y=64.81)

    #remise à zero du score et du chrono
    classique.Label_chrono.configure(text="00 : 00", font= "Arial, 150", bg= "#818181", fg="#ffffff")
    classique.Label_score_rouge.configure(text="00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")
    classique.Label_score_bleu.configure(text="00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")

    #configure le mode de jeu demandé : Bouton commencer la partie
    classique.Bouton_debut.configure(command=lambda:debutPartie(classique, "classique", ecran))
    classique.Bouton_relance.configure(command=lambda: relancePartie(classique, "classique", ecran))
    
    classique.affiche()

def versChrono(menu: Menu, chrono: EnJeu, ecran: Tk):
    menu.cache()
    
    #Titre
    chrono.Label_titre.configure(text= "Chrono", font= "Arial, 50", bg= "#000000", fg="#ffffff")
    chrono.Label_titre.place(x=850 , y=64.81)
    
    #remise à zero du score et du chrono
    chrono.Label_chrono.configure(text="10 : 00", font= "Arial, 150", bg= "#818181", fg="#ffffff")
    chrono.Label_score_rouge.configure(text="00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")
    chrono.Label_score_bleu.configure(text="00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")


    #configure le mode de jeu demandé : Bouton commencer la partie
    chrono.Bouton_debut.configure(command=lambda:debutPartie(chrono, "chrono", ecran))
    chrono.Bouton_relance.configure(command=lambda: relancePartie(chrono, "chrono", ecran))
 
    chrono.affiche()

def versChronoTemps(menu: Menu, chronoTemps: EnJeu, ecran: Tk):
    menu.cache()
    
    #Titre
    chronoTemps.Label_titre.configure(text= "Chrono 10 min", font= "Arial, 50", bg= "#000000", fg="#ffffff")
    chronoTemps.Label_titre.place(x=770 , y=64.81)
    
    #remise à zero du score et du chrono
    chronoTemps.Label_chrono.configure(text="10 : 00", font= "Arial, 150", bg= "#818181", fg="#ffffff")
    chronoTemps.Label_score_rouge.configure(text="00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")
    chronoTemps.Label_score_bleu.configure(text="00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")

    #configure le mode de jeu demandé : Bouton commencer la partie
    chronoTemps.Bouton_debut.configure(command=lambda:debutPartie(chronoTemps, "chronoTemps", ecran))
    chronoTemps.Bouton_relance.configure(command=lambda: relancePartie(chronoTemps, "chronoTemps", ecran))

    chronoTemps.affiche()

def versChronoBut(menu: Menu, chronoBut: EnJeu, ecran: Tk):
    menu.cache()
    
    #Titre
    chronoBut.Label_titre.configure(text= "Chrono buts", font= "Arial, 50", bg= "#000000", fg="#ffffff")
    chronoBut.Label_titre.place(x=790 , y=64.81)

    #remise à zero du score et du chrono
    chronoBut.Label_chrono.configure(text="10 : 00", font= "Arial, 150", bg= "#818181", fg="#ffffff")
    chronoBut.Label_score_rouge.configure(text="00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")
    chronoBut.Label_score_bleu.configure(text="00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")

    #configure le mode de jeu demandé : Bouton commencer la partie
    chronoBut.Bouton_debut.configure(command=lambda:debutPartie(chronoBut, "chronoBut", ecran))
    chronoBut.Bouton_relance.configure(command=lambda: relancePartie(chronoBut, "chronoBut", ecran))
    
    chronoBut.affiche()

#bouton de retour (flèche en arriere)
def versMenu(enJeu: EnJeu, menu: Menu):
    enJeu.cache()
    menu.affiche()


# ----- Apparition et disparition des widgets

#Bouton pour démarrer la partie 
#disparition : bouton retour(flèche en arriere) et bouton debut
#apparition : bouton arret et bouton pause
def debutPartie(enJeu: EnJeu, mode, ecran):

    enJeu.Bouton_retour.place_forget()
    enJeu.Bouton_debut.place_forget()
    
    enJeu.Bouton_arret.place(x=203,y=0)
    enJeu.Bouton_pause.place(x=1069,y=0)

    enJeu.Label_score_rouge.configure(text="00")
    enJeu.Label_score_bleu.configure(text="00")
    
    Capteur.Pause = False

    Capteur.initialisation()
    ecran.update()

    if mode=="classique":
        Capteur.classique(enJeu, ecran)
    elif mode=="chrono":
        Capteur.chrono(enJeu, ecran)
    elif mode=="chronoTemps":
        Capteur.chrono_temps(enJeu, ecran)
    elif mode=="chronoBut":
        Capteur.chrono_but(enJeu, ecran)
    else:
        print("impossible")

#Bouton de pause
#Bouton pause devient Bouton relance
def pausePartie(enJeu: EnJeu, ecran: Tk):

    print("c'est la pause")
    enJeu.Bouton_pause.place_forget()
    
    enJeu.Bouton_relance.place(x=1069,y=0)

    Capteur.Pause = True

    ecran.update()
    

#Bouton de relance
#Bouton relance devient Bouton pause
def relancePartie(enJeu: EnJeu, mode, ecran: Tk):
    print("c'est reparti")
    enJeu.Bouton_relance.place_forget()
    
    enJeu.Bouton_pause.place(x=1069,y=0)
    
    Capteur.Pause = False
    Capteur.Temps_Pause = time.time() - Capteur.debut - Capteur.temps
    ecran.update()

    if mode=="classique":
        Capteur.classique(enJeu, ecran)
    elif mode=="chrono":
        Capteur.chrono(enJeu, ecran)
    elif mode=="chronoTemps":
        Capteur.chrono_temps(enJeu, ecran)
    elif mode=="chronoBut":
        Capteur.chrono_but(enJeu, ecran)
    else:
        print("impossible")

    

#Bouton arret de partie
#Bouton retour et Bouton début de partie apparaissent
#Bouton arret et Bouton relance/pause disparaissent
def arretPartie(enJeu: EnJeu, ecran: Tk):
    Capteur.EnCour = False

    enJeu.Bouton_debut.place(x=204,y=0)
    enJeu.Bouton_retour.place(x=82 , y=62)
    
    enJeu.Bouton_arret.place_forget()
    enJeu.Bouton_relance.place_forget()
    enJeu.Bouton_pause.place_forget()
    ecran.update()
    

#Bouton - bleu
def moinsBleu(enJeu: EnJeu, ecran: Tk):
    if Capteur.score_bleu != 0:
        Capteur.score_bleu = Capteur.score_bleu -1
        texte = Capteur.numberToString(Capteur.score_bleu )
        enJeu.Label_score_bleu.configure(text=texte)
        ecran.update()

#Bouton + bleu
def plusBleu(enJeu: EnJeu, ecran: Tk):
    Capteur.score_bleu = Capteur.score_bleu +1
    texte = Capteur.numberToString(Capteur.score_bleu )
    enJeu.Label_score_bleu.configure(text=texte)
    ecran.update()

#Bouton - rouge
def moinsRouge(enJeu: EnJeu, ecran: Tk):
    if Capteur.score_rouge != 0:
        Capteur.score_rouge = Capteur.score_rouge -1
        texte = Capteur.numberToString(Capteur.score_rouge )
        enJeu.Label_score_rouge.configure(text=texte)
        ecran.update()

#Bouton + rouge
def plusRouge(enJeu: EnJeu, ecran: Tk):
    Capteur.score_rouge = Capteur.score_rouge +1
    texte = Capteur.numberToString(Capteur.score_rouge )
    enJeu.Label_score_rouge.configure(text=texte)
    ecran.update()
