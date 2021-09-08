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

        self.boutons.configure(width=1920, bg="#818181")

        self.intervale1.configure(width=84.75, bg="#818181")
        self.intervale1.pack_propagate(0)

        self.intervale2.configure(width=178, bg="#818181")
        self.intervale2.pack_propagate(0)

        self.intervale3.configure(width=178, bg="#818181")
        self.intervale3.pack_propagate(0)

        self.intervale4.configure(width=178, bg="#818181")
        self.intervale4.pack_propagate(0)

        #Placement des Frames
        self.titre.grid(row=0, column=0)
        self.trait.grid(row=1, column=0)
        self.corps.grid(row=2, column=0)
        self.textes.place(x=0, y=55)
        self.intervale_texte.grid(row=0, column=0)
        self.boutons.place(x=0, y=205)
        self.intervale1.grid(row=0, column=0)
        self.intervale2.grid(row=0, column=2)
        self.intervale3.grid(row=0, column=4)
        self.intervale4.grid(row=0, column=6)

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

        photo_chrono = Image.open(".\Images\Images_Renommee\Mode_Chrono.png")
        taille = (300 , 400)
        photo_chrono = photo_chrono.resize(taille)
        self.photoImage_chrono = ImageTk.PhotoImage(photo_chrono)

        photo_chrono_plus_temps = Image.open(".\Images\Images_Renommee\Mode_Chrono_Deux.png")
        taille = (300 , 400)
        photo_chrono_plus_temps = photo_chrono_plus_temps.resize(taille)
        self.photoImage_chrono_plus_temps = ImageTk.PhotoImage(photo_chrono_plus_temps)

        photo_chrono_plus_but = Image.open(".\Images\Images_Renommee\Mode_But.png")
        taille = (300 , 400)
        photo_chrono_plus_but = photo_chrono_plus_but.resize(taille)
        self.photoImage_chrono_plus_but = ImageTk.PhotoImage(photo_chrono_plus_but)
        
        self.Bouton_classique.configure(image= self.photoImage_classique, bg= "#4f4f4f")
        self.Bouton_chrono.configure(image= self.photoImage_chrono, bg= "#4f4f4f") 
        self.Bouton_chrono_plus_temps .configure(image= self.photoImage_chrono_plus_temps , bg= "#4f4f4f") 
        self.Bouton_chrono_plus_but.configure(image= self.photoImage_chrono_plus_but, bg= "#4f4f4f") 

        

        #Définition des Labels
        self.Label_titre = tk.Label(master= self.titre)
        self.Label_bonjour = tk.Label(master= self.textes)
        
        #Paramétrage des Labels
        self.Label_titre.configure(text= "Menu des différents modes de jeux", font= "Arial, 50", bg= "#000000", fg="#ffffff")
        self.Label_bonjour.configure(text= "Bienvenue dans l'application connectée du Babyfoot", font= "Arial, 25", bg= "#818181", fg="#ffffff")

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


