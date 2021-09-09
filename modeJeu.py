import time
from Capteur import *

def ModeClassique(enJeu, ecran):
    score_rouge = 0
    score_bleu = 0

    while (score_bleu < 10 and score_rouge < 10):
        if but() == 1:
            score_rouge = score_rouge + 1
            enJeu.Label_score_bleu.configure(text=str(score_rouge))
            ecran.update()
            print("Score rouge :" +str(score_rouge))
            time.sleep(1)

        if but() ==2:
            score_bleu = score_bleu + 1
            enJeu.Label_score_rouge.configure(text=str(score_rouge))
            ecran.update()
            print("Score bleu :" +str(score_bleu))
            time.sleep(1)
