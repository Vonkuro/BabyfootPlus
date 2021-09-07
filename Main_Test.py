import tkinter as tk
from Page_Choix import *
from Page_Jeu import *


fenetre = tk.Tk()
fenetre.geometry=('1920x1080')
fenetre.resizable(0, 0) 



menu = Menu()
#jeu = EnJeu()


menu.affiche()

fenetre.mainloop()