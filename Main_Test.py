import tkinter as tk
from Page_Choix import *
from Page_Jeu import *
from boutons_effet import *

ecran = tk.Tk()
ecran.geometry('1920x1080')
ecran.resizable(width=0, height=0)
#ecran.configure(bg="gray")

menu = Menu()
jeu = EnJeu()

#menu
menu.Bouton_classique.configure(command=lambda: versClassique(menu, jeu, ecran))
menu.Bouton_chrono.configure(command=lambda: versChrono(menu,jeu, ecran))
menu.Bouton_chrono_plus_temps.configure(command=lambda: versChronoTemps(menu,jeu, ecran))
menu.Bouton_chrono_plus_but.configure(command=lambda: versChronoBut(menu,jeu, ecran))

#retour vers le menu
jeu.Bouton_retour.configure(command=lambda: versMenu(jeu, menu))

#jeu
jeu.Bouton_pause.configure(command=lambda: pausePartie(jeu))
jeu.Bouton_relance.configure(command=lambda: relancePartie(jeu))
jeu.Bouton_arret.configure(command=lambda: arretPartie(jeu))
"""
jeu.Bouton_moins_bleu.configure(command=lambda: moinsBleu(jeu))
jeu.Bouton_plus_bleu.configure(command=lambda: plusBleu(jeu))
jeu.Bouton_moins_rouge.configure(command=lambda: moinsRouge(jeu))
jeu.Bouton_plus_rouge.configure(command=lambda: plusRouge(jeu))
"""
jeu.affiche()

#menu.cache()

ecran.mainloop()

#menu = Menu()
#menu = EnJeu()
