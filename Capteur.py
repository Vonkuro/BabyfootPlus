from Page_Jeu import EnJeu
import RPi.GPIO as GPIO
import time
import tkinter as Tk

def classique(enJeu: EnJeu, ecran: Tk):
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
    score_bleu=0
    score_rouge=0
    nouveauTemps=0
    debut = time.time()
    
    while (score_bleu < 10 and score_rouge < 10):
        temps = time.time() - debut
        if nouveauTemps<=int(temps):
            nouveauTemps=nouveauTemps+1
            seconde_chrono = int(temps)%60
            minute_chrono = int(temps)/60
            label_chrono= str(minute_chrono)+ " : " + str(seconde_chrono)
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
            enJeu.Label_score_bleu.configure(text=str(score_bleu))
            ecran.update()
            time.sleep(1)
            print('but bleu')
        if distance2<20:
            score_rouge = score_rouge + 1
            enJeu.Label_score_rouge.configure(text=str(score_rouge))
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
    global Pause
    debut = time.time()
    temps = time.time() - debut

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

    but1 = 0
    but2 = 0
    nouveauTemps=0

    while temps<600:
        if Pause :
            time.sleep(0.05)
        else :
            temps = time.time() - debut
            if int(temps)>=nouveauTemps:
                nouveauTemps=nouveauTemps+1
                chronoActuel=600-int(temps)
                seconde_chrono = chronoActuel%60
                minute_chrono = int(chronoActuel/60)
                label_chrono= str(minute_chrono)+ " : " + str(seconde_chrono)
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
                but1 = but1 + 1
                enJeu.Label_score_bleu.configure(text=str(but1))
                ecran.update()
                time.sleep(1)
                print('but bleu')
            if distance2<20:
                but2 = but2 + 1
                enJeu.Label_score_rouge.configure(text=str(but2))
                ecran.update()
                time.sleep(1)
                print('but rouge')
    GPIO.cleanup()
    print('Nombre de buts rouge : ', but1, ' et nombre de buts bleu : ' , but2)

def chrono_temps(enJeu: EnJeu, ecran: Tk):
    debut = time.time()
    temps = time.time() - debut

    

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

    but1 = 0
    but2 = 0
    nouveauTemps=0
    while temps<600:
        temps = time.time() - debut
        if int(temps)>=nouveauTemps:
            nouveauTemps=nouveauTemps+1
            chronoActuel=600-int(temps)
            seconde_chrono = chronoActuel%60
            minute_chrono = int(chronoActuel/60)
            label_chrono= str(minute_chrono)+ " : " + str(seconde_chrono)
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
            but1 = but1 + valeurbut
            enJeu.Label_score_bleu.configure(text=str(but1))
            ecran.update()
            time.sleep(1)
            print('but bleu')
        if distance2<20:
            but2 = but2 + valeurbut
            enJeu.Label_score_rouge.configure(text=str(but2))
            ecran.update()
            time.sleep(1)
            print('but rouge')
    GPIO.cleanup()
    print('Nombre de buts rouge : ', but1, ' et nombre de buts bleu : ' , but2)


def chrono_but(enJeu: EnJeu, ecran: Tk):
    debut = time.time()
    temps = time.time() - debut  

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

    but1 = 0
    but2 = 0
    valeurbut = 1
    nouveauTemps=0
    while temps<600:
        temps = time.time() - debut
        if int(temps)>=nouveauTemps:
            nouveauTemps=nouveauTemps+1
            chronoActuel=600-int(temps)
            seconde_chrono = chronoActuel%60
            minute_chrono = int(chronoActuel/60)
            label_chrono= str(minute_chrono)+ " : " + str(seconde_chrono)
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
            but1 = but1 + valeurbut
            enJeu.Label_score_bleu.configure(text=str(but1))
            ecran.update()
            time.sleep(1)
            valeurbut = valeurbut + 1
            print('but bleu')
        if distance2<20:
            but2 = but2 + valeurbut
            enJeu.Label_score_rouge.configure(text=str(but2))
            ecran.update()
            time.sleep(1)
            valeurbut = valeurbut + 1
            print('but rouge')
    GPIO.cleanup()
    print('Nombre de buts rouge : ', but1, ' et nombre de buts bleu : ' , but2)
