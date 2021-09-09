from Page_Jeu import EnJeu
import RPi.GPIO as GPIO
import time
import tkinter as Tk

Pause = False
debut = time.time()
temps = time.time() - debut
score_bleu = 0
score_rouge = 0
Temps_Pause = 0.0
EnCour = False

def initialisation():
    global Pause, debut, temps, score_bleu, score_rouge, Temps_Pause, EnCour
    Pause = False
    debut = time.time()
    temps = time.time() - debut
    score_bleu = 0
    score_rouge = 0
    Temps_Pause = 0.0
    EnCour = True


def numberToString(number: int):
    if number<=9:
        return "0"+str(number)
    else:
        return str(number)

def classique(enJeu: EnJeu, ecran: Tk):
    global Pause, debut, temps, score_bleu, score_rouge, Temps_Pause, EnCour
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG1 = 23
    ECHO1 = 24

    TRIG2 = 17
    ECHO2 = 27

    GPIO.setup(TRIG1,GPIO.OUT)
    GPIO.setup(ECHO1,GPIO.IN)
    GPIO.output(TRIG1, False)

    GPIO.setup(TRIG2,GPIO.OUT)
    GPIO.setup(ECHO2,GPIO.IN)
    GPIO.output(TRIG2, False)
    #score_bleu=0
    #score_rouge=0
    nouveauTemps=0
    #debut = time.time()
    
    while (score_bleu < 10 and score_rouge < 10) and EnCour:
        if Pause :
            break
        else :
            temps = time.time() - debut - Temps_Pause
            if nouveauTemps<=int(temps):
                nouveauTemps=nouveauTemps+1
                seconde_chrono = int(temps)%60
                minute_chrono = int(temps/60)
                label_seconde= numberToString(seconde_chrono)
                label_minute= numberToString(minute_chrono)
                label_chrono= str(label_minute)+ " : " + str(label_seconde)
                enJeu.Label_chrono.configure(text=label_chrono)
                ecran.update()
            time.sleep(0.01)
            GPIO.output(TRIG1, True)
            time.sleep(0.00001)
            GPIO.output(TRIG1, False)

            while GPIO.input(ECHO1)==0:
                pulse_start1 = time.time()
            while GPIO.input(ECHO1)==1:
                pulse_end1 = time.time()


            pulse_duration1 = pulse_end1 - pulse_start1
            distance1 = pulse_duration1 * 17165
            distance = round(distance1, 1)

            GPIO.output(TRIG2, True)
            time.sleep(0.00001)
            GPIO.output(TRIG2, False)

            while GPIO.input(ECHO2)==0:
                pulse_start2 = time.time()
            while GPIO.input(ECHO2)==1:
                pulse_end2 = time.time()

            pulse_duration2 = pulse_end2 - pulse_start2
            distance2 = pulse_duration2 * 17165
            distance2 = round(distance2, 1)
            
            if distance1<20:
                score_bleu = score_bleu + 1
                label_score_bleu=numberToString(score_bleu)
                enJeu.Label_score_bleu.configure(text=label_score_bleu)
                ecran.update()
                time.sleep(1)
                print('but bleu')
            if distance2<20:
                score_rouge = score_rouge + 1
                label_score_rouge=numberToString(score_rouge)
                enJeu.Label_score_rouge.configure(text=label_score_rouge)
                ecran.update()
                time.sleep(1)
                print('but rouge')
    GPIO.cleanup()
    print('Nombre de buts rouge : ', score_rouge, ' et nombre de buts bleu : ' , score_bleu)

