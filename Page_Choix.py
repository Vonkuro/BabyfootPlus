import tkinter as tk

class Menu():
    def __init__(self):
        #Définition des Frames
        self.page = tk.Frame()
        self.titre =tk.Frame(master= self.page)
        self.trait = tk.Frame(master= self.page)
        self.corps = tk.Frame(master= self.page)
        self.boutons = tk.Frame(master= self.corps)
        self.textes = tk.Frame(master= self.corps)

        #Paramétrage des Frames

        #Placement des Frames
        self.titre.pack()
        self.trait.pack()
        self.corps.pack()
        self.textes.pack()
        self.boutons.pack()

        #Définition des Boutons
        self.Bouton_classique = tk.Button(master= self.boutons)
        self.Bouton_chrono = tk.Button(master= self.boutons)
        self.Bouton_chrono_plus_temps = tk.Button(master= self.boutons)
        self.Bouton_chrono_plus_but = tk.Button(master= self.boutons)

        #Paramétrage des Boutons

        #Définition des Labels
        self.Label_titre = tk.Label(master= self.titre)
        self.Label_bonjour = tk.Label(master= self.textes)
        
        #Paramétrage des Labels

        #Placement des Wigets
        self.Label_titre.pack()
        self.Label_bonjour.pack()
        self.Bouton_classique.grid(row=0, column=0)
        self.Bouton_chrono.grid(row=0, column=1)
        self.Bouton_chrono_plus_temps.grid(row=0, column=2)
        self.Bouton_chrono_plus_but.grid(row=0, column=3)

    def affiche(self):
        self.page.pack()
        

    def cache(self):
        self.page.pack_forget()



