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
    while but == 0:
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
            but = 1
            print('but bleu')
        if distance2<20:
            but = 2
            print('but rouge')
    GPIO.cleanup()
    return but

def chrono():
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

    while temps<600:
        temps = time.time() - debut
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
            but1 = but1 + 1
            time.sleep(1)
            print('but bleu')
        if distance2<20:
            but2 = but2 + 1
            time.sleep(1)
            print('but rouge')
    GPIO.cleanup()
    print('Nombre de buts rouge : ', but1, ' et nombre de buts bleu : ' , but2)

chrono()
