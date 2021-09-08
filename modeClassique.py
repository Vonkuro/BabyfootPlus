import time

if distance1<20:
    Label_score_rouge = Label_score_rouge + 1
    print(Label_score_rouge)

if distance2<20:
    Label_score_bleu = Label_score_bleu + 1
    print(Label_score_bleu)

----------------""" mode chrono """-----------
debut = time.time()
time.sleep(10)

fin = time.time()

temps = fin - debut

print(temps)

while temps < 20:
    if distance1<20:
        Label_score_rouge = Label_score_rouge + 1
        print(Label_score_rouge)

    if distance2<20:
        Label_score_bleu = Label_score_bleu + 1
        print(Label_score_bleu)

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

    