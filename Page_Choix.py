import tkinter as tk
from tkinter.constants import OUTSIDE
from tkinter.ttk import *
from PIL import ImageTk, Image 

class Menu():
    def __init__(self):
        #Définition des Frames
        self.page = tk.Frame()
        self.titre = tk.Frame(master= self.page)
        self.trait = tk.Frame(master= self.page)
        self.corps = tk.Frame(master= self.page)
        self.boutons = tk.Frame(master= self.corps)
        self.intervale1 = tk.Frame(master= self.boutons)
        self.intervale2 = tk.Frame(master= self.boutons)
        self.intervale3 = tk.Frame(master= self.boutons)
        self.intervale4 = tk.Frame(master= self.boutons)
        self.textes = tk.Frame(master= self.corps)
        self.intervale_texte = tk.Frame(master= self.textes)

        #Paramétrage des Frames
        self.titre.configure(width=1920, height=200, bg="#000000")
        self.titre.pack_propagate(0)

        self.trait.configure(width=1920, height=10, bg="#2aff00")
        self.trait.pack_propagate(0)

        self.corps.configure(width=1920, height=880, bg="#818181")
        self.corps.pack_propagate(0)

        self.textes.configure(bg="#818181")

        self.intervale_texte.configure(width=613.56, bg="#818181")
        self.intervale_texte.pack_propagate(0)

        #Placement des Frames
        self.titre.pack()
        self.trait.pack()
        self.corps.pack()
        self.textes.place(x=0, y=55)
        self.intervale_texte.grid(row=0, column=0)
        self.boutons.place(x=0, y=205)

        #Définition des Boutons
        self.Bouton_classique = tk.Button(master= self.boutons)
        self.Bouton_chrono = tk.Button(master= self.boutons)
        self.Bouton_chrono_plus_temps = tk.Button(master= self.boutons)
        self.Bouton_chrono_plus_but = tk.Button(master= self.boutons)

        #Paramétrage des Boutons
            #Images
        photo_classique = Image.open(".\Images\Images_Renommee\Mode_Babyfoot.png")
        taille = (300 , 400)
        photo_classique = photo_classique.resize(taille)

        self.photoImage_classique = ImageTk.PhotoImage(photo_classique)
        
        self.Bouton_classique.configure(image= self.photoImage_classique, bg= "#4f4f4f") 

        #Définition des Labels
        self.Label_titre = tk.Label(master= self.titre)
        self.Label_bonjour = tk.Label(master= self.textes)
        
        #Paramétrage des Labels
        self.Label_titre.configure(text= "Menu des différents modes de jeux", font= "Arial, 50", bg= "#000000", fg="#ffffff")
        self.Label_bonjour.configure(text= "Bienvenue dans l'application connectée du Babyfoot", font= "Arial, 10", bg= "#818181", fg="#ffffff")

        #Placement des Wigets
        self.Label_titre.place(x=495.5, y=65.12)
        self.Label_bonjour.grid(row=0, column=1)
        self.Bouton_classique.grid(row=0, column=1)
        self.Bouton_chrono.grid(row=0, column=3)
        self.Bouton_chrono_plus_temps.grid(row=0, column=5)
        self.Bouton_chrono_plus_but.grid(row=0, column=7)

        

    def affiche(self):
        self.page.pack()
        

    def cache(self):
        self.page.pack_forget()


