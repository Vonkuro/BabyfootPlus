import tkinter as tk
from Page_Choix import *
from Page_Jeu import *

ecran = tk.Tk()
ecran.geometry('1920x1080')
ecran.resizable(width=0, height=0)
ecran.configure(bg="gray")

menu = Menu()
jeu = EnJeu()

menu.affiche()

#menu.cache()

ecran.mainloop()

#menu = Menu()
#menu = EnJeu()
