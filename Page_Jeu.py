import tkinter as tk
from PIL import ImageTk, Image  

class EnJeu():
    def __init__(self):
        """
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
        self.score = tk.Frame(master= self.corps)
        self.equipe = tk.Frame(master= self.corps)
        self.chrono = tk.Frame(master= self.corps)
        self.boutons = tk.Frame(master= self.corps)

        #Paramétrage des Frames

        self.titre.configure(width=1920, height=200, bg="#000000")
        self.titre.pack_propagate(0)
        self.titre.grid_propagate(0)

        self.trait.configure(width=1920, height=10, bg="#2aff00")
        self.trait.pack_propagate(0)
        self.trait.grid_propagate(0)

        self.corps.configure(width=1920, height=880, bg="#818181")
        self.corps.pack_propagate(0)
        self.corps.grid_propagate(0)

        self.score.configure(width=1574, height=209, bg="#4f4f4f", highlightbackground="#000000", highlightthickness=1)
        self.score.pack_propagate(0)
        self.score.grid_propagate(0)

        self.equipe.configure(width=1920, height=120, bg="#818181")
        self.equipe.pack_propagate(0)
        self.equipe.grid_propagate(0)

        self.chrono.configure(width=1920, height=211.93, bg="#818181")
        self.chrono.pack_propagate(0)
        self.chrono.grid_propagate(0)

        self.boutons.configure(width=1920, height=126, bg="#818181")
        self.boutons.pack_propagate(0)
        self.boutons.grid_propagate(0)


        #Placement des Frames
        self.titre.grid(row=0, column=0)
        self.trait.grid(row=1, column=0)
        self.corps.grid(row=2, column=0)
        self.score.place(x=173,y= 34.5)
        self.equipe.place(x=0,y= 270.5)
        self.chrono.place(x=0,y= 409.81)

        self.boutons.place(x=0,y= 660)

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
        photo_retour = Image.open("./Images/Images_Renommee/Fleche_Retour.png")
        taille = (91 , 77)
        photo_retour = photo_retour.resize(taille)
        self.photoImage_retour = ImageTk.PhotoImage(photo_retour)

        photo_debut = Image.open("./Images/Images_Renommee/Bouton_Commencer.png")
        taille = (1513 , 126)
        photo_debut = photo_debut.resize(taille)
        self.photoImage_debut = ImageTk.PhotoImage(photo_debut)

        photo_arret = Image.open("./Images/Images_Renommee/Bouton_Arreter.png")
        taille = (648 , 126)
        photo_arret = photo_arret.resize(taille)
        self.photoImage_arret = ImageTk.PhotoImage(photo_arret)

        photo_pause = Image.open("./Images/Images_Renommee/Bouton_Mettre_Pause.png")
        taille = (648 , 126)
        photo_pause = photo_pause.resize(taille)
        self.photoImage_pause = ImageTk.PhotoImage(photo_pause)

        photo_relance = Image.open("./Images/Images_Renommee/Bouton_Lecture_Partie.png")
        taille = (648 , 126)
        photo_relance = photo_relance.resize(taille)
        self.photoImage_relance = ImageTk.PhotoImage(photo_relance)

        photo_plus_bleu = Image.open("./Images/Images_Renommee/Bouton_Vert.png")
        taille = (126 , 126)
        photo_plus_bleu = photo_plus_bleu.resize(taille)
        self.photoImage_plus_bleu = ImageTk.PhotoImage(photo_plus_bleu)

        photo_moins_bleu = Image.open("./Images/Images_Renommee/Bouton_Rouge.png")
        taille = (126 , 126)
        photo_moins_bleu = photo_moins_bleu.resize(taille)
        self.photoImage_moins_bleu = ImageTk.PhotoImage(photo_moins_bleu)

        photo_plus_rouge = Image.open("./Images/Images_Renommee/Bouton_Vert.png")
        taille = (126 , 126)
        photo_plus_rouge = photo_plus_rouge.resize(taille)
        self.photoImage_plus_rouge = ImageTk.PhotoImage(photo_plus_rouge)

        photo_moins_rouge = Image.open("./Images/Images_Renommee/Bouton_Rouge.png")
        taille = (126 , 126)
        photo_moins_rouge = photo_moins_rouge.resize(taille)
        self.photoImage_moins_rouge = ImageTk.PhotoImage(photo_moins_rouge)

        self.Bouton_retour.configure(image= self.photoImage_retour, bg= "#000000")
        self.Bouton_debut.configure(image= self.photoImage_debut, bg="#818181")
        self.Bouton_arret.configure(image= self.photoImage_arret, bg="#818181")
        self.Bouton_pause.configure(image= self.photoImage_pause, bg="#818181")
        self.Bouton_relance.configure(image= self.photoImage_relance, bg="#818181")

        self.Bouton_plus_bleu.configure(image= self.photoImage_plus_bleu, bg="#4f4f4f")
        self.Bouton_moins_bleu.configure(image= self.photoImage_moins_bleu, bg="#4f4f4f")
        self.Bouton_plus_rouge.configure(image= self.photoImage_plus_rouge, bg="#4f4f4f")
        self.Bouton_moins_rouge.configure(image= self.photoImage_moins_rouge, bg="#4f4f4f")

        #Définition des Labels
        self.Label_titre = tk.Label(master= self.titre)

        self.Label_score_bleu = tk.Label(master= self.score)
        self.Label_score_tiret = tk.Label(master= self.score)
        self.Label_score_rouge = tk.Label(master= self.score)

        self.Label_drapeau_bleu = tk.Label(master= self.equipe)
        self.Label_texte_bleu = tk.Label(master= self.equipe)
        self.Label_drapeau_rouge = tk.Label(master= self.equipe)
        self.Label_texte_rouge = tk.Label(master= self.equipe)

        self.Label_chrono = tk.Label(master= self.chrono)

        
        #Paramétrage des Labels
        photo_drapeau_bleu = Image.open("./Images/Images_Renommee/Drapeau_Bleu.png")
        taille = (95 , 110)
        photo_drapeau_bleu = photo_drapeau_bleu.resize(taille)
        self.photoImage_drapeau_bleu = ImageTk.PhotoImage(photo_drapeau_bleu)

        photo_drapeau_rouge = Image.open("./Images/Images_Renommee/Drapeau_Rouge.png")
        photo_drapeau_rouge = photo_drapeau_rouge.resize(taille)
        self.photoImage_drapeau_rouge = ImageTk.PhotoImage(photo_drapeau_rouge)

        self.Label_drapeau_bleu.configure(image= self.photoImage_drapeau_bleu, bg="#818181")
        self.Label_drapeau_rouge.configure(image= self.photoImage_drapeau_rouge, bg="#818181")

        self.Label_titre.configure(text= "Classique", font= "Arial, 50", bg= "#000000", fg="#ffffff")

        self.Label_score_bleu.configure(text= "00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")
        self.Label_score_tiret.configure(text= "-", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")
        self.Label_score_rouge.configure(text= "00", font= "Arial, 125", bg= "#4f4f4f", fg="#ffffff")

        self.Label_texte_bleu.configure(text= "Equipe Bleue", font= "Arial, 28", bg= "#818181", fg="#ffffff")
        self.Label_texte_rouge.configure(text= "Equipe Rouge", font= "Arial, 28", bg= "#818181", fg="#ffffff")

        self.Label_chrono.configure(text= "00 : 00", font= "Arial, 150", bg= "#818181", fg="#ffffff")


        #Placement des Wigets
        self.Bouton_retour.place(x=82 , y=62)
        self.Label_titre.place(x=821.5 , y=64.81)

        self.Bouton_moins_bleu.place(x= 116, y= 33.5)
        self.Bouton_plus_bleu.place(x= 308, y= 33.5)
        self.Label_score_bleu.place(x= 528, y= 15)
        self.Label_score_tiret.place(x= 760, y= 15)
        self.Label_score_rouge.place(x= 864, y= 15)
        self.Bouton_plus_rouge.place(x= 1140, y= 33.5)
        self.Bouton_moins_rouge.place(x= 1332, y= 33.5)

        self.Label_chrono.place(x= 655, y= 0)

        self.Label_drapeau_bleu.place(x= 290, y= 0)
        self.Label_texte_bleu.place(x= 475, y= 34.37)
        self.Label_drapeau_rouge.place(x= 1535, y= 0)
        self.Label_texte_rouge.place(x= 1200, y= 34.37)

        self.Bouton_debut.place(x=204,y=0)

        #Placement de la fenêtre
        #self.page.mainloop()


    def affiche(self):
        self.page.pack()
        

    def cache(self):
        self.page.pack_forget()
        
