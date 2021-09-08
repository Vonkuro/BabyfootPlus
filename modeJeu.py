import time

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


----------------""" mode chrono """-----------

def ModeChrono(enJeu):
    score_rouge = 0
    score_bleu = 0

debut = time.time()

temps = time.time() - debut
print(temps)

while temps < 20:
    if but() == 1:
        score_rouge = score_rouge + 1
        print("Score rouge :" +str(score_rouge))
        time.sleep(1)

    if but() ==2:
        Label_score_bleu = Label_score_bleu + 1
        print("Score bleu :" +str(score_bleu))
        time.sleep(1)

--------------""" mode chrono plus temps """--------------


while temps < 20: 
    valeurbut = 1
    """quand une minute est passée : valeurbut = valeurbut + 1 """
        if distance1<20:
            Label_score_rouge = Label_score_rouge + valeurbut
            print(Label_score_rouge)

        if distance2<20:
            Label_score_bleu = Label_score_bleu + valeurbut
            print(Label_score_bleu)

--------------""" mode chrono plus but """--------------

while temps < 20:
    valeurbut = 1
    if distance1<20:
        valeurbut = valeurbut + 1
        Label_score_rouge = Label_score_rouge + valeurbut
        print(Label_score_rouge)

    if distance2<20:
        valeurbut = valeurbut + 1
        Label_score_bleu = Label_score_bleu + valeurbut
        print(Label_score_bleu)

    