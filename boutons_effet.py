from Page_Choix import *
from Page_Jeu import *

# ----- Changement des écrans

#les quatres modes de jeu

def versClassique(menu : Menu, classique: EnJeu):
    menu.cache()
    classique.affiche()

def versChrono(menu: Menu, chrono: EnJeu):
    menu.cache()
    chrono.affiche()

def versChronoTemps(menu: Menu, chronoTemps: EnJeu):
    menu.cache()
    chronoTemps.affiche()

def versChronoBut(menu: Menu, chronoBut: EnJeu):
    menu.cache()
    chronoBut.affiche()

#bouton de retour (flèche en arriere)
def versMenu(enJeu: EnJeu, menu: Menu):
    enJeu.cache()
    menu.affiche()


# ----- Apparition et disparition des widgets

#Bouton pour démarrer la partie 
#disparition : bouton retour(flèche en arriere) et bouton debut
#apparition : bouton arret et bouton pause
def debutPartie(enJeu: EnJeu):
    enJeu.Bouton_retour.grid_forget()
    enJeu.Bouton_debut.pack_forget()
    
    enJeu.Bouton_arret.pack()
    enJeu.Bouton_pause.pack()

#Bouton de pause
#Bouton pause devient Bouton relance
def pausePartie(enJeu: EnJeu):
    print("c'est la pause")
    enJeu.Bouton_pause.pack_forget()
    
    enJeu.Bouton_relance.pack()

#Bouton de relance
#Bouton relance devient Bouton pause
def relancePartie(enJeu: EnJeu):
    print("c'est reparti")
    enJeu.Bouton_relance.pack_forget()
    
    enJeu.Bouton_pause.pack()

#Bouton arret de partie
#Bouton retour et Bouton début de partie apparaissent
#Bouton arret et Bouton relance/pause disparaissent
def arretPartie(enJeu: EnJeu):
    enJeu.Bouton_debut.pack()
    enJeu.Bouton_retour.grid(row=0,column=0)
    
    enJeu.Bouton_arret.pack_forget()
    enJeu.Bouton_relance.pack_forget()
    enJeu.Bouton_pause.pack_forget()
    
"""
#Bouton - bleu
def moinsBleu(enJeu: EnJeu):
    if enJeu.Label_score_bleu!=0:
        enJeu.Label_score_bleu=enJeu.Label_score_bleu-1

#Bouton + bleu
def plusBleu(enJeu: EnJeu):
    enJeu.Label_score_bleu=enJeu.Label_score_bleu+1

#Bouton - rouge
def moinsRouge(enJeu: EnJeu):
    if enJeu.Label_score_rouge!=0:
        enJeu.Label_score_rouge=enJeu.Label_score_rouge-1

#Bouton + rouge
def plusRouge(enJeu: EnJeu):
    enJeu.Label_score_rouge=enJeu.Label_score_rouge+1
"""