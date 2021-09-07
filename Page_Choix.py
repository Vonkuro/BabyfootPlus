import tkinter as tk

class Menu():
    def __init__(self):
        #Définition des Frames
        self.page = tk.Frame()
        self.titre =tk.Frame(master= self.page)
        self.trait = tk.Frame(master= self.page)
        self.corps = tk.Frame(master= self.page)
        #Paramétrage des Frames

        #Définition des Boutons
        self.Bouton_classique = tk.Button(master= self.corps)
        self.Bouton_chrono = tk.Button(master= self.corps)
        self.Bouton_chrono_plus_temps = tk.Button(master= self.corps)
        self.Bouton_chrono_plus_but = tk.Button(master= self.corps)
        #Paramétrage des Boutons

        #Définition des Labels
        self.Label_titre = tk.Label(master= self.titre)
        self.Label_bonjour = tk.Label(master= self.corps)
        #Paramétrage des Labels

        #Placement des Wigets