"""
def but():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG1 = 23
    ECHO1 = 24

    TRIG2 = 17
    ECHO2 = 27

    GPIO.setup(TRIG1,GPIO.OUT)
    GPIO.setup(ECHO1,GPIO.IN)
    GPIO.output(TRIG1, False)

    GPIO.setup(TRIG2,GPIO.OUT)
    GPIO.setup(ECHO2,GPIO.IN)
    GPIO.output(TRIG2, False)
    but = 0
    while but == 0:
        time.sleep(0.01)
        GPIO.output(TRIG1, True)
        time.sleep(0.00001)
        GPIO.output(TRIG1, False)

        while GPIO.input(ECHO1)==0:
            pulse_start1 = time.time()
        while GPIO.input(ECHO1)==1:
            pulse_end1 = time.time()


        pulse_duration1 = pulse_end1 - pulse_start1
        distance1 = pulse_duration1 * 17165
        distance = round(distance1, 1)

        GPIO.output(TRIG2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG2, False)

        while GPIO.input(ECHO2)==0:
            pulse_start2 = time.time()
        while GPIO.input(ECHO2)==1:
            pulse_end2 = time.time()

        pulse_duration2 = pulse_end2 - pulse_start2
        distance2 = pulse_duration2 * 17165
        distance2 = round(distance2, 1)

        if distance1<20:
            but = 1
            print('but bleu')
        if distance2<20:
            but = 2
            print('but rouge')
    GPIO.cleanup()
    return but
"""
def chrono(enJeu: EnJeu, ecran: Tk):
    global Pause, debut, temps, score_bleu, score_rouge, Temps_Pause, EnCour
    #debut = time.time()
    #temps = time.time() - debut

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG1 = 23
    ECHO1 = 24

    TRIG2 = 17
    ECHO2 = 27

    GPIO.setup(TRIG1,GPIO.OUT)
    GPIO.setup(ECHO1,GPIO.IN)
    GPIO.output(TRIG1, False)

    GPIO.setup(TRIG2,GPIO.OUT)
    GPIO.setup(ECHO2,GPIO.IN)
    GPIO.output(TRIG2, False)

    #score_bleu = 0
    #score_rouge = 0
    nouveauTemps=0
    #Temps_Pause = 0.0

    while temps<600 and EnCour:
        if Pause :
            break
        else :
            temps = time.time() - debut - Temps_Pause
            
            if int(temps)>=nouveauTemps:
                nouveauTemps=nouveauTemps+1
                chronoActuel=600-int(temps)
                seconde_chrono = chronoActuel%60
                minute_chrono = int(chronoActuel/60)
                label_seconde= numberToString(seconde_chrono)
                label_minute= numberToString(minute_chrono)
                label_chrono= str(label_minute)+ " : " + str(label_seconde)
                enJeu.Label_chrono.configure(text=label_chrono)
                ecran.update()
            time.sleep(0.01)
            GPIO.output(TRIG1, True)
            time.sleep(0.00001)
            GPIO.output(TRIG1, False)

            while GPIO.input(ECHO1)==0:
                pulse_start1 = time.time()
            while GPIO.input(ECHO1)==1:
                pulse_end1 = time.time()


            pulse_duration1 = pulse_end1 - pulse_start1
            distance1 = pulse_duration1 * 17165
            distance = round(distance1, 1)

            GPIO.output(TRIG2, True)
            time.sleep(0.00001)
            GPIO.output(TRIG2, False)

            while GPIO.input(ECHO2)==0:
                pulse_start2 = time.time()
            while GPIO.input(ECHO2)==1:
                pulse_end2 = time.time()

            pulse_duration2 = pulse_end2 - pulse_start2
            distance2 = pulse_duration2 * 17165
            distance2 = round(distance2, 1)
            
            if distance1<20:
                score_bleu = score_bleu + 1
                label_score_bleu=numberToString(score_bleu)
                enJeu.Label_score_bleu.configure(text=label_score_bleu)
                ecran.update()
                time.sleep(1)
            if distance2<20:
                score_rouge = score_rouge + 1
                label_score_rouge=numberToString(score_rouge)
                enJeu.Label_score_rouge.configure(text=label_score_rouge)
                ecran.update()
                time.sleep(1)
    GPIO.cleanup()

