import time

debut = time.time()
time.sleep(10)

fin = time.time()

temps = fin - debut

print(temps)

if temps > 10 : 
    print("yo mon bro")
    """if distance1<20:
        Label_score_rouge = Label_score_rouge + 1

    if distance2<20:
        Label_score_bleu = Label_score_bleu + 1"""