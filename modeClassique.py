import time

if distance1<20:
    Label_score_rouge = Label_score_rouge + 1

if distance2<20:
    Label_score_bleu = Label_score_bleu + 1

--------------""" mode chrono """--------------

while temps pas fini 
    if distance1<20:
        Label_score_rouge = Label_score_rouge + 1

    if distance2<20:
        Label_score_bleu = Label_score_bleu + 1

--------------""" mode chrono plus temps """--------------


while temps pas fini 
    valeurbut = 1
    """quand une minute est passée : valeurbut = valeurbut + 1 """
        if distance1<20:
            Label_score_rouge = Label_score_rouge + valeurbut

        if distance2<20:
            Label_score_bleu = Label_score_bleu + valeurbut

--------------""" mode chrono plus but """--------------

while temps pas fini
    valeurbut = 1
    if distance1<20:
        valeurbut = valeurbut + 1
        Label_score_rouge = Label_score_rouge + valeurbut

    if distance2<20:
        valeurbut = valeurbut + 1
        Label_score_bleu = Label_score_bleu + valeurbut

    