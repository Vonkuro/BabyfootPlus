----------Mode Classique----------

import RPi.GPIO as GPIO
import time

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

    score_bleu = 0
    score_rouge = 0

    while score_bleu or score_rouge <10:
        print ('Waiting a few seconds for the sensor to settle')
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
        
        print ('Distance 1:',distance1,'cm')
        print ('Distance 2:',distance2,'cm')

        if distance1<20:
            score_bleu = score_bleu + 1
            print('score bleu :' + str(score_bleu))
            time.sleep(1)
        if distance2<20:
            cotre_rouge = score_rouge + 1
            print('score rouge :' + str(score_rouge))
            time.sleep(1)
    GPIO.cleanup()
but()
