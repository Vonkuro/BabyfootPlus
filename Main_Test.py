import tkinter as tk
from Page_Choix import *
from Page_Jeu import *

fenetre = tk.Tk()
menu = Menu()
jeu = EnJeu()

jeu.affiche()

fenetre.mainloop()