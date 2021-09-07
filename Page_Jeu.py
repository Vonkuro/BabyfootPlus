import tkinter as tk
from PIL import ImageTk, Image  

class EnJeu():
    def __init__(self):
        #Définition des Frames
        self.page = tk.Frame()
        self.titre =tk.Frame(master= self.page)
        self.trait = tk.Frame(master= self.page)
        self.corps = tk.Frame(master= self.page)
        self.score = tk.Frame(master= self.corps)
        self.equipe = tk.Frame(master= self.corps)
        self.chrono = tk.Frame(master= self.corps)
        self.boutons = tk.Frame(master= self.corps)

        #Paramétrage des Frames

        #Placement des Frames

        #Définition des Boutons
        self.Bouton_retour = tk.Button(master= self.titre)

        self.Bouton_debut = tk.Button(master= self.boutons)
        self.Bouton_arret = tk.Button(master= self.boutons)
        self.Bouton_pause = tk.Button(master= self.boutons)
        self.Bouton_relance = tk.Button(master= self.boutons)

        self.Bouton_plus_bleu = tk.Button(master= self.score)
        self.Bouton_moins_bleu = tk.Button(master= self.score)
        self.Bouton_plus_rouge = tk.Button(master= self.score)
        self.Bouton_moins_rouge = tk.Button(master= self.score)

        #Paramétrage des Boutons
        self.titre.pack()
        self.trait.pack()
        self.corps.pack()
        self.score.pack()
        self.equipe.pack()
        self.chrono.pack()
        self.boutons.pack()

        #Définition des Labels
        self.Label_titre = tk.Label(master= self.titre)

        self.Label_score_bleu = tk.Label(master= self.score)
        self.Label_score_tiret = tk.Label(master= self.score)
        self.Label_score_rouge = tk.Label(master= self.score)

        self.Label_drapeau_bleu = tk.Label(master= self.equipe)
        self.Label_texte_bleu = tk.Label(master= self.equipe)
        self.Label_drapeau_rouge = tk.Label(master= self.equipe)
        self.Label_texte_rouge = tk.Label(master= self.equipe)

        self.Label_minutes = tk.Label(master= self.chrono)
        self.Label_chrono_tiret = tk.Label(master= self.chrono)
        self.Label_secondes = tk.Label(master= self.chrono)
        
        #Paramétrage des Labels

        #Placement des Wigets
        self.Bouton_retour.grid(row=0,column=0)
        self.Label_titre.grid(row=0,column=1)

        self.Bouton_moins_bleu.grid(row=0,column=0)
        self.Bouton_plus_bleu.grid(row=0,column=1)
        self.Label_score_bleu.grid(row=0,column=2)
        self.Label_score_tiret.grid(row=0,column=3)
        self.Label_score_rouge.grid(row=0,column=4)
        self.Bouton_plus_rouge.grid(row=0,column=5)
        self.Bouton_moins_rouge.grid(row=0,column=6)

        self.Label_minutes.grid(row=0,column=0)
        self.Label_chrono_tiret.grid(row=0,column=0)
        self.Label_secondes.grid(row=0,column=0)

        self.Bouton_debut.pack()

    def affiche(self):
        self.page.pack()
        

    def cache(self):
        self.page.pack_forget()
