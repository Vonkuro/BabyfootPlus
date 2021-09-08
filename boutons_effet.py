from Page_Choix import *
from Page_Jeu import *

# ----- Changement des écrans

#les quatres modes de jeu

def versClassique(menu : Menu, classique: EnJeu):
    menu.cache()
    classique.Label_titre.configure(text= "Classique", font= "Arial, 50", bg= "#000000", fg="#ffffff")
    classique.Label_titre.place(x=821.5 , y=64.81)
    classique.affiche()

def versChrono(menu: Menu, chrono: EnJeu):
    menu.cache()
    chrono.Label_titre.configure(text= "Chrono", font= "Arial, 50", bg= "#000000", fg="#ffffff")
    chrono.Label_titre.place(x=821.5 , y=64.81)
    chrono.affiche()

def versChronoTemps(menu: Menu, chronoTemps: EnJeu):
    menu.cache()
    chronoTemps.Label_titre.configure(text= "Chrono 10 min", font= "Arial, 50", bg= "#000000", fg="#ffffff")
    chronoTemps.Label_titre.place(x=821.5 , y=64.81)
    chronoTemps.affiche()

def versChronoBut(menu: Menu, chronoBut: EnJeu):
    menu.cache()
    chronoBut.Label_titre.configure(text= "Chrone buts", font= "Arial, 50", bg= "#000000", fg="#ffffff")
    chronoBut.Label_titre.place(x=821.5 , y=64.81)
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
    enJeu.Bouton_retour.place_forget()
    enJeu.Bouton_debut.place_forget()
    
    enJeu.Bouton_arret.place(x=203,y=0)
    enJeu.Bouton_pause.place(x=1069,y=0)

#Bouton de pause
#Bouton pause devient Bouton relance
def pausePartie(enJeu: EnJeu):
    print("c'est la pause")
    enJeu.Bouton_pause.place_forget()
    
    enJeu.Bouton_relance.place(x=1069,y=0)

#Bouton de relance
#Bouton relance devient Bouton pause
def relancePartie(enJeu: EnJeu):
    print("c'est reparti")
    enJeu.Bouton_relance.place_forget()
    
    enJeu.Bouton_pause.place(x=1069,y=0)

#Bouton arret de partie
#Bouton retour et Bouton début de partie apparaissent
#Bouton arret et Bouton relance/pause disparaissent
def arretPartie(enJeu: EnJeu):
    enJeu.Bouton_debut.place(x=204,y=0)
    enJeu.Bouton_retour.place(x=82 , y=62)
    
    enJeu.Bouton_arret.place_forget()
    enJeu.Bouton_relance.place_forget()
    enJeu.Bouton_pause.place_forget()
    
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