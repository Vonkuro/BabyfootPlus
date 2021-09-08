import time
from Capteur import *

def ModeClassique(enJeu):
    score_rouge = 0
    score_bleu = 0

    while (score_bleu < 10 and score_rouge < 10):
        if but() == 1:
            score_rouge = score_rouge + 1
            print("Score rouge :" +str(score_rouge))
            time.sleep(1)


        if but() ==2:
            Label_score_bleu = Label_score_bleu + 1
            print("Score bleu :" +str(score_bleu))
            time.sleep(1)