def chrono_temps(enJeu: EnJeu, ecran: Tk):
    global Pause, debut, temps, score_bleu, score_rouge, Temps_Pause, EnCour
    #debut = time.time()
    #temps = time.time() - debut

    

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG1 = 23
    ECHO1 = 24

    TRIG2 = 17
    ECHO2 = 27

    GPIO.setup(TRIG1,GPIO.OUT)
    GPIO.setup(ECHO1,GPIO.IN)
    GPIO.output(TRIG1, False)

    GPIO.setup(TRIG2,GPIO.OUT)
    GPIO.setup(ECHO2,GPIO.IN)
    GPIO.output(TRIG2, False)

    #score_rouge= 0
    #score_bleu=0
    nouveauTemps=0
    while temps<600 and EnCour:
        if Pause :
            break
        else :
            temps = time.time() - debut - Temps_Pause
            if int(temps)>=nouveauTemps:
                nouveauTemps=nouveauTemps+1
                chronoActuel=600-int(temps)
                seconde_chrono = chronoActuel%60
                minute_chrono = int(chronoActuel/60)
                label_seconde= numberToString(seconde_chrono)
                label_minute= numberToString(minute_chrono)
                label_chrono= str(label_minute)+ " : " + str(label_seconde)
                enJeu.Label_chrono.configure(text=label_chrono)
                ecran.update()
            time.sleep(0.01)
            GPIO.output(TRIG1, True)
            time.sleep(0.00001)
            GPIO.output(TRIG1, False)

            while GPIO.input(ECHO1)==0:
                pulse_start1 = time.time()
            while GPIO.input(ECHO1)==1:
                pulse_end1 = time.time()


            pulse_duration1 = pulse_end1 - pulse_start1
            distance1 = pulse_duration1 * 17165
            distance = round(distance1, 1)

            GPIO.output(TRIG2, True)
            time.sleep(0.00001)
            GPIO.output(TRIG2, False)

            while GPIO.input(ECHO2)==0:
                pulse_start2 = time.time()
            while GPIO.input(ECHO2)==1:
                pulse_end2 = time.time()

            pulse_duration2 = pulse_end2 - pulse_start2
            distance2 = pulse_duration2 * 17165
            distance2 = round(distance2, 1)
            
            valeurbut = 1 + int(temps/60)
            if distance1<20:
                score_bleu = score_bleu + valeurbut
                label_score_bleu=numberToString(score_bleu)
                enJeu.Label_score_bleu.configure(text=label_score_bleu)
                ecran.update()
                time.sleep(1)
                print('but bleu')
            if distance2<20:
                score_rouge = score_rouge + valeurbut
                label_score_rouge=numberToString(score_rouge)
                enJeu.Label_score_rouge.configure(text=label_score_rouge)
                ecran.update()
                time.sleep(1)
                print('but rouge')
    GPIO.cleanup()

def chrono_but(enJeu: EnJeu, ecran: Tk):
    global Pause, debut, temps, score_bleu, score_rouge, Temps_Pause, EnCour
    #debut = time.time()
    #temps = time.time() - debut  

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG1 = 23
    ECHO1 = 24

    TRIG2 = 17
    ECHO2 = 27

    GPIO.setup(TRIG1,GPIO.OUT)
    GPIO.setup(ECHO1,GPIO.IN)
    GPIO.output(TRIG1, False)

    GPIO.setup(TRIG2,GPIO.OUT)
    GPIO.setup(ECHO2,GPIO.IN)
    GPIO.output(TRIG2, False)

    #score_rouge = 0
    #score_bleu = 0
    valeurbut = 1
    nouveauTemps=0
    while temps<600 and EnCour:
        if Pause :
            break
        else :
            temps = time.time() - debut - Temps_Pause
            if int(temps)>=nouveauTemps:
                nouveauTemps=nouveauTemps+1
                chronoActuel=600-int(temps)
                seconde_chrono = chronoActuel%60
                minute_chrono = int(chronoActuel/60)
                label_seconde= numberToString(seconde_chrono)
                label_minute= numberToString(minute_chrono)
                label_chrono= str(label_minute)+ " : " + str(label_seconde)
                enJeu.Label_chrono.configure(text=label_chrono)
                ecran.update()
            print(valeurbut)
            time.sleep(0.01)
            GPIO.output(TRIG1, True)
            time.sleep(0.00001)
            GPIO.output(TRIG1, False)

            while GPIO.input(ECHO1)==0:
                pulse_start1 = time.time()
            while GPIO.input(ECHO1)==1:
                pulse_end1 = time.time()


            pulse_duration1 = pulse_end1 - pulse_start1
            distance1 = pulse_duration1 * 17165
            distance = round(distance1, 1)

            GPIO.output(TRIG2, True)
            time.sleep(0.00001)
            GPIO.output(TRIG2, False)

            while GPIO.input(ECHO2)==0:
                pulse_start2 = time.time()
            while GPIO.input(ECHO2)==1:
                pulse_end2 = time.time()

            pulse_duration2 = pulse_end2 - pulse_start2
            distance2 = pulse_duration2 * 17165
            distance2 = round(distance2, 1)
            
            if distance1<20:
                score_bleu = score_bleu + valeurbut
                label_score_bleu=numberToString(score_bleu)
                enJeu.Label_score_bleu.configure(text=label_score_bleu)
                ecran.update()
                time.sleep(1)
                valeurbut = valeurbut + 1
                print('but bleu')
            if distance2<20:
                score_rouge = score_rouge + valeurbut
                label_score_rouge=numberToString(score_rouge)
                enJeu.Label_score_rouge.configure(text=label_score_rouge)
                ecran.update()
                time.sleep(1)
                valeurbut = valeurbut + 1
                print('but rouge')
    GPIO.cleanup()