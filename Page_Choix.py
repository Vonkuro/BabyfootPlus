import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image 

class Menu():
    def __init__(self):
        """"
        #Définition de la fenêtre
        self.page = tk.Tk()
        
        #Paramétrage de la fenêtre
        self.page.geometry('1920x1080')
        self.page.resizable(width=0, height=0)
        """     
        #Définition des Frames
        self.page = tk.Frame()
        self.titre = tk.Frame(master= self.page)
        self.trait = tk.Frame(master= self.page)
        self.corps = tk.Frame(master= self.page)
        self.boutons = tk.Frame(master= self.corps)
        self.textes = tk.Frame(master= self.corps)

        #Paramétrage des Frames
        self.titre.configure(width=1920, height=200, bg="#000000")
        self.titre.pack_propagate(0)

        self.trait.configure(width=1920, height=10, bg="#2aff00")
        self.trait.pack_propagate(0)

        self.corps.configure(width=1920, height=880, bg="#818181")
        self.corps.pack_propagate(0)

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
            #Images
        photo_classique = Image.open("D:\EPSI-Volumineux\Test git\BabyfootPlus\Images\Images\Babyfoot_blanc.png")
        photo_classique = ImageTk.PhotoImage(photo_classique)
        self.Bouton_classique.configure(image= photo_classique, bg="#4f4f4f")
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

        #Placement de la fenêtre
        #self.page.mainloop()

    def affiche(self):
        self.page.pack()
        

    def cache(self):
        self.page.pack_forget()

    def _from_rgb(rgb):
    #translates an rgb tuple of int to a tkinter friendly color code
    
        return "#%02x%02x%02x" % rgb   

